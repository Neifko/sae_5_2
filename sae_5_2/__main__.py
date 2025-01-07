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

    # Initialiser le parcours en profondeur récursif (DFS)
    parcours_profondeur = ParcoursProfondeur(hex_grid)

    # Définir le point de départ et d'arrivée
    start_coords = (0, 0, 0)
    target_coords = (2, 2, -4)

    hex_grid.display_neighbors(*start_coords)
    hex_grid.display_neighbors(*target_coords)



    # Lancer DFS récursif
    path = parcours_profondeur.parcours(start_coords, target_coords)

    # Afficher les résultats
    if path:
        print(f"Un chemin existe entre {start_coords} et {target_coords}.")
        # print(f"Distance totale : {distance}")
        print(f"Chemin trouvé : {path}")
    else:
        print(f"Aucun chemin trouvé entre {start_coords} et {target_coords}.")
