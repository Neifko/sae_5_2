from sae_5_2.models.Grid import Grid
from sae_5_2.models.AEtoile import AEtoile

def main():
    # Crée une grille de dimensions 5x5
    width = 10
    height = 5
    grid = Grid(width, height)

    # Affiche la grille sous forme de matrice
    grid.display_grid()

    # Teste l'algorithme A* pour trouver le chemin le plus court
    a_star_solver = AEtoile(grid)
    start = (0, 0, 0)
    goal = (2, 5, -7)
    path = a_star_solver.a_star(start, goal)

    if path:
        print("\nChemin trouvé :")
        for node in path:
            print(f"({node.x}, {node.y}, {node.z})")
    else:
        print("\nAucun chemin trouvé.")

if __name__ == "__main__":
    main()