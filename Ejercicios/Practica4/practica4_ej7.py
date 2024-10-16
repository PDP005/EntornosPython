nombres=list()
nombresFound=list()
while True:
    nombre=input("Anota un nombre:\n=>")
    if nombre=="-1":
        break
    nombres.append(nombre)
maximo=-1

for i in nombres:
    buscar=i
    if i not in nombresFound[1]:
        #tupla de 2 valores paar luego ver que no salga
        nombresFound.append(i,nombresFound.count(i))
        
    
    # else:
                
    # x=0
    # for j in nombres:
    #     if buscar==j:
    #         x+=1
    # print(buscar+": ",x)
    
    # if maximo<x:
    #     maximo=x
print(nombresFound)
