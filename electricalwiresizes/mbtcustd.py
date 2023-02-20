import math, time
from tabulate import tabulate
from .bd import dbConductorCuStd
from .basicelecfunc import RnCd, Rcd, fct

def mbtcustd(Vcd=None,In=None,Nc=None,L=None,Class=None,Ta=None,Vd=None,View=None,Fsc=None, To=None, Break=None, Fcond=None):

    if(Vcd==None or In==None or Nc==None or L==None or Class==None or Ta==None or Vd==None or View==None or Fsc==None or To==None or Break==None or Fcond==None):
        t = time.localtime()
        print('''
                 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                   
                                   ElectricalWireSizes                   
                          
                 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                                                         
                                        ─▄▀─▄▀
                                        ──▀──▀
                                        █▀▀▀▀▀█▄
                                        █░░░░░█─█
                                        ▀▄▄▄▄▄▀▀
                                                                         
                 ----------------------------------------------------------
                 | Los parámetros no son correctos                        |
                 | para el módulo mbtcustd(Vcd,In,Nc,L,Class,Ta,Vd,View,  |
                 |                           Fsc,To,Break,Fcond)          |
                 ---------------------------------------------------------|''')
        return  
    
    FT60=fct(Ta,60)
    FT75=fct(Ta,75)
    FT90=fct(Ta,90)

    if Class==1:
    #Conductores en ducto de PVC
        Rj=1
    elif Class==2:
    #Conductores en ducto de Alumunio
        Rj=2
    elif Class==3:
    #Conductores en ducto de Acero
        Rj=3
    #print(tabulate(datos))

    In=(In*Fsc)/Nc

    LIn=L*In
    
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
    ["700 KCM"],
    ["750 KCM"],
    ["800 KCM"],
    ["900 KCM"],
    ["1000 KCM"],
    ["1250 KCM"],
    ["1500 KCM"],
    ["1750 KCM"],
    ["2000 KCM"]]

    

    #for i in range(len(dbConductor)):
    #datos[i].append(round(Rn(dbConductor[i][1],75),4))

    #for i in range(len(dbConductor)):
    #    datos[i].append(dbConductor[i][2])

    for i in range(len(dbConductorCuStd)):
         Runitaria=Rcd(round(RnCd(dbConductorCuStd[i][Rj],Ta),4))
         datos[i].append(Runitaria[0])
        
    for i in range(len(dbConductorCuStd)):
         datos[i].append(dbConductorCuStd[i][4])

    for i in range(len(dbConductorCuStd)):
         datos[i].append(dbConductorCuStd[i][5])

    for i in range(len(dbConductorCuStd)):
         datos[i].append(dbConductorCuStd[i][6])


    for i in range(len(datos)):
        
        D1=LIn/(datos[i][1]*Vcd)
        datos[i].append(round(D1,3))
        

        datos[i].append(Nc)
        datos[i].append(round(In,2))
            
        datos[i].append(round(datos[i][2],3)*FT60)
        datos[i].append(round(datos[i][3],3)*FT75)
        datos[i].append(round(datos[i][4],3)*FT90)
        
        if Vd > D1:
            if (To==60):
                if ((round(datos[i][2],3)*FT60>=(In)) and (((round(datos[i][2],3))/In)>=Fcond)):
                    datos[i].append('Yes')
                else:
                    datos[i].append('Not')

            elif (To==75):
                if ((round(datos[i][3],3)*FT75>=(In)) and (((round(datos[i][3],3))/In)>=Fcond)):
                    datos[i].append('Yes')
                else:
                    datos[i].append('Not')
            elif (To==90):
                if ((round(datos[i][4],3)*FT90>=(In)) and (((round(datos[i][4],3))/In)>=Fcond)):
                    datos[i].append('Yes')
                else:
                    datos[i].append('Not')
        else:
            datos[i].append('Not')                
        
        SITM=[0,15,20,30,40,50,60,70,80,90,100,110,125,150,175,200,225,250,300,350,400,450,500,600,700,800,1000,1200,1600,2000,2500,3000,4000,5000,6000]

        for j in range(len(SITM)):
            if (SITM[j]>=(Nc*In*Fsc*Break)):
                datos[i].append(SITM[j])
                break
                
    if View == 1:
        #Mostrar información en PSQL
        print(tabulate(datos, headers=["AWG/KCM","Kcd [A,B,C]", "60", "75", "90","%Vd","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))
    elif View == 2:
        #Mostrar la información en lista
        return datos
