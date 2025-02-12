from sae_5_2.models.Grid import Grid
from sae_5_2.models.ParcoursProfondeur import ParcoursProfondeur


class ProfondeurController:
  
    def __init__(self):
        self.grid = None
        self.parcours_profondeur = None

    def set_grid(self, grid):
        self.grid = grid
        self.parcours_profondeur = ParcoursProfondeur(grid)

    def display_profondeur_in_console(self):
        # Créer une grille de taille 5x5
        hex_grid = Grid(3, 3)
        hex_grid.display_grid()

        # Initialiser le parcours en profondeur récursif (DFS)
        parcours_profondeur = ParcoursProfondeur(hex_grid)

        # Définir le point de départ et d'arrivée
        start_coords = (0, 2, -2)
        target_coords = (2,-1,-1)

        # hex_grid.display_neighbors(*start_coords)
        # hex_grid.display_neighbors(*target_coords)

        # Lancer DFS
        path_to_target, total_path = parcours_profondeur.parcours(start_coords, target_coords)

        # Afficher les résultats
        if path_to_target:
            print(f"Un chemin existe entre {start_coords} et {target_coords}.")
            print(f"Chemin vers la cible : {path_to_target}")
        else:
            print(f"Aucun chemin trouvé entre {start_coords} et {target_coords}.")


        print(f"Chemin total parcouru : {total_path}")

    def execute(self, start_coords, target_coords):
        path_to_target, total_path = self.parcours_profondeur.parcours(start_coords, target_coords)
        return path_to_target, total_path

