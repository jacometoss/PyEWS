# Documentación ADUCT

​	La rutina `aduct `tiene la propiedad de calcular la sección de tubería requerida para una instalación eléctrica. 

## Comando

El módulo ADUCT para poder iniciarlo es necesario cargarlo e ingresar el comando siguiente :

* `pipeline` - Iniciar la rutina ADUCT.

## Información General

Para poder dimensionar la sección de la tubería siga los pasos que se muestran.

```
Las opciones de tubería son las siguientes ;

	-EMT Tubo conduit metálico
	-ENT Tubo conduit no metálico
	-FMC Tubo conduit metálico flexible
	-IMC Tubo conduit metálico semipesado
	-LFNC-B Tubo conduit no metálico flexible hermético a los liquidos
	-LFNC-A Tubo conduit no metálico flexible hermético a los liquidos
	-LFMC Tubo conduit metálico flexible hermético a los liquidos
	-RMC Tubo conduit metálico pesado 
	-PVC-80 Tubo conduit rígido de pvc cédula 80
	-PVC-40 Tubo conduit rígido de pvc cédula 40 y HDPE
	-PVC-A Tubo conduit rígido de pvc tipo A
	-PVC-80 Tubo conduit rígido de pvc cédula 80
	
Seleccione el número de conductores para establecer el factor de relleno,

	-1 Conductor
	-2 Conductores
	-3 Mas de tres conductores

Ingrese la sección de todos los conductores en mm².
	
```

## Porcentaje de la sección transversal en tubo conduit 

Se basa en las condiciones más comunes de cableado y alineación de los conductores, cuando la longitud de los tramos y el número de curvas de los cables están dentro de límites razonables. Sin embargo, en determinadas condiciones se podrá ocupar una parte mayor o menor de los conductos.

| Número de conductores | Todos los tipos de conductores |
| --------------------- | ------------------------------ |
| 1                     | 53%                            |
| 2                     | 31%                            |
| Más de 2              | 40%                            |

Los porcentajes anteriores son utilizados en la rutina ACDUCT , basando las secciones de la Tabla 4 del Capítulo 10 de la NOM-001-SEDE-2012.