class ParcoursProfondeur:
    def __init__(self, hex_grid):
        self.grid = hex_grid
        self.visited = set()  # Ensemble pour suivre les nœuds visités

    def dfs_recursive(self, current, target, current_distance, path):
        """Effectuer un parcours en profondeur récursif (DFS) entre start et target."""
        # Si le nœud courant est déjà visité, on retourne
        if current in self.visited:
            return False, float('inf'), []

        # Marquer le nœud comme visité
        self.visited.add(current)

        # Ajouter la position actuelle au chemin et la distance
        path.append(current)
        current_node = self.grid.get_node(*current)
        current_distance += current_node.valeur

        # Si on a trouvé le nœud cible
        if current == target:
            return True, current_distance, path

        # Explorer récursivement les voisins
        for direction, neighbor in current_node.voisins.items():
            neighbor_coords = (neighbor.x, neighbor.y, neighbor.z)
            found, total_distance, full_path = self.dfs_recursive(
                neighbor_coords, target, current_distance, path.copy()
            )

            if found:
                return True, total_distance, full_path

        return False, float('inf'), []  # Aucun chemin trouvé
