import calendar 
from datetime import datetime

while True:
    valor = int(input("Introduce un mes: "))
    if valor< 13 or valor>0:
        if valor==1 or valor==3 or valor==5 or valor==7 or valor==8 or valor==10 or valor==12:
            print("tiene 31 dias") 
            break
        if valor==4 or valor==6 or valor==9 or valor==11:
            print("tiene 30 dias")
            break
        if valor==2:
            fecha_hoy= datetime.now()
            año = fecha_hoy.year
            if calendar.isleap(año):
                print(29)
                break
            else:
                print(28)
                break

         
     
     
