|image1|  |image2| |image3| |image4| |image5| |image6|

Electrical Wire Sizes 
=====================

The Python Electrical Wire Sizes module ``Version 0.1.27`` can be
used to size feeder conductors in low voltage such as the branch circuits 
of an electrical installation. Is tool is very useful for engineers and 
architects immersed in the branch of electrical projects and those familiar 
with some concepts shown here who want to learn related topics like this.

Installing the package
----------------------

The installation of the package is done with the following line

.. code:: python

   pip install ElectricalWireSizes

Modules
-------

The list of modules available in the package in this latest version are

+----+-------------------------------------------------+---------------+
| Id | Descripción                                     | Módulo        |
+====+=================================================+===============+
| 1  | Low voltage module for conductors of copper     | mbtcu         |
|    | class B, C and D voltage from 600V to 2000V     |               |
+----+-------------------------------------------------+---------------+
| 2  | Low voltage module for class B, C and D aluminum| mbtal         |
|    | conductors, voltage 600V to 2000V               |               |
+----+-------------------------------------------------+---------------+
| 3  |Low voltage module for class B, C and D copper   | mbtcustd      |
|    |conductors in direct current up to 2000 V        |               |
+----+-------------------------------------------------+---------------+
| 4  | Module to grpah results                         | graph         |
+----+-------------------------------------------------+---------------+
| 5  | Resistance change in copper conductors          | zpucu         |
+----+-------------------------------------------------+---------------+
| 6  | Resistance change in aluminum conductor         | zpual         |
|    |                                                 |               |
+----+-------------------------------------------------+---------------+
| 7  | Multiple circuits for copper and aluminum       |dbcircuit      |
|    | conductors                                      |               |
+----+-------------------------------------------------+---------------+
| 8  | Multiple circuits for copper conductors         |dbcircuitcd    |
+----+-------------------------------------------------+---------------+

All modules work with units of the International System and in
future versions will include the English System

Start package and module
------------------------

The module has dependencies being necessary to install ``tabulate`` (it is
installs automatically) which serves to give a better appearance
at the time of displaying the results

 In this example we will import the low voltage module
for copper conductors, we will not show the filling of this module
only the order of call.

.. code:: python

   mbtcu()

In this simple way we can start each of the modules
shown in the table shown above. In the following points
you will see how to correctly fill each of the modules and that
result is shown in each of them.


.. |image1| image:: https://badge.fury.io/py/ElectricalWireSizes.svg
   :target: https://badge.fury.io/py/ElectricalWireSizes
.. |image2| image:: https://static.pepy.tech/personalized-badge/electricalwiresizes?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads
   :target: https://pepy.tech/project/electricalwiresizes
.. |image3| image:: https://pepy.tech/badge/electricalwiresizes/month
   :target: https://pepy.tech/project/electricalwiresizes
.. |image4| image:: https://img.shields.io/badge/python-3 | 3.5 | 3.6 | 3.7 | 3.8 | 3.9-blue
   :target: https://pypi.org/project/ElectricalWireSizes/
.. |image5| image:: https://api.codeclimate.com/v1/badges/27c48038801ee954796d/maintainability
   :target: https://codeclimate.com/github/jacometoss/PyEWS/maintainability
.. |image6| image:: https://app.codacy.com/project/badge/Grade/8d8575adf7e149999e6bc84c657fc94e
   :target: https://www.codacy.com/gh/jacometoss/PyEWS/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jacometoss/PyEWS&amp;utm_campaign=Badge_Grade
