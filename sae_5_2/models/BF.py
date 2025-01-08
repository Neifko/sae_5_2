"""
Classe BF.py (Bellman-Ford) : Implementation de l'algorithme Bellman-Ford 
"""
from sae_5_2.models.Grid import Grid
from sae_5_2.models.Node import Node

class BF:
    def __init__(self, grid:Grid):
        """
        Constructeur de la classe BF qui prend en paramètre une grille de noeuds.
        """
        self.grid = grid

    def bellman_ford(self, start_coords:tuple):
        """
        Algorithme de Bellman-Ford pour trouver les plus courts chemins depuis un noeud de départ.
        """
        start_node = self.grid.get_node(*start_coords)
        if not start_node:
            raise ValueError("Le noeud de départ n'existe pas dans la grille.")

        # Initialisation des distances et des prédécesseurs
        distance = {node: float('inf') for node in self.grid.nodes.values()}
        predecessor = {node: None for node in self.grid.nodes.values()}
        distance[start_node] = 0

        # Relaxation des arêtes
        for _ in range(len(self.grid.nodes) - 1):
            for node in self.grid.nodes.values():
                if not node.active:
                    continue
                for neighbor in self.grid.get_neighbors(node.x, node.y, node.z).values():
                    if neighbor and neighbor.active:
                        if distance[node] + neighbor.valeur < distance[neighbor]:
                            distance[neighbor] = distance[node] + neighbor.valeur
                            predecessor[neighbor] = node

        # Vérification des cycles négatifs
        for node in self.grid.nodes.values():
            if not node.active:
                continue
            for neighbor in self.grid.get_neighbors(node.x, node.y, node.z).values():
                if neighbor and neighbor.active:
                    if distance[node] + neighbor.valeur < distance[neighbor]:
                        raise ValueError("Le graphe contient un cycle de poids négatif.")

        return distance, predecessor

    def reconstruct_path(self, predecessor, start_node, goal_node):
        """
        Reconstruit le chemin à partir du dictionnaire des prédécesseurs.
        """
        path = []
        current = goal_node
        while current is not None:
            path.append(current)
            current = predecessor[current]
        path.reverse()
        return path

    def find_shortest_path(self, start_coords: tuple, goal_coords: tuple):
        """
        Trouve le chemin le plus court entre le noeud de départ et le noeud d'arrivée.
        """
        distances, predecessor = self.bellman_ford(start_coords)
        start_node = self.grid.get_node(*start_coords)
        goal_node = self.grid.get_node(*goal_coords)

        if distances[goal_node] == float('inf'):
            raise ValueError("Aucun chemin trouvé entre le noeud de départ et le noeud d'arrivée.")

        path = self.reconstruct_path(predecessor, start_node, goal_node)
        return path, distances[goal_node]
