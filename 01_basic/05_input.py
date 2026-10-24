###
# 05 - Entrada de dades de l'usuari (input()) - versió simplificada
# La funció input() permet obtenir dades de l'usuari a través de la consola.
###

# import os
# os.system("cls") #deprecated fer una actualització*

# Per obtenir dades de l'usuari, es fa servir la funció input()
# La funció input() rep un missatge que es mostra a l'usuari
# i retorna el valor que aquest introdueix
# nom = input("Hola, com et dius?\n")
# print(f"Hola {nom}, encantat de conèixer-te")
# print("Hola " + nom + ", encantat de conèixer-te")

=======
# Ten en cuenta que la función input() devuelve un string
# Así que si queremos obtener un número se debe convertir el string a un número
# age = input("¿Cuántos años tienes?\n")
# print(f"Tendrás {int(age)+3} años dentro de 3 años")  # Esto no funcionará como esperamos
# age = int(age)
# print(f"Tienes {age} años")
>>>>>>> a39c14c40149ec147890d42286dae43591ae41d2

# La funció input() també pot retornar diversos valors
# Per fer-ho, l'usuari els ha de separar amb un espai
print("Obtenir diversos valors alhora")
pais, ciutat = input("A quin país i a quina ciutat vius?\n").split()

# print(f"Vius a {ciutat}, {pais}")
print(f"Vius a {ciutat}, {pais}")