print("Ingresa A para seleccionar al Primer candidato")
print("Ingresa B para seleccionar al Segundo candidato")
print("Ingresa C para seleccionar al Tercer candidato")
try:
    candidato= str(input("Ingrese candidato: "))
    print (candidato)
    if(candidato=="A" or candidato=="a"):
        print("Usted a votado por el primer candidato")

    elif(candidato=="B" or candidato=="b"):
        print("Usted a votado por el segundo candidato")
    elif(candidato=="C" or candidato=="c"):
        print("Usted a votado por el tercer candidato")
    else:
        print("Opcion Erronea")
except:
  print("Opcion Erronea")