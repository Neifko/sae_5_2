import random


class ParcoursProfondeur:
    def __init__(self, hex_grid):
        """
        Initialize depth-first search on a hexagonal grid.
        :param hex_grid: Hexagonal grid
        """
        self.grid = hex_grid
        self.visited = set()  # Set to track visited nodes
        self.parent = {}  # Dictionary to track parent nodes
        self.total_path = []  # List to track the total path traversed

    def parcours(self, start_coords, target_coords):
        """
        Depth-first search
        :param start_coords: Starting coordinates (x, y, z)
        :param target_coords: Target coordinates (x, y, z)
        :return: Tuple containing the path to the target and the total path traversed
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
            unvisited_neighbors = [
                n for n in current_node.voisins.values()
                if (n.x, n.y, n.z) not in self.visited and n.active
            ]

            if unvisited_neighbors:
                for neighbor in unvisited_neighbors:
                    neighbor_coords = (neighbor.x, neighbor.y, neighbor.z)
                    stack.append(neighbor_coords)
                    self.parent[neighbor_coords] = current_coords
            else:
                # Ensure proper backtracking by checking the parent node
                if current_coords in self.parent:
                    stack.append(self.parent[current_coords])
                    self.total_path.append(self.parent[current_coords])


        return path_to_target, self.total_path  # Return the path to the target node and the total path traversed

    def _reconstruct_path(self, target_coords):
        """
        Reconstruct the path from the target coordinates using the parent dictionary.
        :param target_coords: Target coordinates (x, y, z)
        :return: Complete path as a list of coordinates
        """
        path = []
        current_coords = target_coords
        while current_coords is not None:
            path.append(current_coords)
            current_coords = self.parent[current_coords]
        path.reverse()
        return path