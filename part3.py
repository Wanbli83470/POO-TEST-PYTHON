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

    # On crée une méthode statique modifiant la variable pourcentage
    @classmethod
    # on utilise cls en guise de self comme convetion de nommage
    def plus_pourcentage(cls, valeur):
        cls.pourcentage = valeur

    # Création d'un constructeur alternatif...
    @classmethod
    def convert_string(cls, emp_string):
        prenom, nom, salaire = emp_string.split("-")
        return cls(prenom, nom, salaire)

    # La méthode statique n'a pas besoin de cls

    @staticmethod
    def jour_travail(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


Eric = Employé("Eric", 'PETULLA', 700000)
Thomas = Employé("Thomas", "ESTIVAl", 55000)

# on appel sans la méthode de classe
print("on imprime sans la méthode de classe")
print(Employé.pourcentage)

# On augmente le pourcentage avec la méthode de classe
print("On augmente le pourcentage avec la méthode de classe\n----------")
Employé.plus_pourcentage(1.07)

# on appel avec la méthode de classe
print("on imprime avec la méthode de classe")
print(Employé.pourcentage)

emp_string_1 = Employé.convert_string("Cédric-Haoucine-70000")
print(emp_string_1.salaire)

import datetime
ma_date = datetime.date(2018, 11, 24)

print(Employé.jour_travail(ma_date))