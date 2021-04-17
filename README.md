

<img src="https://i.ibb.co/YD4XKb8/02.png" alt="PyEWS" style="zoom: 80%;" />

[![PyPI version](https://badge.fury.io/py/ElectricalWireSizes.svg)](https://badge.fury.io/py/ElectricalWireSizes)
[![Downloads](https://static.pepy.tech/personalized-badge/electricalwiresizes?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/electricalwiresizes)
[![Downloads](https://pepy.tech/badge/electricalwiresizes/month)](https://pepy.tech/project/electricalwiresizes)
[![versons of python supported](https://img.shields.io/badge/python-3%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://pypi.org/project/ElectricalWireSizes/)
[![Maintainability](https://api.codeclimate.com/v1/badges/27c48038801ee954796d/maintainability)](https://codeclimate.com/github/jacometoss/PyEWS/maintainability)[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8d8575adf7e149999e6bc84c657fc94e)](https://www.codacy.com/gh/jacometoss/PyEWS/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jacometoss/PyEWS&amp;utm_campaign=Badge_Grade)

# Python Electrical Wire Sizes 

El módulo PyEWS ( **Versión 0.1.18**) puede ser utilizado para dimensionar conductores  de baja tensión de una instalación eléctrica. Es fácil de utilizar e interpretar sus resultados mostrando un panorama más general al poder visualizar por completo una lista de conductores propuestos con los parámetros de entrada.

## Instalación

La instalación del módulo se realiza con :

```Python
pip install ElectricalWireSizes
```

## Iniciar paquete de instalación

El módulo tiene dependencias siendo necesario instalar `tabulate` el cual da una mejor apariencia al momento de mostrar los resultados.

```tex
#VF: Tensión de fase o en su defecto tensión de línea para sistemas de 1F2H, 2F.
#VL: Tensión de línea.
#In: Corriente nominal total de una de las fases.
#Nc: Número de conductores por fase.
#L : Longitud en metros.
#FA: Número de conducrtores activos en el tubo conduit.
#Type: Tipo de tubo conduit (1:PVC,2:AL,3:ACERO)
#Ta: Temperatura ambiente en centigrados, únicamente ingresar la opcion númerica.
---- 1:20 2:25 3:30 4:35 5:40 6:45 7:50 8:55 9:60 10:65 11:70 12:75
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

```python
import PyEWS
#Para conductores de cobre
PyEWS.MBTCU(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc)
#Para conductores de aluminio
PyEWS.MBTAL(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S,Fp,Op,Fsc)
```

El módulo de corriente directa  necesita la información siguiente :

```python
#MODBTCUSTD(Vcd,In,Nc,L,Class,Ta,Vd,View,Fsc):
#Vcd   :  Tensión en corriente directa.
#In    :  Corriente directa del circuito.
#Nc    :  Número de conductores en corriente directa.
#L     :  Longitud del circuito en metros.
#Class :  Clase de conductor A:1 B:2 y C:3.
#Ta	   :  Temperatura ambiente 
#Vd	   :  Caída de tensión.
#View  :  Mostrar los resultados adecuadamente en una tabla con 1 para multiples cargas debe ser 2.
#Fsc   :  Factor de sobrecorrriente

PyEWS.MBTCUSTD(1200,145,1,100,1,25,3,1,1.25)
```



## PyEWS Módulos

| Id   | Descripción                                                  | Módulo   | Versión |                      Descargar                      |
| ---- | ------------------------------------------------------------ | -------- | ------- | :-------------------------------------------------: |
| 1    | Módulo de baja tensión para conductores de cobre clase B, C y D  tensión de 600V a 2000V | MBTCU    | 0.1.18  | [PyEWS 0.1.18](https://github.com/jacometoss/PyEWS) |
| 2    | Módulo de baja tensión para conductores de aluminio clase B, C y  D, tensión 600V a 2000V | MBTAL    | 0.1.18  | [PyEWS 0.1.18](https://github.com/jacometoss/PyEWS) |
| 3    | Módulo de baja tensión para conductores de cobre clase B, C  y D en corriente directa hasta 2000 V | MBTCUSTD | 0.1.18  | [PyEWS 0.1.18](https://github.com/jacometoss/PyEWS) |

## Test

El módulo tiene dependencias por lo que es necesario instalar `tabulate` el cual da una mejor apariencia al momento de mostrar los resultados.

```python
import PyEWS
PyEWS.MBTCU(127,220,15,1,22,1,1,35,3,1,0.9,1,1.25)
```

Los se resultados muestran con la iteración de todos los conductores tanto para tensión monofásica como trifásica.

- `Vd (Voltage Drop)` es la pérdida de tensión porcentual 

- `60,75,90` la ampacidad real de los conductores.

- `Nc` es el número de conductores por fase.

- `Op` muestra si el resultado es correcto al aparecerer en la columna como  `Yes` .

- `ITM` es la protección del circuito.

  Se puede observar en la columna  `%VD 1F-2H` seleccionada la pérdida de tensión es aceptable con respecto a la mínima ingresada del `%3`. La confirmación de un resultado es aceptable se visualiza en la columna `OP` .  Al utilizar la opción de multiples cargas podrá mostrar el resumen y el desglose como se muestra en la tabla.

![Resultados](https://i.ibb.co/rbttQ7p/0-1-18.jpg)

El circuito mostrado es la solución y para ver el resumen este fue agregado para la opción multiples cargas.

## Base de datos de conductores

Para poder ampliar el módulo se agregó la tabla de conductores donde incluye las resistencias y reactancias como ampacidades. Ingrese el código mostrado para visualizar la tabla completa.

```python
import PyEWS
#1 Conductores de cobre, 
#2 conductores de aluminio, 
#3 conductores de cobre estandar para corriente directa.
PyEWS.DBC(1)
```

## Múltiples cargas en corriente alterna

Para implementar una gran variedad de cargas se organizan como se muestra en el bloque de código, puede agregar hasta ***indefinido número de cargas*** en está nueva versión (0.1.18).

```python
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
#----------PyEWS.DBCIRCUIT(carga,1,1) #Cobre
#----------PyEWS.DBCIRCUIT(carga,1,2) #Aluminio
#Para mostar el resumen únicamente 
#----------PyEWS.DBCIRCUIT(carga,2,1) #Cobre
#----------PyEWS.DBCIRCUIT(carga,2,2) #Aluminio
```

Para mostrar el resumen para  conductores de cobre

```python
PyEWS.DBCIRCUIT(carga,2,1)
```

<img src="https://i.ibb.co/PzFM1sJ/0-1-18-2.jpg" alt="Resultados" style="zoom:100%;" />

Para mostrar el resumen para conductores de aluminio

```python
PyEWS.DBCIRCUIT(carga,2,2)
```

![Resultados](https://i.ibb.co/DttdHzk/B.jpg)

## Múltiples cargas en corriente directa 

Para implementar una gran variedad de cargas se organizan como se muestra en el bloque de código, puede agregar hasta 25 cargas.

```python
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
DBCIRCUITCD(cargacd,2,1)

#Para mostar completo el desarrollo
#----------PyEWS.DBCIRCUITCD(carga,1,1) #Cobre Estándar
#----------PyEWS.DBCIRCUITCD(carga,1,2) #Aluminio No disponible
#Para mostar el resumen únicamente 
#----------PyEWS.DBCIRCUITCD(carga,2,1) #Cobre Estándar
#----------PyEWS.DBCIRCUITCD(carga,2,2) #Aluminio No disponible
```

Para mostrar el resumen para  conductores de cobre estándar

```
DBCIRCUITCD(cargacd,2,2)
```

![MODBTCD](https://i.ibb.co/rswpHm2/04.jpg)

## Impedancia unitaria 

Para obtener las constantes únicamente utilice las líneas siguientes 

```python
import PyEWS
#ZpuCu(Type,Ta,Fp,View)
PyEWS.ZpuCu(1,10,0.9,1) 
#ZpuAl(Type,Ta,Fp,View)
PyEWS.ZpuAl(1,10,0.9,1) 
```

<img src="https://i.ibb.co/D1syMzL/Zpu.jpg" alt="Zpu" style="zoom:70%;" />

## Referencias

[1] Norma Oficial Mexicana NOM-001-SEDE-2012, *Instalaciones Eléctricas (utilización)*

[2] Thue, W., 1978. *Electrical Power Cable Engineering*. 2nd ed. New York, Basel: Marcel Dekker Inc., p.34.



