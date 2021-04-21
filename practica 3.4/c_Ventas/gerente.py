#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
#practica 3.4
from empleado import *

class gerente(empleado):
    def calcularSueldo(self, descuentos, bonos=0):
        return self.sueldoBase-descuentos+bonos

maros=empleado("Marcos Rios", 221, 30000)
julia=gerente("Julia Campos", 109, 6000)
