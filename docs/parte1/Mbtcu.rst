|image1|
|image2|\ |image3|\  |image4|
|image5|\ |image6|

.. _header-n31:

Módulo de baja tensión para conductores de cobre
================================================

El módulo comprende conductores de cobre estandarizados desde clase B, C
y D.

.. _header-n33:

Iniciar paquete de instalación
------------------------------

El módulo tiene dependencias siendo necesario instalar ``tabulate`` el
cual da una mejor apariencia al momento de mostrar los resultados.

.. code:: tex

   #VF: Tensión de fase o en su defecto tensión de línea para sistemas de 1F2H, 2F.
   #VL: Tensión de línea.
   #In: Corriente nominal total de una de las fases.
   #Nc: Número de conductores por fase.
   #L : Longitud en metros.
   #FA: Número de conducrtores activos en el tubo conduit.
   #Type: Tipo de tubo conduit (1:PVC,2:AL,3:ACERO)
   #Ta: Temperatura ambiente en centigrados, únicamente ingresar la opcion númerica.
   #Vd: Caída de tensión (porcentual de 2, 3, 5)
   ---- 2,3,5	
   #S:  Seleccione el sistema que desea propner en base a este se muestran los resultados.
   ---- 1:(1F-2H) 2:(2F-3H) 3:(3F-3H) 4:(3F-4H)
   #Fp: Factor de potencia
   #Op: Opción para mostrar resultados
   	 1: Mostrar los resultados adecuadamente estructurado en una tabla. 
   	 2: Mostrar los resultados como datos acumulados. Esta opción es necesario cuando se activa
   	 	la función para múltiples cargas.
   #Fsc: Factor de sobrecorriente (1.25,1.0)
.. code:: python

   import PyEWS
   #Para conductores de cobre
   PyEWS.MBTCU(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc)

.. _header-n37:

Test MBTCU
----------

El módulo tiene dependencias por lo que es necesario instalar
``tabulate`` el cual da una mejor apariencia al momento de mostrar los
resultados.

.. code:: python

   import PyEWS
   PyEWS.MBTCU(127,220,15,1,22,1,1,35,3,1,0.9,1,1.25)

Los se resultados muestran con la iteración de todos los conductores
tanto para tensión monofásica como trifásica.

-  ``Vd (Voltage Drop)`` es la pérdida de tensión porcentual
-  ``60,75,90`` la ampacidad real de los conductores.
-  ``Nc`` es el número de conductores por fase.
-  ``Op`` muestra si el resultado es correcto al aparecerer en la
   columna como ``Yes`` .
-  ``ITM`` es la protección del circuito.

   Se puede observar en la columna ``%VD 1F-2H`` seleccionada la pérdida
   de tensión es aceptable con respecto a la mínima ingresada del
   ``%3``. La confirmación de un resultado es aceptable se visualiza en
   la columna ``OP`` . Al utilizar la opción de multiples cargas podrá
   mostrar el resumen y el desglose como se muestra en la tabla.

.. figure:: https://i.ibb.co/rbttQ7p/0-1-18.jpg
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
