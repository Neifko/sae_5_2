import random
from sae_5_2.models.Grid import Grid
from sae_5_2.models.BF import BF

def main():
    # Crée une grille de dimensions 7x8
    width = 7
    height = 8
    grid = Grid(width, height)

    # Désactive certains noeuds de manière aléatoire
    num_nodes_to_deactivate = 3
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

    # Change la valeur de quelques noeuds
    num_nodes_to_negate = 10
    for _ in range(num_nodes_to_negate):
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            z = -x - y
            node = grid.get_node(x, y, z)
            if node and node.active and node not in deactivated_nodes:
                node.valeur = abs(node.valeur) * random.randint(1, 7)
                break

    # Affiche les noeuds désactivés
    print("\nNoeuds désactivés (coordonnées x, y, z) :")
    for node in deactivated_nodes:
        print(f"({node.x}, {node.y}, {node.z})")

    # Affiche la grille sous forme de matrice
    grid.display_grid()

    # Coordonnées de départ et d'arrivée
    start = (0, 0, 0)
    goal = (4, 0, -4)

    # Vérifie l'existence du noeud d'arrivée
    if not grid.get_node(*goal):
        print(f"\nLe noeud d'arrivée {goal} n'existe pas dans la grille.")
        return

    # Teste l'algorithme Bellman-Ford pour trouver les plus courts chemins
    bf_solver = BF(grid)
    try:
        path, distance = bf_solver.find_shortest_path(start, goal)
        print("\nChemin trouvé par Bellman-Ford :")
        for node in path:
            print(f"({node.x}, {node.y}, {node.z})")
        print(f"Distance totale : {distance}")
    except ValueError as e:
        print(e)

    # Teste l'algorithme A* pour trouver le chemin le plus court
    # a_star_solver = AEtoile(grid)
    # path = a_star_solver.a_star(start, goal)

    # if path:
    #     print("\nChemin trouvé par A* :")
    #     for node in path:
    #         print(f"({node.x}, {node.y}, {node.z})")
    # else:
    #     print("\nAucun chemin trouvé par A*.")

if __name__ == "__main__":
    main()