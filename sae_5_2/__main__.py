# Exemple d'utilisation
from sae_5_2.models.ParcoursProfondeur import ParcoursProfondeur
from sae_5_2.models.Grid import Grid

if __name__ == "__main__":
    # Exemple d'utilisation
    # rows, cols = 3, 3  # Taille de la grille
    # hex_grid = Grid(rows, cols)
    #
    # # Afficher la grille hexagonale avec les coordonnées dans la console
    # hex_grid.display_grid()
    #
    # # Afficher les voisins d'un nœud particulier
    # hex_grid.display_neighbors(0, 1, -1)  # Coordonnées (x=2, y=2, z=-4)

    # Créer une grille de taille 5x5
    hex_grid = Grid(3, 3)
    hex_grid.display_grid()

    # Initialiser les valeurs des nœuds (poids)
    for node in hex_grid.nodes.values():
        node.valeur = 1  # Par défaut, valeur de chaque nœud = 1

    # Définir des valeurs spécifiques à certains nœuds
    hex_grid.get_node(2, 2, -4).valeur = 2
    hex_grid.get_node(3, 2, -5).valeur = 3

    # Initialiser le parcours en profondeur récursif (DFS)
    hex_dfs_recursive = ParcoursProfondeur(hex_grid)

    # Définir le point de départ et d'arrivée
    start_coords = (2, 2, -4)
    target_coords = (3, 3, -6)

    # Lancer DFS récursif
    path_exists, distance, path = hex_dfs_recursive.dfs_recursive(start_coords, target_coords, 0, [])

    # Afficher les résultats
    if path_exists:
        print(f"Un chemin existe entre {start_coords} et {target_coords}.")
        print(f"Distance totale : {distance}")
        print(f"Chemin trouvé : {path}")
    else:
        print(f"Aucun chemin trouvé entre {start_coords} et {target_coords}.")
