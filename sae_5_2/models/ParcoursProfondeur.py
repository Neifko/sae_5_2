class ParcoursProfondeur:
    def __init__(self, hex_grid):
        self.grid = hex_grid
        self.visited = set()  # Ensemble pour suivre les nœuds visités

    def parcours(self, start_coords, target_coords):
        stack = [start_coords]
        path = []
        self.visited = set()

        while stack:
            current_coords = stack.pop()
            if current_coords in self.visited:
                continue

            self.visited.add(current_coords)
            path.append(current_coords)

            if current_coords == target_coords:
                return path

            current_node = self.grid.get_node(*current_coords)
            for neighbor in current_node.voisins.values():
                if neighbor and (neighbor.x, neighbor.y, neighbor.z) not in self.visited:
                    stack.append((neighbor.x, neighbor.y, neighbor.z))

        return None  # Retourne None si aucun chemin n'est trouvé