import unittest
from app import FunkcjaKwadratowa


class TestFunkcjaKwadratowa(unittest.TestCase):

    def test_zero_rozwiazan(self):
        funkcja = FunkcjaKwadratowa(0, 0, 1)
        self.assertEqual(funkcja.rozwiaz(), "Zero rozwiązań")

    def test_liczba_nieskonczona(self):
        funkcja = FunkcjaKwadratowa(0, 0, 0)
        self.assertEqual(funkcja.rozwiaz(), "Liczba nieskończona")

    def test_funkcja_liniowa(self):
        funkcja = FunkcjaKwadratowa(0, 2, -4)
        self.assertEqual(funkcja.rozwiaz(), "Delta = 0 Funkcja liniowa, jedno miejsce zerowe x = 2.0")

    def test_dwa_miejsca_zerowe(self):
        funkcja = FunkcjaKwadratowa(1, -3, 2)
        result = funkcja.rozwiaz()
        self.assertIn("Delta > 0 , dwa miejsca zerowe. x1 =", result)
        self.assertIn("x2=", result)

    def test_brak_miejsc_zerowych(self):
        funkcja = FunkcjaKwadratowa(1, 0, 1)
        self.assertEqual(funkcja.rozwiaz(), "Delta < 0, brak miejsc zerowych")


if __name__ == '__main__':
    unittest.main()
