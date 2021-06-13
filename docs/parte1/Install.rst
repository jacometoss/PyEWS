| |image1|
| |image2|
| |image3|
| |image4|
| |image5|\ |image6|

Python Electrical Wire Sizes 
============================

El módulo Python Electrical Wire Sizes ( **Versión 0.1.19**) puede ser
utilizado para dimensionar los conductores de alimentadores en baja
tensión como los circuitos derivados de una instalación eléctrica. Esta
herramienta es muy útil para ingenieros y arquitectos sumergidos en la
rama de proyectos eléctricos y aquellos conocedores de algunos conceptos
aquí mostrados que desean aprender temas relacionados como este.

Instalación del paquete
-----------------------

La instalación del paquete se realiza con la línea siguiente

.. code:: python

   pip install ElectricalWireSizes

Módulos
-------

La lista de módulos disponibles en el paquete en esta última versión son

+----+-------------------------------------------------+-------------+
| Id | Descripción                                     | Módulo      |
+====+=================================================+=============+
| 1  | Módulo de baja tensión para conductores de      | mbtcu       |
|    | cobre clase B, C y D tensión de 600V a 2000V    |             |
+----+-------------------------------------------------+-------------+
| 2  | Módulo de baja tensión para conductores de      | mbtal       |
|    | aluminio clase B, C y D, tensión 600V a 2000V   |             |
+----+-------------------------------------------------+-------------+
| 3  | Módulo de baja tensión para conductores de      | mbtcustd    |
|    | cobre clase B, C y D en corriente directa hasta |             |
|    | 2000 V                                          |             |
+----+-------------------------------------------------+-------------+
| 4  | Base de datos de conductores eléctricos         | dbc         |
+----+-------------------------------------------------+-------------+
| 5  | Cambio de resistencia en conductores de cobre   | zpucu       |
+----+-------------------------------------------------+-------------+
| 6  | Cambio de resistencia en conductores de         | zpual       |
|    | aluminio                                        |             |
+----+-------------------------------------------------+-------------+
| 7  | Múltiples circuitos para conductores de cobre y | dbcircuit   |
|    | aluminio                                        |             |
+----+-------------------------------------------------+-------------+
| 8  | Múltiples circuitos para conductores de cobre   | dbcircuitcd |
+----+-------------------------------------------------+-------------+

Todos los módulos trabajan con unidades del Sistema Internacional y en
versiones futuras versiones se incluirá el Sistema Ingles

Iniciar paquete y módulo
------------------------

El módulo tiene dependencias siendo necesario instalar ``tabulate`` (se
instala en forma automática) el cual sirve para dar una mejor apariencia
al momento de mostrar los resultados.

Antes de iniciar a usar los módulos debe importar el
paquete\ ``kelectric`` .

.. code:: python

   import kelectric

La importación de la librería ``kelectric`` se hace de manera única al
iniciar un archivo y para arrancar cada módulo debe anteponer
``kelectric``. En este ejemplo importaremos el módulo de baja tensión
para conductores de cobre, no mostraremos el llenado de este módulo
únicamente el orden de llamado.

.. code:: python

   kelectric.mbtcu()

De esta manera sencilla podemos iniciar cada uno de los módulos
mostrados en la tabla mostrada anteriormente. En los puntos siguientes
se verá como llenar correctamente cada uno de los módulos y que
resultado se muestra en cada uno de ellos

Esta obra está bajo una Licencia Creative Commons
Atribución-CompartirIgual 4.0 Internacional.

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
