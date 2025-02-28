# #  Exercice 2 : Trouver le Plus Grand Nombre (Boucles & Conditions) 
# Énoncé : 
# Demandez à l'utilisateur d'entrer 5 nombres entiers, puis affichez le plus grand. 

#  SANS BOUCLE
# nombre1 = int(input("Nombre numéro 1 : "))
# print(nombre1)
# nombre2 = int(input("Nombre numéro 2 : "))
# print(nombre2)
# nombre3 = int(input("Nombre numéro 3 : "))
# print(nombre3)
# nombre4 = int(input("Nombre numéro 4 : "))
# print(nombre4)
# nombre5 = int(input("Nombre numéro 5 : "))
# print(nombre5)
# plusgrand = max(nombre1, nombre2, nombre3, nombre4, nombre5)  
# print(f"Le chiffre le plus grand entre tout tes nombres ({nombre1},{nombre2},{nombre3},{nombre4},{nombre5}) est : {plusgrand}")


# # Demander à l'utilisateur de saisir 5 mots et les ajouter à la liste vide
# for mot in range(5):
#     motentre = input(f"Veuillez entrer le mot {mot+1}: ")
#     listevide.append(motentre)


nombres = []
for chiffre in range(5): # il part de 0 ducoup c'est écrit nombre 0
    nombre = int(input(f"Nombre numéro {chiffre} : "))
    nombres.append(nombre)

plusgrand = max(nombres)
print(f"Le chiffre le plus grand entre tous tes nombres {nombres} est : {plusgrand}")
