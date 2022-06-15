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
import math, time
from tabulate import tabulate
from .bd import dbConductorCu, dbConductorAl, dbConductorCuStd

def Rn(Ra=None,T2=None):
    
    if(Ra==None or T2==None):
        t = time.localtime()
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                    ElectricalWireSizes                    ")
        print("                 ",time.asctime(t))
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                                                           ")
        print("                          ▄▀─▄▀")
        print("                         ──▀──▀")
        print("                         █▀▀▀▀▀█▄")
        print("                         █░░░░░█─█")
        print("                         ▀▄▄▄▄▄▀▀")
        print("                                                           ")
        print("-----------------------------------------------------------")
        print("| Los parámetros no son correctos para el                 |")
        print("| módulo Rn(Ra,T2)                                        |")
        print("-----------------------------------------------------------")
        return
    
    Rb=(Ra/(234.5+75))*(234.5+T2)
    return Rb

def RnCd(Ra=None,T2=None):

    if(Ra==None or T2==None):
        t = time.localtime()
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                    ElectricalWireSizes                    ")
        print("                 ",time.asctime(t))
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                                                           ")
        print("                          ▄▀─▄▀")
        print("                         ──▀──▀")
        print("                         █▀▀▀▀▀█▄")
        print("                         █░░░░░█─█")
        print("                         ▀▄▄▄▄▄▀▀")
        print("                                                           ")
        print("-----------------------------------------------------------")
        print("| Los parámetros no son correctos para el                 |")
        print("| módulo RnCd(Ra,T2)                                      |")
        print("-----------------------------------------------------------")
        return
    
    Rb=(Ra/(234.5+75))*(234.5+T2)
    return Rb

