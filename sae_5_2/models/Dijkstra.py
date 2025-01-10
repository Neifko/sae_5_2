from heapq import heappush, heappop


class Dijkstra:
    """
    Classe pour implémenter l'algorithme de Dijkstra sur une grille hexagonale

    Cette classe permet de calculer le plus court chemin entre deux node d'une grille hexagonale en utilisant
    l'algorithme de Dijkstra.
    La grille est représentée par une instance de la classe `Grid`, et chaque nœud est une instance de la classe `Node`
    """

    @staticmethod
    def shortest_path(grid, start_coords, target_coords):
        """
        Trouve le plus court chemin entre deux node sur une grille hexagonale

        Cette méthode utilise l'algorithme de Dijkstra pour calculer la distance minimale
        et le chemin entre le nœud de départ et le nœud cible.

        :param grid: Instance de `Grid` représentant la grille hexagonale.
        :param start_coords: Tuple (x, y, z) des coordonnées cubiques du nœud de départ.
        :param target_coords: Tuple (x, y, z) des coordonnées cubiques du nœud cible.
        :return: Tuple contenant :
        - La distance minimale entre les deux node.
        - Une liste des node représentant le chemin emprunté (de départ à cible).

        :raises ValueError: Si les coordonnées de départ ou de destination sont invalides.
        """

        # Récupère les node de départ et d'arrivée à partir de leurs coordonnées
        start_node = grid.get_node(*start_coords)
        target_node = grid.get_node(*target_coords)

        # Vérifie si les node de départ et d'arrivée existent dans la grille
        if not start_node or not target_node:
            raise ValueError("Coordonnées de départ ou de destination invalides")

        # Initialisation des distances avec une valeur infinie pour tous les node
        distances = {node: float('inf') for node in grid.nodes.values()}
        distances[start_node] = 0

        # File de priorité pour suivre les node à explorer
        # Chaque élément de la file est un tuple : (distance, identifiant unique, nœud)
        priority_queue = [(0, id(start_node), start_node)]

        # Dictionnaire pour garder une trace des node précédents dans le chemin
        previous_nodes = {node: None for node in grid.nodes.values()}

        all_paths = {node: [] for node in grid.nodes.values()}
        all_paths[start_node] = [[start_node]]


        # Boucle principale de l'algorithme de Dijkstra
        while priority_queue:
            # Récupère le nœud avec la plus petite distance (file de priorité)
            current_distance, _, current_node = heappop(priority_queue)

            # Si on a atteint le node target, on s'arrete
            if current_node == target_node:
                continue

            # on vérifie les voisins du node actuel
            for neighbor in current_node.voisins.values():

                if not neighbor.active:
                    continue

                # Calcul la distance totale au voisin
                distance = current_distance + neighbor.valeur

                # Si une distance plus courte est trouvée, on met à jour
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    # Ajoute le voisin à la file de priorité avec la nouvelle distance
                    heappush(priority_queue, (distance, id(neighbor), neighbor))

                    all_paths[neighbor] = [path + [neighbor] for path in all_paths[current_node]]

                elif distance == distances[neighbor]:
                    all_paths[neighbor].extend(path + [neighbor] for path in all_paths[current_node])

        # Reconstruction du chemin à partir du dictionnaire previous_nodes
        best_path = []
        current = target_node
        while current is not None:
            best_path.append(current)
            current = previous_nodes[current]

        if distances[target_node] == float('inf') or best_path == [target_node]:
            return None, None, None

        # Le chemin est reconstruit à l'envers, on doit le renverser
        best_path.reverse()

        best_path_tuples = [(node.x, node.y, node.z) for node in best_path]
        all_paths_to_target_tuples = [
            [(node.x, node.y, node.z) for node in path]
            for path in all_paths[target_node]
        ]


        return distances[target_node], best_path_tuples, all_paths_to_target_tuples
