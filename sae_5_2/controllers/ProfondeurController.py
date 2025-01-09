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
        start_coords = (0, 0, 0)
        target_coords = (2,1,-3)

        # hex_grid.display_neighbors(*start_coords)
        # hex_grid.display_neighbors(*target_coords)

        # Lancer DFS récursif
        path = parcours_profondeur.parcours(start_coords, target_coords)

        # Afficher les résultats
        if path:
            print(f"Un chemin existe entre {start_coords} et {target_coords}.")
            # print(f"Distance totale : {distance}")
            print(f"Chemin trouvé : {path}")
        else:
            print(f"Aucun chemin trouvé entre {start_coords} et {target_coords}.")

    def execute(self, start_coords, target_coords):
        path = self.parcours_profondeur.parcours(start_coords, target_coords)
        return path