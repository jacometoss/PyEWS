import csv, time

def list_to_csv(name=None,data=None):

  if((name==None or data==None)):
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
                  | Los parámetros no son correctos                           | 
                  | para el módulo                                            | 
                  | list_to_csv(name,data)                                    |  
                  ------------------------------------------------------------- ''')
        return 

  headers = ['AWG/KCM',  '1F/2H', '2F/3H',  '3F/3H', '3F/4H',  '60 ', '75 ' , '90' , ' %Vd/1F',   '%Vd/2F',   '%Vd/3F',   '%Vd/3F', 'Nc', 'In', '60', '75','90', 'Op', 'ITM' ]
  data_with_headers = [headers] + data

  with open(name+'.csv', 'w', newline='') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerows(data_with_headers)
  print("Se creo el archivo "+ name +".csv")
