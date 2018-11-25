import unittest
# On importe les mocks
from unittest.mock import patch
# On importe request
import request
# depuis le fichier employée on appelle la classe Employée en tant que Salarié
from employée import Employée as Salarié

class TestEmployée(unittest.TestCase):

	# On crée nos instances de classes avant les tests pour "factoriser" le code
	def setUp(self):
		print("setUp")
		self.emp1 = Salarié("Thomas", "ESTIVAL", 50000)
		self.emp2 = Salarié("Eric", "Petulla", 100000)

	def tearDown(self):
		pass

	def test_mail(self):
		print("test_mail")
		self.assertEqual(self.emp1.email, 'Thomas.ESTIVAL@email.com')
		self.assertEqual(self.emp2.email, 'Eric.Petulla@email.com')

	def test_fullname(self):
		print("test_mail")
		self.assertEqual(self.emp1.fullname, 'Thomas ESTIVAL')
	def test_augmentation(self):
		print("test_augmentation")
		self.emp2.apply_raise()
		self.assertEqual(self.emp2.pay, 105000)

	def test_maps(self):
		with patch('Salarié.request.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = "Success"
	# Introduction aux Mocks


if __name__ == "__main__":
	unittest.main()