
def segundos(horas,minutos,segundos):
    resultado=horas*3600+minutos*60+segundos   
    return resultado
def tiempotot(seg):
    horas=seg//3600
    min=(seg%3600)//60
    segundos=(seg%3600)%60
    return(str(horas)+" "+str(min)+" "+str(segundos))