class ParcoursProfondeur:
    def __init__(self, hex_grid):
        """
        Initialiser le parcours en profondeur sur une grille hexagonale.
        :param hex_grid: Grille hexagonale
        """
        self.grid = hex_grid
        self.visited = set()  # Ensemble pour suivre les nœuds visités

    def parcours(self, start_coords, target_coords):
        """
        Parcours en profondeur
        :param start_coords: Coordonnées de départ (x, y, z)
        :param target_coords: Coordonnées d'arrivée (x, y, z)
        :return: Chemin entre les deux points
        """
        stack = [start_coords]
        path = []
        self.visited = set()

        while stack:
            current_coords = stack.pop()
            if current_coords in self.visited:
                continue

            self.visited.add(current_coords)
            path.append(current_coords)

            if target_coords is not None and current_coords == target_coords:
                return path

            current_node = self.grid.get_node(*current_coords)
            for neighbor in current_node.voisins.values():
                if neighbor and neighbor.active and (neighbor.x, neighbor.y, neighbor.z) not in self.visited:
                    stack.append((neighbor.x, neighbor.y, neighbor.z))

        if target_coords is None:
            return path


        return None  # Retourne None si aucun chemin n'est trouvé