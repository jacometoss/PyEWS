def changelog():
    print("""
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    | PYEWS, ElectricalWireSizes, 20/02/2023                                 |
    | Version : 0.1.30                                                       |
    | Autor : Marco Polo Jacome Toss                                         |
    | License: GNU Affero General Public License v3 (GPL-3.0)                |
    | Requires: Python >=3.5                                                 |
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    Changelog:

    0.1.30  : Versión estable. Incluye un nuevo módulo para calcular pérdidas de tensión en 
              distintos puntos de caga y se agrega la opción de capacidad de corriente en los 
              conductores para los módulos `mbtcu()` y  `mbtal()`. Además, se actualizan las 
              protecciones del módulo `mbtcustd()`.  

    0.1.30rc1: Se modifica y clasifica las protecciones por sistema, descartando
            las no comerciales.

    0.1.29   : Versión estable, en esta nueva actualización se agrega al módulo
               graph una línea indicadora de pérdida de tensión.

    0.1.29rc1: Se modifican los módulos mbtcu, mbtal, mbtcustd, dbcircuit, dbcircuitcd
               adicionando un nuevo argumento Fcond y condiciones para el cumplimento
               del 125% de ampacidad en alimentadores y circuitos derivados sin considerar
               cualquier factor de ajuste. Todas las versiones anteriores no cuentan con
               esta condición y esto puede causar error cuando se tienen las condiciones
               ideales en un conductor, sin agrupar y a temperatura ambiente de 30°C.

    0.1.28   : Versión estable.

    0.1.28rc2: Separación de operaciones entre conductor y protección.

    0.1.28rc1: En esta versión se actualiza las protecciones y la fórmula de corriente 
               incluyendo el factor de sobrecorriente. En la versión 0.1.27 no se logra 
               ver la actualización de la corriente nominal en la lista o tabla.

    0.1.27rc3: En esta versión los módulos se han clasificado e independizado
               en distintos archivos además se mejora la salida de datos
               del módulo dbcircuit para funciones futuras.

    0.1.27   : Versione estable.

   0.1.27rc2 : Corrección en las fechas de actualización en módulos. Los módulos mbtcustd, 
               dbcircuitcd fueron modificados conforme a los requerimientos de protección y 
               capacidad de corriente de los conductores.

   0.1.27rc1 : Esta versión presenta un nuevo campo para el ajuste de la protección conforme a 
               la NOM-001-SEDE-2012 de Instalaciones Eléctricas. Los módulos que sufrieron cambios 
               son: mtbcu , mbtal, dbcircuit conforme a los requerimientos de protección y capacidad 
               de conductores.
    """)