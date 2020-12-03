from tabulate import tabulate
import math

'''

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
| PYEWS, ElectricalWireSizes, 09/11/2020                                 |
| Version : 0.1.12                                                       |
| Autor : Marco Polo Jacome Toss                                         |
| License: GNU Affero General Public License v3 (GPL-3.0)                |
| Requires: Python >=3.5                                                 |
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

'''
dbConductor=[["14 AWG",10.171,0.1903,10.171,0.1903,10.171,0.2395,20,20,25],
["12 AWG",6.5617,0.1772,6.5617,0.1772,6.5617,0.2231,25,25,30],
["10 AWG",3.937,0.1640,3.937,0.1640,3.937,0.2067,30,35,40],
["8 AWG",2.5591,0.1706,2.5591,0.1706,2.5591,0.2133,40,50,55],
["6 AWG",1.6076,0.1673,1.6076,0.1673,1.6076,0.2100,55,65,75],
["4 AWG",1.0171,0.1575,1.0171,0.1575,1.0171,0.1969,70,85,95],
["2 AWG",0.6234,0.1476,0.6562,0.1476,0.6562,0.1870,95,115,130],
["1/0 AWG",0.3937,0.1444,0.4265,0.1444,0.3937,0.1804,125,150,170],
["2/0 AWG",0.3281,0.1411,0.3281,0.1411,0.3281,0.1772,145,175,195],
["3/0 AWG",0.2526,0.1378,0.269,0.1378,0.2592,0.1706,165,200,225],
["4/0 AWG",0.2034,0.1345,0.2198,0.1345,0.2067,0.1673,195,230,260],
["250 KCM",0.1706,0.1345,0.187,0.1345,0.1772,0.1706,215,255,290],
["300 KCM",0.1444,0.1345,0.1608,0.1345,0.1476,0.1673,240,285,320],
["350 KCM",0.1247,0.1312,0.1411,0.1312,0.128,0.1640,260,310,350],
["400 KCM",0.1083,0.1312,0.1247,0.1312,0.1148,0.1608,280,335,380],
["500 KCM",0.0886,0.1280,0.105,0.1280,0.0951,0.1575,320,380,430],
["600 KCM",0.0755,0.1280,0.0919,0.1280,0.082,0.1575,355,420,475],
["750 KCM",0.0623,0.1247,0.0787,0.1247,0.0689,0.1575,400,475,535],
["1000 KCM",0.0492,0.1214,0.0623,0.1214,0.0591,0.1509,455,545,615]]

def Rn(Ra,T2):
    Rb=(Ra/(234.5+75))*(234.5+T2)
    return Rb

