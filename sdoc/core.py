r"""
"""
import h5py
import os

PWD = os.path.dirname(os.path.abspath(__file__))


class SDOC(object):
    r"""
    """
    def __init__(self, load=True, mode='r'):
        r"""
        """
        if load:
            self.mode = mode
            self.db = self.__load__(mode)

    @staticmethod
    def __load__(mode):
        r"""Load the HDF database."""
        hf = h5py.File(PWD+'/data/sdoc.h5', mode)
        return hf

    def __getitem__(self, key):
        r"""
        """
        return self.db[key]

    def insert_constant(self, group, material, ocpath, mid=None, subgroup=None,
                        reference=None, density=None):
        r"""
        Insert an optical constant to the HDF database.

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
            To see all the compound IDs use ....

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

        """
        assert self.mode == 'w', "Assure HDF is initialized with mode='w"

    def listdb(self, group=None):
        r"""
        """
        def walker(name, obj):
            if isinstance(obj, h5py._hl.dataset.Dataset) & \
               (group in name):
                print(name)
                for key, val in obj.attrs.items():
                    print("    %s: %s" % (key, val))
        self.db.visititems(walker)

    @staticmethod
    def walker(name, obj, group):
        if (group in name) & isinstance(obj, h5py._hl.dataset.Dataset):
            return name

    def save(self):
        r"""
        """
