import random
""" O es amarillo """
colores=['R', 'O', 'A', 'V', 'B', 'N', 'F'] # 7
coloresmaquina=list()

def sacarcolores():
    return random.randint(0,6)

for i in range(0,5):
    coloresmaquina.append(colores[sacarcolores()])
print(coloresmaquina)