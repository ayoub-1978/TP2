import unittest
from exo1 import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_result(self):
        # résultat attendu pour les 15 premiers nombres
        attendu = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
        self.assertEqual(affiche(15), attendu)

if __name__ == "__main__":
    unittest.main()
