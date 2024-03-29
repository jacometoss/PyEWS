|image1| |image2| |image3| |image4| |image5|\ |image6|

Base de datos de conductores DBC
================================

La base de datos de conductores ocupadas en la librería puede ser
visualizada con la siguiente línea

.. code:: python

   dbc()

1. Muestra la resistencia en corriente alterna y reactancia inductiva
   para conductores de cobre en una tubería de material de pvc, aluminio
   y acero.

2. Muestra la resistencia en corriente alterna y reactancia inductiva
   para conductores de aluminio en una tubería de material de pvc,
   aluminio y acero.

3. Muestra la resistencia en corriente directa para conductores clase B,
   C y D.

Información requerida en el módulo mbtcustd
===========================================

El llenado del módulo requiere la información siguiente :

.. code:: tex

   #Vcd: Tensión de fase a neutro en volts.
   #P : Potencia en Watts.
   #Nc: Número de conductores por fase.
   #L : Longitud en metros.
   #Class: Clase de conductor (1:Clase A,2:Clase B,3:Clase C)
   #Ta: Temperatura ambiente en centigrados, únicamente ingresar la opción numérica.
   #Vd: Caída de tensión (porcentual de 2, 3, 5)
   ---- 2,3,5	
   #View: Opción para mostrar resultados
   	 1: Mostrar los resultados adecuadamente estructurado en una tabla. 
   	 2: Mostrar los resultados como datos acumulados. Esta opción es necesario cuando se activa
   	 	la función para múltiples cargas.
   #Fsc: Factor de sobrecorriente (1.25,1.0) cuando existe carga continua.
   #To:  Temperatura de operación del conductor.
   #Break: Esta opción determina el portentaje de uso de la protección eléctrica.
   ---- 1:100%
   -----2:80%

Importado ``PyEWS`` la información requerida en orden sería

.. code:: python

   #Módulo de baja tensión para conductores de cobre para corriente directa
   mbtcustd(Vcd,P,Nc,L,Class,Ta,Vd,View,Fsc,To,Break)

..

   El módulo se limita a los conductores mostrados en el ``dbc`` que son
   conductores comerciales.

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
