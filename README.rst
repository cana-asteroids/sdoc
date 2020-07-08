SDOC: Small Database of Optical Constants
==========================================

Database of selected optical contants to be used in compositional modeling of solar system minor bodies.

All data of the optical constants are stored in a single HDF file, for easy sharing and access of the data.

This repository is focused only on the maintainment of database, to see compositional models access github.com/depra/cana

**This database is currently under construction, the contents of the database are incomplete and used for testing purposes only.
A version of database with carefully selected optical constants and their metadata will be available soon.**


HDF Database Schema
--------------------

.. image:: https://raw.githubusercontent.com/depra/sdoc/master/docs/images/sdoc.png?token=ABGQYMSV3D54GENOC4OQR3K7AUUJA
   :align: center
   :scale: 50

What is inside?
---------------

==== =========== ============ ======== ======== ================= ===== ===== =========== ======================
id   material ID material     subgroup group    reference         state phase temperature path                  
==== =========== ============ ======== ======== ================= ===== ===== =========== ======================
H_0  H           Poly-HCN     Misc     organics Khare et al. 1994 -     -     -           /organics/Misc/H/H_0  
I_0  I           Ice Tholin   Misc     organics Khare et al. 1993 -     -     -           /organics/Misc/I/I_0  
K_0  K           Kerogen      Misc     organics Khare et al. 1990 -     -     -           /organics/Misc/K/K_0  
M_0  M           Murchison    Misc     organics Khare et al.      -     -     -           /organics/Misc/M/M_0  
T_0  T           Titan Tholin Misc     organics Khare et al. 1984 -     -     -           /organics/Misc/T/T_0  
at_0 at          Tholin alpha Misc     organics Khare et al. 1987 -     -     -           /organics/Misc/at/at_0
==== =========== ============ ======== ======== ================= ===== ===== =========== ======================

Dependencies
------------

- h5py
- pandas
- numpy


How to install
--------------

If you have `Anaconda <https://www.anaconda.com/distribution/>`_ or `pip <https://pypi.org/project/pip/>`_ installed: 
Download the last release or clone this repository using git,  unpack it if necessary, go into the directory "*sdoc-master*", and run on a terminal shell:

::

   pip install .
   
Usage
-----
For a example of how to access the database and search for a optical constant, take a look at `notebooks <https://github.com/depra/sdoc/blob/master/notebooks/accesing_the_database.ipynb>`_.
   
Cite
----
  
A paper with the description of the database and the compositional modeling techniques are in preparation. However, if you use the optical constants inserted in the db, **make sure to cite the references from where the optical constants were extracted.**
