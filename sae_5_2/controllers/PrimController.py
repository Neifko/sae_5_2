from sae_5_2.models.Grid import Grid
from sae_5_2.models.Prim import Prim

class PrimController:

    def __init__(self):
        self.grid = None
        self.prim = None

    def set_grid(self, grid):
        self.grid = grid
        self.prim = Prim(grid)

    def display_prim_in_console(self):
        # Créer une grille de taille 5x5
        hex_grid = Grid(5, 5)
        hex_grid.display_grid()

        # Initialiser le parcours
        prim = Prim(hex_grid)

        # Définir le point de départ et d'arrivée
        start_coords = (0, 2, -2)

        # hex_grid.display_neighbors(*start_coords)
        # hex_grid.display_neighbors(*target_coords)

        # Lancer Prim
        path_to_target, total_path = prim.prim_algorithm(start_coords)

        # Afficher les résultats
        if path_to_target:
            print(f"Un chemin existe entre {start_coords}.")
            print(f"Chemin vers la cible : {path_to_target}")
        else:
            print(f"Aucun chemin trouvé entre {start_coords}.")


        print(f"Chemin total parcouru : {total_path}")

    def execute(self, start_coords):
        best_path, total_weight = self.prim.prim_algorithm(start_coords)
        print(best_path)
        return best_path