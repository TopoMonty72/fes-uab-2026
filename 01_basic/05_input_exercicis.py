###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###


# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nombre_tecnico = input("Como se llama el tecnico: \n")
nombre_red = input("Que red esta instalando: \n")
print(f"El tecnico se llama {nombre_tecnico} y esta instalando la red {nombre_red}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.

longitud = input("Longitud enllaç en km: \n")
velocitat = input ("Velocitat trnsmissió: \n")



=======
longitud_enlace = float(input("Longitud del enlace de fibra en kilometros: \n"))
velocidad_tranmision = float(input("Velocidad de transmision en Gbps: \n"))
tiempo = 8 / velocidad_tranmision
print(f"El enlace tardaria {tiempo} en a traves de {longitud_enlace} de cable ")
>>>>>>> bf269f6412313de6e13ec47b2318259f049d0c6e

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

horas_trabajadas = float(input("Horas trabajadas: \n"))
precio_hora = float(input("Precio por hora trabajada: \n"))
precio_material = float(input("Precio del material: \n"))
coste_total = precio_hora * precio_material + precio_material

print(f"El precio total seria de {coste_total} euros")