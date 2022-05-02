|image1| |image2| |image3| |image4| |image5|\ |image6|

Graficar resultados
===================

Mediante ``matplotlib`` y\ ``numpy`` es posible obtener gráficos, la
instalación de esta librería es automática al instalar
``ElectricalWireSizes``.

Es posible graficar los resultados de pérdida de tensión de un único
cálculo por el momento como se muestra en la figura siguiente :

.. figure:: https://i.ibb.co/LkYKVqS/graph-mbtcu.png
   :alt: 

Esta limitado para conductores en corriente alterna, el procedimiento
para generar la figura es mediante :

.. code:: python

   from PyEWS import mbtal, graph
   mydata=mbtcu(127,220,30,1,45,1,1,35,3,1,0.9,2,1,60,1.00)
   graph(mydata,"10 AWG","4/0 AWG", 10, 5, 1,"rbkg",1)

El llenado del módulo es un poco complejo

-  Realice un cálculo para conductores de cobre, en el ejemplo se guardo
   en ``mydata`` .

-  Llamamos al módulo llenamos como se indica

.. code:: python

   graph(mydata,"Calibre Inicial","Calibre Final", Ancho, Alto, Aluminio/Cobre, "Color",Sistema)

Los calibres deben ir como se muestra en los resultados y entre comillas
dobles indicando un conductor inicial y final disponible, el ancho y
alto son pulgadas en formato ``integer`` o ``float``. Dependiendo el
material del conductor (``1:Cobre, 2:Aluminio``) y el color de las
barras puede usar ``k: negro``, ``b: azul``, ``g:verde``, ``r:rojo`` que
son estándar en reportes, finalmente el sistema
``1:1F-2H``,\ ``2:2F-3H``,\ ``3:3F-3H`` y ``4:3F:4H``.

No olvide que el arreglo de datos ``mydata`` debe ser correcto y
definido.

.. |image1| image:: https://badge.fury.io/py/ElectricalWireSizes.svg
   :target: https://badge.fury.io/py/ElectricalWireSizes
.. |image2| image:: https://static.pepy.tech/personalized-badge/electricalwiresizes?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads
   :target: https://pepy.tech/project/electricalwiresizes
.. |image3| image:: https://pepy.tech/badge/electricalwiresizes/month
   :target: https://pepy.tech/project/electricalwiresizes
.. |image4| image:: https://img.shields.io/badge/python-3 | 3.5 | 3.6 | 3.7 | 3.8 | 3.9 | 3.10-blue
   :target: https://pypi.org/project/ElectricalWireSizes/
.. |image5| image:: https://api.codeclimate.com/v1/badges/27c48038801ee954796d/maintainability
   :target: https://codeclimate.com/github/jacometoss/PyEWS/maintainability
.. |image6| image:: https://app.codacy.com/project/badge/Grade/8d8575adf7e149999e6bc84c657fc94e
   :target: https://www.codacy.com/gh/jacometoss/PyEWS/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jacometoss/PyEWS&amp;utm_campaign=Badge_Grade
