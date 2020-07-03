SDOC: Small Database of Optical Constants
==========================================

Database of selected optical contants to be used in compositional modeling of solar system minor bodies.

All data of the optical constants are stored in a single HDF file, for easy sharing and access of the data.

This repository is focused only on the maintainment of database, to see compositional models that use SDOC, 
access github.com/depra/cana

HDF Database Schema
--------------------

.. image:: https://raw.githubusercontent.com/depra/sdoc/master/docs/images/sdoc.png?token=ABGQYMSV3D54GENOC4OQR3K7AUUJA
   :align: center
   :scale: 50

What is inside?
---------------

==== =========== ============ ======== ======== ===== ========= ===== ================= ======================
id   material ID material     subgroup group    state reference phase temperature       path                  
==== =========== ============ ======== ======== ===== ========= ===== ================= ======================
H_0  H           Poly-HCN     Misc     organics -     -         -     Khare et al. 1994 /organics/Misc/H/H_0  
I_0  I           Ice Tholin   Misc     organics -     -         -     Khare et al. 1993 /organics/Misc/I/I_0  
K_0  K           Kerogen      Misc     organics -     -         -     Khare et al. 1990 /organics/Misc/K/K_0  
M_0  M           Murchison    Misc     organics -     -         -     Khare et al.      /organics/Misc/M/M_0  
T_0  T           Titan Tholin Misc     organics -     -         -     Khare et al. 1984 /organics/Misc/T/T_0  
at_0 at          Tholin alpha Misc     organics -     -         -     Khare et al. 1987 /organics/Misc/at/at_0
==== =========== ============ ======== ======== ===== ========= ===== ================= ======================


Dependencies
------------

- h5py
- pandas
- numpy


How to install
--------------

If you have `Anaconda <https://www.anaconda.com/distribution/>`_ or `pip <https://pypi.org/project/pip/>`_ installed:

::

      pip install sdoc
      
Os, alternatively, download the last release or clone this repository using git,  Unpack it, if necessary, and go into the directory "*sdoc-master*", then run the below commands on a terminal shell:

::

   pip install .
