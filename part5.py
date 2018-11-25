class Employé:

    nombre_employés = 0
    pourcentage = 1.05

    def __init__(self, prenom, nom, salaire):
        self.prenom = prenom
        self.nom = nom
        self.salaire = salaire
        self.email = prenom + '.' + nom + "@hotmail.com"

        Employé.nombre_employés += 1

    def nom_complet(self):
        return '{} {}'.format(self.prenom, self.nom)

    def augmentation(self):
        self.salaire = int(self.salaire * self.pourcentage)

    # Méthode magique affichant une information claire en lieu et place de l'instance de classe et son code
    def __repr__(self):
        return "Employé('{}', '{}', {})".format(self.prenom, self.nom, self.salaire)

    # Méthode magique 2 affichant une information claire en lieu et place de l'instance de classe et son code
    def __str__(self):
        return '{} - {}'.format(self.nom_complet(), self.email)
    # On personnalise une méthode spécial, ici en décidant d'ajouter des salaires
    def __add__(self, other):
        return self.salaire + other.salaire

    def __len__(self):
        return len(self.nom_complet())

Eric = Employé("Eric", 'PETULLA', 700000)

Thomas = Employé("Thomas", "ESTIVAl", 55000)

# Python affiche en priorité la méthode __str__

print(Eric)

print(repr(Eric))

print(str(Eric))

# On utilise la méthode __add__
print(Eric + Thomas)
# On utilise la méthode __len__
print(len(Thomas))