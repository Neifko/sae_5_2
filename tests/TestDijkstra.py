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
        print("\nTest 1: Chemin simple")
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
        with self.assertRaises(ValueError):
            self.dijkstra.shortest_path(
                self.grid,
                (10, 10, -20),
                (0, 0, 0)
            )
            print("\nTest 3: Aucun chemin possible")


    def test_path_to_self(self):
        distance, path = self.dijkstra.shortest_path(
            self.grid,
            (0, 0, 0),
            (0, 0, 0)
        )
        print("\nTest 2: Départ et arrivée identiques")
        print("Nombre de déplacement :", distance)
        print("Chemin trouvé :", path)
        self.assertEqual(distance, 0)
        self.assertEqual(len(path), 1)

    def test_3(self):
        start = self.grid.get_node(0, 0, 0)
        goal = self.grid.get_node(5, 5, -10)
        path = self.dijkstra.shortest_path(self.grid, *start, *goal)
        print("\nTest 3: Aucun chemin possible")
        print("Chemin trouvé :", path)
        self.assertListEqual(path, [], "Le chemin doit être None si aucun chemin n'est possible")

    def test_4(self):
        start = self.grid.get_node(-2, -2, 4)
        goal = self.grid.get_node(2, 2, -4)
        path = self.dijkstra.shortest_path(self.grid, start, goal)
        print("\nTest 4: Plus grand chemin")
        print("Chemin trouvé :", path)
        self.assertIsNotNone(path, "Le chemin ne doit pas être None")
        self.assertGreater(len(path), 0, "Le chemin doit contenir au moins un nœud")

if __name__ == '__main__':
    unittest.main()
