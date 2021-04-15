#jesus eduardo medel alamillo
#informatica
#desarrollo web
#practica_2.3_funciones
#una disculpa profesor no soy muy bueno pensando para la programacion, hice el intento mas no lo logre.
from random import randrange
clas1 = 0
clas2 = 0
clas3 = 0
clas4 = 0
clas5 = 0


precio = int(input("Precio del boleto al dia de hoy: "))

i = 1
while i <= 100:
    edad = randrange(5, 70)
    if (edad in (5,6,7,8,9,10,11,12,13,14)):
        d1 = (30/100)
        pd1 = (1 - d1) * precio
        clas1 = clas1 + 1
        print(edad," años de edad le dan un descuento del 30%, ahora pagara: $",pd1," de $",precio)
        i = i +1
    elif (edad in (15,16,17,18,19)):
        d2 = (10/100)
        pd2 = (1 - d2) * precio
        clas2 = clas2 + 1
        print(edad," años de edad le dan un descuento del 10%, ahora pagara: $",pd2," de $",precio)
        i = i +1
    elif (edad in (20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45)):
        d3 = (15/100)
        pd3 = (1 - d3) * precio
        clas3 = clas3 + 1
        print(edad," años de edad le dan un descuento del 15%, ahora pagara: $",pd3," de $",precio)
        i = i +1
    elif (edad in (46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65)):
        d4 = (25/100)
        pd4 = (1 - d4) * precio
        clas4 = clas4 + 1
        print(edad," años de edad le dan un descuento del 25%, ahora pagara: $",pd4," de $",precio)
        i = i +1

    elif (edad in (66,67,68,69,70)):
        d5 = (35/100)
        pd5 = (1 - d5) * precio
        clas5 = clas5 + 1
        print(edad," años de edad le dan un descuento del 35%, ahora pagara: $",pd5," de $",precio)
        i = i +1
print ("Find del programa")