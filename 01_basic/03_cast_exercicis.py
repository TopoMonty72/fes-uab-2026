###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquetes_recibidos = int(input("Paquetes recibido encaminador: \n"))
paquetes_total = paquetes_recibidos + 1200
print(f"El total es {paquetes_total}")

# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocidad_Mbps = int(input("Introduce la velocidad de la conexion en Mbps: \n"))
velocidad_MB = (velocidad_Mbps/8)
print(f"La velocidad en MB es de {velocidad_MB} MB/s")