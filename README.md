<img src="https://warehouse-camo.ingress.cmh1.psfhosted.org/07dd58e07a7999d21a7006484b86782e8c006192/68747470733a2f2f692e6962622e636f2f6a5652506e70482f456c656374726963616c2d576972652d53697a657330312e6a7067" alt="kElectric" style="zoom: 100%;" />

[![PyPI version](https://badge.fury.io/py/ElectricalWireSizes.svg)](https://badge.fury.io/py/ElectricalWireSizes) [![Downloads](https://static.pepy.tech/personalized-badge/electricalwiresizes?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/electricalwiresizes) [![Downloads](https://pepy.tech/badge/electricalwiresizes/month)](https://pepy.tech/project/electricalwiresizes) [![versons of python supported](https://img.shields.io/badge/python-3%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://pypi.org/project/ElectricalWireSizes/) [![Maintainability](https://api.codeclimate.com/v1/badges/27c48038801ee954796d/maintainability)](https://codeclimate.com/github/jacometoss/PyEWS/maintainability)[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8d8575adf7e149999e6bc84c657fc94e)](https://www.codacy.com/gh/jacometoss/PyEWS/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jacometoss/PyEWS&amp;utm_campaign=Badge_Grade)

# Python Electrical Wire Sizes 

[Electrical Wires Sizes](https://pyews.readthedocs.io/) es una librería hecha en el lenguaje de programación Python y fue creada con la finalidad de acortar el tiempo en el dimensionamiento de conductores eléctricos u obtención de las secciones de los conductores de una instalación eléctrica.

Esta idea nace debido a la popularidad del lenguaje de programación Python y buscar una aplicación de este lenguaje dentro del área de ingeniería eléctrica en la especialidad de diseño de instalaciones eléctricas. En la práctica esta librería le será útil cuando trate de dimensionar una cantidad considerable de alimentadores como circuitos derivados.

La librería cuenta por el momento con **9 módulos** que internamente son llamados para realizar el dimensionamiento de conductores en baja tensión para conductores comerciales de 600 V hasta 2000 V, los resultados obtenidos se muestran en forma matricial o tabla para una mejor comprensión de los resultados.

La dependencia de este lenguaje de otros paquetes es baja únicamente usa `tabulate` en primer grado y en forma muy secundaría `numpy` y `matplotlib` no encontrándose limitado por el momento a una versión. Estas últimas dos librerías se usan para graficar las pérdidas de tensión de los conductores de corriente alterna.

La versión disponible la puedes consultar mediante  :

```python
version()
```

## [Donativos](https://ko-fi.com/jacometoss) 

**¿Te gusta este proyecto?, puedes apoyarme mediante**

La vida es como una batería y en cada momento uno va perdiendo una pequeña parte de esta cada día, puedes apoyarme en el desarrollo de este proyecto y motivar aún más mi creatividad para que sea de gran utilidad esta herramienta. Puedes contactarme si desconoces del medio proporcionado pero se basa en el sistema de pagos de PayPal.

[El apoyo es mediante un café :](https://ko-fi.com/jacometoss)

           ─▄▀─▄▀
           ──▀──▀
           █▀▀▀▀▀█▄
           █░░░░░█─█
           ▀▄▄▄▄▄▀▀
       Url para donativos      
    https://ko-fi.com/jacometoss                     

Este donativo es mínimo pero ayuda a mi creatividad, realmente la mínima cantidad es de $2 dólares.

## Instalación

La instalación del paquete se realiza mediante la instrucción siguiente :

```Python
pip install ElectricalWireSizes
```

## PyEWS Módulos

Los módulos disponibles por el momento para esta versión son los siguientes :

| Id   | Descripción                                                  | Módulo        |
| :--- | :----------------------------------------------------------- | :------------ |
| 1    | Módulo para conductores de cobre clase B, C y D tensión de 600V a 2000V. | mbtcu()       |
| 2    | Módulo para conductores de aluminio clase B, C y D, tensión 600V a 2000V. | mbtal()       |
| 3    | Módulo para conductores de cobre clase B, C y D en CD hasta 2000 V. | mbtcustd()    |
| 4    | Módulo para el cálculo de impedancia, conductores de cobre.  | zpucu()       |
| 5    | Módulo para el cálculo de impedancia, conductores de aluminio. | zpual()       |
| 6    | Módulo para dimensionar múltiples conductores de cobre y aluminio., corriente alterna. | dbcircuit()   |
| 7    | Módulo para dimensionar múltiples conductores de cobre, corriente directa. | dbcircuitcd() |
| 8    | Módulo para graficar resultados                              | graph()       |
| 9    | Módulo de Icc para conductores de cobre y aluminio           | icc()         |

## Test básico

En el ejemplo siguiente vamos a realizar un pequeño calculo donde es usado el módulo `mbtcu`.

```python
mbtcu(120,220,15,1,10,1,1,35,3,1,0.9,1,1.00,60)
```

Los resultados  se muestran con la iteración de todos los conductores tanto para tensión monofásica como trifásica, recordando que debe seleccionar el sistema como la cantidad de pérdida de tensión permitida.

- `Vd (Voltage Drop)` es la pérdida de tensión porcentual 

- `60,75,90` la ampacidad real de los conductores.

- `Nc` es el número de conductores por fase.

- `Op` muestra si el resultado es correcto al aparecer en la columna la palabra en ingles  `Yes` .

- `ITM` es la protección del circuito.

  Se puede observar en la columna  `%VD 1F-2H` seleccionada, la pérdida de tensión es aceptable con respecto a la mínima ingresada del `%3`. La confirmación de un resultado aceptable se visualiza en la columna `OP` .  Al utilizar la opción de múltiples cargas podrá mostrar el resumen y el desglose como se muestra en la tabla.

![ElectricalWireSizes0.1.23](https://i.ibb.co/yVPWvxN/k-Electric-0-1-23.jpg)

El circuito marcado en amarillo es la solución para realizar un resumen use la opción múltiples cargas.

## Base de datos de conductores

Para poder ampliar el módulo se agregó la tabla de conductores donde incluye las resistencias y reactancias como ampacidades. Ingrese el código mostrado para visualizar la tabla completa.

```python
dbc(1)
```

## Impedancia unitaria 

Para obtener las constantes únicamente utilice las líneas siguientes 

```python
#ZpuCu(Type,Ta,Fp,View)
zpucu(1,10,0.9,1) 
#ZpuAl(Type,Ta,Fp,View)
zpual(1,10,0.9,1) 
```

<img src="https://i.ibb.co/D1syMzL/Zpu.jpg" alt="Zpu" style="zoom:70%;" />

## Graficar resultados

Mediante  `matplotlib` y`numpy`  es posible obtener gráficos, la instalación de esta librería es automática al instalar  `ElectricalWireSizes`.

Es posible graficar los resultados de pérdida de tensión de un único cálculo por el momento como se muestra en la figura siguiente :

![graph](https://i.ibb.co/XFzQyZJ/Graph2.jpg)

Esta limitado para conductores en corriente alterna, el procedimiento para generar la figura es mediante :

```python
mydata=mbtal(127,220,55,1,45,1,1,35,3,1,0.9,2,1)
graph(mydata,"6 AWG","4/0 AWG", 8, 5, 2,"k",1)
```

El llenado del módulo es un poco complejo

- Realice un cálculo para conductores de cobre, en el ejemplo se guardo en  `mydata` .
- Llamamos al módulo llenamos como se indica 

```python
graph(mydata,"Calibre Inicial","Calibre Final", Ancho, Alto, Aluminio/Cobre, "Color",Sistema)
```

Los calibres deben ir como se muestra en los resultados y entre comillas dobles indicando un conductor inicial y final disponible, el ancho y alto son pulgadas en formato `integer` o `float`. Dependiendo el material del conductor (`1:Cobre, 2:Aluminio`) y el color de las barras puede usar `k: negro`, `b: azul`, `g:verde`, `r:rojo` que son estándar en reportes, finalmente el sistema `1:1F-2H`,`2:2F-3H`,`3:3F-3H` y `4:3F:4H`.

No olvide que el arreglo de datos  `mydata` debe ser correcto y definido.

## Nivel de corto circuito en conductores 

En esta versión (0.1.22) se incluye el cálculo del corto circuito de los conductores de cobre y aluminio en corriente alterna. Únicamente por el momento sirve de consulta para  determinar si el conductor.

Una forma sencilla de ingresar a este módulo usando la línea siguiente :

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

Un ejemplo práctico de las corriente de corto circuito para los conductores comerciales es :

```python
icc(1,75,200,60,1)
```

![](https://i.ibb.co/PwpdbTj/nivel-corto-circuito-conductores-cobre-aluminio.jpg)

> En forma práctica los termoplásticos como lo son el **PVC** tienen temperatura en corto circuito de 105,130,150 para las temperaturas de operación continua de 60,75,90. Los termoestables **XLPE**  y **EPR** en corto circuito usan temperaturas de 250 cada uno para una temperatura de operación continua de 90 °C.

## Desarrollador y versión

La presente versión tiene corrección de entrada de parámetros como ampliación de la base de datos y corrección de errores mínimos dentro de algunas estructuras del  paquete.

```text
[Packqge]: ElectricalWireSizes 0.1.23
[Autor]: Marco Polo Jácome Toss
[Licencia]: GNU General Public License v3.0
[Fecha]: 20-Octubre-2021
[Páis]: México
```

## Referencias

[1] Norma Oficial Mexicana NOM-001-SEDE-2012, *Instalaciones Eléctricas (utilización)*

[2] Thue, W., 1978. *Electrical Power Cable Engineering*. 2nd ed. New York, Basel: Marcel Dekker Inc., p.34.

[3] Norma Oficial Mexicana NOM-001-SEDE-2018, *Instalaciones Eléctricas (utilización)*

