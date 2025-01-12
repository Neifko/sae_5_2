from sae_5_2.models.Grid import Grid
from sae_5_2.models.AEtoile import AEtoile


class AEtoileController:
    """
    Classe AEtoileController : permet de gérer l'algorithme A* sur l'interface.
    Cette classe permet de définir une grille, d'exécuter l'algorithme A* pour trouver le chemin optimal,
    et de récupérer les résultats du parcours.
    """

    def __init__(self):
        """
        Initialise le contrôleur avec une grille non définie et un objet A* non initialisé.
        """
        self.grid = None
        self.a_etoile = None

    def set_grid(self, grid):
        """
        Définit la grille à utiliser pour l'algorithme A*.
        """
        self.grid = grid
        self.a_etoile = AEtoile(grid)

    def execute(self, start_coords, target_coords):
        """
        Exécute l'algorithme A* pour trouver le chemin optimal entre deux points dans la grille.

        Args:
            start_coords (tuple): Coordonnées (x, y, z) du nœud de départ.
            target_coords (tuple): Coordonnées (x, y, z) du nœud d'arrivée.

        Returns:
            tuple: 
                - path_to_target (list): Liste des nœuds représentant le chemin obtenu par l'algorithme,	
                  ou une liste vide si aucun chemin n'existe.
                - total_path (list): Liste des nœuds visités pendant le parcours.
        """
        path_to_target, total_path = self.a_etoile.parcours(start_coords, target_coords)
        return path_to_target, total_path
