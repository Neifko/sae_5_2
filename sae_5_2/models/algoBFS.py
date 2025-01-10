class AlgoBFS:
    """
    Implémente l'algorithme de parcours en largeur (BFS) pour trouver un chemin entre deux nœuds dans une grille hexagonale.
    
    Attributs:
        grid (Grid): La grille hexagonale dans laquelle le parcours est effectué.

    Méthodes:
        __init__(grid): Initialise l'instance avec une grille donnée.
        find_path(start, goal): Trouve un chemin entre le nœud de départ et le nœud d'arrivée.
        _reconstruct_path(visited, start, goal): Reconstruit le chemin à partir des informations de provenance.
    """

    def __init__(self, grid):
        """
        Initialise l'algorithme BFS avec une grille hexagonale.

        Args:
            grid (Grid): Instance de la classe Grid représentant la grille hexagonale.
        """
        self.grid = grid  # Associe la grille fournie à l'algorithme.
        self.total_path = []  # Liste pour suivre le chemin total parcouru


    def find_path(self, start, goal):
        """
        Trouve un chemin entre deux nœuds en utilisant l'algorithme BFS.

        Args:
            start (Node): Le nœud de départ.
            goal (Node): Le nœud d'arrivée.

        Returns:
            list[Node]: Liste des nœuds formant le chemin du départ à l'arrivée, ou une liste vide si aucun chemin n'existe.
        """
        # Si le départ et l'arrivée sont les mêmes, retourne immédiatement le nœud de départ.
        if start == goal:
            return [start]

        # Initialise la file d'attente BFS avec le nœud de départ.
        queue = [start]
        # Dictionnaire pour stocker le parent de chaque nœud visité.
        visited = {start: None}
        self.total_path = []  # Réinitialise le chemin total parcouru

        # Boucle principale du BFS.
        while queue:
            current = queue.pop(0)  # Récupère le nœud actuel en début de file.
            self.total_path.append(current)  # Ajoute le nœud actuel au chemin total parcouru

            # Si on atteint le nœud d'arrivée, reconstruit et retourne le chemin.
            if current == goal:
                return self._reconstruct_path(visited, start, goal), self.total_path

            # Parcourt les voisins du nœud actuel.
            for direction, neighbor in current.voisins.items():
                # Si le voisin n'a pas encore été visité, on l'ajoute à la file et on marque son origine.
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = current
                    #self.total_path.append(current)  # Ajoute le nœud actuel au chemin total parcouru

        return [], self.total_path  # Retourne une liste vide si aucun chemin n'existe, et le chemin total parcouru


    def _reconstruct_path(self, visited, start, goal):
        """
        Reconstruit le chemin en remontant depuis le nœud d'arrivée jusqu'au nœud de départ.

        Args:
            visited (dict): Dictionnaire contenant les informations de provenance des nœuds.
            start (Node): Le nœud de départ.
            goal (Node): Le nœud d'arrivée.

        Returns:
            list[Node]: Liste des nœuds formant le chemin du départ à l'arrivée.
        """
        current = goal  # Commence à partir du nœud d'arrivée.
        path = []  # Initialise la liste pour stocker le chemin.

        # Remonte les nœuds jusqu'à atteindre le départ.
        while current != start:
            path.append(current)
            current = visited[current]

        # Ajoute le nœud de départ au chemin.
        path.append(start)
        # Inverse la liste pour obtenir le chemin dans l'ordre correct.
        path.reverse()
        return path  # Retourne le chemin complet