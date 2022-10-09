from calificaciones import calcula_nota_cuestionario


from calificaciones import *

def main():
    aciertos= lee_entero("Dame tus aciertos: ")
    errores= lee_entero("Dame tus errores: ")
    respuestas_totales= lee_entero("dame el total de respuestas correctas del test: ")
    nota=calcula_nota_cuestionario(aciertos,errores, respuestas_totales)
    print("Tu nota es : ",nota) 

if __name__ == "__main__":
    main()