def Z(R,X,FP):
    Z=(R*FP+X*math.sin(math.acos(FP)))
    FN=1/((2*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    FFN=1/((math.sqrt(3)*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    FFFN=1/((math.sqrt(3)*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    FFF=1/((math.sqrt(3)*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    return [round(FN,4),round(FFN,4),round(FFFN,4),round(FFF,4),round(Z,4)]

def Rcd(R):
    Rcond=(R)
    PN=1/((2*100)*((Rcond)/1000))
    return [round(PN,4),round(Rcond,4)]

def dbc(conductor=None):

    if(conductor==None):
        t = time.localtime()
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                    ElectricalWireSizes                    ")
        print("                 ",time.asctime(t))
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                                                           ")
        print("                          ▄▀─▄▀")
        print("                         ──▀──▀")
        print("                         █▀▀▀▀▀█▄")
        print("                         █░░░░░█─█")
        print("                         ▀▄▄▄▄▄▀▀")
        print("                                                           ")
        print("-----------------------------------------------------------")
        print("| Los parámetros no son correctos para el                 |")
        print("| módulo dbc(conductor)                                   |")
        print("-----------------------------------------------------------")
        return  

    if conductor ==1:
        print(tabulate(dbConductorCu, headers=["AWG/KCM","R(Ω/km)", "X (Ω/km)","R (Ω/km)","X (Ω/km)", "R (Ω/km)", "X (Ω/km)", "60°C", "75°C", "90°C", "S[mm²]"], tablefmt='psql'))
    elif conductor==2:
        print(tabulate(dbConductorAl, headers=["AWG/KCM","R(Ω/km)", "X (Ω/km)","R (Ω/km)","X (Ω/km)", "R (Ω/km)", "X (Ω/km)", "60°C", "75°C", "90°C","S[mm²]"], tablefmt='psql'))
    elif conductor==3:
        print(tabulate(dbConductorCuStd, headers=["AWG/KCM","R[A](Ω/km)", "R[B](Ω/km)","R[C](Ω/km)", "60°C", "75°C", "90°C","S[mm²]"], tablefmt='psql'))
    elif (conductor>3 or conductor<=0):
        t = time.localtime()
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                    ElectricalWireSizes                    ")
        print("                 ",time.asctime(t))
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                                                           ")
        print("                         ─▄▀─▄▀")
        print("                         ──▀──▀")
        print("                         █▀▀▀▀▀█▄")
        print("                         █░░░░░█─█")
        print("                         ▀▄▄▄▄▄▀▀")
        print("                                                           ")
        print("-----------------------------------------------------------")
        print("| Por el momento tenemos únicamente tres opciones         |")
        print("| Cobre 1, Aluminio 2, Cobre CD                           |")
        print("-----------------------------------------------------------")        
    
def FCT(Ta=None):

    if(Ta==None):
        t = time.localtime()
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                    ElectricalWireSizes                    ")
        print("                 ",time.asctime(t))
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                                                           ")
        print("                         ─▄▀─▄▀")
        print("                         ──▀──▀")
        print("                         █▀▀▀▀▀█▄")
        print("                         █░░░░░█─█")
        print("                         ▀▄▄▄▄▄▀▀")
        print("                                                           ")
        print("-----------------------------------------------------------")
        print("| Los parámetros no son correctos para el                 |")
        print("| módulo FCT(Ta)                                          |")
        print("-----------------------------------------------------------")
        return  

    if Ta >= 60:
        FT60=0.0
    else:
        FT60=round(math.sqrt((60-Ta)/(60-30)),3)
        return FT60
    if Ta >= 75:
        FT75=0.0
    else:
        FT75=round(math.sqrt((75-Ta)/(75-30)),3)
        return FT75
    if Ta >= 90:
        FT90=0.0
    else :
        FT90=round(math.sqrt((90-Ta)/(90-30)),3)
        return FT90


def zpucu(Type=None,Ta=None,Fp=None,View=None):

    if(Type==None or Ta==None or Fp==None or View==None):
        t = time.localtime()
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                    ElectricalWireSizes                    ")
        print("                 ",time.asctime(t))
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                                                           ")
        print("                         ─▄▀─▄▀")
        print("                         ──▀──▀")
        print("                         █▀▀▀▀▀█▄")
        print("                         █░░░░░█─█")
        print("                         ▀▄▄▄▄▄▀▀")
        print("                                                           ")
        print("-----------------------------------------------------------")
        print("| Los parámetros no son correctos para el                 |")
        print("| módulo zpucu(Type,Ta,Fp,View)                           |")
        print("-----------------------------------------------------------")
        return 

    if Type==1:
    #Conductores en ducto de PVC
        Rj=1
        Xj=2
    elif Type==2:
    #Conductores en ducto de Alumunio
        Rj=3
        Xj=4
    elif Type==3:
    #Conductores en ducto de Acero
        Rj=5
        Xj=6
    #print(tabulate(datos))

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

    for i in range(len(dbConductorCu)):
        Zunitaria=Z(round(Rn(dbConductorCu[i][Rj],Ta),4),dbConductorCu[i][Xj],Fp)
        datos[i].append(Zunitaria[0])

    for i in range(len(dbConductorCu)):
        Zunitaria=Z(round(Rn(dbConductorCu[i][Rj],Ta),4),dbConductorCu[i][Xj],Fp)
        datos[i].append(Zunitaria[1])

    for i in range(len(dbConductorCu)):
        Zunitaria=Z(round(Rn(dbConductorCu[i][Rj],Ta),4),dbConductorCu[i][Xj],Fp)
        datos[i].append(Zunitaria[2])

    for i in range(len(dbConductorCu)):
        Zunitaria=Z(round(Rn(dbConductorCu[i][Rj],Ta),4),dbConductorCu[i][Xj],Fp)
        datos[i].append(Zunitaria[3])
        
    if (View ==1):    
        return print(tabulate(datos, headers=["AWG/KCM","1F/2H", "2F/3H","3F/3H","3F/4H"], tablefmt='psql'))
    elif (View==2):
        return  datos
    

def zpual(Type=None,Ta=None,Fp=None,View=None):

    if(Type==None or Ta==None or Fp==None or View==None):
        t = time.localtime()
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                    ElectricalWireSizes                    ")
        print("                 ",time.asctime(t))
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("                                                           ")
        print("                         ─▄▀─▄▀")
        print("                         ──▀──▀")
        print("                         █▀▀▀▀▀█▄")
        print("                         █░░░░░█─█")
        print("                         ▀▄▄▄▄▄▀▀")
        print("                                                           ")
        print("-----------------------------------------------------------")
        print("| Los parámetros no son correctos para                    |")
        print("| el módulo zpual(Type,Ta,Fp,View)                        |")
        print("-----------------------------------------------------------")
        return     
    

    if Type==1:
    #Conductores en ducto de PVC
        Rj=1
        Xj=2
    elif Type==2:
    #Conductores en ducto de Alumunio
        Rj=3
        Xj=4
    elif Type==3:
    #Conductores en ducto de Acero
        Rj=5
        Xj=6
    #print(tabulate(datos))

    datos=[
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

    for i in range(len(dbConductorAl)):
         Zunitaria=Z(round(Rn(dbConductorAl[i][Rj],Ta),4),dbConductorAl[i][Xj],Fp)
         datos[i].append(Zunitaria[0])
         
    for i in range(len(dbConductorAl)):
         Zunitaria=Z(round(Rn(dbConductorAl[i][Rj],Ta),4),dbConductorAl[i][Xj],Fp)
         datos[i].append(Zunitaria[1])
         
    for i in range(len(dbConductorAl)):
         Zunitaria=Z(round(Rn(dbConductorAl[i][Rj],Ta),4),dbConductorAl[i][Xj],Fp)
         datos[i].append(Zunitaria[2])
         
    for i in range(len(dbConductorAl)):
         Zunitaria=Z(round(Rn(dbConductorAl[i][Rj],Ta),4),dbConductorAl[i][Xj],Fp)
         datos[i].append(Zunitaria[3])
        
    if (View ==1):    
        return print(tabulate(datos, headers=["AWG/KCM","1F/2H", "2F/3H","3F/3H","3F/4H"], tablefmt='psql'))
    elif (View==2):
        return  datos 
