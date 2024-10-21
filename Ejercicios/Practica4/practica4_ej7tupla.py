nombres=list()
nombresFound=list()
while True:
    nombre=input("Anota un nombre:\n=>")
    if nombre=="-1":
        break
    nombres.append(nombre)
maximo=-1
print(nombres)

def isInLista(n,lista):
    for t in lista:
        if t[0]==n:
            return True
    return False

for i in nombres:
    if i not in nombresFound:
        if isInLista(i,nombresFound)==False:
            """ si no lo encuentra lo añade contando cuántos hay  """
            f=nombres.count(i)
            t=(i,f)
            nombresFound.append(t)
                
print(nombresFound)
