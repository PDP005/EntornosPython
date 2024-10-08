import random

num = random.randint(0,100)
print(num)
intentos=0
while True:
    valor = int(input("Introduce un num: "))
    intentos+=1
    if valor==num:
        print("CORRECTO")
        break
    if valor>num:
        print("es MENOR")
    if valor<num:
        print("es MAYOR")
    if intentos==10:
        print("HAS ALCANZADO EL NUMRO DE INTENTOS")
        break