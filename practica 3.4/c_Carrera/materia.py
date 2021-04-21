#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
#practica 3.4
class materia:
    def __init__(self, nombre, profesor):
        self.nombre=nombre
        self.profesor=profesor

    @property
    def fechainicioDictado(self):
        return self._fechainicioDictado

    @fechainicioDictado.setter
    def fechainicioDictado(self, fecha):
        if fecha<2006:
            self._fechainicioDictado=2006
        else:
            self._fechainicioDictado=fecha

            

ing=carrera("Ingenieria")
algebra=materia("Algebra", "Ricardo Quinteros")
fisica=materia("fisica", "Margarita Gomez")
quimica=materia("Quimica", "Lorena Rios")