lista=[]
pares=[]
while True:
    ct=int(input("Dime num "))
    
    if ct<0:
        break
    else:
        lista.append(ct)
        if ct%2==0:
            pares.append(ct)

print(lista)
print(pares)
print(max(lista))


        
