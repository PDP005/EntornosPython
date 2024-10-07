valor = input("Introduce un caracter ")
if len(valor)==1:
    if valor>='a' and valor<='z':
        print("es minúscula")
    elif valor>='A' and valor<='Z':
        print("es mayuscula")
    elif int(valor)>=0 and int(valor)<=9:
        print("es un numero")
else:
    print("pon solo una letra")