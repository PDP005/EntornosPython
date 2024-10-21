cad:str=" "
import random
listanums=list()
# numhansalido=list() para si tienen que ser dif
def numeros ():
    return random.randint(1, 49)

print(" ---------------")
for i in range(0,10):
    cad=" "
    for q in range(0,5):
        if q==0:
            if i==0:
                num="*"
            else:
                num=str(i)
        else:
            num=i+(q*10)
        cad=cad+" "+str(num)
    print(cad)
print(" ---------------")

for i in range(0,6):
    """ if de q sea > 0 y < 40 """
    num=int(input("Di números "))
    listanums.append(num)
print(listanums)
numerosacertados=0
for q in range(0,6):
    num=numeros()
    print(num)
    # if num not in numhansalido:
    if num in listanums:
        numerosacertados+=1
        print("tienes el ",num)
print("has acertado ",numerosacertados)       
""" if con los premios  """



  