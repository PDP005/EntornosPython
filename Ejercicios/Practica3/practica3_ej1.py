altura= int(input("ALTURA: "))
ancho= int(input("ANCHO: "))
caracter=input("SÍMBOLO: ")

def filas(anchura,caracter):
    cad=""
    for i in range (0,anchura):
        cad=cad+caracter
    return cad

fila=str(filas(ancho,caracter))

for w in range(0,altura):
    print(fila)

""" poner q el print sea dentro  """
