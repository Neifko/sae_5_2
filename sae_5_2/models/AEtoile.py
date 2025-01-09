from sae_5_2.models.Grid import Grid
from sae_5_2.models.Node import Node


class AEtoile:
    """
    Classe AEtoile.py (A*) : Implementation de l'algorithme A*
    """
    def __init__(self, grid:Grid):
        """
        Constructeur de la classe AEtoile qui prend en paramètre une grille de noeuds.
        """
        self.grid = grid

    def heuristic(self, node1:Node, node2:Node) -> int:
        """
        Méthode heuristique pour estimer la distance entre deux noeuds.
        Utilise la distance de Manhattan pour les coordonnées cubiques.
        """
        return max(abs(node1.x - node2.x), abs(node1.y - node2.y), abs(node1.z - node2.z))

    def parcours(self, start_coords: tuple, goal_coords: tuple):
        """
        Méthode parcours qui permet qui réalise le parcours A* et explore les chemins.
        Prend en paramètre les coordonées de départ et d'arrivée.
        """
        start_node = self.grid.get_node(*start_coords)
        goal_node = self.grid.get_node(*goal_coords)

        open_set = [start_node]  # Liste des noeuds à évaluer, initialisée avec le noeud de départ
        came_from = {}  # Dictionnaire pour garder la trace du chemin
        g_score = {start_node: 0}  # Coût du chemin le plus court depuis le départ jusqu'à ce noeud
        f_score = {start_node: self.heuristic(start_node, goal_node)}  # Estimation du coût total du départ à l'objectif en passant par ce noeud

        total_path = []

        while open_set:
            # Trouver le noeud dans open_set avec le plus petit f_score
            current = min(open_set, key=lambda node: f_score.get(node, float('inf')))
            total_path.append((current.x, current.y, current.z))

            if current == goal_node:
                path_to_target = self.reconstruct_path(came_from, current)
                return path_to_target, total_path

            open_set.remove(current)

            for neighbor in self.grid.get_neighbors(current.x, current.y, current.z).values():
                if neighbor is None or not neighbor.active:
                    continue

                tentative_g_score = g_score[current] + neighbor.valeur

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:                # Logique pour évaluer le voisin et mettre à jour les valeurs si nécessaire.
                    came_from[neighbor] = current                                                   # Si le voisin n'a pas encore été évalué ou si le nouveau chemin est meilleur que l'ancien,
                    g_score[neighbor] = tentative_g_score                                           # alors on met à jour les valeurs et on l'ajoute à la liste des noeuds à évaluer (s'il n'y est pas encore).
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal_node)
                    if neighbor not in open_set:
                        open_set.append(neighbor)

        return None, total_path

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