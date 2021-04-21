#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
#practica 3.4
from classGato import *

a = Gato("michi", 2)
b = Gato("mimi", 4)

a.alimentos=["leche", "croquetas", "pollo"]
b.alimentos=["pescado", "croquetas", "pollo"]

print("El nombre del gato1: ", a.nombre)
print("El nombre del gato2: ", b.nombre)
print("Edad del gato1: ", a.edad)
a.verEtapaDeVida()
print("Edad del gato2: ", b.edad)
b.verEtapaDeVida()

print(a.esAlimentoFavorito("leche"))
print(b.esAlimentoFavorito("pasta"))
