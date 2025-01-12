from sae_5_2.models.Grid import Grid
from sae_5_2.models.Dijkstra import Dijkstra

class DijkstraController:
    """
    Contrôleur pour exécuter et afficher l'algorithme de Dijkstra sur une grille.
    Permet de définir une grille, de trouver le chemin le plus court entre deux points, et de visualiser les résultats.
    """

    def __init__(self):
        """
        Initialise le contrôleur avec une grille et un objet Dijkstra non définis.
        """
        self.grid = None
        self.dijkstra = None

    def set_grid(self, grid):
        """
        Définit la grille à utiliser pour l'algorithme de Dijkstra.

        Args:
            grid (Grid): Instance de la classe Grid représentant la grille.
        """
        self.grid = grid
        self.dijkstra = Dijkstra(grid)

    def display_dijkstra_in_console(self):
        """
        Affiche dans la console un exemple d'exécution de l'algorithme de Dijkstra sur une grille.
        Fonction de tests
        """
        # Créer une grille de taille 5x5
        hex_grid = Grid(5, 5)
        hex_grid.display_grid()

        # Initialiser le parcours
        dijkstra = Dijkstra(hex_grid)

        # Définir le point de départ et d'arrivée
        start_coords = (0, 2, -2)
        target_coords = (2, -1, -1)

        # Lancer Dijkstra
        path_to_target, total_path = dijkstra.shortest_path(start_coords, target_coords)

        # Afficher les résultats
        if path_to_target:
            print(f"Un chemin existe entre {start_coords} et {target_coords}.")
            print(f"Chemin vers la cible : {path_to_target}")
        else:
            print(f"Aucun chemin trouvé entre {start_coords} et {target_coords}.")

        print(f"Chemin total parcouru : {total_path}")

    def execute(self, start_coords, target_coords):
        """
        Exécute l'algorithme de Dijkstra pour trouver le chemin le plus court entre deux points de la grille.

        Args:
            start_coords (tuple): Coordonnées (x, y, z) du nœud de départ.
            target_coords (tuple): Coordonnées (x, y, z) du nœud d'arrivée.

        Returns:
            tuple: 
                - best_path (list): Liste des nœuds qui donne le chemin obtenu par l'algorithme,
                  ou une liste vide si aucun chemin n'existe.
                - all_path (list): Liste des nœuds visités pendant le parcours.
        """
        best_path, all_path = self.dijkstra.shortest_path(start_coords, target_coords)
        return best_path, all_path
