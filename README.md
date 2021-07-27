<img src="https://i.ibb.co/86M4K2Z/PYEWS.jpg" alt="PyEWS" style="zoom: 100%;" />

[![PyPI version](https://badge.fury.io/py/ElectricalWireSizes.svg)](https://badge.fury.io/py/ElectricalWireSizes) [![Downloads](https://static.pepy.tech/personalized-badge/electricalwiresizes?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/electricalwiresizes) [![Downloads](https://pepy.tech/badge/electricalwiresizes/month)](https://pepy.tech/project/electricalwiresizes) [![versons of python supported](https://img.shields.io/badge/python-3%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://pypi.org/project/ElectricalWireSizes/) [![Maintainability](https://api.codeclimate.com/v1/badges/27c48038801ee954796d/maintainability)](https://codeclimate.com/github/jacometoss/PyEWS/maintainability)[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8d8575adf7e149999e6bc84c657fc94e)](https://www.codacy.com/gh/jacometoss/PyEWS/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jacometoss/PyEWS&amp;utm_campaign=Badge_Grade)

# Python Electrical Wire Sizes 

[Electrical Wires Sizes](https://pyews.readthedocs.io/) es una librería hecha en el lenguaje de programación Python y fue creada con la finalidad de acortar el tiempo en el dimensionamiento de conductores eléctricos u obtención de las secciones de los conductores de una instalación eléctrica.

Esta idea nace debido a la popularidad del lenguaje de programación Python y buscar una aplicación de este lenguaje dentro del área de ingeniería eléctrica en la especialidad de diseño de instalaciones eléctricas. En la práctica esta librería le será útil cuando trate de dimensionar una cantidad considerable de alimentadores como circuitos derivados.

La librería cuenta por el momento con 8 módulos que internamente son llamados para realizar el dimensionamiento de conductores en baja tensión para conductores comerciales de 600 V hasta 2000 V, los resultados obtenidos se muestran en forma matricial o tabla para una mejor comprensión de los resultados.

La dependencia de este lenguaje de otros paquetes es baja únicamente usa `tabulate` en primer grado y en forma muy secundaría `numpy` y `matplotlib` no encontrándose limitado por el momento a una versión. Estas últimas dos librerías se usan para graficar las pérdidas de tensión de los conductores de corriente alterna.

La versión disponible la puedes consular mediante :

```python
import PyEWS
PyEWS.version()
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

## Iniciar paquete de instalación

El módulo tiene dependencias siendo necesario instalar `tabulate` el cual da una mejor apariencia al momento de mostrar los resultados, la instalación es automática de este paquete. La información que se muestra en el bloque son algunas de las variables de llenado para cada uno de los módulos.

```tex
#VF: Tensión de fase o en su defecto tensión de línea para sistemas de 1F2H, 2F.
#VL: Tensión de línea.
#In: Corriente nominal total de una de las fases.
#Nc: Número de conductores por fase.
#L : Longitud en metros.
#FA: Número de conducrtores activos en el tubo conduit.
#Type: Tipo de tubo conduit (1:PVC,2:AL,3:ACERO)
#Ta: Temperatura ambiente en centigrados.
---- Valor númerico de temperatura, por ejemplo 30°C.
#Vd: Caída de tensión (porcentual de 2, 3, 5)
---- 2,3,5	
#S:  Seleccione el sistema que desea propner en base a este se muestran los resultados.
---- 1:(1F-2H) 2:(2F-3H) 3:(3F-3H) 4:(3F-4H)
#Fp: Factor de potencia
#Op: Opción para mostrar resultados
	 1: Mostrar los resultados adecuadamente estructurado en una tabla. 
	 2: Mostrar los resultados como datos acumulados. Esta opción es necesario cuando se activa
	 	la función para múltiples cargas.
#Fsc: Factor de sobrecorriente (1.25,1.0)
```

Esta es la estructura básica de llenado de los módulos de bata tensión para conductores de cobre y aluminio en corriente alterna.

```python
import PyEWS
#Para conductores de cobre
PyEWS.mbtcu(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc)
#Para conductores de aluminio
PyEWS.mbtal(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc)
```

El módulo de corriente directa  necesita la información siguiente :

```python
#modbtcustd(Vcd,In,Nc,L,Class,Ta,Vd,View,Fsc):

#Vcd   :  Tensión en corriente directa.
#In    :  Corriente directa del circuito.
#Nc    :  Número de conductores en corriente directa.
#L     :  Longitud del circuito en metros.
#Class :  Clase de conductor A:1 B:2 y C:3.
#Ta	   :  Temperatura ambiente 
#Vd	   :  Caída de tensión.
#View  :  Mostrar los resultados adecuadamente en una tabla con 1 para multiples cargas debe ser 2.
#Fsc   :  Factor de sobrecorrriente

PyEWS.mbtcustd(1200,145,1,100,1,25,3,1,1.25)
```

## PyEWS Módulos

Los módulos disponibles por el momento son los siguientes :

| Id   | Descripción                                                  | Módulo        |
| ---- | ------------------------------------------------------------ | ------------- |
| 1    | Módulo de baja tensión para conductores de cobre clase B, C y D  tensión de 600V a 2000V. | mbtcu()       |
| 2    | Módulo de baja tensión para conductores de aluminio clase B, C y  D, tensión 600V a 2000V. | mbtal()       |
| 3    | Módulo de baja tensión para conductores de cobre clase B, C  y D en CD hasta 2000 V. | mbtcustd()    |
| 4    | Módulo para el cálculo de la impedancia para conductores de cobre. | zpucu()       |
| 5    | Módulo para el cálculo de la impedancia para conductores de aluminio. | zpual()       |
| 6    | Módulo para dimensionar múltiples conductores de cobre y aluminio., corriente alterna. | dbcircuit()   |
| 7    | Módulo para dimensionar múltiples conductores de cobre, corriente directa. | dbcircuitcd() |
| 8    | Módulo para graficar resultados                              | graph()       |

## Test

En el ejemplo siguiente vamos a realizar un pequeño calculo donde es usado el módulo `mbtcu`.

```python
from PyEWS import mbtcu
mbtcu(127,220,15,1,22,1,1,35,3,1,0.9,1,1.25)
```

Los resultados  se muestran con la iteración de todos los conductores tanto para tensión monofásica como trifásica, recordando que debe seleccionar el sistema como la cantidad de pérdida de tensión permitida.

- `Vd (Voltage Drop)` es la pérdida de tensión porcentual 

- `60,75,90` la ampacidad real de los conductores.

- `Nc` es el número de conductores por fase.

- `Op` muestra si el resultado es correcto al aparecer en la columna la palabra en ingles  `Yes` .

- `ITM` es la protección del circuito.

  Se puede observar en la columna  `%VD 1F-2H` seleccionada, la pérdida de tensión es aceptable con respecto a la mínima ingresada del `%3`. La confirmación de un resultado aceptable se visualiza en la columna `OP` .  Al utilizar la opción de múltiples cargas podrá mostrar el resumen y el desglose como se muestra en la tabla.

![Resultados](https://i.ibb.co/rbttQ7p/0-1-18.jpg)

El circuito marcado en amarillo es la solución para realizar un resumen use la opción múltiples cargas.

## Base de datos de conductores

Para poder ampliar el módulo se agregó la tabla de conductores donde incluye las resistencias y reactancias como ampacidades. Ingrese el código mostrado para visualizar la tabla completa.

```python
import PyEWS
#1 Conductores de cobre, 
#2 conductores de aluminio, 
#3 conductores de cobre estandar para corriente directa.
PyEWS.dbc(1)
```

## Múltiples cargas en corriente alterna

Para implementar una gran variedad de cargas se organizan como se muestra en el bloque de código. 

```python
from PyEWS import mbtcu, dbcircuit
carga=[
     ["1",127,220,15,1,22,1,1,35,3,1,0.9,2,1.25],
     ["2",127,220,12,1,10,1,1,25,3,1,0.9,2,1.25],
     ["3",127,220,22,1,15,1,1,25,3,1,0.9,2,1.25],
     ["4",127,220,22,1,15,1,1,25,3,1,0.9,2,1.25],
     ["4",127,220,22,1,20,1,1,25,3,1,0.9,2,1.25],
     ["6",127,220,22,1,10,1,1,25,3,1,0.9,2,1.25],
     ["7",127,220,22,1,30,1,1,25,3,1,0.9,2,1.25],
     ["8",127,220,22,1,25,1,1,25,3,1,0.9,2,1.25],
     ["9",127,220,15,1,31,1,1,35,3,1,0.9,2,1.25],    
     ["10",127,220,22,1,14,1,1,25,3,1,0.9,2,1.25],
     ["11",127,220,15,1,20,1,1,35,3,1,0.9,2,1.25],
     ["12",127,220,22,1,32,1,1,25,3,1,0.9,2,1.25],
     ["13",127,220,22,1,25,1,1,25,3,1,0.9,2,1.25],
     ["14",127,220,22,1,24,1,1,25,3,1,0.9,2,1.25],
     ["15",127,220,22,1,18,1,1,25,3,1,0.9,2,1.25],
     ["16",127,220,22,1,17,1,1,25,3,1,0.9,2,1.25],
     ["17",127,220,22,1,12,1,1,25,3,1,0.9,2,1.25],    
     ["18",127,220,22,1,10,1,1,25,3,1,0.9,2,1.25],
     ["19",127,220,22,1,21,1,1,25,3,1,0.9,2,1.25],
     ["20",127,220,196,3,55,0.8,3,75,3,3,0.9,2,1.25]
    ]
#Una forma sencilla de mostrar el total de cargas
print("Total de cargas : ",len(carga))
#Para mostar completo el desarrollo
#----------dbcircuit(carga,1,1) #Cobre
#----------dbcircuit(carga,1,2) #Aluminio
#Para mostar el resumen únicamente 
#----------dbcircuit(carga,2,1) #Cobre
#----------dbcircuit(carga,2,2) #Aluminio
```

Para mostrar el resumen de los resultados utilizando conductores de cobre (ca) se utiliza el código :

```python
dbcircuit(carga,2,1)
```

<img src="https://i.ibb.co/PzFM1sJ/0-1-18-2.jpg" alt="Resultados" style="zoom:100%;" />

Para mostrar el resumen de los resultados utilizando conductores de aluminio (ca) se utiliza el código :

```python
dbcircuit(carga,2,2)
```

![Resultados](https://i.ibb.co/DttdHzk/B.jpg)

## Múltiples cargas en corriente directa 

Para implementar una gran variedad de cargas se organizan como se muestra en el bloque de código.

```python
from PyEWS import dbcircuitcd
#(Vcd,In,Nc,L,Class,Ta,Vd,View):
cargacd=[
    ["1",1200,30,1,100,1,25,3,2,1],
    ["2",1200,30,1,100,1,25,3,2,1],
    ["3",1200,30,1,100,1,25,3,2,1],
    ["4",1200,30,1,100,1,25,3,2,1],
    ["5",1200,30,1,100,1,25,3,2,1],
    ["6",1200,30,1,100,1,25,3,2,1],
    ["7",1200,30,1,100,1,25,3,2,1],
    ["8",1200,30,1,100,1,25,3,2,1],
    ["9",1200,30,1,100,1,25,3,2,1],
    ["10",1200,30,1,100,1,25,3,2,1],
    ["11",1200,30,1,100,1,25,3,2,1],
    ["12",1200,30,1,100,1,25,3,2,1],
    ["13",1200,30,1,100,1,25,3,2,1],
    ["14",1200,30,1,100,1,25,3,2,1]
    ]
print("Total de cargas : ",len(cargacd))
dbcircuitcd(cargacd,2,1)

#Para mostar completo el desarrollo
#----------dbcircuitcd(carga,1,1) #Cobre Estándar
#----------dbcircuitcd(carga,1,2) #Aluminio No disponible
#Para mostar el resumen únicamente 
#----------dbcircuitcd(carga,2,1) #Cobre Estándar
#----------dbcircuitcd(carga,2,2) #Aluminio No disponible
```

Para mostrar el resumen de los resultados utilizando conductores de cobre estándar se utiliza el código :

```
dbcircuitcd(cargacd,2,2)
```

![MODBTCD](https://i.ibb.co/rswpHm2/04.jpg)

## Impedancia unitaria 

Para obtener las constantes únicamente utilice las líneas siguientes 

```python
from PyEWS import zpucu, zpual
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
from PyEWS import mbtal, graph
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

## Referencias

[1] Norma Oficial Mexicana NOM-001-SEDE-2012, *Instalaciones Eléctricas (utilización)*

[2] Thue, W., 1978. *Electrical Power Cable Engineering*. 2nd ed. New York, Basel: Marcel Dekker Inc., p.34.

[3] Norma Oficial Mexicana NOM-001-SEDE-2018, *Instalaciones Eléctricas (utilización)*

## Acerca de la versión

La presente versión tiene corrección de entrada de parámetros como ampliación de la base de datos y corrección de errores mínimos dentro de algunas estructuras del  paquete.

```text
[Packqge]: ElectricalWireSizes 0.1.21
[Autor]: Marco Polo Jácome Toss
[Licencia]: GNU General Public License v3.0
```
