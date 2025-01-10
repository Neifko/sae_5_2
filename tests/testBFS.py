import unittest
from sae_5_2.models.Grid import Grid
from sae_5_2.models.algoBFS import AlgoBFS

class TestBFS(unittest.TestCase):
    def test_bfs(self):
        """
        Fonction de test pour l'algorithme BFS sur une grille hexagonale.
        Teste différents scénarios pour vérifier la validité de l'implémentation.
        """
        print("=== Test de l'algorithme BFS ===")
        
        # Création d'une grille hexagonale 5x5
        grid = Grid(5, 5)  # Initialise une grille hexagonale de 5 lignes et 5 colonnes.
        bfs = AlgoBFS(grid)  # Crée une instance de l'algorithme BFS avec cette grille.

        # Test 1 : Chemin simple entre deux nœuds
        start = grid.get_node(0, 0, 0)  # Nœud de départ
        goal = grid.get_node(2, 2, -4)  # Nœud d'arrivée
        path = bfs.find_path(start, goal)  # Recherche le chemin
        print("\nTest 1: Chemin simple")
        print("Chemin trouvé :", path)
        self.assertIsNotNone(path, "Le chemin ne doit pas être None")
        self.assertGreater(len(path), 0, "Le chemin doit contenir au moins un nœud")

        # Test 2 : Départ et arrivée sont le même nœud
        start = grid.get_node(1, 1, -2)  # Nœud de départ et d'arrivée
        goal = grid.get_node(1, 1, -2)
        path = bfs.find_path(start, goal)  # Recherche le chemin
        print("\nTest 2: Départ et arrivée identiques")
        print("Chemin trouvé :", path)
        self.assertEqual(path, [start], "Le chemin doit contenir uniquement le nœud de départ")

        # Test 3 : Aucun chemin possible
        # Supposons que certains nœuds sont déconnectés ou inexistants
        start = grid.get_node(0, 0, 0)  # Nœud de départ
        goal = grid.get_node(5, 5, -10)  # Nœud d'arrivée inexistant
        path = bfs.find_path(start, goal)  # Recherche le chemin
        print("\nTest 3: Aucun chemin possible")
        print("Chemin trouvé :", path)
        self.assertIsNone(path, "Le chemin doit être None si aucun chemin n'est possible")

        # Test 4 : Plus grand chemin dans une grille dense
        start = grid.get_node(0, 0, 0)  # Nœud de départ
        goal = grid.get_node(4, 0, -4)  # Nœud d'arrivée à l'autre extrémité de la grille
        path = bfs.find_path(start, goal)  # Recherche le chemin
        print("\nTest 4: Plus grand chemin")
        print("Chemin trouvé :", path)
        self.assertIsNotNone(path, "Le chemin ne doit pas être None")
        self.assertGreater(len(path), 0, "Le chemin doit contenir au moins un nœud")

if __name__ == '__main__':
    unittest.main()