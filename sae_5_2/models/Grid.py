from sae_5_2.models.Node import Node

class Grid:
    """
    Classe représentant une grille contenant des noeuds hexagonaux.
    La grille est générée en utilisant des coordonnées cubiques (pour les déplacements qui seront fait par les algorithmes).
    """

    def __init__(self, rows, cols):
        """
        Constructeur de la classe Grid qui prend en paramètre le nombre de lignes et de colonnes.
        """
        self.rows = rows  
        self.cols = cols  
        self.nodes = {}    # Dictionnaire pour stocker les nœuds
        self.directions = {
            "N": (0, -1, +1),  # Nord
            "NE": (+1, -1, 0),  # Nord-Est
            "SE": (+1, 0, -1),  # Sud-Est
            "S": (0, +1, -1),  # Sud
            "SW": (-1, +1, 0),  # Sud-Ouest
            "NW": (-1, 0, +1)  # Nord-Ouest
        }
        self._create_grid()

    def _create_grid(self):
        """
        Méthode qui permet d'ajouter les noeuds de la grille en les créant et en les connectant entre eux.
        Place l'origine (0, 0, 0) en bas à gauche.
        """
        offset = 0
        for col in range(self.cols):

            for row in range(self.rows):
                # Adjust horizontal offset for columns based on rows
                x = col
                y = row - offset
                z = -x - y

                # Create the node
                self.nodes[(x, y, z)] = Node(x, y, z)

            if col % 2 == 1:
                offset += 1



        # Connect neighbors
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
        """
        Affiche la grille en ligne de commande avec les coordonnées cubiques de chaque nœud.
        """
        print("Grille des noeuds (coordonnées x, y, z) :")
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