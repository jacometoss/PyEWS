|image1| |image2| |image3| |image4| |image5| |image6|

Python Electrical Wire Sizes 
============================

El módulo Python Electrical Wire Sizes ( **Versión 0.1.21**) puede ser
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

El módulo tiene dependencias siendo necesario instalar ``tabulate`` (se
instala en forma automática) el cual sirve para dar una mejor apariencia
al momento de mostrar los resultados.

Antes de iniciar a usar los módulos debe importar el paquete\ ``PyEWS``
.

.. code:: python

   import PyEWS

La importación de la librería ``PyEWS`` se hace de manera única al
iniciar un archivo y para arrancar cada módulo debe anteponer ``PyEWS``.
En este ejemplo importaremos el módulo de baja tensión para conductores
de cobre, no mostraremos el llenado de este módulo únicamente el orden
de llamado.

.. code:: python

   PyEWS.mbtcu()

De esta manera sencilla podemos iniciar cada uno de los módulos
mostrados en la tabla mostrada anteriormente. En los puntos siguientes
se verá como llenar correctamente cada uno de los módulos y que
resultado se muestra en cada uno de ellos

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
