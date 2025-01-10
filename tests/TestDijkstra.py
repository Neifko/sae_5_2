import unittest

from sae_5_2.models.Dijkstra import Dijkstra
from sae_5_2.models.Grid import Grid


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        # Création d'une grille hexagonale 5x5
        self.grid = Grid(5, 5)
        self.dijkstra = Dijkstra()

    def test_shortest_path_adjacent(self):
        self.grid.get_node(2, -1, -1).valeur = 2
        self.grid.get_node(2, -0, -2).valeur = 2
        self.grid.get_node(1, 1, -2).active = False
        self.grid.get_node(2, -1, -1).active = False
        self.grid.get_node(2, -0, -2).active = False
        self.grid.get_node(0, 2, -2).active = True

        distance, best_chemin, list_all_chemin = self.dijkstra.shortest_path(
            self.grid,
            (0, 0, 0),
            (4, -2, -2)
        )

        self.assertIsNotNone(best_chemin)
        print("\ntest_shortest_path_adjacent: Chemin simple")
        print("Nombre de déplacement :", distance)
        print("Meilleur chemin trouvé :", best_chemin)
        print("Tous les autres chemins possibles :")
        for path in list_all_chemin:
            print(path)


    def test_shortest_path_diagonal(self):
        self.grid.get_node(0, 2, -2).valeur = 3
        self.grid.get_node(1, 1, -2).active = False

        distance, best_chemin, list_all_chemin = self.dijkstra.shortest_path(
            self.grid,
            (0, 0, 0),
            (3, 3, -6)
        )
        print("\ntest_shortest_path_adjacent: Chemin simple")
        print("Nombre de déplacement :", distance)
        print("Meilleur chemin trouvé :", best_chemin)
        print("Tous les autres chemins possibles :")
        for path in list_all_chemin:
            print(path)
        self.assertIsNotNone(best_chemin)

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
