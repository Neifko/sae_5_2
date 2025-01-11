import random

class ParcoursProfondeur:
    def __init__(self, hex_grid):
        """
        Initialise la recherche en profondeur sur une grille hexagonale.
        :param hex_grid: Grille hexagonale
        """
        self.grid = hex_grid
        self.visited = set()  # Ensemble pour suivre les noeuds visités
        self.parent = {}  # Dictionnaire pour suivre les noeuds parents
        self.total_path = []  # Liste pour suivre le chemin total parcouru

    def parcours(self, start_coords, target_coords):
        """
        Recherche en profondeur
        :param start_coords: Coordonnées de départ (x, y, z)
        :param target_coords: Coordonnées cibles (x, y, z)
        :return: Tuple contenant le chemin vers la cible et le chemin total parcouru
        """
        stack = [start_coords]  # Pile pour gérer les noeuds à visiter
        self.visited = set()  # Réinitialise l'ensemble des noeuds visités
        self.parent = {start_coords: None}  # Réinitialise le dictionnaire des parents
        self.total_path = []  # Réinitialise le chemin total parcouru
        path_to_target = None  # Initialisation du chemin vers la cible


        while stack:
            current_coords = stack.pop()  # Récupère le noeud actuel
            if current_coords in self.visited:
                continue  # Passe au suivant si déjà visité

            self.visited.add(current_coords)  # Marque le noeud comme visité
            self.total_path.append(current_coords)  # Ajoute le noeud au chemin total

            if current_coords == target_coords and path_to_target is None:
                path_to_target = self._reconstruct_path(target_coords)  # Reconstruit le chemin vers la cible

            current_node = self.grid.get_node(*current_coords)  # Récupère le noeud actuel dans la grille
            unvisited_neighbors = [
                n for n in current_node.voisins.values()
                if (n.x, n.y, n.z) not in self.visited and n.active
            ]  # Liste des voisins non visités et actifs

            if unvisited_neighbors:
                for neighbor in unvisited_neighbors:
                    neighbor_coords = (neighbor.x, neighbor.y, neighbor.z)
                    stack.append(neighbor_coords)  # Ajoute les voisins à la pile
                    self.parent[neighbor_coords] = current_coords  # Met à jour le parent du voisin
            else:
                # Assurer un bon retour en arrière en vérifiant le noeud parent
                while current_coords in self.parent and not unvisited_neighbors:
                    current_coords = self.parent[current_coords]
                    if current_coords is None:
                        break
                    current_node = self.grid.get_node(*current_coords)
                    unvisited_neighbors = [
                        n for n in current_node.voisins.values()
                        if (n.x, n.y, n.z) not in self.visited and n.active
                    ]
                    self.total_path.append(current_coords)  # Ajoute le noeud au chemin total
                if unvisited_neighbors:
                    stack.append(current_coords)  # Ajoute le noeud à la pile

        return path_to_target, self.total_path  # Retourne le chemin vers le noeud cible et le chemin total parcouru

    def _reconstruct_path(self, target_coords):
        """
        Reconstruit le chemin à partir des coordonnées cibles en utilisant le dictionnaire des parents.
        :param target_coords: Coordonnées cibles (x, y, z)
        :return: Chemin complet sous forme de liste de coordonnées
        """
        path = []
        current_coords = target_coords
        while current_coords is not None:
            path.append(current_coords)  # Ajoute le noeud au chemin
            current_coords = self.parent[current_coords]  # Passe au parent
        path.reverse()  # Inverse le chemin pour obtenir l'ordre correct
        return path  # Retourne le chemin complet

