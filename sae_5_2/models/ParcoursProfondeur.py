class ParcoursProfondeur:
    def __init__(self, hex_grid):
        self.grid = hex_grid  # La grille hexagonale
        self.visited = set()  # Ensemble des nœuds visités pour éviter les cycles

    def dfs(self, start, target):
        """Parcours en profondeur (DFS) pour trouver un chemin entre start et target"""
        self.visited.clear()  # Réinitialiser les nœuds visités à chaque nouveau parcours
        return self._dfs_recursive(start, target)

    def _dfs_recursive(self, current, target):
        """Méthode récursive pour effectuer le DFS"""
        # Si le nœud courant est déjà visité, on ignore ce parcours
        if current in self.visited:
            return False

        # Marquer le nœud comme visité
        self.visited.add(current)

        # Si on atteint le nœud cible, le parcours est réussi
        if current == target:
            return True

        # Récursion sur les voisins du nœud courant
        x, y, z = current
        node = self.grid.get_node(x, y, z)
        if node:
            for neighbor in node.voisins.values():
                neighbor_coords = (neighbor.x, neighbor.y, neighbor.z)
                if self._dfs_recursive(neighbor_coords, target):
                    return True

        return False