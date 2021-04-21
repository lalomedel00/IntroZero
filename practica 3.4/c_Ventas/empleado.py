#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
#practica 3.4
class empleado:
    def __init__(self, nombre, edad, legajo, sueldo):
        self.nombre=nombre
        self.edad=edad
        self.legajo=legajo
        self.sueldoBase=sueldo

    def calcularSueldo(self, descuentos, bonos):
        return self.sueldoBase-descuentos+bonos
