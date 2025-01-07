# Exemple d'utilisation
from sae_5_2.models.ParcoursProfondeur import ParcoursProfondeur
from sae_5_2.models.Grid import Grid

if __name__ == "__main__":
    # Exemple d'utilisation
    rows, cols = 3, 3  # Taille de la grille
    hex_grid = Grid(rows, cols)

    # Afficher la grille hexagonale avec les coordonnées dans la console
    # hex_grid.display_grid()

    for node in hex_grid.nodes.values():
        hex_grid.display_neighbors(node.x, node.y, node.z)
    # Afficher les voisins d'un nœud particulier
    # hex_grid.display_neighbors(0, 0, 0)  # Coordonnées (x=2, y=2, z=-4)

    print("FAIT")
