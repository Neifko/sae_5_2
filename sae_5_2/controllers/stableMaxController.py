from sae_5_2.models.Grid import Grid
from sae_5_2.models.stableMax import StableMaximumSetSolver

class stableMaxController:
    """
    Contrôleur pour trouver un ensemble stable maximum dans une grille.
    Permet de définir une grille, de résoudre le problème d'ensemble stable maximum et de récupérer les résultats.
    """

    def __init__(self):
        """
        Initialise le contrôleur avec une grille non définie et des ensembles (actuel et maximum) vides.
        """
        self.grid = None
        self.max_set = []  # Contiendra l'ensemble stable maximum trouvé.
        self.current_set = []  # Peut être utilisé pour gérer un ensemble stable temporaire.

    def set_grid(self, grid):
        """
        Définit la grille à utiliser pour la résolution du problème d'ensemble stable maximum.
        """
        self.grid = grid
        self.stableMax = StableMaximumSetSolver(grid)

    def run_stableMax(self):
        """
        Exécute l'algorithme pour trouver un ensemble stable maximum dans la grille.

        Returns:
            set: L'ensemble stable maximum trouvé par l'algorithme.
        """
        if self.grid is None:
            raise ValueError("Grid is not set.")
        solver = StableMaximumSetSolver(self.grid)
        return solver.find_stableMax()