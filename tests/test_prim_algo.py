import unittest
from sae_5_2.models.Grid import Grid
from sae_5_2.models.Prim import prim_algorithm


class TestPrimAlgorithm(unittest.TestCase):

    def setUp(self):
        """
        Configuration initiale avant chaque test.
        Création d'une grille hexagonale pour les tests.
        """
        self.grid = Grid(4, 4)  # Grille de 4x4
        self.start_coords = (0,0,0)  # Coordonnées du nœud de départ

        # Modifier les valeurs des nœuds pour les tests
        self.grid.get_node(2, 2, -4).valeur = 2
        self.grid.get_node(0, 1, -1).valeur = 3
        self.grid.get_node(1, 0, -1).valeur = 1
        self.grid.get_node(1, 1, -2).valeur = 5
        self.grid.get_node(0, 2, -2).valeur = 4

    def test_mst_structure(self):
        """
        Teste la structure du MST renvoyé par l'algorithme.
        Vérifie que tous les nœuds sont connectés correctement.
        """
        mst, total_weight = prim_algorithm(self.grid, self.start_coords)

        # Vérifie que le MST contient 3 arêtes pour une grille 4x4
        self.assertEqual(len(mst), len(self.grid.nodes) - 1)

        # Vérifie que chaque arête contient un nœud source, un nœud cible et un poids
        for edge in mst:
            self.assertEqual(len(edge), 3)

    def test_mst_total_weight(self):
        """
        Teste si le poids total est correct pour la configuration actuelle.
        """
        mst, total_weight = prim_algorithm(self.grid, self.start_coords)

        # Poids attendu basé sur les valeurs assignées dans `setUp`
        # Ex. MST = (0, 0, 0) -> (0, 1, -1) -> (1, 1, -2)
        expected_weight = 3+4+1+1+1+5+1+1+1+1+2+1+1+1+1 # Ça fait 25 # Somme des poids des arêtes
        self.assertEqual(total_weight, expected_weight)

    def test_invalid_start_coords(self):
        """
        Teste si une erreur est levée pour des coordonnées invalides.
        """
        invalid_coords = (10, 10, -20)  # Coordonnées qui n’existent pas
        with self.assertRaises(ValueError):
            prim_algorithm(self.grid, invalid_coords)

    def test_chemin_bloque(self):
        """
        Teste si l'algorithme ignore correctement les nœuds inactifs (obstacles).
        """
        self.grid.get_node(0, 2, -2).active = False  # Rendre un nœud inactif
        self.grid.get_node(1, 1, -2).active = False  # Rendre un nœud inactif
        self.grid.get_node(2, 0, -2).active = False  # Rendre un nœud inactif
        self.grid.get_node(0, 1, -1).active = False  # Rendre un nœud inactif
        mst, total_weight = prim_algorithm(self.grid, self.start_coords)

        # Poids attendu, en ignorant le nœud inactif
        expected_weight = 1+1+1+1+1+1+1+1+2+1+1 # Ca fait 12 # chemin (0,0,0) -> (1,0,-1) -> (2,-1,-1) ...
        self.assertEqual(total_weight, expected_weight)
        print(mst)
        print(total_weight)


if __name__ == "__main__":
    unittest.main()
