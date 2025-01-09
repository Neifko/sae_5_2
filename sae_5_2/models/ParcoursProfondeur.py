class ParcoursProfondeur:
    def __init__(self, hex_grid):
        """
        Initialiser le parcours en profondeur sur une grille hexagonale.
        :param hex_grid: Grille hexagonale
        """
        self.grid = hex_grid
        self.visited = set()  # Ensemble pour suivre les nœuds visités
        self.parent = {}  # Dictionnaire pour suivre les parents des nœuds
        self.total_path = []  # Liste pour suivre le chemin total parcouru

    def parcours(self, start_coords, target_coords):
        """
        Parcours en profondeur
        :param start_coords: Coordonnées de départ (x, y, z)
        :param target_coords: Coordonnées d'arrivée (x, y, z)
        :return: Tuple contenant le chemin vers la cible et le chemin total parcouru
        """
        stack = [start_coords]
        self.visited = set()
        self.parent = {start_coords: None}
        self.total_path = []
        path_to_target = None

        while stack:
            current_coords = stack.pop()
            if current_coords in self.visited:
                continue

            self.visited.add(current_coords)
            self.total_path.append(current_coords)

            if current_coords == target_coords and path_to_target is None:
                path_to_target = self._reconstruct_path(target_coords)

            current_node = self.grid.get_node(*current_coords)
            for neighbor in current_node.voisins.values():
                neighbor_coords = (neighbor.x, neighbor.y, neighbor.z)
                if neighbor and neighbor_coords not in self.visited:
                    stack.append(neighbor_coords)
                    self.parent[neighbor_coords] = current_coords

        return path_to_target, self.total_path  # Retourne le chemin vers le nœud cible et le chemin total parcouru

    def _reconstruct_path(self, target_coords):
        """
        Reconstruit le chemin à partir des coordonnées cibles en utilisant le dictionnaire des parents.
        :param target_coords: Coordonnées d'arrivée (x, y, z)
        :return: Chemin complet sous forme de liste de coordonnées
        """
        path = []
        current_coords = target_coords
        while current_coords is not None:
            path.append(current_coords)
            current_coords = self.parent[current_coords]
        path.reverse()
        return path