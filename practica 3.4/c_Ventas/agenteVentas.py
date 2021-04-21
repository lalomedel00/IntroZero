#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
#practica 3.4
from empleado import *

class agenteVentas(empleado):
    def __init__(self,  nombre, edad, legajo, sueldo, mostrador):
        self.numeroMostrador=mostrador
        super().__init__(nombre, edad, legajo, sueldo)