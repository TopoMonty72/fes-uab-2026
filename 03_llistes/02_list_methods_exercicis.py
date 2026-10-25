###
# EXERCICIS
# Fes servir, sempre que puguis, els mètodes que has après.
###

# Exercici 1: Afegir i modificar elements
# Crea una llista amb els nombres de l'1 al 5.
# Afegeix-hi el nombre 6 al final fent servir append().
# Insereix-hi el nombre 10 a la posició 2 fent servir insert().
# Modifica el primer element de la llista perquè sigui 0.

lista = [1, 2, 3, 4, 5]

lista.append(6)
lista.insert(2, '10')
lista[0] = '0' 
print(lista)

# Exercici 2: Combinar i buidar llistes
# Crea dues llistes:
# llista_a = [1, 2, 3]
# llista_b = [4, 5, 6, 1, 2]
# Amplia llista_a amb llista_b fent servir extend().
# Elimina la primera aparició del nombre 1 de llista_a fent servir remove().
# Elimina l'element de l'índex 3 de llista_a fent servir pop(). Imprimeix l'element eliminat.
# Buida completament llista_b fent servir clear().

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

lista_a.extend(lista_b)
lista_a.remove(1)
removed = lista_a.pop(3)
lista_a.pop(3)
print(removed)
lista_b.clear()
print (lista_a, lista_b)


# Exercici 3: Slicing i eliminació amb del
# Crea una llista amb els nombres de l'1 al 10.
# Fes servir slicing i del per eliminar els elements des de l'índex 2 fins al 5
# (sense incloure el 5).
# Imprimeix la llista resultant.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[2:5]
print(lista)

# Exercici 4: Ordenar i comptar
# Crea una llista amb els nombres següents: [5, 2, 8, 1, 9, 4, 2].
# Ordena la llista de manera ascendent fent servir sort().
# Compta quantes vegades apareix el nombre 2 a la llista fent servir count().
# Comprova si el nombre 7 és a la llista fent servir in.

lista = [5, 2, 8, 1, 9, 4, 2]
lista.sort()
print(lista.count(2))
print(7 in lista)
print(lista)


# Exercici 5: Còpia i referència
# Crea una llista anomenada original amb els nombres [1, 2, 3].
# Crea'n una còpia anomenada copia_1 fent servir slicing.
# Crea'n una altra còpia anomenada copia_2 fent servir copy().
# Crea una referència a la llista original anomenada referencia.
# Modifica a 10 el primer element de la llista referencia.
# Imprimeix les quatre llistes (original, copia_1, copia_2 i referencia) i observa'n els canvis.

original = [1, 2, 3]
copia_1 = original[0:3]
copia_2 = original.copy()
referencia = original
referencia [0] = 10
print(original, copia_1, copia_2, referencia)


# Exercici 6: Ordenar cadenes sense distingir entre majúscules i minúscules
# Crea una llista amb les cadenes següents: ["Poma", "pera", "PLÀTAN", "taronja"].
# Ordena la llista sense distingir entre majúscules i minúscules.

cadena = ["Poma", "pera", "PLÀTAN", "taronja"]
cadena_ordenada = cadena.sort(key=str.lower)
print(cadena_ordenada)