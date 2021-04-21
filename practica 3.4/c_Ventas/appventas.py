#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
#practica 3.4
from empleado import *
from agenteVentas import *
from Tripulante import *
from gerente import *

Mario = empleado("Mario Medel", 18, "MAME", 2000)
print(Mario.nombre)
print(Mario.calcularSueldo(100,1500))

Eliseo = Tripulante("Eliseo Medel", 45, "EMP0", 6000)
print(Eliseo.mostrarRenovacionLicencia())

Lorena = gerente("Lorena Alamillo", 45, "LAE0", 8000)
print(Lorena.calcularSueldo(500,4000))
