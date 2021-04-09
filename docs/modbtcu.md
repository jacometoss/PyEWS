# Documentación MODBTCU (0.2.44.09)

El módulo de baja tensión para conductores de cobre puede puede usarse para tensiones de 600 V hasta 2000 V, para tensiones superiores es necesario implementar otra serie de módulos. 

Los conductores de esta aplicación son de Clase B, Clase C, Clase D sin estañar, cobre puro.

## Comando

El módulo MODBTCU para poder iniciarlo es necesario cargarlo e ingresar el comando siguiente :

* `vd01` - Iniciar la aplicación MODBTCU.

  



![MODBTCU](https://i.ibb.co/M73nNSS/SELISP-0-2-44-09.jpg)





## Información General

En esta sección es necesario ingresar un nombre para el circuito y el tipo de sistema de alimentación para la carga deseada.

```text
N.Circuto: (En esta opción se ingresa el nombre del circuito)

Sistema: (Debe seleccionar una opción)
	-LN   [1 Fase  - 2 Hilos]
	-LLN  [2 Fases - 3 Hilos] 
	-LLL  [3 Fases - 3 Hilos]
	-LLLN [3 Fases - 4 Hilos]
	-LL   [2 Fases - 2 Hilos]
SD:(La casilla sostiene el diálogo para cálculos posteriores)
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
	-opciones [14 AWG / 12 AWG / 10 AWG / 8 AWG / 6 AWG / 4 AWG / 2AWG / 1/0 AWG / 2/0 AWG 
	           3/0 AWG / 4/0 AWG / 250 KCM / 300 KCM / 350 KCM / 400 KCM / 500 KCM / 600 KCM 
	           700 KCM / 750 KCM / 1000 KCM]
```

## Aislamiento

Seleccione el aislamiento adecuado  para suministrar la energía a la carga. 

```text
Calibre: (Seleccione una opción)
	-opciones [RHH / RHW-2 / THW-2 / THHW-LS / THWN-2 / THHN-RAD / XHHW / XHHW-2
	           RHH-XLPE / RHW-2-XLPE]
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

El autoajuste del conductor desprecia el calibre seleccionado, por lo tanto debe plantear si ajustará el conductor.  El ajuste por el momento no puede alterar el número de conductores por fase para un optimo ajuste pero en versiones futuras se incorporará.

```text
Icc.          : Nivel de corto circuito de la instalación.
				-Icc [10 kA, 14 kA, 18 kA, 25 kA]
Carga. 		  : Carga dedicada o no dedicada significa el 80% de la protección o el 100%.
Autoajustar   : Ajuste para la selección adecuada del conductor.
				- Si
				- No
```

## Ejemplo No.1 Carga Instalada en una vivienda general.

Tenemos una pequeña planta de vivienda de 112.75 m²,  si la carga promedio es de 30 VA/m²  y el lugar presenta una temperatura ambiente de 35 °C  y la longitud  del centro de carga de la planta hacia el tablero principal es de 20 metros, considerando la eficiencia del circuito de un 100% y se desea proteger con un interruptor termomagnético. Dimensionar el conductor necesario para alimentar la carga de la planta. 

La carga aproximada instalada en la planta es de 3382.5 VA y se instalará una acometida monofásica que parte de un tablero principal. Véase la ilustración.

![Planta](https://i.ibb.co/GnbpRBt/Home02.jpg)

Se consideró como un circuito alimentador el cual no debe rebasar el  2% de pérdida de tensión, considerando en el interior de la vivienda circuitos derivados. 

Se propone como conductor inicial el 10 AWG pero se ha seleccionado la casilla de autoajuste con la opción "SI".

**Norma Oficial Mexicana NOM-001-SEDE-2012** 

> **B. Clasificación de los circuitos derivados.**
>
> **210-19. Conductores. Ampacidad y tamaños mínimos.**
>
> Nota 4 : Los conductores de circuitos derivados como están definidos en el Artículo 100, dimensionados para evitar una caída de tensión mayor que 3 por ciento en la salida más lejana que alimente a cargas de calefacción, de fuerza, de alumbrado o cualquier combinación de ellas y en los que la caída máxima de tensión combinada de los circuitos alimentadores y de los circuitos derivados hasta el contacto más lejano no supere el 5 por ciento, proporcionarán una razonable eficiencia de funcionamiento.

Podemos observar el llenado de la ventana de la aplicación. El nivel de Icc es 10 kA debido a que los transformadores locales no superan los 112.5 kVA el cual nos daría un nivel de corto circuito de 9372.56 A o 9.37 kA al 100% de carga.

![Alimentador](https://i.ibb.co/F6w8r7n/SELISP-0-2-44-09-2.jpg)

## Reporte general

Planteando este pequeño ejemplo para la pequeña vivienda con una consumo de  3044.25 Watts se puede alimentar con un conductor del 8 AWG  con aislamiento THHW-LS 75 °C  y un conductor de puesta a tierra de 8 AWG. 

La corriente nominal de la vivienda en un sistema de 1Fase-2Hilos es de 26.63 A, por lo tanto puede reducirse el conductor aplicando el factor de demanda, pero realmente si la vivienda aumenta su consumo en futuro a 10 años puede que sea viable el 100% de carga demandada.

Para el cálculo del diámetro de la tubería el reporte muestra 82.019 mm³, por lo tanto puede utilizar una tubería de 3/4 de pulgada de material PVC.



```text
-------------------------------------------------------------------------------
::::::::::::::::::::::::::::::::[REPORTE GENERAL]:::::::::::::::::::::::::::::::
--------------------------------------------------------------------------------
                                                                                
:::[DATOS DE CARGA]:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	Circuito : Vivienda
	Alimentación : 1F-2H
	Tipo : Alimentador
	Potencia : 3044.25 Watts
	Potencia aparente : 3382.5 VA
	Conductor de Cobre Aceptable
	Fp : 0.9
	Eficiencia : 100 %
	Fd : 100
	Fsc : 100
	Longitud : 20 ml
	Tuberia : PVC
	T.Ambiente : 35 C
:::[ITM]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	Proteccion : 1Px35A
	Capacidad : 10kA
:::[CONDUCTOR]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	Calibre 8 AWG (8.367 mm²)
	Cond. Fase : 1
	Aislamiento : THHW-LS 75 C
	Area Cond. : 27.3397 mm² 
	R Cos A : 2.0052 Ohms/Km
	X Sin A : 0.0744 Ohms/Km
	Z Cond : 2.0796 Ohms/Km
	Ampacidad : 50 A
:::[CALCULO POR AMPACIDAD]::::::::::::::::::::::::::::::::::::::::::::::::::::::
	In : 26.6339 A
	In/Nc : 26.6339 A
	F.A. : 1
	F.T. : 0.9428
	Ampacidad : 47.1405 A
:::[CALCULO POR CAIDA DE TENSION]:::::::::::::::::::::::::::::::::::::::::::::::
	Z : 0.0416 Ohms
	Vd : 2.2184 V
	Vs : 127 V
	Vd : 1.7468 %
:::[SPT]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	T - 8 AWG
:::[SECCION DE CONDUCTORES]:::::::::::::::::::::::::::::::::::::::::::::::::::::
	Area total de : 2C +1T
	2C : 54.6794 mm²
	1T : 27.3397 mm²
	Total : 82.0191 mm²
:::[PESO DE CONDUCTORES]::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	Fase : 4.16 Kg
	Tierra : 2.08 Kg
:::[LONGITUD DE CONDUCTORES]::::::::::::::::::::::::::::::::::::::::::::::::::::
	Fase : 40 m
	Tierra : 20 m
:::[Resumen]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Vivienda,1F-2H,3044.25,3382.5,Aceptable,0.9,100,100,20,PVC,35,8 AWG,8.367,1,THHW-LS 75C,27.3397,2.0052,0.0744,2.0796,50,26.6339,26.6339,1,0.9428,47.1405,0.0416,2.2184,127,1.7468,8,1Px35A,10kA,2,54.6794,1,27.3397,82.0191,4.16,2.08,40,20,Alimentador,1

```

Para dimensionar la tubería utilizamos la sección total 82.01 mm².

![SELISP-0-2-44-09-DUCTOS](https://i.ibb.co/zPXQL9Z/SELISP-0-2-44-09-DUCTOS.jpg)



