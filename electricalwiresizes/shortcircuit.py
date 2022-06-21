'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
| PYEWS, ElectricalWireSizes, 15/06/2022                                 |
| Version : 0.1.28                                                       |
| Autor : Marco Polo Jacome Toss                                         |
| License: GNU Affero General Public License v3 (GPL-3.0)                |
| Requires: Python >=3.5                                                 |
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Changelog:

0.1.28   : Versión estable.

0.1.28rc2: Separación de operaciones, conductor y protección.

0.1.28rc1: En esta versión se actualiza las protecciones y se actualiza
           la fórmula de corriente incluyendo el factor de sobrecorriente,
           en la versión 0.1.27 no se logra ver la actualización de la
           corriente nominal.

0.1.27rc3: En esta versión los módulos se han clasificado e independizado
           en distintos archivos además se mejora la salida de datos
           del módulo dbcircuit para funciones futuras.

0.1.27:    Versione estable.

'''

from tabulate import tabulate
import math, time
from .bd import dbConductorCu, dbConductorAl

def icc(conductor=None,T1=None,T2=None,fhz=None,view=None):

    if((conductor==None or T1==None or T2==None or fhz==None or view==None)):
        t = time.localtime()
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                    ElectricalWireSizes                      ")
        print("                 ",time.asctime(t))
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                                                             ")
        print("                         ─▄▀─▄▀")
        print("                         ──▀──▀")
        print("                         █▀▀▀▀▀█▄")
        print("                         █░░░░░█─█")
        print("                         ▀▄▄▄▄▄▀▀")
        print("                                                             ")
        print("-------------------------------------------------------------")
        print("| Los parámetros no son correctos                           |")
        print("| para el módulo                                            |")
        print("| icc(conductor,T1,T2,fhz,view)                             |") 
        print("----------------------------------------------- -------------")
        return  
    
    if conductor==1:
        datos=[["14 AWG"],
            ["12 AWG"],
            ["10 AWG"],
            ["8 AWG"],
            ["6 AWG"],
            ["4 AWG"],
            ["2 AWG"],
            ["1/0 AWG"],
            ["2/0 AWG"],
            ["3/0 AWG"],
            ["4/0 AWG"],
            ["250 KCM"],
            ["300 KCM"],
            ["350 KCM"],
            ["400 KCM"],
            ["500 KCM"],
            ["600 KCM"],
            ["750 KCM"],
            ["1000 KCM"]]

        k=0.0297

        for i in range(len(dbConductorCu)):
            Seccion=dbConductorCu[i][10]
            datos[i].append(Seccion)

        t=1/fhz
        for i in range(len(dbConductorCu)):
            CM=round(dbConductorCu[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=2/fhz
        for i in range(len(dbConductorCu)):
            CM=round(dbConductorCu[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=4/fhz
        for i in range(len(dbConductorCu)):
            CM=round(dbConductorCu[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))
        t=8/fhz
        for i in range(len(dbConductorCu)):
            CM=round(dbConductorCu[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=16/fhz
        for i in range(len(dbConductorCu)):
            CM=round(dbConductorCu[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=30/fhz
        for i in range(len(dbConductorCu)):
            CM=round(dbConductorCu[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=60/fhz
        for i in range(len(dbConductorCu)):
            CM=round(dbConductorCu[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=100/fhz
        for i in range(len(dbConductorCu)):
            CM=round(dbConductorCu[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        if view==1:
            headers = ["Calibre","S[mm²]","1C[kA]","2C[kA]","4C[kA]", "8C[kA]", "16C[kA]", "30C[kA]", "60C[kA]", "100C[kA]"]
            print(tabulate(datos, headers, tablefmt="pretty"))
        elif view==2:
            return datos
    
    elif conductor==2:
        
        datos=[["6 AWG"],
            ["4 AWG"],
            ["2 AWG"],
            ["1/0 AWG"],
            ["2/0 AWG"],
            ["3/0 AWG"],
            ["4/0 AWG"],
            ["250 KCM"],
            ["300 KCM"],
            ["350 KCM"],
            ["400 KCM"],
            ["500 KCM"],
            ["600 KCM"],
            ["750 KCM"],
            ["1000 KCM"]]

        k=0.0125

        for i in range(len(dbConductorAl)):
            Seccion=dbConductorAl[i][10]
            datos[i].append(Seccion)

        t=1/fhz
        for i in range(len(dbConductorAl)):
            CM=round(dbConductorAl[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=2/fhz
        for i in range(len(dbConductorAl)):
            CM=round(dbConductorAl[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=4/fhz
        for i in range(len(dbConductorAl)):
            CM=round(dbConductorAl[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))
        t=8/fhz
        for i in range(len(dbConductorAl)):
            CM=round(dbConductorAl[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=16/fhz
        for i in range(len(dbConductorAl)):
            CM=round(dbConductorAl[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=30/fhz
        for i in range(len(dbConductorAl)):
            CM=round(dbConductorCu[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=60/fhz
        for i in range(len(dbConductorAl)):
            CM=round(dbConductorAl[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        t=100/fhz
        for i in range(len(dbConductorAl)):
            CM=round(dbConductorAl[i][10]*1973.525241,2)
            datos[i].append(round(math.sqrt(((pow(CM,2)*(k*math.log10((T2+234)/(T1+234)))))/t)/1000,2))

        if view==1:
            headers = ["Calibre","S[mm²]","1C[kA]","2C[kA]","4C[kA]", "8C[kA]", "16C[kA]", "30C[kA]", "60C[kA]", "100C[kA]"]
            print(tabulate(datos, headers, tablefmt="pretty"))
        elif view==2:
            return datos
