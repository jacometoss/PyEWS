from tabulate import tabulate
from .bd import dbConductorCuStd   
import math, time
from .mbtcustd import mbtcustd
from .basicelecfunc import fct

def dbcircuitcd(carga=None,view=None):

    if(carga==None or view==None):
        t = time.localtime()
        print('''
                 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
                                
                                    ElectricalWireSizes                       
                             
                 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 
                                                                           
                                      ─▄▀─▄▀ 
                                      ──▀──▀ 
                                      █▀▀▀▀▀█▄ 
                                      █░░░░░█─█ 
                                      ▀▄▄▄▄▄▀▀ 
                                                                           
                 ------------------------------------------------------------- 
                 | Los parámetros no son correctos para el módulo            | 
                 | dbcircuitcd(Load,View)                                    | 
                 -------------------------------------------------------------''') 
        return      
    
    dbcircuit = [[str(i + 1)] for i in range(len(carga))]
    
    datos=[]  
    for i in range(len(carga)):
        datos.append(mbtcustd(carga[i][1],carga[i][2],carga[i][3],carga[i][4],carga[i][5],carga[i][6],carga[i][7],carga[i][8],carga[i][9],carga[i][10],carga[i][11],carga[i][12])) 
        if view==1:
            print("Id [",i+1,"]============================================================================================================")
            print(tabulate(datos[i], headers=["AWG/KCM","Kcd [A,B,C]", "", "60", "75", "90","%Vd","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))



        
    dbConductor=dbConductorCuStd
        
    for i in range(len(carga)):
        for j in range(len(dbConductor)):
            
            if datos[i][j][11]=="Yes":
                
                dbcircuit[i].append(datos[i][j][0])
                dbcircuit[i].append(datos[i][j][1])
                dbcircuit[i].append(carga[i][2])
                dbcircuit[i].append(carga[i][7]) 
                dbcircuit[i].append("CD [+-]")
                dbcircuit[i].append(fct(carga[i][6]))
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
