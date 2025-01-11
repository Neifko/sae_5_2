from sae_5_2.models.Grid import Grid
from sae_5_2.models.Dijkstra import Dijkstra

class DijkstraController:

    def __init__(self):
        self.grid = None
        self.dijkstra = None

    def set_grid(self, grid):
        self.grid = grid
        self.dijkstra = Dijkstra(grid)

    def display_dijkstra_in_console(self):
        # Créer une grille de taille 5x5
        hex_grid = Grid(5, 5)
        hex_grid.display_grid()

        # Initialiser le parcours
        dijkstra = Dijkstra(hex_grid)

        # Définir le point de départ et d'arrivée
        start_coords = (0, 2, -2)
        target_coords = (2,-1,-1)

        # hex_grid.display_neighbors(*start_coords)
        # hex_grid.display_neighbors(*target_coords)

        # Lancer Dijkstra
        path_to_target, total_path = dijkstra.shortest_path(start_coords, target_coords)

        # Afficher les résultats
        if path_to_target:
            print(f"Un chemin existe entre {start_coords} et {target_coords}.")
            print(f"Chemin vers la cible : {path_to_target}")
        else:
            print(f"Aucun chemin trouvé entre {start_coords} et {target_coords}.")


        print(f"Chemin total parcouru : {total_path}")

    def execute(self, start_coords, target_coords):
        best_path = self.dijkstra.shortest_path(start_coords, target_coords)
        return best_path