![ElectricalWireSizes](https://raw.githubusercontent.com/jacometoss/PyEWS/2d9a120c2e96200550d415797cd04340050112e0/docs/logoElectricalWireSizes.svg)

[![PyPI version](https://badge.fury.io/py/ElectricalWireSizes.svg)](https://badge.fury.io/py/ElectricalWireSizes) [![Downloads](https://static.pepy.tech/personalized-badge/electricalwiresizes?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/electricalwiresizes) [![Downloads](https://pepy.tech/badge/electricalwiresizes/month)](https://pepy.tech/project/electricalwiresizes) [![versons of python supported](https://img.shields.io/badge/python-3%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://pypi.org/project/ElectricalWireSizes/) [![Maintainability](https://api.codeclimate.com/v1/badges/27c48038801ee954796d/maintainability)](https://codeclimate.com/github/jacometoss/PyEWS/maintainability)[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8d8575adf7e149999e6bc84c657fc94e)](https://www.codacy.com/gh/jacometoss/PyEWS/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jacometoss/PyEWS&amp;utm_campaign=Badge_Grade)

# **Electrical Wire Sizes** 

[Electrical Wires Sizes](https://electricalwiresizes.org/) es una librería hecha en el lenguaje de programación Python creada con la finalidad de acortar el tiempo en el dimensionamiento de conductores eléctricos u obtención de las secciones de los conductores de una instalación eléctrica.

Esta idea nace debido a la popularidad del lenguaje de programación Python y en la búsqueda de una aplicación en relación a este lenguaje dentro del área de ingeniería eléctrica. En la práctica esta librería le será útil cuando trate de dimensionar una cantidad considerable de alimentadores como circuitos derivados.

La librería cuenta por el momento con **9 módulos** que internamente son llamados para realizar el dimensionamiento de conductores en baja tensión especialmente conductores comerciales con aislamiento de 600 V hasta 2000 V.  Los resultados obtenidos con este paquete es posible obtenerlos en forma matricial o en formato tabla para una mejor comprensión.

La dependencia de este lenguaje de otros paquetes es baja únicamente usa `tabulate` en primer grado y en forma muy secundaría `numpy` y `matplotlib` no encontrándose limitado a una versión en especifico, estas últimas dos librerías se usan para graficar las pérdidas de tensión en los conductores cuando se utiliza corriente alterna.

La versión disponible de este paquete puede ser consultada con el bloque siguiente:

```python
version()
```

## **[Donativos](https://ko-fi.com/jacometoss)** 

**¿Te gusta este proyecto?, puedes apoyarme mediante**

La vida es como una batería y en cada momento uno va perdiendo una pequeña parte de esta cada día, puedes apoyarme en el desarrollo de este proyecto y motivar aún más mi creatividad para que sea de gran utilidad esta herramienta. Puedes contactarme si desconoces del medio proporcionado pero se basa en el sistema de pagos de PayPal.

[El apoyo es en forma representativa al precio de un café :](https://ko-fi.com/jacometoss)

           ─▄▀─▄▀
           ──▀──▀
           █▀▀▀▀▀█▄
           █░░░░░█─█
           ▀▄▄▄▄▄▀▀
       Url para donativos      
    https://ko-fi.com/jacometoss                     

Este donativo apoya este proyecto, la mínima cantidad aceptada es de $2 dólares algo prácticamente insignificante para algo de este nivel, espero puedas apoyar donando.

## **Instalación**

La instalación del paquete se realiza mediante la instrucción siguiente:

```Python
pip install ElectricalWireSizes
```

## **Módulos**

En la tabla que se muestra a continuación contiene los módulos disponibles los cuales son:

| **Id** | **Descripción**                                              | **Módulo**                                                   |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1      | Módulo de baja tensión (c.a.) para conductores de cobre en clase B, C y D,  tensión máxima de servicio de 600V a 2000V. | [mbtcu()](https://electricalwiresizes.org/mbtcu.html)        |
| 2      | Módulo de baja tensión (c.a.) para conductores de aluminio clase B, C y  D, tensión máxima de servicio de 600V a 2000V. | [mbtal()](https://electricalwiresizes.org/mbtal.html)        |
| 3      | Módulo de baja tensión (c.d.) para conductores de cobre clase B, C  y D, tensión máxima de servicio hasta 2000 V. | [mbtcustd()](https://electricalwiresizes.org/mbtcustd.tml)   |
| 4      | Módulo para el cálculo de la impedancia en conductores de cobre. | [zpucu()](https://electricalwiresizes.org/zpucu.html)        |
| 5      | Módulo para el cálculo de la impedancia en conductores de aluminio. | [zpual()](https://electricalwiresizes.org/zpual.html)        |
| 6      | Módulo para dimensionar múltiples conductores de cobre y aluminio en tensión alterna. | [dbcircuit()](https://electricalwiresizes.org/dbcircuit.html) |
| 7      | Módulo para dimensionar múltiples conductores de cobre en tensión de directa. | [dbcircuitcd()](https://electricalwiresizes.org/dbcircuitcd.html) |
| 8      | Módulo para graficar resultados.                             | [graph()](https://electricalwiresizes.org/graph.html)        |
| 9      | Módulo de corto circuito (Icc) para conductores de cobre y aluminio. | [icc()](https://electricalwiresizes.org/icc.html)            |

## **Base de datos de conductores**

Para poder ampliar el paquete se agregó la tabla de conductores donde se incluye las resistencias, reactancias y ampacidades. Ingrese el bloque de código mostrado para visualizar la tabla completa.

```python
dbc(1)
```

## **Graficar resultados**

Mediante el uso de  `matplotlib` y`numpy`  es posible obtener un gráfico de la pérdida de tensión en los conductores de cobre o aluminio cuando se utiliza tensión alterna.

El gráfico que se muestra a continuación presenta las pérdidas de tensión de los conductores del calibre #6 hasta el calibre #4/0 cuando se utiliza el sistema de una fase dos hilos.

![graph](https://i.ibb.co/XFzQyZJ/Graph2.jpg)

Este módulo esta limitado por el momento para conductores de cobre y aluminio cuando se utiliza tensión alterna. El procedimiento para generar el gráfico anterior es usando el bloque de código siguiente:

```python
mydata=mbtal(127,220,55,1,45,1,1,35,3,1,0.9,2,1,1,1)
graph(mydata,"6 AWG","4/0 AWG", 8, 5, 2,"k",1)
```

El llenado del módulo es un poco complejo

- Se realiza un cálculo con el módulo  `mbtcu`  o  `mbtal` y el resultado se guarda en  `mydata` .
- Llamamos al módulo `graph` como se muestra a continuación: 

```python
graph(mydata,"Calibre Inicial","Calibre Final", Ancho, Alto, Aluminio/Cobre, "Color",Sistema)
```

Los calibres deben ir como se muestra en el bloque anterior y entre comillas dobles indicando un conductor inicial y final dentro del rango disponible, el ancho y alto del gráfico debe estar en pulgadas en formato `integer` o `float`. Dependiendo el material del conductor (`1:Cobre, 2:Aluminio`) el color de las barras disponible puede ser `k: negro`, `b: azul`, `g:verde`, `r:rojo` que son estándar en reportes no obstante puede usar otros disponibles en la paleta de colores de `matplotlib` .Finalmente, seleccione el sistema `1:1F-2H`,`2:2F-3H`,`3:3F-3H` y `4:3F:4H`.

No olvide que el arreglo de datos `mydata` debe ser correcto y definido.

## **Corto circuito en conductores** 

En la versión (0.1.22) se incluye el cálculo del corto circuito de los conductores de cobre y aluminio en corriente alterna el cual sirve para dimensionar un conductor en estado de corto circuito.

Una forma sencilla de ingresar a este módulo se especifica en el bloque de código siguiente:

```text
icc(conductor,t1,t2,fhz,view)
#conductor: Material conductor.
---- 1:(1F-2H) 2:(2F-3H) 3:(3F-3H) 4:(3F-4H)
#t1: Temperatura de operación en °C.
#t2: Temperatura de corto circuito en °C.
#fhz: Frecuencia 50hz o 60hz.
#view: Modo de visualizar
---- 1:(Tabla) 2:(Lista)
```

Un ejemplo práctico de las corriente de corto circuito para los conductores comerciales de material de cobre se muestra en el bloque siguiente:

```python
icc(1,75,200,60,1)
```

![](https://i.ibb.co/PwpdbTj/nivel-corto-circuito-conductores-cobre-aluminio.jpg)

> En forma práctica los termoplásticos como lo es el **PVC** tienen temperatura de operación en corto circuito de 105,130,150 centígrados y en condiciones  normales de 60,75,90 centígrados. Los termoestables **XLPE**  y **EPR** en corto circuito usan temperaturas de 250 cada uno para una temperatura de operación continua de 90 °C.

## Desarrollador y versión

La versión 0.1.28 es por el momento la más reciente. 

```text
[Packqge]: ElectricalWireSizes 0.1.28
[Autor]: Marco Polo Jácome Toss
[Licencia]: GNU General Public License v3.0
[Fecha]: 15-Junio-2022
[Páis]: México
```

## **Control de versiones (Changelog)**

**0.1.28**: Versión estable.

**0.1.28rc2**: Separación de operaciones, conductor y protección.

**0.1.28rc1** - En esta versión se actualiza las protecciones y se actualiza la fórmula de corriente incluyendo el factor de sobrecorriente en la versión 0.1.27 no se logra ver la actualización de la corriente nominal. [*01.06.2022*]

**0.1.27** - Versión estable. [*20.04.2022*]

**0.1.27rc3** - En esta versión los módulos se han clasificado e independizado en distintos archivos, además se mejora la salida de datos del módulo `dbcircuit` para funciones futuras. [*20.04.2022*]

**0.1.27rc2** - Corrección de  fechas de actualización de módulos. Los módulos `mbtcustd`, `dbcircuitcd` fueron modificados conforme a los requerimientos de protección y capacidad de corriente de los conductores.  [*19.03.2022*]

**0.1.27rc1** - Presenta un nuevo campo para el ajuste de la protección conforme a la NOM-001-SEDE-2012 de instalaciones eléctricas. Los módulos que sufrieron cambios son: `mtbcu` ,`mbtal`, `dbcircuit` conforme a los requerimientos de protección y capacidad de conductores.  [*13.03.2022*]





```mermaid

graph TD

B[ElectricalWireSizes]-->db[(Database)]
	db -->|load| A[mbtcu]-->|result| I[graph]
    db -->|load| C[mbtal]-->|result| I[graph]	
    db -->|load| D[mbtcustd]
    db -->|parameters| E[zpucu]
    db -->|parameters| F[zpual]
    db -->|parameters| J[icc]
    db -->|loads| G[dbcircuit] --> H[[Subroutine]]
    H -->|loads| k[mbtcu]--> id1>Not Graph]
    H -->|loads| l[mbtcu]--> id1>Not Graph]
    

```

## **Referencias**

**[1]** Norma Oficial Mexicana NOM-001-SEDE-2012, Instalaciones Eléctricas (utilización)

**[2]** Thue, W., 1978. Electrical Power Cable Engineering. 2nd ed. New York, Basel: Marcel Dekker Inc., p.34.

**[3]** Norma Oficial Mexicana NOM-001-SEDE-2018, Instalaciones Eléctricas (utilización)

## **Copyright**

Copyright © 2020 en adelante, Marco Polo Jácome Toss (http://electricalwiresizes.org).

Este programa es software libre: usted puede redistribuirlo y /o modificarlo bajo los términos de la Licencia General GNU (GNU General Public License) publicado por la Fundación para el Software Libre para la versión 3 de dicha Licencia o anterior, o cualquier versión posterior.

Este programa se distribuye con la esperanza de que sea útil pero sin ninguna garantía; incluso sin la garantía implícita de comercialización o idoneidad para  un propósito en particular.

Vea la información de Licencia de `ElectricalWireSizes` para más detalle.

------

Copyright © 2020  en adelante, [ElectricalWireSizes](https://electricalwiresizes.org/)

