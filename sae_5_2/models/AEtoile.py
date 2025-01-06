from sae_5_2.models.Node import Node

class AEtoile:
    def __init__(self, grid):
        """
        Constructeur de la classe AEtoile qui prend en paramètre une grille de noeuds.
        """
        self.grid = grid

    def heuristic(self, node1, node2):
        """
        Fonction heuristique pour estimer la distance entre deux noeuds.
        Utilise la distance de Manhattan pour les coordonnées cubiques.
        """
        return max(abs(node1.x - node2.x), abs(node1.y - node2.y), abs(node1.z - node2.z))

    def a_star(self, start_coords, goal_coords):
        """
        Algorithme A* pour trouver le chemin le plus court entre deux noeuds.
        """
        start_node = self.grid.get_node(*start_coords)
        goal_node = self.grid.get_node(*goal_coords)

        open_set = [start_node]
        came_from = {}
        g_score = {start_node: 0}
        f_score = {start_node: self.heuristic(start_node, goal_node)}

        while open_set:
            # Trouver le noeud dans open_set avec le plus petit f_score
            current = min(open_set, key=lambda node: f_score.get(node, float('inf')))

            if current == goal_node:
                return self.reconstruct_path(came_from, current)

            open_set.remove(current)

            for neighbor in self.grid.get_neighbors(current.x, current.y, current.z).values():
                if neighbor is None or not neighbor.active:
                    continue

                tentative_g_score = g_score[current] + neighbor.valeur

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal_node)
                    if neighbor not in open_set:
                        open_set.append(neighbor)

        return None

    def reconstruct_path(self, came_from, current):
        """
        Reconstruit le chemin à partir du dictionnaire came_from.
        """
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        total_path.reverse()
        return total_path