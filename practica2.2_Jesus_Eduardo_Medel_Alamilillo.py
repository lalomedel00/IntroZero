#Jesus Eduardo Medel Alamillo
#Iformatica.
#Desarrollo de aplicaciones web
#practica 2.2
fecha = input ("fecha (formato 'dia, DD/MM'): ")#toma el formato de la fecha
fecha = fecha.lower()#convierte las letras a minusculas
dia = fecha[0:fecha.find(',')]#toma solo el dato que se ingresa en la parte del formato "dia,"
dian = int(fecha[fecha.find(" ")+1:fecha.find("/")])#tomamos el dia en digitos d numero y convertimos a entero, seleccionamos de donde a donde vamos a utilizar el numero
mesn = int(fecha[fecha.find("/")+1:])#tomamos el mes en numero y convertimos a entero de igual manera se selecciona de donde comienza a tomar el dato y hasta el final.
if dian > 31 or mesn > 12:
    print("Fecha Incorrecta") #esto rome el programa si no es comptible con la condicion
else: #aqui empieza la seleccion de los dias de la semana.
    if dia in "lunes,martes,miercoles": #si el dia escrito esta dentro de este arreglo dara comienzo a la condicion
        inicio=input("¿Se tomaron examenes? s/n: ")#que es preguntar si se tomaron examenes.
        if inicio.lower() == "s": #en caso de que si preguntara cuantos aprobaro y reproaron.
            ap = int(input("¿Cuantos aprobaron?: "))
            rp = int(input("¿Cuantos reprobaron?: "))
            print ("Porcentaje aprobatorio: ", (ap*100)/(ap+rp) ,"%")#y arrojara el porcentaje de aprobacion
    elif dia == "jueves": #seleccion del dia jueves
        asistencia = int(input("Porcentaje de asistencia: "))#se pregunta la asistencia
        if asistencia>50:#si es mayor a 50 dira que asisitio la mayoria si no dira lo contrario
            print("Asistio la mayoria.")
        else:
            print("No asisitio la mayoria")
    elif dia == "viernes":#seleccion del dia viernes
        if dian == 1 and (mesn == 1 or mesn == 7):
            print("Comienzo de nuevo ciclo")
            alumnos = int(input("Cantidad de alumnos: "))
            cuota = float(input("Cuota por alumno: $"))
            print ("Ingreso total: $", alumnos * cuota)
    else:
        print("Dia Incorrecto.")

print("Fin del programa...")