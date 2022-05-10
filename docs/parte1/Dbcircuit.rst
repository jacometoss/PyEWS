|image1| |image2| |image3| |image4| |image5|\ |image6|

Múltiples cargas en corriente alterna con dbcircuit
===================================================

Para implementar una gran variedad de cargas se organizan como se
muestra en el bloque de código, puede agregar hasta **indefinido número
de cargas** . El número consecutivo de orden de las cargas no afecta a
los resultados y puede colocar cualquier otro nombre corto para poder
identificar la carga.

Para mostrar el resumen de los resultados de cada carga ingresada usamos
la siguiente línea de código.

.. code:: python

   dbcircuit()

Para poder utilizar el módulo debemos primero definir el archivo de
cargas

.. code:: python

   load=[
        ["1",VF,VL,P,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc,Itm],
        ["2",VF,VL,P,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc,Itm],
        ["3",VF,VL,P,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc,Itm]
       ]

Podemos observar que son los mismos de los módulos ``mbtcu`` y ``mbtal``
pero mostrado en una lista bien definida y ordenada. Este módulo se
encuentra limitado al ser usado en el IDLE de Python pero no cuando lo
ejecutamos en símbolo del sistema resulta más eficiente aunque suena un
poco confuso si desconoce un poco de como ejecutar Python desde el
símbolo del sistema.

   Para implementar la carga dentro del módulo ``dbcircuit`` cada carga
   individual debe tener la lista como opción de visualización y no en
   tabla.

Iniciar el módulo dbcircuit
===========================

Configurado el archivo de cargas individuales y nombradas o numeradas a
gusto personal se procede a llenar ``resultViewer`` y ``conductor``

.. code:: python

   dbcircuit(load,resultViewer,coductor)

Información requerida en el módulo dbcircuit
============================================

El llenado del módulo requiere la información siguiente :

.. code:: tex

   #load: Listado de cargas.
   #resultViewer: Muestra los resultados de forma individual como resumida.
   ---- 1:Muestra cada resultado individual y el resumen de resultados en una tabla.
   -----2:Resumida de resultados en una tabla.
   #conductor : Esta opción es para seleccionar los conductores de cobre y aluminio.
   ---- 1:Conductores de cobre para corriente alterna.
   -----2:Conductores de aluminio para corriente alterna.

..

   El módulo se limita a los conductores mostrados en el ``dbc`` que son
   conductores comerciales.
 
Resultados del módulo ``dbc`` para conductores de cobre
=======================================================

El módulo ``dbc`` muestra en forma resumida el cálculo de múltiples circuitos.


====  ======  ======  ====  ====  =====  =====  ====  ====  ====  ====  =======  ====  =====  ======  ======  ======  =====
  Id  #CAL      L[m]    Vd    FP  ALM      Fct    Fa    60    75    90    Vd[%]    Nc     In      60      75      90    ITM
====  ======  ======  ====  ====  =====  =====  ====  ====  ====  ====  =======  ====  =====  ======  ======  ======  =====
   1  10 AWG      20     3   0.9  1F/2H  0.913   0.8    30    35    40    1.754     6  16.67  21.912  26.404  30.624    100
   2  4 AWG       20     3   0.9  1F/2H  0.913   0.8    70    85    95    1.125     3  39     51.128  64.124  72.732    125
   3  10 AWG      20     3   0.9  1F/2H  0.913   0.8    30    35    40    1.789     1  17     21.912  26.404  30.624     20
   4  10 AWG      20     3   0.9  1F/2H  0.913   0.8    30    35    40    1.789     1  17     21.912  26.404  30.624     20
   5  10 AWG       6     2   0.9  3F/3H  0.876   0.8    30    35    40    0.227     2  15     21.024  25.732  30.08      40
   6  6 AWG       20     3   0.9  1F/2H  0.913   0.8    55    65    75    1.111     1  25     40.172  49.036  57.42      35
   7  4 AWG       50     3   0.9  3F/4H  0.913   0.8    70    85    95    1.39      3  40     51.128  64.124  72.732    150
====  ======  ======  ====  ====  =====  =====  ====  ====  ====  ====  =======  ====  =====  ======  ======  ======  =====

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
