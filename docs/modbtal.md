# Documentación MODBTAL

​	El módulo de baja tensión para conductores de aluminio puede puede usarse para tensiones de 600 V hasta 2000 V, para tensiones superiores es necesario implementar otra serie de módulos. 

## Comando

El módulo MODBTCU para poder iniciarlo es necesario cargarlo e ingresar el comando siguiente :

* `vd02` - Iniciar la aplicación MODBTAL.

  



![MODBTCU](https://i.ibb.co/SrzyZVj/vd02.jpg)





## Información General

En esta sección es necesario ingresar un nombre al circuito y que tipo de sistema de alimentación de la carga instalada.

```text
N.Circuto: (En esta opción se ingresa el nombre del circuito)

Sistema: (Debe seleccionar una opción)
	-LN   [1 Fase  - 2 Hilos]
	-LLN  [2 Fases - 3 Hilos] 
	-LLL  [3 Fases - 3 Hilos]
	-LLLN [3 Fases - 4 Hilos]
	-LL   [2 Fases - 2 Hilos]
```

## Datos de carga

Puede seleccionar la unidad de carga como el factor de potencia y de demanda, estos últimos no tienen unidades y son expresados por unidad..

```text
Carga : (En esta opción se ingresa la carga del circuito)
Unidad: (Debe seleccionar una opción)
	-W   [Watts]
	-VA  [Voltioamperio] 
	-I   [Amperio]
	-HP  [Caballos de fuerza]
Factor de potencia : No tiene unidades y su valor oscila entre 0.65-0.95
	-Fp  [0-1]
Factor de demanda : Se expresa por unidad y depende del tipo de carga.	
	-Fd  [0-1]
```



## Alimentación y tuberías

Las unidades de carga se puede seleccionar adecuadamente como el factor de potencia y de demanda, estos últimos no tienen unidades y son expresados por unidad.

```text
Carga : (En esta opción se ingresa la carga del circuito)
Unidad: (Debe seleccionar una opción)
	-W   [Watts]
	-VA  [Voltioamperio] 
	-I   [Amperio]
	-HP  [Caballos de fuerza]
Factor de potencia : No tiene unidades y su valor oscila entre 0.65-0.95
	-Fp  [0-1]
Factor de demanda : Se expresa por unidad y depende del tipo de carga.	
	-Fd  [0-1]
```

## Tensión

La unidad de tensión predeterminada son los volts, ingrese el adecuado.

```text
Unidad: (Ingrese el tensión)
	-V   [Volts]
```

## Pérdida de tensión

Seleccione la  pérdida de tensión en porcentaje adecuada para la carga.

```text
Unidad: (Seleccione una opción)
	-CT   [5%, 4%, 3%, 2%, 1%]
```

## Calibre

Ingrese el conductor deseado o adecuado para su cálculo como su aislamiento y número de conductores por fase. Para efectuar el dimensionamiento del conductor seleccionado debe dejar la opción de autoajuste en "No".

```text
Calibre: (Seleccione el calibre deseado)
	-opciones [6 AWG / 4 AWG / 2AWG / 1/0 AWG / 2/0 AWG 
	           3/0 AWG / 4/0 AWG / 250 KCM / 300 KCM / 350 KCM / 400 KCM / 500 KCM / 600 KCM 
	           700 KCM / 750 KCM]
```

## Aislamiento

Seleccione el aislamiento adecuado  para suministrar la energía a la carga. 

```text
Calibre: (Seleccione una opción)
	-opciones [ RHH / RHW-2 / XHHW / XHHW-2]
```

## Temperatura de operación

La temperatura de operación es importante para la situación adecuada.

```text
Calibre: (Seleccione una opción)
	-opciones [60°C, 75°C, 90°C]
```

## Número de conductores por fase 

Cuando no sea posible satisfacer las necesidades de corriente y pérdida de tensión es posible incrementar el número de conductores por fase. Por defecto se encuentra  1 en la casilla, el autoajuste no incluye el aumento de conductores por fase.

```text
Nc: (Ingrese los conductors por fase)
	- 1, 2, 3, 4 ... n
```

## Condiciones de carga 

La distancia, eficiencia del circuito, número de conductores activos y factor de sobre carga son manejados como condiciones de carga. Por defecto se encuentran llenas algunas casillas, pero tiene la opción de ingresar otros valores adecuados a su cálculo.

```text
Dist. : La distancia de la carga debe ingresarse en metros.
Nca   : El número de conductores activos depende de la distribución de las canalizaciones.
		- 1 a 3, 4 a 6 etc.
Fsc   : El factor de sobrecarga depende la norma utilizada por defecto tiene precargado 1.25
	    que equivale al 125% más de carga.
Eff   : La eficiencia del circuito depende de las caracteristicas de conductores y carga. 
        Por defecto se tiene expresado por unidad donde 1 equivale al 100%.
```

## Protección y conductor 

El nivel de corto circuito máximo debe plantearse para la instalación, algunos conductores deben pasar esta prueba. Generalmente colocaremos la primera opción.

El autoajuste del conductor desprecia el calibre seleccionado, por lo tanto debe plantear si ajustará el conductor.  El ajuste por el momento no puede alterar número de conductores por fase para un optimo ajuste pero en versiones futuras se incorporará.

```text
Icc.          : Nivel de corto circuito de la instalación.
				-Icc [10 kA, 14 kA, 18 kA, 25 kA]
Autoajustar   : Ajuste para la selección adecuada del conductor.
				- Si
				- No
```

## Reporte general

En este ejemplo se utiliza una carga de 1250 Watts (1F-2H) con un factor de potencia de 0.9 a una distancia de 30 metros y temperatura ambiente de 40 °C. La eficiencia del circuito ideal es del 100% con un factor de demanda del 100% y la tubería ocupada para proteger los cables es de PVC.

```
--------------------------------------------------------------------------------
::::::::::::::::::::::::::::::::[REPORTE GENERAL]:::::::::::::::::::::::::::::::
--------------------------------------------------------------------------------
                                                                                
:::[DATOS DE CARGA]:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	Circuito : ROOM
	Alimentación : 1F-2H
	Potencia : 1250 Watts
	Potencia Reactiva : 1388.8889 VA
	Conductor de Aluminio : Aceptable
	Fp : 0.9
	Eficiencia : 100
	Longitud : 30 ml
	Tuberia : PVC
	T.Ambiente : 40 C
:::[ITM]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	Proteccion : 1Px15A
	Capacidad : 10kA
:::[CONDUCTOR]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	Calibre 6 AWG (13.3 mm2)
	Cond. Fase : 1
	Aislamiento : XHHW 75 C
	Area Cond. : 35.2565 mm2 
	R Cos A : 2.1155 Ohms/Km
	X Sin A : 0.0729 Ohms/Km
	Z Cond : 2.1884 Ohms/Km
	Ampacidad : 50
:::[CALCULO POR AMPACIDAD]::::::::::::::::::::::::::::::::::::::::::::::::::::::
	In : 11.5741 A
	In/Nc : 11.5741 A
	F.A. : 1
	F.T. : 0.8819
	Ampacidad : 44.0959 A
:::[CALCULO POR CAIDA DE TENSION]:::::::::::::::::::::::::::::::::::::::::::::::
	Z : 0.0657 Ohms
	Vd : 1.5212 V
	Vs : 120 V
	Vd : 1.2677 %
:::[SPT]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	T - 6 AWG
:::[SECCION DE CONDUCTORES]:::::::::::::::::::::::::::::::::::::::::::::::::::::
	Area total de : 2C +1T
	2C : 70.513 mm²
	1T : 35.2565 mm²
	Total : 105.7696 mm²
:::[PESO DE CONDUCTORES]::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	Fase : 3.48 Kg
	Tierra : 1.74 Kg
:::[LONGITUD DE CONDUCTORES]::::::::::::::::::::::::::::::::::::::::::::::::::::
	Fase : 60 m
	Tierra : 30 m
:::[Resumen]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
ROOM,1F-2H,1250,1388.8889,Aceptable,0.9,100,30,PVC,40,6 AWG,13.3,1,XHHW 75C,35.2565,2.1155,0.0729,2.1884,50,11.5741,11.5741,1,0.8819,44.0959,0.0657,1.5212,120,1.2677,6,1Px15A,10kA,2,70.513,1,35.2565,105.7696,3.48,1.74,60,30
```

