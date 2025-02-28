# # Exercice 1 : Calcul du Prix avec Remise (Variables & Conditions) 
# Énoncé : 
# Un magasin propose une réduction de 10% si un client dépense plus de 100€. 
# Demandez à l'utilisateur d'entrer le montant total de ses achats et appliquez la 
# remise si nécessaire. 

Achat = (int(input(f"Pour combien venez vous d'acheter ? ")))
if Achat >= 100: # obligé de mettre un int au dessus pour que le >= fonctionne
    print (f"Merci pour vos achat, vous bénéficiez de 10 % équivalent à {Achat * 0.1} € d'économie cela fait donc {Achat - Achat * 0.1} €")
else:
    print (f"Merci pour vos achat, cela fait donc {Achat} €")
