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
from .bd import dbConductorCuStd   
import math, time
from .mbtcustd import mbtcustd
from .basicelecfunc import Rn, RnCd, Rcd, FCT

def dbcircuitcd(carga=None,view=None,conductor=None):

    if(carga==None or view==None or conductor==None):
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
        print("| para el módulo DBCIRCUITCD(carga,view,conductor)          |")
        print("-------------------------------------------------------------")
        return      
    
    dbcircuit = [[str(i + 1)] for i in range(len(carga))]
    
    datos=[]  
    for i in range(len(carga)):
        if conductor == 1:
            datos.append(mbtcustd(carga[i][1],carga[i][2],carga[i][3],carga[i][4],carga[i][5],carga[i][6],carga[i][7],carga[i][8],carga[i][9],carga[i][10],carga[i][11])) 
            if view==1:
                print("Id [",i+1,"]============================================================================================================")
                print(tabulate(datos[i], headers=["AWG/KCM","Kcd [A,B,C]", "", "60", "75", "90","%Vd","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))
        elif conductor == 2:
            datos.append(mbtcustd(carga[i][1],carga[i][2],carga[i][3],carga[i][4],carga[i][5],carga[i][6],carga[i][7],carga[i][8],carga[i][9],carga[i][10],carga[i][11]))
            if view==1:
                print("Id [",i+1,"]============================================================================================================")
                print(tabulate(datos[i], headers=["AWG/KCM","Kcd [A,B,C]", "", "60", "75", "90","%Vd","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))


            
    if conductor==1:
        dbConductor=dbConductorCuStd
    elif conductor==2:
        dbConductor=dbConductorCuStd
        
    for i in range(len(carga)):
        for j in range(len(dbConductor)):
            
            if datos[i][j][11]=="Yes":
                
                dbcircuit[i].append(datos[i][j][0])
                dbcircuit[i].append(datos[i][j][1])
                dbcircuit[i].append(carga[i][2])
                dbcircuit[i].append(carga[i][7]) 
                dbcircuit[i].append("CD [+-]")
                dbcircuit[i].append(FCT(carga[i][6]))
                dbcircuit[i].append(datos[i][j][2])
                dbcircuit[i].append(datos[i][j][3])
                dbcircuit[i].append(datos[i][j][4])
                dbcircuit[i].append(datos[i][j][5])
                dbcircuit[i].append(datos[i][j][6])
                dbcircuit[i].append(datos[i][j][7])
                dbcircuit[i].append(datos[i][j][8])
                dbcircuit[i].append(datos[i][j][9])
                dbcircuit[i].append(datos[i][j][10])
                #dbcircuit[i].append(datos[i][j][11])
                dbcircuit[i].append(datos[i][j][12])
                break

            

    #return dbcircuit
    print("::::::: [ RESUMEN DE CARGAS ]::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    #print(tabulate(dbcircuit, headers=["Id","#CAL","L[m]", "Vd","FP","ALM", "Fct","Fa","60", "75", "90","Vd[%]","Nc", "In", "60", "75", "90", "ITM"], tablefmt='psql'))
    
    #print(tabulate(dbcircuit, headers=["Idx","#CAL","L[m]", "Vd","ALM", "Fct","60", "75", "90","Vd[%]","Nc", "In", "60", "75", "90", "ITM"], tablefmt='psql'))
    
    print(tabulate(dbcircuit, headers=["Id","#CAL","Kcd [A,B,C]","L[m]", "Vd", "ALM", "Fct", "60", "75", "90", "Vd[%]", "Nc", "In", "60", "75", "90", "ITM"],  tablefmt='psql'))
