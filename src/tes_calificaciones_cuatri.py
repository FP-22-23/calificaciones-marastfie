
from calificaciones import *


def main():
    c1= lee_real("Dame nota: ")
    c2= lee_real("Dame nota: ")
    c3= lee_real("Dame nota: ")
    pr1 =lee_real("Dame nota: ")
    ex1= lee_real("Dame nota: ")
    cuatrimestre1= calcula_nota_cuatrimestre(c1,c2,c3,pr1,ex1)
    c4= lee_real("Dame nota: ")
    c5= lee_real("Dame nota: ")
    c6= lee_real("Dame nota: ")
    pr2 =lee_real("Dame nota: ")
    ex2= lee_real("Dame nota: ")
    cuatrimestre2= calcula_nota_cuatrimestre(c4,c5,c6,pr2,ex2)
    print("Tu nota de evaluacioon continua:", calcula_nota_evaluacion_continua((cuatrimestre1*cuatrimestre2)/2)) 
    
if __name__ == "__main__":
    main()