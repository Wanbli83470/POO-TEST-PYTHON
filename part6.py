class Employé:

    def __init__(self, prenom, nom):
    	self.prenom = prenom
    	self.nom = nom
        
    # La méthode property évite d'avoir à appeller la fonction comme une méthode avec ()
    @property
    def nom_complet(self):
    	return '{} {}'.format(self.prenom, self.nom)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.prenom, self.nom)

emp1 = Employé("John","Smith")

print(emp1.prenom)

# Il est possible de modifier un attribut directement tel une variale

emp1.prenom = "Darky"
# le Prénom est bien changé !
print(emp1.prenom)

print(emp1.nom_complet)