Graficar resultados
===================

Mediante ``matplotlib`` y\ ``numpy`` es posible obtener gráficos, la
instalación de esta librería es automática al instalar
``ElectricalWireSizes``.

Es posible graficar los resultados de pérdida de tensión de un único
cálculo por el momento como se muestra en la figura siguiente :

.. figure:: https://i.ibb.co/XFzQyZJ/Graph2.jpg
   :alt: 

Esta limitado para conductores en corriente alterna, el procedimiento
para generar la figura es mediante :

.. code:: python

   from PyEWS import mbtal, graph
   mydata=mbtal(127,220,55,1,45,1,1,35,3,1,0.9,2,1)
   graph(mydata,"6 AWG","4/0 AWG", 8, 5, 2,"k",1)

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
