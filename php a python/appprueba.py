#Jesus Eduardo Medel Alamillo
#informatica
#Desarrollo de aplicaciones web
from caja import *
cajita = caja(40,60,20)

print ("medidas caja: ",cajita.mostrar())
print ("Volumen: ", cajita.calcularVolumen())
print("Area Total: ", cajita.areaTotal())
miClon = cajita.clon()
print ("medidas del clon: ",miClon)
caja25masGrande = cajita.crearCajaGrande()
print (caja25masGrande.mostrar)
de = miClon.cabe1dentrode2(cajita, caja25masGrande)
print ("Mas grande?: ", de)