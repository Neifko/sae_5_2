from sae_5_2.models.Grid import Grid
from sae_5_2.models.stableMax import StableMaximumSetSolver

class stableMaxController:
    def __init__(self):
        self.grid = None
        self.max_set = []
        self.current_set =  []

    def set_grid(self, grid):
        self.grid = grid
        self.stableMax = StableMaximumSetSolver(grid)

    def run_stableMax(self):
        if self.grid is None:
            raise ValueError("Grid is not set.")
        return self.stableMax.find_stable_maximum_set()