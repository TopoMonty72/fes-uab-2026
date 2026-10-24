###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nombre_encaminador = input("Nombre encaminador: \n")
ubicacion = input("Ubicacion: \n")
nombre_puerto = input("Nombre puerto: \n")
estado = bool(input("Encenido (1) o apagado (0) \n"))
if estado == 1 :
    estado_enseñar = "Encendido"
else :
    estado_enseñar = "Apagado"
print(f"{nombre_encaminador}, {ubicacion}, {nombre_puerto}, {estado_enseñar}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.

GB_plan = int(input("GB incluidos en el plan: \n"))
GB_consumido = int(input("GB usados: \n"))
GB_total = GB_plan - GB_consumido
print(f"Quedan {GB_total} GB libres \n")

GB_consumido = int(input("GB usados: \n"))
GB_total = GB_plan - GB_consumido
print(f"Quedan {GB_total} GB libres \n")
