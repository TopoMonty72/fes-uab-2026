###
# EXERCICIS
###

# Exercici 1: Determinar el més gran de dos nombres
# Demana a l'usuari que introdueixi dos nombres i mostra un missatge
# que indiqui quin és més gran o si són iguals.
num_1 = int(input("Introduce primer numero: \n"))
num_2 = int(input("Introduce el segundo numero: \n"))

if num_1 == num_2 :
    print(f"{num_1} y {num_2} son el mismo numero")
elif num_1 > num_2 :
    print(f"{num_1} es mayor que {num_2}")
else :
    print(f"{num_2} es mayor que {num_1}")


# Exercici 2: Calculadora senzilla
# Demana a l'usuari dos nombres i una operació (+, -, *, /).
# Fes l'operació i mostra'n el resultat (gestiona la divisió per zero).
num_1 = int(input("Introduce primer numero: \n"))
num_2 = int(input("Introduce el segundo numero: \n"))
operacion = input("Introduce que operacion hacer: \n").strip()

if operacion == "+" :
    calculo = num_1 + num_2
    print(f"{calculo}")
elif operacion == "-" :
    calculo = num_1 - num_2
    print(f"{calculo}")
elif operacion == "*" :
    calculo = num_1 * num_2
    print(f"{calculo}")
elif operacion == "/" and num_2 == 0 :
    print("No se puede dividir")
elif operacion == "/" :
    calculo = num_1 / num_2
    print(f"{calculo}")
else :
    print("Operacion incorrecta")



# Exercici 3: Any de traspàs
# Demana a l'usuari que introdueixi un any i determina si és de traspàs.
# Un any és de traspàs si és divisible per 4, excepte si és divisible per 100
# però no per 400.

year = int(input("Introduce el year: \n"))

if year % 4 != 0 :
    print ("No es bisiesto")
elif year % 100 == 0 :
    if year % 400 != 0 :
        print ("No es bisiesto")
    else :    
        print ("Es bisiesto")
else :
    print ("Es bisiesto")


# Exercici 4: Classificar edats
# Demana a l'usuari que introdueixi una edat i classifica-la en:
# - Nadó (0-2 anys)
# - Infant (3-12 anys)
# - Adolescent (13-17 anys)
# - Adult (18-64 anys)
# - Persona gran (65 anys o més)

edad = int(input("Introduce tu edad: \n"))
if edad >= 65 :
    print("Persona mayor")
elif 64 >= edad >= 18 :
    print("Adulto")
elif 17 >= edad >= 13 :
    print("Adolescente")
elif 12 >= edad >= 3 :
    print ("Menor")
elif 2 >= edad >= 0 :
    print("Baby")

# Exercici 5: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble


# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = float(input("Introduce la latencia en milisegundos: \n"))
paquetes_perdidos = float(input("Introduce porcentaje de paquetes perdidos: \n"))
if latencia < 0 or paquetes_perdidos < 0 or 100 < paquetes_perdidos :
    print("Parametros fuera del valor")
else :
    if latencia <= 30 and paquetes_perdidos <= 1 :
        print("Conexion excelente")
    elif latencia <= 80 and paquetes_perdidos <= 3 :
        print("Conexion buena")
    elif latencia <= 150 and paquetes_perdidos <= 5 :
        print("Conexion aceptable")
    else : 
        print("Conexion deficiente")

# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.

# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
