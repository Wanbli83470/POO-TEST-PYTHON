# On importe unittest
import unittest
# On importe le fichier à tester
import calc
# on crée une classe test avec unittest.TestCase obligatoirement
class TestCalc(unittest.TestCase):

	# TOUS LES TEST DOIVENT COMMENCER PAR "test"
	def test_add(self):
		result = calc.add(10, 5)
		self.assertEqual(result, 15)
		# syntaxe 2 sans variable !
		self.assertEqual(calc.add(10,2), 12)
		self.assertEqual(calc.add(10,7), 17)
		self.assertEqual(calc.add(10,9), 19)

	def test_soustra(self):
		result = calc.soustra(10, 6)
		self.assertEqual(result, 4)

	def test_multiply(self):
		result = calc.multiply(10, 6)
		self.assertEqual(result, 60)

	def test_division(self):
		result = calc.division(5, 2)
		self.assertEqual(result, 2.5)

		with self.assertRaises(ValueError):
			calc.division(10, 0)


if __name__ == "__main__":
	unittest.main()

"""---------LACEMENT DU TEST SANS MAIN------------"""
"""---python3 -m unittest test_calc.py---"""

"""---------LACEMENT DU TEST AVEC MAIN------------"""
"""---python3 test_calc.py---"""

# 15
# .F. indique une erreur(F) sur 3 tests.