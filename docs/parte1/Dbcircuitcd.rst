.. _header-n2:

Múltiples cargas en corriente directa 
=====================================
|image1|
|image2|\ |image3|\ |image4|
|image5|\ |image6|

Para implementar una gran variedad de cargas se organizan como se
muestra en el bloque de código, puede agregar indefinidamente cargas.

.. code:: python

   from PyEWS import DBCIRCUITCD
   #(Vcd,In,Nc,L,Class,Ta,Vd,View):
   cargacd=[
       ["1",1200,30,1,100,1,25,3,2,1,1],
       ["2",1200,30,1,100,1,25,3,2,1,1],
       ["3",1200,30,1,100,1,25,3,2,1,1],
       ["4",1200,30,1,100,1,25,3,2,1,1],
       ["5",1200,30,1,100,1,25,3,2,1,1],
       ["6",1200,30,1,100,1,25,3,2,1,1],
       ["7",1200,30,1,100,1,25,3,2,1,1],
       ["8",1200,30,1,100,1,25,3,2,1,1],
       ["9",1200,30,1,100,1,25,3,2,1,1],
       ["10",1200,30,1,100,1,25,3,2,1,1],
       ["11",1200,30,1,100,1,25,3,2,1,1],
       ["12",1200,30,1,100,1,25,3,2,1,1],
       ["13",1200,30,1,100,1,25,3,2,1,1],
       ["14",1200,30,1,100,1,25,3,2,1,1]
       ]
   print("Total de cargas : ",len(cargacd))
   DBCIRCUITCD(cargacd,2,1)

   #Para mostar completo el desarrollo
   #----------PyEWS.DBCIRCUITCD(carga,1,1) #Cobre Estándar
   #----------PyEWS.DBCIRCUITCD(carga,1,2) #Aluminio No disponible
   #Para mostar el resumen únicamente 
   #----------PyEWS.DBCIRCUITCD(carga,2,1) #Cobre Estándar
   #----------PyEWS.DBCIRCUITCD(carga,2,2) #Aluminio No disponible

Para mostrar el resumen para conductores de cobre estándar

.. code:: 

   DBCIRCUITCD(cargacd,2,2)

.. figure:: https://i.ibb.co/rswpHm2/04.jpg
   :alt: 

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
