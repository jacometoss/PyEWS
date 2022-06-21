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
import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects):
    """Funcion para agregar una etiqueta con el valor en cada barra"""
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 1),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def graph(mydata=None,condA=None,condB=None,w=None,h=None,material=None,color=None,sistema=None):


    if((mydata==None or not mydata) or condA==None or condB==None or w==None or h==None or material==None or color==None or sistema==None):
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
        print("| graph(mydata,Cal,Cal,Ancho,Alto,Material,Color,Sistema)   |") 
        print("----------------------------------------------- -------------")
        return         


    xdata=[]
    ydata=[]
    y1data=[]
    y2data=[]

    for i in range(len(mydata)):
        xdata.append(mydata[i][0])
            
        if(sistema==1):
            slabel="%Vd 1F/2H"
            ydata.append(mydata[i][8])
        elif(sistema==2):
            slabel="%Vd 2F/3H"
            ydata.append(mydata[i][9])
        elif(sistema==3):
            slabel="%Vd 3F/3H"
            ydata.append(mydata[i][10])
        elif(sistema==4):
            slabel="%Vd 3F/4H"
            ydata.append(mydata[i][10])
  
    if material==1:
        xConductor =["14 AWG", "12 AWG", "10 AWG", "8 AWG", "6 AWG", "4 AWG", "2 AWG", "1/0 AWG", "2/0 AWG", "3/0 AWG", "4/0 AWG", "250 KCM", "300 KCM", "350 KCM", "400 KCM", "500 KCM", "600 KCM", "750 KCM", "1000 KCM"]
    elif material==2:
        xConductor =["6 AWG", "4 AWG", "2 AWG", "1/0 AWG", "2/0 AWG", "3/0 AWG", "4/0 AWG", "250 KCM", "300 KCM", "350 KCM", "400 KCM", "500 KCM", "600 KCM", "750 KCM", "1000 KCM"]


    for i in range(len(xConductor)):
        if condA==xConductor[i]:
            a=i
            break

    for i in range(len(xConductor)):
        if condB==xConductor[i]:
            b=i+1
            break


    x=xdata
    #print(x)
    numero_de_grupos = len(ydata[a:b])
    indice_barras = np.arange(numero_de_grupos)
    ancho_barras =0.5
    plt.figure(figsize=(w,h))
    rects1 = plt.bar(indice_barras + ancho_barras/10,ydata[a:b], width=ancho_barras,label=slabel, color=color)
    plt.legend(loc='best')
    autolabel(rects1)
    plt.xticks(indice_barras, (x[a:b]))
  
    plt.ylabel('Caída de tensión porcentual [%Vd]')
    plt.xlabel('Calibre de conductores elécticos')
    plt.title('Caída de tensión en conductores eléctricos')
    plt.grid()
    plt.show()
