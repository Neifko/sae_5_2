from sae_5_2.models.Grid import Grid
from sae_5_2.models.Node import Node

class BF:
    """
    Classe BF.py (Bellman-Ford) : Implementation de l'algorithme Bellman-Ford 
    """
    def __init__(self, grid:Grid):
        """
        Constructeur de la classe BellmanFord qui prend en paramètre une grille de noeuds.
        """
        self.grid = grid
        self.visited = set()  # Ensemble pour suivre les noeuds visités
        self.parent = {}  # Dictionnaire pour suivre les noeuds parents
        self.total_path = []  # Liste pour suivre le chemin total parcouru

    def bellman_ford(self, start_coords:tuple):
        """
        Implémente l'algorithme de Bellman-Ford pour trouver le plus court chemin depuis un nœud de départ.
        """
        # Initialisation
        distance = {node: float('inf') for node in self.grid.nodes.values()}
        predecessor = {node: None for node in self.grid.nodes.values()}
        start_node = self.grid.get_node(*start_coords)
        distance[start_node] = 0

        # Relaxation des arêtes
        for _ in range(len(self.grid.nodes) - 1):
            updated = False
            for node in self.grid.nodes.values():
                if not node.active:
                    continue
                for neighbor in self.grid.get_neighbors(node.x, node.y, node.z).values():
                    if neighbor and neighbor.active:
                        if distance[node] + neighbor.valeur < distance[neighbor]:
                            distance[neighbor] = distance[node] + neighbor.valeur
                            predecessor[neighbor] = node
                            self.total_path.append((neighbor.x, neighbor.y, neighbor.z))
                            updated = True
            if not updated:
                break

        # Vérification des cycles négatifs
        for node in self.grid.nodes.values():
            if not node.active:
                continue
            for neighbor in self.grid.get_neighbors(node.x, node.y, node.z).values():
                if neighbor and neighbor.active:
                    if distance[node] + neighbor.valeur < distance[neighbor]:
                        raise ValueError("Le graphe contient un cycle de poids négatif.")

        return distance, predecessor

    def find_shortest_path(self, start_coords:tuple, goal_coords:tuple):
        """
        Trouve le chemin le plus court entre le noeud de départ et le noeud d'arrivée en utilisant Bellman-Ford.
        """
        distance, predecessor = self.bellman_ford(start_coords)
        start_node = self.grid.get_node(*start_coords)
        goal_node = self.grid.get_node(*goal_coords)

        if distance[goal_node] == float('inf'):
            raise ValueError("Aucun chemin trouvé entre le noeud de départ et le noeud d'arrivée.")

        path = self.reconstruct_path(predecessor, goal_node)
        
        # Ajouter le chemin de retour à l'origine à total_path
        current = goal_node
        while current is not None:
            self.total_path.append((current.x, current.y, current.z))
            current = predecessor[current]
        
        return path, distance[goal_node]

    def reconstruct_path(self, predecessor:dict, goal_node:Node):
        """
        Reconstruit le chemin à partir du dictionnaire des prédécesseurs.
        """
        path = []
        current = goal_node
        while current is not None:
            path.append((current.x, current.y, current.z))
            current = predecessor[current]
        path.reverse()
        return path

    def parcours(self, start_coords:tuple, goal_coords:tuple):
        """
        Méthode parcours qui réalise le parcours Bellman-Ford et explore les chemins.
        Prend en paramètre les coordonnées de départ et d'arrivée.
        """
        path_to_target, _ = self.find_shortest_path(start_coords, goal_coords)
        return path_to_target, self.total_path