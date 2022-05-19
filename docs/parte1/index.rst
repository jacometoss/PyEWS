Electrical Wire Sizes (Español)
===============================
|image8|

|image1|\ |image2|\  |image3|\  |image4|\ |image5|\  |image6|



Electrical Wires Sizes es una librería hecha en el lenguaje de programación Python creada con la finalidad de acortar el tiempo en el dimensionamiento de conductores eléctricos u obtención de las secciones de los conductores de una instalación eléctrica.

Esta idea nace debido a la popularidad del lenguaje de programación Python y establecer un paquete para este lenguaje dentro del área de ingeniería eléctrica en la especialidad de diseño de instalaciones eléctricas. En la práctica esta librería le será útil cuando trate de dimensionar una cantidad considerable de alimentadores como de circuitos derivados.

La librería cuenta por el momento con 9 módulos para dimensionar conductores eléctricos con aislamiento de 600 V y 2000 V. Los resultados obtenidos con estos módulos los puede visualizar mediante una arreglo matricial o tabla esta para una mejor comprensión de los resultados.

La dependencia de este paquete de otros es baja, únicamente usa ``tabulate`` en primer grado y en forma secundaría ``numpy`` como ``matplotlib``. No se encuentra limitado por el momento a una versión de ``Python3``. Las últimas librerías mencionadas se usan para graficar las pérdidas de tensión de los conductores de corriente alterna con la finalidad de comparar cada uno de los conductores disponibles.

La versión disponible la puedes consular mediante :

.. code:: python

   version()



**Donativos :**
**¿Te gusta este proyecto?, puedes apoyarme mediante . . .**

La vida es como una batería y en cada momento uno va perdiendo una pequeña parte de esta cada día,
puedes apoyarme en el desarrollo de este proyecto y motivar aún más mi creatividad para 
que sea de gran utilidad esta herramienta.

Puedes comprarme un café en forma de donativo en el enlace siguiente : 

|image7|

No es mucho pero sirve de algo para mejorar este proyecto, acepto críticas como sugerencias.


**Contenido**


.. toctree::
    :maxdepth: 11

    Install
    Mbtcu
    Mbtal
    Graph
    Mbtcustd
    Dbc
    Zpucu
    Zpual
    Dbcircuit
    Dbcircuitcd
    Reference
    Denveloped

.. _PyEWS: https://pypi.org/project/ElectricalWireSizes/
.. _ElectricalWireSizes: https://pypi.org/project/ElectricalWireSizes/0.1.21/
.. |image1| image:: https://badge.fury.io/py/ElectricalWireSizes.svg
   :target: https://badge.fury.io/py/ElectricalWireSizes   
.. |image2| image:: https://static.pepy.tech/personalized-badge/electricalwiresizes?period=total&units=international_system&left_color=red&right_color=grey&left_text=Downloads
  :target: https://pepy.tech/project/electricalwiresizes

.. |image3| image:: https://pepy.tech/badge/electricalwiresizes/month
   :target: https://pepy.tech/project/electricalwiresizes
.. |image4| image:: https://img.shields.io/badge/python-3 | 3.5 | 3.6 | 3.7 | 3.8 | 3.9 | 3.10-blue
   :target: https://pypi.org/project/ElectricalWireSizes/
.. |image5| image:: https://api.codeclimate.com/v1/badges/27c48038801ee954796d/maintainability
   :target: https://codeclimate.com/github/jacometoss/PyEWS/maintainability
.. |image6| image:: https://app.codacy.com/project/badge/Grade/8d8575adf7e149999e6bc84c657fc94e
   :target: https://www.codacy.com/gh/jacometoss/PyEWS/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jacometoss/PyEWS&amp;utm_campaign=Badge_Grade

.. |image7| image:: https://ko-fi.com/img/githubbutton_sm.svg
   :target: https://ko-fi.com/B0B356BR4
.. |image8| image:: https://github.com/jacometoss/PyEWS/blob/master/docs/logoElectricalWireSizes.svg
   :target: https://pyews.readthedocs.io/
