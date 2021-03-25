#Nombre: Jesus Eduardo Medel Alamillo.
#carrera: Informatica.
#Materia: Desarrollo web.
#Practica_2.1_parte2.
import random
candidatoA = 0
candidatoB = 0
candidatoC = 0
count = 0
#aquie se pone el numero de votos que queremos simular.
while(count<2000000000):
    voto = random.randrange(1, 4)
    if(voto==1):
        candidatoA=candidatoA+1
    elif(voto==2):
        candidatoB=candidatoB+1
    else:
        candidatoC=candidatoC+1
    count =count+1

print("Votos candidato A: "+str(candidatoA))
print("Votos candidato B: "+str(candidatoB))
print("Votos candidato C: "+str(candidatoC))