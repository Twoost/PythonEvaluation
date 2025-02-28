# Énoncé : 
# Créez une classe `Livre` et une classe `LivreEmpruntable` qui hérite de `Livre`. 
# Ajoutez des méthodes pour emprunter et retourner un livre. 

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def afficher_info(self):
        print(f"LIVRE D'EXPOSITION / Ne pas prendre \ Titre: {self.titre}, Auteur: {self.auteur}")

class LivreEmpruntable(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur)
        self.emprunte = False

    def emprunter(self):
        if not self.emprunte:
            self.emprunte = True
            print(f"Tu viens de prendre Le livre {self.titre}.")
        else:
            print(f"Le livre {self.titre}  à déja été emprunté.")

    def retourner(self):
        if self.emprunte:
            self.emprunte = False
            print(f"Tu viens de retourner le livre {self.titre}")
        else:
            print(f"Le livre {self.titre} à toujours été la, tu es fou ??!")


#  Ca affiche un livre d'exposition il n'est pas empruntable 
LivreToutCourt = Livre("Petit-Chaperons-Rouge","GorgeleRouge")
LivreToutCourt.afficher_info()


Livre1 = LivreEmpruntable("Le Madalade Imaginaire", "Rimbaud")
Livre1.afficher_info()
#  Il prend le livre la
Livre1.emprunter()
#  Il n'est pas cénsé pouvoir le reprendre puisque il est déja pris
Livre1.emprunter()
#  Il redonne le livre
Livre1.retourner()
# Il ne peut pas redonner un livre qui été déja la 
Livre1.retourner()
