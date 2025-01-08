from models.Node import Node

class Grid:
    """
    Classe représentant une grille contenant des noeuds hexagonaux.
    La grille est générée en utilisant des coordonnées cubiques (pour les déplacements qui seront fait par les algorithmes).
    """
    def __init__(self, rows: int, cols: int):
        """
        Constructeur de la classe Grid qui prend en paramètre le nombre de lignes et de colonnes.
        """
        self.rows = rows  
        self.cols = cols  
        self.nodes = {}           # Dictionnaire pour stocker les nœuds
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
        Méthode qui permet d'ajouter les noeuds de la grille en les créant et en les connectant entre eux.
        """
        for x in range(self.cols):
            for y in range(self.rows):
                z = -x - y  # Calcul de z pour respecter x + y + z = 0
                self.nodes[(x, y, z)] = Node(x, y, z)

        # Connecter les voisins pour chaque nœud
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
        for y in range(self.rows):
            for x in range(self.cols):
                z = -x - y
                node = self.get_node(x, y, z)
                if node:
                    print(f"({node.x}, {node.y}, {node.z})", end=" ")
                else:
                    print("(None)", end=" ")
            print()  # Nouvelle ligne pour chaque rangée

    def __repr__(self):
        return f"Grid(rows={self.rows}, cols={self.cols}, nodes={self.nodes})"