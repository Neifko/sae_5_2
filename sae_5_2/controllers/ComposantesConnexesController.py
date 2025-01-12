from sae_5_2.models.ComposantesConnexes import ComposantesConnexes
from sae_5_2.models.Grid import Grid
from sae_5_2.models.Dijkstra import Dijkstra

class ComposantesConnexesController:

    def __init__(self):
        self.grid = None
        self.composantes_connexes = None

    def set_grid(self, grid):
        self.grid = grid
        self.composantes_connexes = ComposantesConnexes(grid)

    def display_composantes_connexes_in_console(self):
        # Créer une grille de taille 5x5
        hex_grid = Grid(5, 5)
        hex_grid.display_grid()

        # Initialiser le parcours
        composantes_connexes = ComposantesConnexes(hex_grid)

        # Récupérer les composantes connexes
        composantes_connexes_list = composantes_connexes.find_connected_components()

        # Afficher les résultats
        print("Composantes connexes trouvées :")
        for i, component in enumerate(composantes_connexes_list):
            print(f"Composante {i + 1} : {component}")


    def execute(self):
        if self.grid is None:
            raise ValueError("La grille n'est pas initialisée")
        composantes_connexes = ComposantesConnexes(self.grid)
        return composantes_connexes.find_connected_components()