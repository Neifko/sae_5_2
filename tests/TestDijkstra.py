import unittest

from sae_5_2.models.Dijkstra import Dijkstra
from sae_5_2.models.Grid import Grid


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        # Création d'une grille hexagonale 5x5
        self.grid = Grid(5, 5)
        self.dijkstra = Dijkstra(self.grid)

    def test_shortest_path_adjacent(self):
        self.grid.get_node(2, -1, -1).valeur = 5
        self.grid.get_node(2, -0, -2).active = False

        best_chemin = self.dijkstra.shortest_path((4, -2, -2),
            (0, 0, 0))

        self.assertIsNotNone(best_chemin, "La cible n'est pas atteignable")
        print("\ntest_shortest_path_adjacent: Chemin horizontal")
        print("Meilleur chemin trouvé :", best_chemin)


    def test_shortest_path_diagonal(self):
        self.grid.get_node(0, 2, -2).valeur = 3
        self.grid.get_node(1, 1, -2).active = False

        best_chemin = self.dijkstra.shortest_path((0, 0, 0), (3, 3, -6))
        self.assertIsNotNone(best_chemin)
        print("\ntest_shortest_path_adjacent: Chemin diagonal")
        print("Meilleur chemin trouvé :", best_chemin)


    # def test_invalid_coordinates(self):
    #     with self.assertRaises(ValueError, msg="Le chemin n'est pas possible si la case est inexistante"):
    #         self.dijkstra.shortest_path(
    #             self.grid,
    #             (10, 10, -20),
    #             (0, 0, 0)
    #         )
    #     print("\ntest_invalid_coordinates: Aucun chemin possible")

if __name__ == '__main__':
    unittest.main()