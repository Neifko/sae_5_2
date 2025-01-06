# Exemple d'utilisation
from sae_5_2.models.ParcoursProfondeur import ParcoursProfondeur
from sae_5_2.models.Grid import Grid

if __name__ == "__main__":
    # Exemple d'utilisation
    rows, cols = 3, 3  # Taille de la grille
    hex_grid = Grid(rows, cols)

    # Afficher la grille hexagonale avec les coordonnées dans la console
    hex_grid.display_grid()

    # Afficher les voisins d'un nœud particulier
    hex_grid.display_neighbors(0, 1, -1)  # Coordonnées (x=2, y=2, z=-4)

    # # Création d'une grille hexagonale de 4x4
    # hex_grid = HexGrid(4, 4)
    #
    # # Création de l'instance DFS
    # hex_dfs = HexDFS(hex_grid)
    #
    # # Exemple de parcours DFS pour vérifier s'il existe un chemin entre deux nœuds
    # start_coords = (2, 2, -4)  # Nœud de départ
    # target_coords = (1, 3, -4)  # Nœud cible
    #
    # # Vérifier si un chemin existe entre les deux nœuds
    # path_exists = hex_dfs.dfs(start_coords, target_coords)
    #
    # # Afficher le résultat
    # print(f"Un chemin existe entre {start_coords} et {target_coords}: {path_exists}")
