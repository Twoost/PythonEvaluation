# Exercice 3 : Vérification de Mot de Passe (Fonctions & Conditions) 
# Énoncé : 
# Créez une fonction `verifier_mot_de_passe(mot_de_passe)` qui vérifie si un mot de 
# passe contient au moins 8 caractères et un chiffre. 

# def verifier_mot_de_passe(mot_de_passe):
#     if len(mdp) < 8:
#         return False
#     chiffre = False
#     for lettre in mdp:
#         if lettre in [1,2,3,4,5,6,7,8,9]:
#             chiffre = True
#     return chiffre
# mdp = input("Entrez votre mot de passe : ")
# if verifier_mot_de_passe(mdp):
#     print("mdp valide")
# else:
#     print("Au moins 8 caractères & 1 chiffre")

def verifier_mot_de_passe(mot_de_passe):
    if len(MotdePasse) < 8:
        return False
    chiffre = False
    for lettre in MotdePasse:
        if lettre.isdigit():
            chiffre = True
            break
    return chiffre

MotdePasse = input("Entrez votre mot de passe : ")
if verifier_mot_de_passe(MotdePasse):
    print("Mot de passe valide")
else:
    print("Le mot de passe doit avoir au  minimum 8 caractères et 1 chiffre")