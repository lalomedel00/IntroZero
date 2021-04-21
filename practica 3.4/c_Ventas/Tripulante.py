#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
#practica 3.4
from empleado import *

class Tripulante(empleado):
    def mostrarRenovacionLicencia(self):
        if self.edad<50:
        print("Renueva su licencia cada año.")

    else:
        print("Renueva su licencia cada 6 meses.")
