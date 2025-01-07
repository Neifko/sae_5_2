import unittest

from sae_5_2.models.Dijkstra import Dijkstra
from sae_5_2.models.Grid import Grid


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        # Création d'une grille hexagonale 5x5
        self.grid = Grid(5, 5)
        self.dijkstra = Dijkstra()

    def test_shortest_path_adjacent(self):
        distance, path = self.dijkstra.shortest_path(
            self.grid,
            (0, 0, 0),
            (1, -1, 0)
        )
        print("\ntest_shortest_path_adjacent: Chemin simple")
        print("Nombre de déplacement :", distance)
        print("Chemin trouvé :", path)
        self.assertEqual(distance, 1)
        self.assertEqual(len(path), 2)

    def test_shortest_path_diagonal(self):
        distance, path = self.dijkstra.shortest_path(
            self.grid,
            (0, 0, 0),
            (2, -1, -1)
        )
        print("\ntest_shortest_path_diagonal: Chemin diagonal")
        print("Nombre de déplacement :", distance)
        print("Chemin trouvé :", path)
        self.assertEqual(distance, 2)
        self.assertEqual(len(path), 3)

    def test_invalid_coordinates(self):
        with self.assertRaises(ValueError, msg="Le chemin n'est pas possible si la case est inexistante"):
            self.dijkstra.shortest_path(
                self.grid,
                (10, 10, -20),
                (0, 0, 0)
            )
        print("\ntest_invalid_coordinates: Aucun chemin possible")


    def test_path_to_self(self):
        distance, path = self.dijkstra.shortest_path(
            self.grid,
            (0, 0, 0),
            (0, 0, 0)
        )
        print("\ntest_path_to_self: Départ et arrivée identiques")
        print("Nombre de déplacement :", distance)
        print("Chemin trouvé :", path)
        self.assertEqual(distance, 0)
        self.assertEqual(len(path), 1)

if __name__ == '__main__':
    unittest.main()
