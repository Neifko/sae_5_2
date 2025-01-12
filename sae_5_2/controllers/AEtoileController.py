from sae_5_2.models.Grid import Grid
from sae_5_2.models.AEtoile import AEtoile


class AEtoileController:
    """
    Classe AEtoileController : permet de gérer l'algorithme A* sur l'interface.
    """
    def __init__(self):
        self.grid = None
        self.a_etoile = None

    def set_grid(self, grid):
        self.grid = grid
        self.a_etoile = AEtoile(grid)
    
    def execute(self, start_coords, target_coords):
        path_to_target, total_path = self.a_etoile.parcours(start_coords, target_coords)
        return path_to_target, total_path