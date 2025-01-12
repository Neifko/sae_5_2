from sae_5_2.models.Grid import Grid
from sae_5_2.models.algoBFS import AlgoBFS

class algoBFSController:
    """
    Contrôleur pour exécuter l'algorithme de parcours en largeur (BFS) sur une grille.
    Permet de définir une grille, d'initialiser l'algorithme BFS, et de trouver un chemin entre deux nœuds.
    """

    def __init__(self):
        """
        Initialise le contrôleur avec une grille et un algorithme BFS.
        """
        self.grid = None
        self.parcours_largeur = None

    def set_grid(self, grid):
        """
        Définit la grille pour le parcours en largeur.

        Params:
            grid (Grid): Instance de la classe Grid représentant la grille.
        """
        self.grid = grid
        self.parcours_largeur = AlgoBFS(grid)

    def run_bfs(self, start_node, end_node):
        """
        Exécute l'algorithme BFS pour trouver un chemin entre deux nœuds de la grille.

        Params:
            start_node (tuple): Coordonnées (x, y, z) du nœud de départ.
            end_node (tuple): Coordonnées (x, y, z) du nœud d'arrivée.

        Returns:
            list: Une liste de nœuds avec le chemin obtenu par l'algorithme 
            ou une liste vide si aucun chemin n'existe.
        """
        if self.grid is None:
            raise ValueError("Grid is not set.")
        start_node = self.grid.get_node(*start_node)
        end_node = self.grid.get_node(*end_node)
        return self.parcours_largeur.find_path(start_node, end_node)