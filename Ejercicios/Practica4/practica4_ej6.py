import random

def ataque():
    return random.randint(1, 10)
def defensa():
    return random.randint(1,15)

def atacar(atacante,defensor):
    
    daño=int(atacante[1])
    defensa=int(defensor[2])
    """ hacer la resta de los ints  """
    daño=defensa-daño
    defensor[2]=daño
    print(atacante[0]," ataca a ",defensor[0])
    if defensor[2]<=0:
        print("***** ",defensor[0]," pierde *****")    
        return 0
    return 1

n1="samu"
n2="pdp"

# n1=input("nombre j1 ")
# n2=input("nombre j2 ")

j1=[n1,ataque(),defensa()]
j2=[n2,ataque(),defensa()]

print(j1)
print(j2)

empieza=random.randint(1,2)
terminar=1
while terminar!=0:
    if empieza==1:
        terminar=atacar(j1,j2)
        empieza=2
    else:
        terminar=atacar(j2,j1)
        empieza=1
        
    


