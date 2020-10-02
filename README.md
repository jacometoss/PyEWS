![PyEWS](https://i.ibb.co/YD4XKb8/02.png)



# PyEWS - Python Electrical Wire Sizes



El módulo PyEWS sirve para obtener el dimensionamiento de conductores para una instalación eléctrica. Es fácil de utilizar e interpretar sus resultados generando un panorama más general al poder visualizar por completo una lista de conductores con los parámetros de entrada.

## Instalación

La instalación del módulo se realiza con :

```Python
pip install ElectricalWireSizes
```

## Iniciar paquete de instalación

El módulo tiene dependencias por lo que es necesario instalar `tabulate` el cual da una mejor apariencia al momento de mostrar los resultados.

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
#S:
---- 1:(1F-2H) 2:(2F-3H) 3:(3F-3H) 4:(3F-4H)
	
```

```python
import PyEWS 
PyEWS.MBTCU(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S)
```

## PyEWS Módulos

| Id   | Descripción                                                  | Módulo | Versión |                     Descargar                      |
| ---- | ------------------------------------------------------------ | ------ | ------- | :------------------------------------------------: |
| 1    | Módulo de baja tensión para conductores de cobre clase B con máxima tensión de operación de 600 V hasta 2000V | MBTCU  | 0.1.9   | [PyEWS 0.1.9](https://github.com/jacometoss/PyEWS) |

## Test

El módulo tiene dependencias por lo que es necesario instalar `tabulate` el cual da una mejor apariencia al momento de mostrar los resultados.

```python
import PyEWS
PyEWS.MBTCU(127,220,25,1,35,1,1,2,3,1)
```

Los se resultados muestran con la iteración de todos los conductores tanto para tensión monofásica como trifásica.

- `Vd (Voltage Drop)` es la pérdida de tensión porcentual 
- `60,75,90` la ampacidad real de los conductores.
- `Nc` es el numero de conductores por fase.
- `Op` muestra si el resultado es correcto al aparecerer en la columna como Yes 
- `ITM` es la protección del circuito.

![Resultados](https://i.ibb.co/KDwv9jX/01.png)

## Referencias

1. [Norma Oficial Mexicana NOM-001-SEDE-2012, Instalaciones Eléctricas (utilización)](http://www.issste-cmn20n.gob.mx/Datos/Normas/136NOM.pdf)

