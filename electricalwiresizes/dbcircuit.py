from tabulate import tabulate
from .bd import dbConductorCu, dbConductorAl
import math, time
from .mbtcu import mbtcu
from .mbtal import mbtal
from .basicelecfunc import fct


def dbcircuit(carga=None,view=None,conductor=None, output=None):


    if(carga==None or view==None or conductor==None or output==None):
        t = time.localtime()
        print('''
                 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                               
                                 ElectricalWireSizes                      
                             
                 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                                                          
                                      ─▄▀─▄▀
                                      ──▀──▀
                                      █▀▀▀▀▀█▄
                                      █░░░░░█─█
                                      ▀▄▄▄▄▄▀▀
                                                                          
                 -------------------------------------------------------------
                 | Los parámetros no son correctos                           |
                 | para el módulo dbcircuit(Load,View,Conductor,Output)     |
                 -------------------------------------------------------------''')
        return  
    
    dbcircuit = [[str(i + 1)] for i in range(len(carga))]
        
    datos=[]  
    for i in range(len(carga)):
        if conductor ==1:
            datos.append(mbtcu(carga[i][1],carga[i][2],carga[i][3],carga[i][4],carga[i][5],carga[i][6],carga[i][7],carga[i][8],carga[i][9],carga[i][10],carga[i][11],carga[i][12],carga[i][13],carga[i][14],carga[i][15],carga[i][16])) 
        elif conductor ==2:
            datos.append(mbtal(carga[i][1],carga[i][2],carga[i][3],carga[i][4],carga[i][5],carga[i][6],carga[i][7],carga[i][8],carga[i][9],carga[i][10],carga[i][11],carga[i][12],carga[i][13],carga[i][14],carga[i][15],carga[i][16])) 
        if view==1:
            print("Id [",i+1,"]========================================================================================================================================================================")
            print(tabulate(datos[i], headers=["AWG/KCM","1F/2H", "2F/3H","3F/3H","3F/4H", "60", "75", "90","%Vd/1F", "%Vd/2F","%Vd/3F","%Vd/3F","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))
        #elif view==2:
        #    print("Id [",i+1,"] View = 1 PyEWS.DBCUIRCUIT(carga,1)") 
            
    if conductor==1:
        dbConductor=dbConductorCu
    elif conductor==2:
        dbConductor=dbConductorAl
        
    for i in range(len(carga)):
        for j in range(len(dbConductor)):
        
            if datos[i][j][17]=="Yes":
                dbcircuit[i].append(datos[i][j][0])
                #dbcircuit[i].append(datos[i][j][1])
                dbcircuit[i].append(carga[i][5])
                dbcircuit[i].append(carga[i][9])
                dbcircuit[i].append(carga[i][11])
             

                if carga[i][10]==1:
                    dbcircuit[i].append("1F/2H")
                elif carga[i][10]==2:
                    dbcircuit[i].append("2F/3H")
                elif carga[i][10]==3:
                    dbcircuit[i].append("3F/3H")
                elif carga[i][10]==4:
                    dbcircuit[i].append("3F/4H")
                
                
                dbcircuit[i].append(fct(carga[i][8],carga[i][14]))
                dbcircuit[i].append(carga[i][6]) 
                
                
                #dbcircuit[i].append(datos[i][j][2])
                #dbcircuit[i].append(datos[i][j][3])
                #dbcircuit[i].append(datos[i][j][4])
                dbcircuit[i].append(datos[i][j][5])
                dbcircuit[i].append(datos[i][j][6])
                dbcircuit[i].append(datos[i][j][7])
                
                #Error encontrado desde la version 0.1.13 en la selección 
           
                
                if carga[i][10]==1:
                    dbcircuit[i].append(datos[i][j][8])
                elif carga[i][10]==2:
                    dbcircuit[i].append(datos[i][j][9])
                elif carga[i][10]==3:
                    dbcircuit[i].append(datos[i][j][10])
                elif carga[i][10]==4:
                    dbcircuit[i].append(datos[i][j][11])
                
                
                dbcircuit[i].append(datos[i][j][12])
                dbcircuit[i].append(datos[i][j][13])
                dbcircuit[i].append(datos[i][j][14])
                dbcircuit[i].append(datos[i][j][15])
                dbcircuit[i].append(datos[i][j][16])
                #dbcircuit[i].append(datos[i][j][17])
                dbcircuit[i].append(datos[i][j][18])
                break

            

    #return dbcircuit
    print("::::::: [ RESUMEN DE CARGAS ]:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    #print(tabulate(dbcircuit, headers=["Id","AWG/KCM","l", "2F/3H","3F/3H","3F/4H", "60", "75", "90","%Vd/1F", "%Vd/2F","%Vd/3F","%Vd/3F","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))
    print(tabulate(dbcircuit, headers=["Id","#CAL","L[m]", "Vd","FP","ALM", "Fct","Fa","60", "75", "90","Vd[%]","Nc", "In", "60", "75", "90", "ITM"], tablefmt=output))

