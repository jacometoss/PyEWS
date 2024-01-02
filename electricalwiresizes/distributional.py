import math, time
from tabulate import tabulate
from .basicelecfunc import Rn, RnCd, Z, Rcd, dbc, fct, zpucu, zpual, sistemaIn
from tabulate import tabulate 

def  redbtal(network=None,conductors=None,view=None):

    if(network==None or conductors==None  or view==None):
        t = time.localtime()
        print('''
                 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                
                                    ElectricalWireSizes                       
                             
                 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 
                                                                           
                                      ─▄▀─▄▀ 
                                      ──▀──▀ 
                                      █▀▀▀▀▀█▄ 
                                      █░░░░░█─█ 
                                      ▀▄▄▄▄▄▀▀ 
                                                                           
                 ------------------------------------------------------------- 
                 | Los parámetros no son correctos para el módulo            | 
                 | redbtal(network,conductors,view)                          | 
                 -------------------------------------------------------------''') 
        return 

    dtb=network[:][:]

    iDCal=["6 AWG", "4 AWG", "2 AWG", "1/0 AWG", "2/0 AWG", "3/0 AWG", "4/0 AWG", "250 KCM", "300 KCM", "350 KCM", "400 KCM", "500 KCM", "600 KCM", "750 KCM", "1000 KCM"]
    iDAlm=["", "1F/2H","2F/3H","3F/3H","3F/4H"]




    for i in range(len(network)):  
         for j in range(len(iDCal)):
            if (iDCal[j]==network[i][1]):
                for k in range(len(iDAlm)):
                    if (network[i][2]==iDAlm[k]):
                        #Zpu se complementa
                        dtb[i].append(conductors[j][k])
                        #print (datos[j][k])
    #print ("-------------------------------------")                     

    for i in range(len(network)):
        #Agregamos la corriente a la tabla
        dtb[i].append(sistemaIn(network,i))
        #print (SistemaIn(network,i))

    #print ("----------Corrientes--------") 
    #for j in range(len(dtb)-1, -1, -1):
    #     print(dtb[j][8]) 
    #print ("-------------------------------------") 


    Isuma= 0

    for i in range(len(dtb)-1, -1, -1):
        #print ("Valor sumado: ",dtb[i][4], "Index_",i)
        Isuma += (dtb[i][4])
        dtb[i].append(Isuma)


    Isuma= 0

    for i in range(len(dtb)-1, -1, -1):
        #print ("Valor sumado: ",dtb[i][3], "Index_",i)
        Isuma += (dtb[i][3])
        dtb[i].append(Isuma)


    Isuma= 0 

    for i in range(len(dtb)-1, -1, -1):
        #print ("Valor sumado: ",dtb[i][8], "Index_",i)
        Isuma += (dtb[i][8])
        dtb[i].append(Isuma)


    for i in range(len(dtb)):
        #print ("Valor sumado: ",dtb[i][9]*dtb[i][11], "Index_",i)
        dtb[i].append(dtb[i][11]*dtb[i][3])


    Isuma= 0 
    for i in range(len(dtb)-1,-1,-1):
        #print ("Valor sumado: ",dtb[i][9]*dtb[i][11], "Index_",i)
        Isuma = (dtb[i][12]/(dtb[i][6]*dtb[i][7]))
        dtb[i].append(round(Isuma,3))    

    Isuma= 0     
    for i in range(len(dtb)-1, -1, -1):
        #print ("Valor sumado: ",dtb[i][8], "Index_",i)
        Isuma += (dtb[i][13])
        dtb[i].append(round(Isuma,3))

    
    if view==1:
        print(tabulate(dtb,headers=["Punto","Cal.", "Fases", "D[m]", "P[W]","Fp", "T[V]", "Kcable", "In", "Psum+", "Dsum", "Is", "[Is][D]", "%Vd","%Vd+-"],tablefmt="psql"))
    elif view==2:
        print(dtb)
    else:
        print(tabulate(dtb,headers=["Punto","Cal.", "Fases", "D[m]", "P[W]","Fp", "T[V]", "Kcable", "In", "Psum+", "Dsum", "Is", "[Is][D]", "%Vd","%Vd+-"],tablefmt="psql"))
