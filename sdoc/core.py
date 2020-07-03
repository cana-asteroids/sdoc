import os
import pandas as pd
import numpy as np
import h5py

PWD = os.path.dirname(os.path.abspath(__file__))


class SDOC(h5py.File):
    r"""
    Extended HDF5 File object for the Small Database of Optical Constants.

    Extended Attributes
    -------------------
    contents: pandas visualization of what is inside the database.
    """

    def __init__(self, sdocfile=PWD+'/data/sdoc.h5', mode='a'):
        r"""
        Create a new HDF file object with extended methods for SDOC.

        For extended documentation on handling HDF files with h5py visit
        https://www.h5py.org/

        Parameters
        ----------
        sdocfile: str
            The path for the SDOC hdf file.

        mode: str
            r        Readonly, file must exist (default)
            r+       Read/write, file must exist
            w        Create file, truncate if exists
            w- or x  Create file, fail if exists
            a        Read/write if exists, create otherwise

        """
        h5py.File.__init__(self, sdocfile, mode=mode)
        self.contents = pd.DataFrame(columns=['material ID', 'subgroup',
                                              'group', 'material',
                                              'state', 'reference',
                                              'phase', 'temperature',
                                              'path'])
        self.build_contents()

    def build_contents(self, input=None):
        r"""Build pandas.DataFrame of what is inside the SDOC file."""
        if input is None:
            input = self
        for key, value in input.items():
            if isinstance(value, h5py.Group):
                self.build_contents(input=value)
            elif isinstance(value, h5py.Dataset):
                aux = value.name.split('/')[1:]
                aux.reverse()
                if len(aux) < 4:
                    aux.append(None)
                material = self[os.path.dirname(value.name)].attrs['material']
                self.contents.loc[aux[0]] = [*aux[1:], material,
                                             value.attrs['state'],
                                             value.attrs['phase'],
                                             value.attrs['temperature'],
                                             value.attrs['reference'],
                                             value.name]
        return self.contents

    def update_contents(self):
        r"""Update the contents DataFrame."""
        self.contents = pd.DataFrame(columns=['material ID', 'subgroup',
                                              'group', 'material',
                                              'state', 'reference',
                                              'phase', 'temperature',
                                              'path'])
        self.build_contents()
        return self.contents

    def list_materials(self):
        r"""List the materials and respective IDs."""
        sdb = self.contents[['material ID', 'material']]
        sdb = sdb.set_index('material ID')
        sdb.drop_duplicates()
        return sdb

    def select_group(self, group, paths_only=False):
        r"""
        Select a compositional group.

        Parameters
        ----------
        group: str
            The name of the group or subgroup
            (e.g. 'organics', 'silicates', 'hydrated'...)

        return_paths: boolean
            If True will return a list with the datasets of the group.
            False will return a pandas.DataFrame with the group contents.

        Returns
        -------
        list or pandas.DataFrame

        """
        if group in list(self.contents['group'].values):
            sdb = self.contents[(self.contents['group'] == group)]
        elif group in list(self.contents['subgroup'].values):
            sdb = self.contents[(self.contents['subgroup'] == group)]
        else:
            raise(KeyError("group '{0}' not found.".format(group)))
        if paths_only:
            sdb = list(sdb['path'])
        return sdb

    def select_material(self, material, paths_only=False):
        r"""
        Select a compositional group.

        Parameters
        ----------
        material: str
            The name of the material
            (e.g. 'Ice Tholin', 'Murchison'...)

        return_paths: boolean
            If True will return a list with the datasets of the materials.
            False will return a pandas.DataFrame with the material contents.

        Returns
        -------
        list or pandas.DataFrame
        """
        try:
            sdb = self.contents[(self.contents['material'] == material)]
        except KeyError as error:
            raise(error('Material {0} not found.'.format(material)))
        if paths_only:
            sdb = list(sdb['path'])
        return sdb

    def get_constant(self, constant):
        r"""
        Get the optical constant data.

        Parameters
        ----------
        constant: str
            The optical constant id or path (e.g. "H_0", "organics/Misc/H/H_0")

        Returns
        -------
        label: str
            the optical constant id
        data: numpy structured array
            the optical constant data (dtype=['w', 'n', 'k'])

        """
        if constant in self.contents.index:
            label = constant
            aux = self.contents.loc[constant]['path']
        elif constant in self.contents['path']:
            label = self.contents[(self.contents['path'] == constant)].index[0]
            aux = constant
        return label, self[aux][()]

    def insert_constant(self, group, material, ocpath, mid=None, subgroup=None,
                        reference=None, density=None, state=None, phase=None,
                        temperature=None):
        r"""
        Insert an optical constant to the SDOC database.

        To save the changes you must close the database:
        ..: sdb = SDOC()
        ..: sdb.insert_constant(...)
        ..: sdb.close()

        Parameters
        ----------
        group: str
            The name of the compositional group (e.g. Organics, Silicates,
            Ices...).

        material: str
            The full name of the compound material (e.g. Titan Tholin,
            Serpentine).

        mid: str (optional)
            The ID for the compound (e.g. H, W, Ss). If none, it will search
            for the standard IDs from ___. However it will raise an error if
            mid is not assigned and the compound is not found in the list.
            To see all the compound IDs use .... If mid=None and is not found
            in the list of IDs, it will set mid='U' (for undefined).

        ocpath: str
            The path for the optical constant file. The file must have three
            columns: wavelength, real refractory index, imaginary refractory
            index.

        subgroup: str (optional)
            The ID of the subgroup, if any (e.g. for Silicates are Piroxenes,
            Hydrated...)

        reference: str (optional)
            The name of the reference for the optical constant

        density: float (optional)
            The density value for the compound

        state: string (optional)
            The state of the material (pure, diluted, isolated)

        phase: string (optional)
            The phase of the material (amorphous, crystalline)

        temperature: float (optional)
            The temperature of the material
        """
        assert self.mode in ['w', 'a', 'r+'], "Assure SDOC is initialized with mode='w'"

        if group not in self.keys():
            self.create_group(group)

        if subgroup not in self[group].keys():
            self[group].create_group(subgroup)

        if (mid is None):
            aux = self.list_materials()
            if (material in aux['materials']):
                mid = aux[(aux['material'] == material)].index[0]
            else:
                mid = 'U'

        if mid not in self[group][subgroup].keys():
            self[group][subgroup].create_group(mid)
            self[group][subgroup][mid].attrs['material'] = material

        id = '{0}_{1}'.format(mid, len(self[group][subgroup][mid]))
        try:
            oc = np.loadtxt(ocpath, dtype=[('w', np.float64),
                                           ('n', np.float64),
                                           ('k', np.float64)])
        except ValueError as error:
            raise(error + r"""Check if the file have threecolumns: wavelength,
                              real refractory index, imaginary refractory
                              index.""")

        self[group][subgroup][mid].create_dataset(id, data=oc)
        self[group][subgroup][mid][id].attrs['reference'] = reference
        self[group][subgroup][mid][id].attrs['density'] = density
        self[group][subgroup][mid][id].attrs['state'] = state
        self[group][subgroup][mid][id].attrs['temperature'] = temperature
        self[group][subgroup][mid][id].attrs['phase'] = phase

        self.update_contents()
