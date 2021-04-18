|image1|
|image2|\ |image3|\ |image4|
|image5|\ |image6|

.. _header-n4:

Módulo de baja tensión para conductores de aluminio
===================================================

El módulo tiene dependencias por lo que es necesario instalar
``tabulate`` el cual da una mejor apariencia al momento de mostrar los
resultados.

.. code:: python

   import PyEWS
   PyEWS.MBTAL(127,220,15,1,22,1,1,35,3,1,0.9,1,1.25)

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

.. figure:: https://i.ibb.co/mt8HPSg/0-1-18-3.jpg
   :alt: 

La tabla anterior nos da un panorama más amplio de los resultados.

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
