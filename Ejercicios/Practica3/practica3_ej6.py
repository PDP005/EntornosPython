""" 
convertir (sg,**nargs)
convertir(121221) convierte
convertir(121,221) NO convierte
convertir(121,2,21) Si convierte

"""

ct=input("Escribe texto ")
array=ct.split(",")
print(array)
print(array[0])
print(len(array))

def segunosATiempo (arr):
    horas=int(int(arr[0])/3600)
    mins=int(int(arr[0])%3600/60)
    seg=int(int(arr[0])%3600%60)
    print(f"horas: {horas} mins: {mins} seg: {seg}")
    """print("horas: "+horas+" mins: "+mins)"""

def tiempoASefundos(arr):
    segundos=int(int(arr[0])*3600)+int(int(arr[1])*60)+int(arr[2])
    print(f"en seg son: {segundos}")

if len(array)==1:
    segunosATiempo(array)
elif len(array)==3:
    tiempoASefundos(array)
else:
    print("ERROR")
