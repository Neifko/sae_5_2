from sae_5_2.models.Grid import Grid
from sae_5_2.models.Node import Node

class AEtoile:
    """
    Classe AEtoile.py (A*) : Implementation de l'algorithme A*
    """
    def __init__(self, grid: Grid):
        """
        Constructeur de la classe AEtoile qui prend en paramètre une grille de noeuds.
        """
        self.grid = grid
        self.visited = set()  # Ensemble pour suivre les noeuds visités
        self.parent = {}  # Dictionnaire pour suivre les noeuds parents
        self.total_path = []  # Liste pour suivre le chemin total parcouru

    def heuristic(self, node1: Node, node2: Node) -> int:
        """
        Méthode heuristique pour estimer la distance entre deux noeuds.
        Utilise la distance de Manhattan pour les coordonnées cubiques.
        """
        return max(abs(node1.x - node2.x), abs(node1.y - node2.y), abs(node1.z - node2.z))

    def parcours(self, start_coords: tuple, goal_coords: tuple):
        """
        Méthode parcours qui réalise le parcours A* et explore les chemins.
        Prend en paramètre les coordonnées de départ et d'arrivée.
        """
        start_node = self.grid.get_node(*start_coords)
        goal_node = self.grid.get_node(*goal_coords)

        open_set = [start_node]  # Liste des noeuds à évaluer, initialisée avec le noeud de départ
        came_from = {}  # Dictionnaire pour garder la trace du chemin
        g_score = {start_node: 0}  # Coût du chemin le plus court depuis le départ jusqu'à ce noeud
        f_score = {start_node: self.heuristic(start_node, goal_node)}  # Estimation du coût total du départ à l'objectif en passant par ce noeud

        while open_set:
            # Trouver le noeud dans open_set avec le plus petit f_score
            current = min(open_set, key=lambda node: f_score.get(node, float('inf')))

            if current == goal_node:
                path_to_target = self.reconstruct_path(came_from, current)
                total_path = self.construct_total_path(came_from, start_node, goal_node)
                print(f"\n came_from : {came_from}")
                return path_to_target, total_path

            open_set.remove(current)
            self.visited.add(current)

            for neighbor in self.grid.get_node(current.x, current.y, current.z).voisins.values():
                if neighbor is None or not neighbor.active or neighbor in self.visited:
                    continue

                tentative_g_score = g_score[current] + neighbor.valeur

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal_node)
                    if neighbor not in open_set:
                        open_set.append(neighbor)

        return None, []

    def reconstruct_path(self, came_from: dict, current: Node) -> list:
        """
        Méthode reconstruct_path qui permet de construire le chemin idéal après l'exploration
        faite par le parcours.
        """
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        total_path.reverse()
        return [(node.x, node.y, node.z) for node in total_path]


    def construct_total_path(self, came_from: dict, start_node: Node, goal_node: Node) -> list:
        """
        Méthode pour construire le chemin complet basé sur came_from.
        """
        total_path = [(start_node.x, start_node.y, start_node.z)]
        for node, parent in came_from.items():
            total_path.append((node.x, node.y, node.z))
            total_path.append((parent.x, parent.y, parent.z))
        total_path.append((start_node.x, start_node.y, start_node.z))
        total_path.append((goal_node.x, goal_node.y, goal_node.z))
        return total_path

