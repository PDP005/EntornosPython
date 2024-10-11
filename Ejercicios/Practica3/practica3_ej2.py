ancho= int(input("ANCHO: "))
caracter=input("SÍMBOLO: ")

def triangulo(anchuramax,caracter):
    cad=""
    anchura=0
    while anchura < anchuramax:
        anchura+=1
        for i in range (anchura-1,anchura):
            cad = cad+caracter
        print(cad)

triangulo(ancho,caracter)

def terminartriangulo(anchuramax,caracter):
    anchuramax-=1
    for anchura in range(anchuramax, 0, -1):
        cad = caracter * anchura 
        print(cad)

terminartriangulo(ancho,caracter)
        

""" terminar hacia abajo  """

"""
def altura(anchura):
    alto=anchura/2
    print(alto)
    alto=(round(alto))
    print(alto)
    return alto
    """"print(alto)"""
"""
alt =int(altura(ancho))
"""
"""
def triangulo(anchura,caracter):
    cad=""
    for i in range (0,anchura):
        cad=cad+caracter
    print(cad)

""""""
anch=1

for w in range(0,(alt*2)-1):
   bajar=False
   triangulo(anch,caracter)
   if anch==alt:
       bajar=True
   if bajar==False:
       anch+=1
   if bajar==True:
       anch-=1
   
"""

