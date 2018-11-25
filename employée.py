import request

class Employée:

	pourcentage = 1.05

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)
	
	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.pourcentage)

	# Introduction aux Mocks

	def maps(self):
		response = request.get("https://maps.googleapis.com/maps/api/geocode/json?address=adresse+openclassrooms&key=AIzaSyALFscZvQOVMBXm_0hwRR5EQcqaZLuTpE0")
		if response.ok:
			return response.txt
		else:
			return 'Bad Response'

emp1 = Employée("Thomas", "ESTIVAL", 50000)
print(emp1.email)

emp2 = Employée("Eric", "Petulla", 100000)
emp2.apply_raise()
print(emp2.pay)