# On déclare la classe employé 
class Employé:
	# on utilise le constructeur def __init__
    def __init__(self, prenom, nom, salaire):
    	self.prenom = prenom
    	self.nom = nom
    	self.salaire = salaire
    	# self.email est le résultat d'autres constructeur,
    	# il n'est donc pas déclaré dans le constructeur
    	self.email = prenom + '.' + nom + "@hotmail.com"

    # On déclare une méthode de classe avec self pour 
    # accéder aux données de l'objet construit
    def nom_complet(self):
    	return '{} {}'.format(self.prenom, self.nom)

Eric = Employé("Eric", 'PETULLA', 700000)

Thomas = Employé("Thomas", "ESTIVAl", 55000)

print(Thomas)
# Ici on obtient le détail de l'instance de classe 
# <__main__.Employé object at 0x7f3d31f88c18>


print(Thomas.email)
# Ici on obtient un détail en précisant 
# l'attribut au quel on veut accéder

print(Thomas.nom_complet())
# Ici on utilise la méthode permettant d'afficher le nom complet

print(Employé.nom_complet(Eric))