lista=['Lucas', 'Emma', 'Mateo', 'Sofia', 'Liam', 'Isabella', 'Noah', 'Mia', 'Ethan', 'Olivia']

def filtrarPalabras(lista,n):
    for x in lista:
        if len(x)>=n:
            print(x)

num=int(input("Letras "))

filtrarPalabras(lista,num)
