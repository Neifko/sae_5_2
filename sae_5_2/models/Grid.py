from sae_5_2.models.Node import Node

class Grid:
    """
    Classe représentant une grille hexagonale et son graphe.
    La grille est générée en utilisant des coordonnées cubiques.
    """
    def __init__(self, rows, cols):
        """
        Constructeur de la classe Grid qui prend en paramètre le nombre de lignes et de colonnes.
        """
        self.rows = rows  # Nombre de lignes dans la grille
        self.cols = cols  # Nombre de colonnes dans la grille
        self.nodes = {}    # Dictionnaire pour stocker les nœuds
        self.directions = {
            "N": (+1, -1, 0),     # Nord
            "NE": (+1, 0, -1),    # Nord-Est
            "SE": (0, +1, -1),    # Sud-Est
            "S": (-1, +1, 0),     # Sud
            "SW": (-1, 0, +1),    # Sud-Ouest
            "NW": (0, -1, +1)     # Nord-Ouest
        }
        self._create_grid()

    def _create_grid(self):
        """
        Génère une grille hexagonale avec une disposition en nid d'abeilles
        et une origine au centre de la grille.
        """
        center_row = self.rows // 2
        center_col = self.cols // 2

        for row in range(-center_row, center_row + 1):
            for col in range(-center_col, center_col + 1):
                # Décalage horizontal pour les colonnes en fonction des lignes
                x = col - (row // 2)
                z = row
                y = -x - z

                # Création du nœud
                self.nodes[(x, y, z)] = Node(x, y, z)

        # Connexions des voisins
        for (x, y, z), node in self.nodes.items():
            for direction, (dx, dy, dz) in self.directions.items():
                neighbor_coords = (x + dx, y + dy, z + dz)
                if neighbor_coords in self.nodes:
                    node.voisins[direction] = self.nodes[neighbor_coords]

    def get_node(self, x, y, z):
        """
        Retourne le noeud aux coordonnées spécifiées.
        """
        return self.nodes.get((x, y, z))

    def get_neighbors(self, x, y, z):
        """
        Retourne les voisins d'un noeud donné dans toutes les directions possibles.
        """
        neighbors = {}
        for direction, (dx, dy, dz) in self.directions.items():
            neighbor_coords = (x + dx, y + dy, z + dz)
            neighbors[direction] = self.get_node(*neighbor_coords)
        return neighbors

    def display_grid(self):
        for y in range(-self.rows // 2, self.rows // 2 + 1):
            line = ""
            for x in range(-self.cols // 2, self.cols // 2 + 1):
                z = -x - y
                if (x, y, z) in self.nodes:
                    if y % 2 == 0:
                        line += f" ({x},{y},{z}) "
                    else:
                        line += f"   ({x},{y},{z}) "
            print(line)

    def display_neighbors(self, x, y, z):
        """Affiche les voisins d'un nœud spécifique avec leurs directions cardinales"""
        node = self.get_node(x, y, z)
        if not node:
            print(f"Pas de nœud trouvé aux coordonnées ({x}, {y}, {z}).")
            return

        print(f"\nNœud ({x}, {y}, {z}): {node}")
        print("Voisins :")
        for direction, neighbor in node.voisins.items():
            print(f"  Direction {direction}: {neighbor}")

    def __repr__(self):
        return f"Grid(rows={self.rows}, cols={self.cols}, nodes={self.nodes})"