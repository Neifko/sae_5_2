from sae_5_2.models.Grid import Grid
from sae_5_2.models.algoBFS import AlgoBFS

class algoBFSController:
  
    def __init__(self):
        self.grid = None
        self.parcours_largeur = None

    def set_grid(self, grid):
        self.grid = grid
        self.parcours_largeur = AlgoBFS(grid)

    def run_bfs(self, start_node, end_node):
        if self.grid is None:
            raise ValueError("Grid is not set.")
        start_node = self.grid.get_node(*start_node)
        end_node = self.grid.get_node(*end_node)
        return self.parcours_largeur.find_path(start_node, end_node)