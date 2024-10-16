def ordenado(lista):
    listabn=list(lista) 
    listabn.sort()
    if listabn==lista:
        print("esta ordenada")
    else :
        print("no esta ordenada ")

listaOrdenado=[1,2,3,4,5,6,7,8,9,10,11,12]
listaCaos=[3,1,2,4,5,6,7,8,10,12,11,9]

ordenado(listaOrdenado)
ordenado(listaCaos)