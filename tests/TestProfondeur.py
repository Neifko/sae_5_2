import unittest

from sae_5_2.controllers.ProfondeurController import ProfondeurController


class TestProfondeur(unittest.TestCase):
    def test_profondeur(self):
        profcont = ProfondeurController()
        profcont.display_profondeur_in_console()

if __name__ == '__main__':
    unittest.main()