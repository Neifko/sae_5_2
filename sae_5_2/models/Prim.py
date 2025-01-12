from heapq import heappush, heappop

from sae_5_2.models.Grid import Grid

class Prim:

    def __init__(self, grid):
        self.grid = grid

    def prim_algorithm(self, start_coords):
        """
        Algo de Prim
        :param start_coords: Tuple (x, y, z) des coordonnées du noeud de départ
        :return: Tuple
        - Liste du plus petit chemin en partant de start_coords
        - Poid total de l'arbre
        """

        # Noeud de départ
        start_node = self.grid.get_node(*start_coords)
        if not start_node:
            raise ValueError("Les coordonnées de départ sont invalides")

        visited = set() # Ensemble des noeuds visités
        mst = [] # Liste du plus petit chemin
        priority_queue = [] # File de priorité pour les aretes
        total_weight = 0

        visited.add(start_node)
        mst.append((start_node.x, start_node.y, start_node.z))

        for direction, neighbor in start_node.voisins.items():
            if neighbor.active:
                heappush(priority_queue, (neighbor.valeur, id(neighbor), start_node, neighbor))

        while priority_queue:
            weight, _, node1, node2 = heappop(priority_queue)

            if node2 in visited:
                continue

            visited.add(node2)
            mst.append((node2.x, node2.y, node2.z))
            total_weight += weight

            for direction, neighbor in node2.voisins.items():
                if neighbor not in visited and neighbor.active:
                    heappush(priority_queue, (neighbor.valeur, id(neighbor), start_node, neighbor))
        print(mst)
        return mst, total_weight

# Exemple d'utilisation
if __name__ == "__main__":
    grid = Grid(4, 3)  # Crée une grille hexagonale de 4x3
    start_coords = (0, 0, 0)  # Coordonnées de départ

    prim = Prim(grid)
    mst, total_weight = prim.prim_algorithm(start_coords)
    print("Arbre couvrant minimum (MST):")
    print(mst)
    print(f"Poids total de l'arbre couvrant minimum: {total_weight}")