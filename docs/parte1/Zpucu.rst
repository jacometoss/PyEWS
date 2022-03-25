|image1| |image2| |image3| |image4| |image5| |image6|

Constantes de impedancia para conductores de cobre zpucu
========================================================

Este módulo se utiliza internamente pero puede ser usado para calcular
la resistencia de un conductor de corriente alterna a cualquier
temperatura y factor de potencia. Las constantes mostradas ``k`` son las
usadas en los cálculos y pueden ser usadas para dimensionar conductores
en los diferentes sistemas de alimentación o circuitos derivados.

.. code:: python

   zpucu()

-  ``Type`` : Selecciona la tubería y resistencia del conductor de
   corriente alterna. 1 (PVC), 2 (Aluminio), 3 (Acero).

-  ``Ta`` : La temperatura ambiente del lugar.

-  ``Fp`` : Factor de potencia de la carga.

-  ``View`` : Esta opción nos deja ver una tabla ordenada (1) y un
   arreglo (2).

Información requerida en el módulo zpucu
========================================

El llenado del módulo requiere la información siguiente :

.. code:: tex

   #Type : Selecciona la tubería y resistencia del conductor de corriente alterna. 1 (PVC), 2 (Aluminio), 3 (Acero)
   #Ta : La temperatura ambiente del lugar
   #Fp : Factor de potencia de la carga
   #View :  Esta opción nos deja ver una tabla ordenada (1) y un arreglo (2)

Importado ``kelectric`` la información requerida en orden sería

.. code:: python

   #Módulo de baja tensión para conductores de cobre para corriente directa
   zpucu(Type,Ta,Fp,View)

..

   El módulo se limita a los conductores mostrados en el ``dbc`` que son
   conductores comerciales.

Nota : Recuerda importar correctamento ``ElectricalWireSizes``

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
