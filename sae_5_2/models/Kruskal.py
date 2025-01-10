from sae_5_2.models.Grid import Grid


def kruskal_algorithm(grid):
    """
     minimum.
    :param grid: Instance de Grid
    :return: Tuple
        - Liste des arêtes de l'arbre couvrant minimum
        - Poids total de l'arbre couvrant minimum
    """
    edges = []
    mst = []
    total_weight = 0

    # Crée une liste d'arêtes (voisinages actifs uniquement)
    for node_coords, node in grid.nodes.items():
        if node.active:
            for direction, neighbor in node.voisins.items():
                if neighbor and neighbor.active:
                    weight = node.valeur + neighbor.valeur
                    edges.append((weight, node, neighbor))

    # Trie les arêtes par poids (croissant)
    edges.sort(key=lambda edge: edge[0])

    # Initialisation de la structure Union-Find
    parent = {}
    rank = {}

    def find(node):
        """
        Trouve le représentant d'une composante (avec compression de chemin).
        """
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        """
        Fait l'union de deux composantes en utilisant les rangs.
        """
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    # Initialise chaque nœud comme une composante distincte
    for node_coords, node in grid.nodes.items():
        if node.active:
            parent[node] = node
            rank[node] = 0

    # Construction de l'arbre couvrant minimum
    for weight, node1, node2 in edges:
        if find(node1) != find(node2):  # Vérifie qu'il n'y a pas de cycle
            union(node1, node2)
            mst.append((node1, node2, weight))
            total_weight += weight

    return mst, total_weight


if __name__ == "__main__":
    grid = Grid(3, 3)  # Crée une grille hexagonale de 4×4

    # Désactive quelques nœuds pour créer plusieurs composantes connexes
    grid.get_node(1, 0, -1).active = False
    grid.get_node(2, 1, -3).active = False
    grid.get_node(1, 1, -2).active = False

    mst, total_weight = kruskal_algorithm(grid)

    print("Arbre couvrant minimum (MST):")
    listeMst = []
    for i in range(len(mst)):
        listeMst.append((mst[i][0].x, mst[i][0].y, mst[i][0].z))
    print(listeMst)
    print(f"Poids total de l'arbre couvrant minimum: {total_weight}")