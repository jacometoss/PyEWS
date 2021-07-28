|image1| |image2| |image3| |image4| |image5|  |image6|

Múltiples cargas en corriente alterna dbcircuitcd
=================================================

Para implementar una gran variedad de cargas se organizan como se
muestra en el bloque de código, puede agregar hasta **indefinido número
de cargas** . El número consecutivo de orden de las cargas no afecta a
los resultados y puede colocar cualquier otro nombre corto para poder
identificar la carga.

Para mostrar el resumen de los resultados de cada carga ingresada usamos
la siguiente línea de código.

.. code:: python

   dbcircuitcd()

Para poder utilizar el módulo debemos primero definir el archivo de
cargas

.. code:: python

   load=[
        ["1",Vcd,In,Nc,L,Class,Ta,Vd,View,Fsc],
        ["2",Vcd,In,Nc,L,Class,Ta,Vd,View,Fsc],
        ["3",Vcd,In,Nc,L,Class,Ta,Vd,View,Fsc]
       ]

Este módulo se encuentra limitado al ser usado en el IDLE de Python pero
no cuando lo ejecutamos en símbolo del sistema resulta más eficiente
aunque suena un poco confuso si desconoce un poco de como ejecutar
Python desde el símbolo del sistema. El ``View`` debe encontrarse en el
número\ ``2`` para poder ejecutar las múltiples cargas, recuerde es muy
diferentes un array que una tabla en forma visual.

   Para implementar la carga dentro del módulo ``dbcircuitcd`` cada
   carga individual debe tener la lista como opción de visualización y
   no en tabla.

Iniciar el módulo dbcircuitcd
=============================

Configurado el archivo de cargas individuales y nombradas o numeradas a
gusto personal se procede a llenar ``resultViewer`` y ``conductor``

.. code:: python

   dbcircuit(load,resultViewer,coductor)

Información requerida en el módulo dbcircuitcd
==============================================

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
