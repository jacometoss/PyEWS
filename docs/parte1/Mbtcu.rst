|image1| |image2| |image3| |image4| |image5|\ |image6|

Módulo de baja tensión mbtcu
============================

El módulo comprende conductores de cobre estandarizados desde clase B, C
y D. La información que debe ser ingresada en este módulo debe ser en
Sistema Internacional y para poder hacer su llamado se escribe lo
siguiente :

.. code:: python

   mbtcu()

El resultado puede ser visualizado en un array o tabla mediante
``tabulate`` el cual se instala por defecto en el programa.

Información requerida en el módulo mbtcu
========================================

El llenado del módulo requiere la información siguiente :

.. code:: tex

   #VF: Tensión de fase o en su defecto tensión de línea para sistemas de 1F2H, 2F.
   #VL: Tensión de línea.
   #In: Corriente nominal total de una de las fases.
   #Nc: Número de conductores por fase.
   #L : Longitud en metros.
   #FA: Número de conducrtores activos en el tubo conduit.
   #Type: Tipo de tubo conduit (1:PVC,2:AL,3:ACERO)
   #Ta: Temperatura ambiente en centigrados.
   ---- Valor númerico de temperatura, por ejemplo 30°C.
   #Vd: Caída de tensión (porcentual de 2, 3, 5)
   ---- 2,3,5	
   #S:  Seleccione el sistema que desea propner en base a este se muestran los resultados.
   ---- 1:(1F-2H) 2:(2F-3H) 3:(3F-3H) 4:(3F-4H)
   #Fp: Factor de potencia.
   #Op: Opción para mostrar resultados.
   	 1: Mostrar los resultados adecuadamente estructurado en una tabla. 
   	 2: Mostrar los resultados como datos acumulados. Esta opción es necesario cuando se activa
   	 	la función para múltiples cargas.
   #Fsc: Factor de sobrecorriente.
   #To: Temperatura de operación.
   #Break: Ajuste de protección.
   
Importado el módulo ``mbtcu`` ingrese la informaciíon requerida.

.. code:: python

   #Módulo de baja tensión para conductores de cobre
   mbtcu(VF,VL,P,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc,To,Break)

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