def Z(R,X,FP):
    Z=(R*FP+X*math.sin(math.acos(FP)))
    FN=1/((2*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    FFN=1/((100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    FFFN=1/((math.sqrt(3)*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    FFF=1/((math.sqrt(3)*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    return [round(FN,4),round(FFN,4),round(FFFN,4),round(FFF,4),round(Z,4)]

def DBC():
    print(tabulate(dbConductor, headers=["AWG/KCM","R(Ω/km)", "X (Ω/km)","R (Ω/km)","X (Ω/km)", "R (Ω/km)", "X (Ω/km)", "60°C", "75°C", "90°C"], tablefmt='psql'))
    
def MBTCU(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S,Fp):

    if Ta >= 60:
        FT60=0.0
    else :
        FT60=round(math.sqrt((60-Ta)/(60-30)),3)

    if Ta >= 75:
        FT75=0.0
    else :
        FT75=round(math.sqrt((75-Ta)/(75-30)),3)


    if Ta >= 90:
        FT90=0.0
    else :
        FT90=round(math.sqrt((90-Ta)/(90-30)),3)



    SITM=[0,15,20,25,30,35,40,45,50,60,70,80,90,100,110,125,150,175,200,225,250,300,350,400,450,500,600,700,800,1000,1200,1600,2000,2500,3000,4000,5000,6000]


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

    In=In/Nc

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
    ["750 KCM"],
    ["1000 KCM"]]




    #for i in range(len(dbConductor)):
    #datos[i].append(round(Rn(dbConductor[i][1],75),4))

    #for i in range(len(dbConductor)):
    #    datos[i].append(dbConductor[i][2])

    for i in range(len(dbConductor)):
         Zunitaria=Z(round(Rn(dbConductor[i][Rj],Ta),4),dbConductor[i][Xj],Fp)
         datos[i].append(Zunitaria[0])
         
    for i in range(len(dbConductor)):
         Zunitaria=Z(round(Rn(dbConductor[i][Rj],Ta),4),dbConductor[i][Xj],Fp)
         datos[i].append(Zunitaria[1])
         
    for i in range(len(dbConductor)):
         Zunitaria=Z(round(Rn(dbConductor[i][Rj],Ta),4),dbConductor[i][Xj],Fp)
         datos[i].append(Zunitaria[2])
         
    for i in range(len(dbConductor)):
         Zunitaria=Z(round(Rn(dbConductor[i][Rj],Ta),4),dbConductor[i][Xj],Fp)
         datos[i].append(Zunitaria[3])

    for i in range(len(dbConductor)):
         datos[i].append(dbConductor[i][7])

    for i in range(len(dbConductor)):
         datos[i].append(dbConductor[i][8])

    for i in range(len(dbConductor)):
         datos[i].append(dbConductor[i][9])


    for i in range(len(datos)):

        if S==1:
            
            D1=LIn/(datos[i][1]*VF)
            datos[i].append(round(D1,3))
        
            D2=LIn/(datos[i][2]*VF)
            datos[i].append(round(D2,3))

            D3=LIn/(datos[i][3]*VL)
            datos[i].append(round(D3,3))

            D4=LIn/(datos[i][4]*VL)
            datos[i].append(round(D4,3))
            
            datos[i].append(Nc)
            datos[i].append(round(In,2))
            
            datos[i].append(round(datos[i][5],3)*FA*FT60)
            datos[i].append(round(datos[i][6],3)*FA*FT75)
            datos[i].append(round(datos[i][7],3)*FA*FT90)
            
            if Vd > D1:
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][5],3)*FA*FT75>In) or (round(datos[i][5],3)*FA*FT90>In)):
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
                    
            else:
                datos[i].append('Not')
                
            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
                    
                    
            
        elif S==2:
            
            D1=LIn/(datos[i][1]*VF)
            datos[i].append(round(D1,3))

            D2=LIn/(datos[i][2]*VF)
            datos[i].append(round(D2,3))

            D3=LIn/(datos[i][3]*VL)
            datos[i].append(round(D3,3))

            D4=LIn/(datos[i][4]*VL)
            datos[i].append(round(D4,3))

            datos[i].append(Nc)
            datos[i].append(round(In,2))
            
            datos[i].append(round(datos[i][5],3)*FA*FT60)
            datos[i].append(round(datos[i][6],3)*FA*FT75)
            datos[i].append(round(datos[i][7],3)*FA*FT90)

            if Vd > D2:
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][5],3)*FA*FT75)>In or (round(datos[i][5],3)*FA*FT90>In)):
                    
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
            else:
                datos[i].append('Not')
            
            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
                     

                    
        
        elif S==3:
            
            D1=LIn/(datos[i][1]*VF)
            datos[i].append(round(D1,3))

            D2=LIn/(datos[i][2]*VF)
            datos[i].append(round(D2,3))

            D3=LIn/(datos[i][3]*VL)
            datos[i].append(round(D3,3))

            D4=LIn/(datos[i][4]*VL)
            datos[i].append(round(D4,3))

            datos[i].append(Nc)
            datos[i].append(round(In,2))
            
            datos[i].append(round(datos[i][5],3)*FA*FT60)
            datos[i].append(round(datos[i][6],3)*FA*FT75)
            datos[i].append(round(datos[i][7],3)*FA*FT90)
            
            if Vd > D3:
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][5],3)*FA*FT75>In) or (round(datos[i][5],3)*FA*FT90>In)):
                    
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
                    
            else:
                datos[i].append('Not')

            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
                                    
        
        elif S==4:
            
            D1=LIn/(datos[i][1]*VF)
            datos[i].append(round(D1,3))

            D2=LIn/(datos[i][2]*VF)
            datos[i].append(round(D2,3))

            D3=LIn/(datos[i][3]*VL)
            datos[i].append(round(D3,3))

            D4=LIn/(datos[i][4]*VL)
            datos[i].append(round(D4,3))

            datos[i].append(Nc)
            datos[i].append(round(In,2))
            
            datos[i].append(round(datos[i][5],3)*FA*FT60)
            datos[i].append(round(datos[i][6],3)*FA*FT75)
            datos[i].append(round(datos[i][7],3)*FA*FT90)
            
            if Vd > D4:
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][5],3)*FA*FT75>In) or (round(datos[i][5],3)*FA*FT90>In)):
                    
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
            else:
                datos[i].append('Not')
                    
            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
        
    print(tabulate(datos, headers=["AWG/KCM","1F/2H", "2F/3H","3F/3H","3F/4H", "60", "75", "90","%Vd/1F", "%Vd/2F","%Vd/3F","%Vd/3F","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))

