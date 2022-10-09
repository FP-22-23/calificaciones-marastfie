
def lee_entero():
    res=int(input())
    return res 

def calcula_nota_cuestionario(aciertos,errores,respuestas_totales):
    return 10

def lee_real(mensaje):
    res = float(input(mensaje))
    return res
def calcula_nota_cuatrimestre(cuestionarios):
    res=10.0
    if cuestionarios[3] < 5 :
        res(3.0)
    else: 
        res= 0.1* (cuestionarios[0]+ cuestionarios[1] + cuestionarios[2]) + 0.1*cuestionarios[3] + 0.6*cuestionarios[4]
        return res

def calcula_nota_evaluacion_continua(cuatrimestre1,cuatrimestre2):
    if cuatrimestre1< 4.0 or cuatrimestre2<4.0:
        res = 4.0
    else: 
        res= (cuatrimestre1+cuatrimestre2)/2
        return res

