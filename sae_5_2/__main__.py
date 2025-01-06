from sae_5_2.models.Grid import Grid
from sae_5_2.models.AEtoile import AEtoile

import random

def main():
    # Crée une grille de dimensions 5x5
    width = 10
    height = 5
    grid = Grid(width, height)

    # Affiche la grille sous forme de matrice
    grid.display_grid()

    # Désactive certains noeuds de manière aléatoire
    num_nodes_to_deactivate = 7
    deactivated_nodes = []
    for _ in range(num_nodes_to_deactivate):
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            z = -x - y
            node = grid.get_node(x, y, z)
            if node and node.active:
                node.active = False
                deactivated_nodes.append(node)
                break

    # Affiche les noeuds désactivés
    print("\nNoeuds désactivés (coordonnées x, y, z) :")
    for node in deactivated_nodes:
        print(f"({node.x}, {node.y}, {node.z})")


    # Teste l'algorithme A* pour trouver le chemin le plus court
    a_star_solver = AEtoile(grid)
    start = (0, 0, 0)
    goal = (2, 5, -7)
    path = a_star_solver.a_star(start, goal)

    print("\nDépart :", start)
    print("Arrivée :", goal)

    if path:
        print("\nChemin trouvé :")
        for node in path:
            print(f"({node.x}, {node.y}, {node.z})")
    else:
        print("\nAucun chemin trouvé.")

if __name__ == "__main__":
    main()