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

# On crée une classe héritant de la classe Employé Parent

class Graphiste(Employé):
    # On peut modifier une variable de classe de "Employé"
    pourcentage = 1.2
    # On peut modifier le constructeur sans se répéter
    def __init__(self, prenom, nom, salaire, logiciel):
        # On hérite de la construction avec super()
        super().__init__(prenom, nom, salaire)
        # on s'occupe des langages compétences
        self.logiciel = logiciel

class Commercial(Employé):
    pourcentage = 1.5
    def __init__(self, prenom, nom, salaire, client=None):
        super().__init__(prenom, nom, salaire)
        # On gère conditionnellement un client ajouté ou non !
        if client is None:
            self.client = []
        else :
            self.client = client

class client():
    pass

Eric = Commercial("Eric", 'PETULLA', 700000)
Thomas = Graphiste("Thomas", "ESTIVAl", 55000, ["Illustrator", "Photoshop"])

# On demande à Python si Eric est bien un Commercial ?
print(isinstance(Eric, Commercial))
# retourne True ou False

# ON demande à python si la classe est une sous classe d'une autre ?
print(issubclass(Graphiste, Employé))
# Retourne True
print(issubclass(client, Employé))
# Retourne False