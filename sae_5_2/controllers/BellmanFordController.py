from sae_5_2.models.Grid import Grid
from sae_5_2.models.BF import BF


class BellmanFordController:
    """
    Classe BellmanFordController : permet de gérer l'algorithme Bellman-Ford sur l'interface.
    """
    def __init__(self):
        self.grid = None
        self.bellman_ford = None

    def set_grid(self, grid:Grid):
        self.grid = grid
        self.bellman_ford = BF(grid)
    
    def execute(self, start_coords, target_coords):
        path_to_target, total_path = self.bellman_ford.parcours(start_coords, target_coords)
        return path_to_target, path_to_target