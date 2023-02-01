SDOC: Small Database of Optical Constants
==========================================

Database of selected optical contants to be used in compositional modeling of solar system minor bodies.

All data of the optical constants are stored in a single HDF file, for easy sharing and access of the data.

This repository is focused only on the maintainment of database, to see compositional models access github.com/depra/cana

**This database is currently under construction, the contents of the database are incomplete and used for testing purposes only.
A version of database with carefully selected optical constants and their metadata will be available soon.**


HDF Database Schema
--------------------

.. image:: https://raw.githubusercontent.com/depra/sdoc/master/docs/images/sdoc.png
   :align: center
   :scale: 50

Dependencies
------------

- h5py
- pandas
- numpy


How to install
--------------

If you have `Anaconda <https://www.anaconda.com/distribution/>`_ or `pip <https://pypi.org/project/pip/>`_ installed: 

::

   pip install git+https://github.com/cana-asteroids/sdoc.git

   
Usage
-----
For a example of how to access the database and search for a optical constant, take a look at `notebooks <https://github.com/depra/sdoc/blob/master/notebooks/accesing_the_database.ipynb>`_.
   
Cite
----
  
A paper with the description of the database and the compositional modeling techniques are in preparation. However, if you use the optical constants inserted in the db, **make sure to cite the references from where the optical constants were extracted.**
