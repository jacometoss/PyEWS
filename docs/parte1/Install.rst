|image1| |image2| |image3| |image4| |image5| |image6|

Electrical Wire Sizes 
=====================

El módulo Python Electrical Wire Sizes ( **Versión 0.1.26**) puede ser
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

+----+-----------------------------------------------+---------------+
| Id | Descripción                                   | Módulo        |
+====+===============================================+===============+
| 1  | Módulo de baja tensión para conductores de    | mbtcu()       |
|    | cobre clase B, C y D tensión de 600V a 2000V. |               |
+----+-----------------------------------------------+---------------+
| 2  | Módulo de baja tensión para conductores de    | mbtal()       |
|    | aluminio clase B, C y D, tensión 600V a       |               |
|    | 2000V.                                        |               |
+----+-----------------------------------------------+---------------+
| 3  | Módulo de baja tensión para conductores de    | mbtcustd()    |
|    | cobre clase B, C y D en CD hasta 2000 V.      |               |
+----+-----------------------------------------------+---------------+
| 4  | Módulo para el cálculo de la impedancia para  | zpucu()       |
|    | conductores de cobre.                         |               |
+----+-----------------------------------------------+---------------+
| 5  | Módulo para el cálculo de la impedancia para  | zpual()       |
|    | conductores de aluminio.                      |               |
+----+-----------------------------------------------+---------------+
| 6  | Módulo para dimensionar múltiples conductores | dbcircuit()   |
|    | de cobre y aluminio., corriente alterna.      |               |
+----+-----------------------------------------------+---------------+
| 7  | Módulo para dimensionar múltiples conductores | dbcircuitcd() |
|    | de cobre, corriente directa.                  |               |
+----+-----------------------------------------------+---------------+
| 8  | Módulo para graficar resultados               | graph()       |
+----+-----------------------------------------------+---------------+
| 9  | Módulo de corto circuito para conductores     | icc()         |
|    | en corriente alterna, aluminio y cobre.       |               |    
+----+-----------------------------------------------+---------------+

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
   Las importacion de los módulos puede ser variada.

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
