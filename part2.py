class Employé:
    # On crée des variables de classe
    nombre_employés = 0
    pourcentage = 1.05

    def __init__(self, prenom, nom, salaire):
        self.prenom = prenom
        self.nom = nom
        self.salaire = salaire
        self.email = prenom + '.' + nom + "@hotmail.com"

        # On incrémente de +1 à chaque employé crée !
        Employé.nombre_employés += 1

    def nom_complet(self):
        return '{} {}'.format(self.prenom, self.nom)

    def augmentation(self):
        # 1 On crée la fonction
        # 2 on accède à la variable de classe avec self
        self.salaire = int(self.salaire * self.pourcentage)

Eric = Employé("Eric", 'PETULLA', 700000)

Thomas = Employé("Thomas", "ESTIVAl", 55000)

# On veut accéder à la variable de classe pourcentage
print("\nOn veut accéder à la variable de classe pourcentage\n")
print(Employé.pourcentage)

# On veut modifier la variable de classe pourcentage
print("\nOn veut modifier la variable de classe pourcentage\n")
Employé.pourcentage = 1.06
print(Employé.pourcentage)

# On veut modifier le pourcentage pour un Employé : Thomas !
print("\nOn veut modifier le pourcentage pour un Employé : Thomas !\n")
Thomas.pourcentage = 1.4
print("Thomas à : ", Thomas.pourcentage)
print("\nEric à : ", Eric.pourcentage)

# On veut créer un dictionnaire des attributs de Thomas
print("\nOn veut créer un dictionnaire des attributs de Thomas\n")
dico = Thomas.__dict__
print(dico)

# On imprime le salaire sans augmentation
print("# On imprime le salaire sans augmentation")
print(Thomas.salaire)

# On augmente le salaire ! 
Thomas.augmentation()

# On imprime le salaire avec augmentation
print("On imprime le salaire avec augmentation")
print(Thomas.salaire)

# On imprime le nombre_employés
print("\nNombre d'employés : ")
print(Employé.nombre_employés)