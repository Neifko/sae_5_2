class AlgoBFS:
    """
    Implémente l'algorithme de parcours en largeur (BFS) pour trouver un chemin entre deux nœuds dans une grille hexagonale.
    
    Attributs:
        grid (Grid): La grille hexagonale dans laquelle le parcours est effectué.

    Méthodes:
        __init__(grid): Initialise l'instance avec une grille donnée.
        find_path(start, goal): Trouve un chemin entre le nœud de départ et le nœud d'arrivée.
        _reconstruct_path(visited, start, goal): Reconstruit le chemin à partir des informations de provenance.
    """

    def __init__(self, grid):
        """
        Initialise l'algorithme BFS avec une grille hexagonale.

        Args:
            grid (Grid): Instance de la classe Grid représentant la grille hexagonale.
        """
        self.grid = grid  # Associe la grille fournie à l'algorithme.

    def find_path(self, start, goal):
        """
        Trouve un chemin entre deux nœuds en utilisant l'algorithme BFS.

        Args:
            start (Node): Le nœud de départ.
            goal (Node): Le nœud d'arrivée.

        Returns:
            list[Node]: Liste des nœuds formant le chemin du départ à l'arrivée, ou une liste vide si aucun chemin n'existe.
        """
        # Si le départ et l'arrivée sont les mêmes, retourne immédiatement le nœud de départ.
        if start == goal:
            return [start]

        # Initialise la file d'attente BFS avec le nœud de départ.
        queue = [start]
        # Dictionnaire pour stocker le parent de chaque nœud visité.
        visited = {start: None}

        # Boucle principale du BFS.
        while queue:
            current = queue.pop(0)  # Récupère le nœud actuel en début de file.

            # Si on atteint le nœud d'arrivée, reconstruit et retourne le chemin.
            if current == goal:
                return self._reconstruct_path(visited, start, goal)

            # Parcourt les voisins du nœud actuel.
            for direction, neighbor in current.voisins.items():
                # Si le voisin n'a pas encore été visité, on l'ajoute à la file et on marque son origine.
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = current

        # Si aucun chemin n'a été trouvé, retourne une liste vide.
        return []

    def _reconstruct_path(self, visited, start, goal):
        """
        Reconstruit le chemin en remontant depuis le nœud d'arrivée jusqu'au nœud de départ.

        Args:
            visited (dict): Dictionnaire contenant les informations de provenance des nœuds.
            start (Node): Le nœud de départ.
            goal (Node): Le nœud d'arrivée.

        Returns:
            list[Node]: Liste des nœuds formant le chemin du départ à l'arrivée.
        """
        current = goal  # Commence à partir du nœud d'arrivée.
        path = []  # Initialise la liste pour stocker le chemin.

        # Remonte les nœuds jusqu'à atteindre le départ.
        while current != start:
            path.append(current)
            current = visited[current]

        # Ajoute le nœud de départ au chemin.
        path.append(start)
        # Inverse la liste pour obtenir le chemin dans l'ordre correct.
        path.reverse()
        return path

import unittest
import Grid

class TestBFS(unittest.TestCase):
    def test_bfs(self):
        """
        Fonction de test pour l'algorithme BFS sur une grille hexagonale.
        Teste différents scénarios pour vérifier la validité de l'implémentation.
        """
        print("=== Test de l'algorithme BFS ===")
        
        # Création d'une grille hexagonale 5x5
        grid = Grid.Grid(3, 3)  # Initialise une grille hexagonale de 5 lignes et 5 colonnes.
        bfs = AlgoBFS(grid)  # Crée une instance de l'algorithme BFS avec cette grille.

        # Test 1 : Chemin simple entre deux nœuds
        start = grid.get_node(0, 2, -2)  # Nœud de départ
        goal = grid.get_node(2, 0, -2)  # Nœud d'arrivée
        path = bfs.find_path(start, goal)  # Recherche le chemin
        print("\nTest 1: Chemin simple")
        print("Chemin trouvé :", path)
        self.assertIsNotNone(path, "Le chemin ne doit pas être None")
        self.assertGreater(len(path), 0, "Le chemin doit contenir au moins un nœud")

        # # Test 2 : Départ et arrivée sont le même nœud
        # start = grid.get_node(1, 1, -2)  # Nœud de départ et d'arrivée
        # goal = grid.get_node(1, 1, -2)
        # path = bfs.find_path(start, goal)  # Recherche le chemin
        # print("\nTest 2: Départ et arrivée identiques")
        # print("Chemin trouvé :", path)
        # self.assertEqual(path, [start], "Le chemin doit contenir uniquement le nœud de départ")

        # # Test 3 : Aucun chemin possible
        # # Supposons que certains nœuds sont déconnectés ou inexistants
        # start = grid.get_node(0, 0, 0)  # Nœud de départ
        # goal = grid.get_node(5, 5, -10)  # Nœud d'arrivée inexistant
        # path = bfs.find_path(start, goal)  # Recherche le chemin
        # print("\nTest 3: Aucun chemin possible")
        # print("Chemin trouvé :", path)
        # self.assertIsNone(path, "Le chemin doit être None si aucun chemin n'est possible")

        # # Test 4 : Plus grand chemin dans une grille dense
        # start = grid.get_node(0, 0, 0)  # Nœud de départ
        # goal = grid.get_node(4, 0, -4)  # Nœud d'arrivée à l'autre extrémité de la grille
        # path = bfs.find_path(start, goal)  # Recherche le chemin
        # print("\nTest 4: Plus grand chemin")
        # print("Chemin trouvé :", path)
        # self.assertIsNotNone(path, "Le chemin ne doit pas être None")
        # self.assertGreater(len(path), 0, "Le chemin doit contenir au moins un nœud")

if __name__ == '__main__':
    unittest.main()