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

What is inside?
---------------

===== === =============== ======================== ========= =========== ===== ==== ======= === ==================== =================================
id    mid material        formula                  group     phase       temp  wmin wmax    res hpath                ref                              
===== === =============== ======================== ========= =========== ===== ==== ======= === ==================== =================================
car_0 car Carbon          Kbr embebed              carbon    -           50K   0.3  4.99002 470 /carbon/car/car_0    Rouleau&Martin 1991              
car_1 car Carbon          Kbr embebed              carbon    -           20K   0.3  4.99002 470 /carbon/car/car_1    Draine 1985                      
amo_3 amo Ammonia         NH3                      ices      amorphous   40K   0.3  4.99002 470 /ices/amo/amo_3      Roser et al. 2021                
cod_1 cod Carbon dioxide  CO2                      ices      -           150K  0.3  4.99002 469 /ices/cod/cod_1      Hansen et al. 1997               
com_0 com Carbon monoxide CO                       ices      -           10K   0.3  4.99002 470 /ices/com/com_0      PubChem                          
eta_0 eta Ethane          C2H6                     ices      crystalline 30K   0.3  4.99002 470 /ices/eta/eta_0      Hudson et al. 2014               
eta_1 eta Ethane          C2H6                     ices      crystalline 40K   0.3  4.99002 470 /ices/eta/eta_1      Hudson et al. 2014               
eta_2 eta Ethane          C2H6                     ices      amorphous   30K   0.3  4.99002 470 /ices/eta/eta_2      Hudson et al. 2014               
eta_3 eta Ethane          C2H6                     ices      amorphous   40K   0.3  4.99002 470 /ices/eta/eta_3      Hudson et al. 2014               
eta_4 eta Ethane          C2H6                     ices      amorphous   60K   0.3  4.99002 470 /ices/eta/eta_4      Hudson et al. 2014               
eth_0 eth Ethylene        C2H4                     ices      amorphous   30K   0.3  4.99002 470 /ices/eth/eth_0      Hudson et al. 2014               
eth_1 eth Ethylene        C2H4                     ices      amorphous   40K   0.3  4.99002 470 /ices/eth/eth_1      Hudson et al. 2014               
eth_2 eth Ethylene        C2H4                     ices      crystalline 30K   0.3  4.99002 470 /ices/eth/eth_2      Hudson et al. 2014               
eth_3 eth Ethylene        C2H4                     ices      crystalline 40K   0.3  4.99002 470 /ices/eth/eth_3      Hudson et al. 2014               
met_0 met Methane         CH4                      ices      crystalline 39K   0.3  4.99002 470 /ices/met/met_0      SShade and Grundy et al. 2002    
mol_0 mol Methanol        CH3OH                    ices      -           100K  0.3  4.99002 470 /ices/mol/mol_0      Hudgins et al 1993 and Brown 1995
nit_0 nit Nitrogen        N2                       ices      -           36.5K 0.3  4.99002 470 /ices/nit/nit_0      B.Schmitt et al.                 
wat_2 wat Water           H2O                      ices      amorphous   40K   0.3  4.99002 470 /ices/wat/wat_2      Mastrapa et al., 2008 and 2009   
wat_4 wat Water           H2O                      ices      crystalline 40K   0.3  4.99002 470 /ices/wat/wat_4      Mastrapa et al., 2008 and 2009   
wat_5 wat Water           H2O                      ices      crystalline 50K   0.3  4.99002 470 /ices/wat/wat_5      Mastrapa et al., 2008 and 2009   
wat_6 wat Water           H2O                      ices      amorphous   50K   0.3  4.99002 470 /ices/wat/wat_6      Mastrapa et al., 2008 and 2009   
m03_0 m03 Mixture 3       NH3(1)-N2(1.7)           mixtures  -           15K   0.3  4.99002 470 /mixtures/m03/m03_0  Zanchet et al. 2013              
m04_0 m04 Mixture 4       H2O(20)-CH4(1)           mixtures  -           40K   0.3  4.99002 470 /mixtures/m04/m04_0  Hudgins et al 1993               
m05_0 m05 Mixture 5       CH4-N2                   mixtures  beta        38K   0.3  4.99002 470 /mixtures/m05/m05_0  Quirico and schmitt 1992, SShade 
tit_0 tit Titan Tholin    -                        organics  -           -     0.3  4.99002 470 /organics/tit/tit_0  Khare et al 1984                 
trt_0 tri Triton Tholin   -                        organics  -           -     0.3  4.99002 470 /organics/tri/trt_0  Khare                            
oli_0 oli Olivine         Mg_2y,Fe_2-2y,SiO4,y=0.5 silicates -           -     0.3  4.99002 470 /silicates/oli/oli_0 Dorschner et al. 1995            
oli_1 oli Olivine         Mg_2y,Fe_2-2y,SiO4,y=0.5 silicates -           -     0.3  4.99002 470 /silicates/oli/oli_1 Dorschner et al. 1995            
pyr_1 pyr Pyroxene        Mg_x,Fe_1-x,SiO3,x=0.50  silicates -           -     0.3  4.99002 470 /silicates/pyr/pyr_1 Dorschner et al. 1995            
pyr_2 pyr Pyroxene        Mg_x,Fe_1-x,SiO3,x=0.50  silicates -           -     0.3  4.99002 470 /silicates/pyr/pyr_2 Dorschner et al. 1995            
pyr_3 pyr Pyroxene        Mg_x,Fe_1-x,SiO3,x=0.50  silicates -           -     0.3  4.99002 470 /silicates/pyr/pyr_3 Dorschner et al. 1995            
pyr_4 pyr Pyroxene        Mg_x,Fe_1-x,SiO3,x=0.50  silicates -           -     0.3  4.99002 470 /silicates/pyr/pyr_4 Dorschner et al. 1995            
pyr_5 pyr Pyroxene        Mg_x,Fe_1-x,SiO3,x=0.50  silicates -           -     0.3  4.99002 470 /silicates/pyr/pyr_5 Dorschner et al. 1995            
pyr_6 pyr Pyroxene        Mg_x,Fe_1-x,SiO3,x=0.50  silicates -           -     0.2  5.5     42  /silicates/pyr/pyr_6 Dorschner et al. 1995            
===== === =============== ======================== ========= =========== ===== ==== ======= === ==================== =================================

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
