from heapq import heappush, heappop

from sae_5_2.models.Grid import Grid

class Prim():

    def __init__(self):
        """
        Configuration initiale avant chaque test.
        Création d'une grille hexagonale pour les tests.
        """
        self.grid = Grid(4, 4)  # Grille de 4x4
        self.start_coords = (0,0,0)  # Coordonnées du nœud de départ

        # Modifier les valeurs des nœuds pour les tests
        self.grid.get_node(2, 2, -4).valeur = 2
        self.grid.get_node(0, 1, -1).valeur = 3
        self.grid.get_node(1, 0, -1).valeur = 1
        self.grid.get_node(1, 1, -2).valeur = 5
        self.grid.get_node(0, 2, -2).valeur = 4

        self.grid.get_node(0, 2, -2).active = False
        self.grid.get_node(1, 1, -2).active = False
        self.grid.get_node(2, 0, -2).active = False
        self.grid.get_node(0, 1, -1).active = False

    def prim_algorithm(self, grid, start_coords):
        """
        Algo de Prim
        :param grid: Instance de Grid
        :param start_coords: Tuple (x, y, z) des coordonnées du noeud de départ
        :return: Tuple
        - Liste du plus petit chemin en partant de start_coords
        - Poids total de l'arbre
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

        print(mst)
        return mst, total_weight

# Exemple d'utilisation
if __name__ == "__main__":
    grid = Grid(4, 4)
    start_coords = (0,0,0)

    prim = Prim()

    mst_filtree, total_weight = prim.prim_algorithm(grid, start_coords)
    print("Arbre couvrant minimum (MST):")
    print(mst_filtree)
    for edge in mst_filtree:
        print(f"De {edge[0]} à {edge[1]} avec un poids de {edge[2]}")
    print(f"Poids total de l'arbre couvrant minimum: {total_weight}")