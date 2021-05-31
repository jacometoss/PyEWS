|image1|
|image2|\ |image3|\ |image4|
|image5|\ |image6|

.. _header-n2:

Múltiples cargas en corriente alterna
=====================================

Para implementar una gran variedad de cargas se organizan como se
muestra en el bloque de código, puede agregar hasta **indefinido número
de cargas** en está nueva versión (0.1.18). El número consecutivo de
orden de las cargas no afecta a los resultados y puede colocar cualquier
otro nombre corto para poder identificar la carga.

.. code:: python

   from PyEWS import DBCIRCUIT
   #Definimos las cargas
   carga=[
        ["1",127,220,15,1,22,1,1,35,3,1,0.9,2,1.25],
        ["2",127,220,12,1,10,1,1,25,3,1,0.9,2,1.25],
        ["3",127,220,22,1,15,1,1,25,3,1,0.9,2,1.25],
        ["4",127,220,22,1,15,1,1,25,3,1,0.9,2,1.25],
        ["4",127,220,22,1,20,1,1,25,3,1,0.9,2,1.25],
        ["6",127,220,22,1,10,1,1,25,3,1,0.9,2,1.25],
        ["7",127,220,22,1,30,1,1,25,3,1,0.9,2,1.25],
        ["8",127,220,22,1,25,1,1,25,3,1,0.9,2,1.25],
        ["9",127,220,15,1,31,1,1,35,3,1,0.9,2,1.25],    
        ["10",127,220,22,1,14,1,1,25,3,1,0.9,2,1.25],
        ["11",127,220,15,1,20,1,1,35,3,1,0.9,2,1.25],
        ["12",127,220,22,1,32,1,1,25,3,1,0.9,2,1.25],
        ["13",127,220,22,1,25,1,1,25,3,1,0.9,2,1.25],
        ["14",127,220,22,1,24,1,1,25,3,1,0.9,2,1.25],
        ["15",127,220,22,1,18,1,1,25,3,1,0.9,2,1.25],
        ["16",127,220,22,1,17,1,1,25,3,1,0.9,2,1.25],
        ["17",127,220,22,1,12,1,1,25,3,1,0.9,2,1.25],    
        ["18",127,220,22,1,10,1,1,25,3,1,0.9,2,1.25],
        ["19",127,220,22,1,21,1,1,25,3,1,0.9,2,1.25],
        ["20",127,220,196,3,55,0.8,3,75,3,3,0.9,2,1.25]
       ]
   #Una forma sencilla de mostrar el total de cargas
   print("Total de cargas : ",len(carga))
   #Para mostar completo el desarrollo
   #----------PyEWS.DBCIRCUIT(carga,1,1) #Cobre
   #----------PyEWS.DBCIRCUIT(carga,1,2) #Aluminio
   #Para mostar el resumen únicamente 
   #----------PyEWS.DBCIRCUIT(carga,2,1) #Cobre
   #----------PyEWS.DBCIRCUIT(carga,2,2) #Aluminio

Para mostrar el resumen de los resultados de cada carga ingresada usamos
la siguiente línea de código.

.. code:: python

   PyEWS.DBCIRCUIT(carga,2,1)

Al ingresar la línea de código siguiente pude obtener detalles de cada
cálculo y al final el resumen de cada uno.

.. code:: python

   PyEWS.DBCIRCUIT(carga,1,1)

Es más práctico obtener el reporte corto de cargas.

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
