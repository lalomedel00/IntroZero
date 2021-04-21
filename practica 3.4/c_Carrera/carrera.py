#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
#practica 3.4
class carrera:
    def __init__(self, nombre):
        self.nombre=nombre
        self.__materias={}

    def agregarMateria(self, materia, codigo):
        self.__materias[codigo]=materia

ing=carrera("Ingenieria")
algebra=materia("Algebra", "Ricardo Quinteros")
fisica=materia("fisica", "Margarita Gomez")
quimica=materia("Quimica", "Lorena Rios")