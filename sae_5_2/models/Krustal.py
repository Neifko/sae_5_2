from heapq import heappush, heappop

from sae_5_2.models.Grid import Grid


def krustal_algorithm(grid, start_coords):
    """
    Algo de Krustal
    :param grid: Instance de Grid
    :param start_coords: Tuple (x, y, z) des coordonnées du noeud de départ
    :return: Tuple
    - Liste du plus petit chemin en partant de start_coords
    - Poid total de l'arbre
    """

    # Noeud de départ
    start_node = grid.get_node(*start_coords)
    if not start_node:
        raise ValueError("Les coordonnées de départ sont invalides")

    visited = set() # Ensemble des noeuds visités
    mst = [] # Liste du plus petit chemin
    priority_queue = [] # File de priorité pour les aretes
    total_weight = 0

    visited.add(start_node)
    for direction, neighbor in start_node.voisins.items():
        if neighbor.active:
            heappush(priority_queue, (neighbor.valeur, id(neighbor), start_node, neighbor))

    while priority_queue:
        weight, _, node1, node2 = heappop(priority_queue)

        if node2 in visited:
            continue

        visited.add(node2)
        mst.append((node1, node2, weight))
        total_weight += weight

        for direction, neighbor in node2.voisins.items():
            if neighbor not in visited and neighbor.active:
                heappush(priority_queue, (neighbor.valeur, id(neighbor), start_node, neighbor))

    return mst, total_weight

# Exemple d'utilisation
if __name__ == "__main__":
    grid = Grid(4, 3)  # Crée une grille hexagonale de 4x3
    start_coords = (0, 0, 0)  # Coordonnées de départ

    mst, total_weight = krustal_algorithm(grid, start_coords)
    print("Arbre couvrant minimum (MST):")
    print(mst)
    for edge in mst:
        print(f"De {edge[0]} à {edge[1]} avec un poids de {edge[2]}")
    print(f"Poids total de l'arbre couvrant minimum: {total_weight}")