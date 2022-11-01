|image1| |image2| |image3| |image4| |image5| |image6|

Electrical Wire Sizes 
=====================

El módulo Python Electrical Wire Sizes puede ser
utilizado para dimensionar los conductores de alimentadores en baja
tensión como los circuitos derivados de una instalación eléctrica. Esta
herramienta es muy útil para ingenieros y arquitectos sumergidos en la
rama de proyectos eléctricos y aquellos conocedores de algunos conceptos
aquí mostrados que desean aprender temas relacionados como este.

Instalación del paquete
-----------------------

La instalación del paquete se realiza con la línea siguiente :

.. code:: python

   pip install ElectricalWireSizes

PyEWS Módulos
-------------

Los módulos disponibles por el momento son los siguientes :

+---+---------------------------------+---------------------------------+
|id | **Descripción**                 | **Módulo**                      |
|   |                                 |                                 |
+===+=================================+=================================+
| 1 | Módulo de baja tensión (c.a.)   | `mbtcu() <https://electri       |
|   | para dimensionar conductores de | calwiresizes.org/mbtcu.html>`__ |
|   | cobre en clase B, C y D,        |                                 |
|   | tensión máxima de servicio de   |                                 |
|   | 600V a 2000V.                   |                                 |
+---+---------------------------------+---------------------------------+
| 2 | Módulo de baja tensión (c.a.)   | `mbtal() <https://electri       |
|   | para dimensionar conductores de | calwiresizes.org/mbtal.html>`__ |
|   | aluminio clase B, C y D,        |                                 |
|   | tensión máxima de servicio de   |                                 |
|   | 600V a 2000V.                   |                                 |
+---+---------------------------------+---------------------------------+
| 3 | Módulo de baja tensión (c.d.)   | `mbtcustd() <https://electrica  |
|   | para dimensionar conductores de | lwiresizes.org/mbtcustd.tml>`__ |
|   | cobre clase B, C y D, tensión   |                                 |
|   | máxima de servicio hasta 2000   |                                 |
|   | V.                              |                                 |
+---+---------------------------------+---------------------------------+
| 4 | Módulo de impedancia en         | `zpucu() <https://electri       |
|   | conductores de cobre.           | calwiresizes.org/zpucu.html>`__ |
+---+---------------------------------+---------------------------------+
| 5 | Módulo de impedancia en         | `zpual() <https://electri       |
|   | conductores de aluminio.        | calwiresizes.org/zpual.html>`__ |
+---+---------------------------------+---------------------------------+
| 6 | Módulo para dimensionar         | `d                              |
|   | múltiples conductores de cobre  | bcircuit() <https://electricalw |
|   | y aluminio en tensión alterna.  | iresizes.org/dbcircuit.html>`__ |
+---+---------------------------------+---------------------------------+
| 7 | Módulo para dimensionar         | `dbcir                          |
|   | múltiples conductores de cobre  | cuitcd() <https://electricalwir |
|   | en tensión de directa.          | esizes.org/dbcircuitcd.html>`__ |
+---+---------------------------------+---------------------------------+
| 8 | Módulo de gráficas de barras.   | `graph() <https://electri       |
|   |                                 | calwiresizes.org/graph.html>`__ |
+---+---------------------------------+---------------------------------+
| 9 | Módulo de corto circuito (Icc)  | `icc() <https://elect           |
|   | para conductores de cobre y     | ricalwiresizes.org/icc.html>`__ |
|   | aluminio.                       |                                 |
+---+---------------------------------+---------------------------------+

Todos los módulos trabajan con unidades del Sistema Internacional y en
versiones futuras versiones se incluirá el Sistema Ingles

Iniciar paquete y módulo
------------------------

El módulo tiene dependencias siendo necesario instalar ``tabulate``el cual sirve para dar 
una mejor apariencia al momento de mostrar los resultados y no mostrar un arreglo
común como en los lenguajes de programación.

Antes de iniciar a usar los módulos debe importar el paquete.

En este ejemplo importaremos el módulo de baja tensión para conductores
de cobre, no se muestra el llenado de este módulo únicamente la llamada.

.. code:: python

   mbtcu()

De esta manera sencilla podemos iniciar cada uno de los módulos
mostrados al inicio (`Tabla`_). En los puntos siguientes
se verá como llenar correctamente cada uno de los módulos y que
resultado se muestra en cada uno de ellos

.. note::
   Existe diferentes formas de importar un módulo o módulos

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
   
.. _Tabla: https://pyews.readthedocs.io/parte1/Install.html
