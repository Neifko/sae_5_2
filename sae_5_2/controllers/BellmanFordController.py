from sae_5_2.models.Grid import Grid
from sae_5_2.models.BF import BF


class BellmanFordController:
    """
    Classe BellmanFordController : permet de gérer l'algorithme Bellman-Ford sur l'interface.
    Cette classe permet de définir une grille, d'exécuter l'algorithme de Bellman-Ford pour trouver le chemin le plus court,
    et de récupérer les résultats du parcours.
    """

    def __init__(self):
        """
        Initialise le contrôleur avec une grille non définie et un objet Bellman-Ford non initialisé.
        """
        self.grid = None
        self.bellman_ford = None

    def set_grid(self, grid: Grid):
        """
        Définit la grille à utiliser pour l'algorithme de Bellman-Ford.
        """
        self.grid = grid
        self.bellman_ford = BF(grid)

    def execute(self, start_coords, target_coords):
        """
        Exécute l'algorithme de Bellman-Ford pour trouver le chemin le plus court entre deux points dans la grille.

        Args:
            start_coords (tuple): Coordonnées (x, y, z) du nœud de départ.
            target_coords (tuple): Coordonnées (x, y, z) du nœud d'arrivée.

        Returns:
            tuple: 
                - path_to_target (list): Liste des nœuds qui donne le chemin le plus court obtenu par l'algorithme,
                  ou une liste vide si aucun chemin n'existe.
                - total_path (list): Liste des nœuds visités pendant le parcours.
        """
        path_to_target, total_path = self.bellman_ford.parcours(start_coords, target_coords)
        return path_to_target, total_path
