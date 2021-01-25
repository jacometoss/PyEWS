from tabulate import tabulate
import math

'''
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
| PYEWS, ElectricalWireSizes, 24/01/2021                                 |
| Version : 0.1.16                                                       |
| Autor : Marco Polo Jacome Toss                                         |
| License: GNU Affero General Public License v3 (GPL-3.0)                |
| Requires: Python >=3.5                                                 |
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''
dbConductorCu=[["14 AWG",10.171,0.1903,10.171,0.1903,10.171,0.2395,20,20,25],
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

dbConductorAl=[["6 AWG",2.658,0.1673,2.658,0.1673,2.658,0.2100,40,50,60],
["4 AWG",1.673,0.1575,1.673,0.1575,1.673,0.1969,55,65,75],
["2 AWG",1.050,0.1476,1.050,0.1476,1.050,0.1870,75,90,100],
["1/0 AWG",0.688,0.1444,0.689,0.1444,0.656,0.1804,100,120,135],
["2/0 AWG",0.525,0.1411,0.525,0.1411,0.525,0.1772,115,135,150],
["3/0 AWG",0.427,0.1378,0.427,0.1378,0.427,0.1706,130,155,175],
["4/0 AWG",0.328,0.1345,0.361,0.1345,0.328,0.1673,150,180,205],
["250 KCM",0.279,0.1345,0.295,0.1345,0.282,0.1706,170,205,230],
["300 KCM",0.233,0.1345,0.249,0.1345,0.236,0.1673,190,230,255],
["350 KCM",0.200,0.1312,0.217,0.1312,0.207,0.1640,210,250,280],
["400 KCM",0.178,0.1312,0.194,0.1312,0.180,0.1608,225,270,305],
["500 KCM",0.141,0.1280,0.158,0.1280,0.148,0.1575,260,310,350],
["600 KCM",0.118,0.1280,0.135,0.1280,0.124,0.1575,285,340,385],
["750 KCM",0.095,0.1247,0.112,0.1247,0.102,0.1575,320,385,435],
["1000 KCM",0.089,0.1214,0.082,0.1214,0.097,0.1509,375,445,500]]

dbConductorCuStd=[["14 AWG",8.43,8.43,8.43,15,20,25],
["12 AWG",5.45,5.45,5.45,20,25,30],
["10 AWG",3.41,3.41,3.41,30,35,40],
["8 AWG",2.14,2.14,2.14,40,50,55],
["6 AWG",1.35,1.35,1.35,55,65,75],
["4 AWG",0.846,0.846,0.846,70,85,95],
["2 AWG",0.531,0.531,0.531,95,115,130],
["1/0 AWG",0.335,0.335,0.335,125,150,170],
["2/0 AWG",0.266,0.266,0.266,145,175,195],
["3/0 AWG",0.211,0.211,0.211,165,200,225],
["4/0 AWG",0.1670,0.1670,0.1670,195,230,260],
["250 KCM",0.1410,0.1410,0.1410,215,255,290],
["300 KCM",0.118,0.118,0.118,240,285,320],
["350 KCM",0.101,0.101,0.101,260,310,350],
["400 KCM",0.0882,0.0882,0.0882,280,335,380],
["500 KCM",0.0708,0.0708,0.0708,320,380,430],
["600 KCM",0.0590,0.0590,0.0590,350,420,475],
["700 KCM",0.0505,0.0505,0.0505,385,460,520],
["750 KCM",0.0472,0.0472,0.0472,400,475,535],
["800 KCM",0.0443,0.0443,0.0443,410,490,555],
["900 KCM",0.0394,0.0394,0.0394,435,520,585],
["1000 KCM",0.0354,0.0354,0.0354,455,545,615],
["1250 KCM",0.0283,0.0283,0.0283,495,590,665],
["1500 KCM",0.0236,0.0236,0.0236,525,625,705],
["1750 KCM",0.0202,0.0202,0.0202,545,650,735],
["2000 KCM",0.0177,0.0177,0.0177,555,665,750]]



def Rn(Ra,T2):
    Rb=(Ra/(234.5+75))*(234.5+T2)
    return Rb

def RnCd(Ra,T2):
    Rb=(Ra/(234.5+25))*(234.5+T2)
    return Rb

def Z(R,X,FP):
    Z=(R*FP+X*math.sin(math.acos(FP)))
    FN=1/((2*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    FFN=1/((100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    FFFN=1/((math.sqrt(3)*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    FFF=1/((math.sqrt(3)*100)*((R*FP+X*math.sin(math.acos(FP)))/1000))
    return [round(FN,4),round(FFN,4),round(FFFN,4),round(FFF,4),round(Z,4)]

def Rcd(R):
    Rcond=(R)
    PN=1/((2*100)*((Rcond)/1000))
    return [round(PN,4),round(Rcond,4)]

def DBC(conductor):
    if conductor ==1:
        print(tabulate(dbConductorCu, headers=["AWG/KCM","R(Ω/km)", "X (Ω/km)","R (Ω/km)","X (Ω/km)", "R (Ω/km)", "X (Ω/km)", "60°C", "75°C", "90°C"], tablefmt='psql'))
    elif conductor==2:
        print(tabulate(dbConductorAl, headers=["AWG/KCM","R(Ω/km)", "X (Ω/km)","R (Ω/km)","X (Ω/km)", "R (Ω/km)", "X (Ω/km)", "60°C", "75°C", "90°C"], tablefmt='psql'))
    elif conductor==3:
        print(tabulate(dbConductorCuStd, headers=["AWG/KCM","R[A](Ω/km)", "R[B](Ω/km)","R[C](Ω/km)", "60°C", "75°C", "90°C"], tablefmt='psql'))        
    
def FCT(Ta):
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
        
    
def MBTCU(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S,Fp,View):

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

    for i in range(len(dbConductorCu)):
         datos[i].append(dbConductorCu[i][7])

    for i in range(len(dbConductorCu)):
         datos[i].append(dbConductorCu[i][8])

    for i in range(len(dbConductorCu)):
         datos[i].append(dbConductorCu[i][9])


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
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][6],3)*FA*FT75>In) or (round(datos[i][7],3)*FA*FT90>In)):
                    datos[i].append('Yes')
                else:
                    datos[i].append('Not')
                    
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
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][6],3)*FA*FT75)>In or (round(datos[i][7],3)*FA*FT90>In)):
                    
                    datos[i].append('Yes')
                else:
                    datos[i].append('Not')
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
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][6],3)*FA*FT75>In) or (round(datos[i][7],3)*FA*FT90>In)):
                    
                    datos[i].append('Yes')
                else:
                    datos[i].append('Not')
                    
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
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][6],3)*FA*FT75>In) or (round(datos[i][7],3)*FA*FT90>In)):
                    
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
            else:
                datos[i].append('Not')
                    
            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
    if View == 1:
        #Mostrar información en PSQL
        print(tabulate(datos, headers=["AWG/KCM","1F/2H", "2F/3H","3F/3H","3F/4H", "60", "75", "90","%Vd/1F", "%Vd/2F","%Vd/3F","%Vd/3F","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))
    elif View == 2:
        #Mostrar la información en lista
        return datos
    

def MBTAL(VF,VL,In,Nc,L,FA,Type,Ta,Vd,S,Fp,View):

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

    

    #for i in range(len(dbConductor)):
    #datos[i].append(round(Rn(dbConductor[i][1],75),4))

    #for i in range(len(dbConductor)):
    #    datos[i].append(dbConductor[i][2])

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

    for i in range(len(dbConductorAl)):
         datos[i].append(dbConductorAl[i][7])

    for i in range(len(dbConductorAl)):
         datos[i].append(dbConductorAl[i][8])

    for i in range(len(dbConductorAl)):
         datos[i].append(dbConductorAl[i][9])


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
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][6],3)*FA*FT75>In) or (round(datos[i][7],3)*FA*FT90>In)):
                    datos[i].append('Yes')
                else:
                    datos[i].append('Not')
                    
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
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][6],3)*FA*FT75)>In or (round(datos[i][7],3)*FA*FT90>In)):
                    
                    datos[i].append('Yes')
                else:
                    datos[i].append('Not')
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
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][6],3)*FA*FT75>In) or (round(datos[i][7],3)*FA*FT90>In)):
                    
                    datos[i].append('Yes')
                else:
                    datos[i].append('Not')
                    
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
                
                if ((round(datos[i][5],3)*FA*FT60>In) or (round(datos[i][6],3)*FA*FT75>In) or (round(datos[i][7],3)*FA*FT90>In)):
                    
                    datos[i].append(' Yes')
                else:
                    datos[i].append(' Not')
            else:
                datos[i].append('Not')
                    
            for j in range(len(SITM)):
                if (SITM[j]>Nc*In*1.25):
                    datos[i].append(SITM[j])
                    break
    if View == 1:
        #Mostrar información en PSQL
        print(tabulate(datos, headers=["AWG/KCM","1F/2H", "2F/3H","3F/3H","3F/4H", "60", "75", "90","%Vd/1F", "%Vd/2F","%Vd/3F","%Vd/3F","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))
    elif View == 2:
        #Mostrar la información en lista
        return datos
##-----------------------------------------------------------------------------------------------------------##
def MBTCUSTD(Vcd,In,Nc,L,Class,Ta,Vd,View):

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
            if ((round(datos[i][4],3)*FT60>In) or (round(datos[i][5],3)*FT75>In) or (round(datos[i][6],3)*FT90>In)):
                datos[i].append('Yes')
            else:
                datos[i].append('Not')
        else:
            datos[i].append('Not')                
        
        for j in range(len(SITM)):
            if (SITM[j]>Nc*In*1.25):
                datos[i].append(SITM[j])
                break
                
    if View == 1:
        #Mostrar información en PSQL
        print(tabulate(datos, headers=["AWG/KCM","Kcd [A,B,C]", "60", "75", "90","%Vd","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))
    elif View == 2:
        #Mostrar la información en lista
        return datos
    
def DBCIRCUIT(carga,view,conductor):

    if len(carga)==1:
        dbcircuit=[["1"]] 
    elif len(carga)==2:
        dbcircuit=[["1"],["2"]] 
    elif len(carga)==3:
        dbcircuit=[["1"],["2"],["3"]] 
    elif len(carga)==4:
        dbcircuit=[["1"],["2"],["3"],["4"]] 
    elif len(carga)==5:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"]] 
    elif len(carga)==6: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"]]     
    elif len(carga)==7:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"]] 
    elif len(carga)==8:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"]]     
    elif len(carga)==9:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"]]     
    elif len(carga)==10:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"]] 
    elif len(carga)==11:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"]] 
    elif len(carga)==12:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"]] 
    elif len(carga)==13:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"]] 
    elif len(carga)==14:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"]] 
    elif len(carga)==15:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"]]    
    elif len(carga)==16:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"]]     
    elif len(carga)==17:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"]] 
    elif len(carga)==18:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"]] 
    elif len(carga)==19:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"]]     
    elif len(carga)==20: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"]]     
    elif len(carga)==21: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"]]          
    elif len(carga)==22: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"],["22"]]          
    elif len(carga)==23: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"],["22"],["23"]]         
    elif len(carga)==24: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"],["22"],["23"],["24"]]
    elif len(carga)==25: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"],["22"],["23"],["24"],["25"]]
        
    datos=[]  
    for i in range(len(carga)):
        if conductor ==1:
            datos.append(MBTCU(carga[i][1],carga[i][2],carga[i][3],carga[i][4],carga[i][5],carga[i][6],carga[i][7],carga[i][8],carga[i][9],carga[i][10],carga[i][11],carga[i][12])) 
        elif conductor ==2:
            datos.append(MBTAL(carga[i][1],carga[i][2],carga[i][3],carga[i][4],carga[i][5],carga[i][6],carga[i][7],carga[i][8],carga[i][9],carga[i][10],carga[i][11],carga[i][12])) 
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
                    dbcircuit[i].append("3F/3H")
                
                
                dbcircuit[i].append(FCT(carga[i][8]))
                dbcircuit[i].append(carga[i][6]) 
                
                
                #dbcircuit[i].append(datos[i][j][2])
                #dbcircuit[i].append(datos[i][j][3])
                #dbcircuit[i].append(datos[i][j][4])
                dbcircuit[i].append(datos[i][j][5])
                dbcircuit[i].append(datos[i][j][6])
                dbcircuit[i].append(datos[i][j][7])
                
                if carga[i][9]==1:
                    dbcircuit[i].append(datos[i][j][8])
                elif carga[i][9]==2:
                    dbcircuit[i].append(datos[i][j][9])
                elif carga[i][9]==3:
                    dbcircuit[i].append(datos[i][j][10])
                elif carga[i][9]==4:
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
    print(tabulate(dbcircuit, headers=["Id","#CAL","L[m]", "Vd","FP","ALM", "Fct","Fa","60", "75", "90","Vd[%]","Nc", "In", "60", "75", "90", "ITM"], tablefmt='psql'))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------#            
def DBCIRCUITCD(carga,view,conductor):

    if len(carga)==1:
        dbcircuit=[["1"]] 
    elif len(carga)==2:
        dbcircuit=[["1"],["2"]] 
    elif len(carga)==3:
        dbcircuit=[["1"],["2"],["3"]] 
    elif len(carga)==4:
        dbcircuit=[["1"],["2"],["3"],["4"]] 
    elif len(carga)==5:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"]] 
    elif len(carga)==6: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"]]     
    elif len(carga)==7:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"]] 
    elif len(carga)==8:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"]]     
    elif len(carga)==9:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"]]     
    elif len(carga)==10:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"]] 
    elif len(carga)==11:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"]] 
    elif len(carga)==12:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"]] 
    elif len(carga)==13:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"]] 
    elif len(carga)==14:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"]] 
    elif len(carga)==15:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"]]    
    elif len(carga)==16:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"]]     
    elif len(carga)==17:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"]] 
    elif len(carga)==18:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"]] 
    elif len(carga)==19:
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"]]     
    elif len(carga)==20: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"]]     
    elif len(carga)==21: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"]]          
    elif len(carga)==22: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"],["22"]]          
    elif len(carga)==23: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"],["22"],["23"]]         
    elif len(carga)==24: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"],["22"],["23"],["24"]]
    elif len(carga)==25: 
        dbcircuit=[["1"],["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["10"],["11"],["12"],["13"],["14"],["15"],["16"],["17"],["18"],["19"],["20"],["21"],["22"],["23"],["24"],["25"]]
        
    datos=[]  
    for i in range(len(carga)):
        if conductor == 1:
            datos.append(MBTCUSTD(carga[i][1],carga[i][2],carga[i][3],carga[i][4],carga[i][5],carga[i][6],carga[i][7],carga[i][8])) 
            if view==1:
                print("Id [",i+1,"]============================================================================================================")
                print(tabulate(datos[i], headers=["AWG/KCMxx","Kcd [A,B,C]", "", "60", "75", "90","%Vd","Nc", "In", "60", "75", "90", "Op", "ITM"], tablefmt='psql'))
        elif conductor == 2:
            datos.append(MBTCUSTD(carga[i][1],carga[i][2],carga[i][3],carga[i][4],carga[i][5],carga[i][6],carga[i][7],carga[i][8]))
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
