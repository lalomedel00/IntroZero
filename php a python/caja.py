#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
#una disculpa profe el programa me gano a partir de la comparacion de cajas.
class caja:
    def __init__(self, Ancho,Largo, Alto):
        self.ancho=Ancho
        self.largo=Largo
        self.alto=Alto

    def mostrar(self):
        mos = ("Alto ",self.alto," Ancho ", self.ancho," Largo ",self.largo)
        return mos
    def calcularVolumen(self):
        cv = ("Volumen: ",self.alto * self.ancho * self.alto)
        return cv

    def areaFrontal(self):
        af = ("Area frontal: ",self.alto * self.ancho)
        return af

    def areaLateral(self):
        ala = ("Area lateral: ",self.largo * self.alto)
        return ala

    def areaSuperior(self):
        asu = ("Area superior: ",self.largo * self.ancho)
        return asu

    def areaTotal(self):
        return (2*self.areaFrontal()) + (2*self.areaSuperior()) + (2*self.areaLateral())

    def clon(self):
        c = (self.ancho, self.largo, self.alto)
        return c

    def crearCajaGrande(self):
        nvoAlto = self.alto * 1.25
        nvoAncho = self.ancho * 1.25
        nvoLargo = self.largo * 1.25

        cajaNva = caja(nvoAlto, nvoAncho, nvoLargo)
        return cajaNva

    def cabe1dentrode2(self, clon, crearCajaGrande):
        if c.ancho< cajaNva.ancho and c.alto< cajaNva.alto and c.largo< cajaNva.largo:
            return "Si cabe"
        else:
            return "No cabe"