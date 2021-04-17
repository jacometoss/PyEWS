|image1|\ |image2|\ |image3|\ |image4|\ |image5|\ |image6|

.. _header-n50:

Python Electrical Wire Sizes 
============================

El módulo PyEWS ( **Versión 0.1.18**) puede ser utilizado para
dimensionar conductores de baja tensión de una instalación eléctrica. Es
fácil de utilizar e interpretar sus resultados mostrando un panorama más
general al poder visualizar por completo una lista de conductores
propuestos con los parámetros de entrada.

.. _header-n52:

Instalación
-----------

La instalación del módulo se realiza con :

.. code:: python

   pip install ElectricalWireSizes

.. _header-n55:

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
   ---- 1:20 2:25 3:30 4:35 5:40 6:45 7:50 8:55 9:60 10:65 11:70 12:75
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
   #Para conductores de aluminio
   PyEWS.MBTAL(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc)

El módulo de corriente directa necesita la información siguiente :

.. code:: python

   #MODBTCUSTD(Vcd,In,Nc,L,Class,Ta,Vd,View,Fsc):
   #Vcd   :  Tensión en corriente directa.
   #In    :  Corriente directa del circuito.
   #Nc    :  Número de conductores en corriente directa.
   #L     :  Longitud del circuito en metros.
   #Class :  Clase de conductor A:1 B:2 y C:3.
   #Ta	   :  Temperatura ambiente 
   #Vd	   :  Caída de tensión.
   #View  :  Mostrar los resultados adecuadamente en una tabla con 1 para multiples cargas debe ser 2.
   #Fsc   :  Factor de sobrecorrriente

   PyEWS.MBTCUSTD(1200,145,1,100,1,25,3,1,1.25)

.. _header-n62:

PyEWS Módulos
-------------

+----+---------------------+----------+---------+---------------------+
| Id | Descripción         | Módulo   | Versión | Descargar           |
+====+=====================+==========+=========+=====================+
| 1  | Módulo de baja      | MBTCU    | 0.1.18  | `PyEWS              |
|    | tensión para        |          |         | 0.1.18 <h           |
|    | conductores de      |          |         | ttps://github.com/j |
|    | cobre clase B, C y  |          |         | acometoss/PyEWS>`__ |
|    | D tensión de 600V a |          |         |                     |
|    | 2000V               |          |         |                     |
+----+---------------------+----------+---------+---------------------+
| 2  | Módulo de baja      | MBTAL    | 0.1.18  | `PyEWS              |
|    | tensión para        |          |         | 0.1.18 <h           |
|    | conductores de      |          |         | ttps://github.com/j |
|    | aluminio clase B, C |          |         | acometoss/PyEWS>`__ |
|    | y D, tensión 600V a |          |         |                     |
|    | 2000V               |          |         |                     |
+----+---------------------+----------+---------+---------------------+
| 3  | Módulo de baja      | MBTCUSTD | 0.1.18  | `PyEWS              |
|    | tensión para        |          |         | 0.1.18 <h           |
|    | conductores de      |          |         | ttps://github.com/j |
|    | cobre clase B, C y  |          |         | acometoss/PyEWS>`__ |
|    | D en corriente      |          |         |                     |
|    | directa hasta 2000  |          |         |                     |
|    | V                   |          |         |                     |
+----+---------------------+----------+---------+---------------------+

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
