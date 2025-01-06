from sae_5_2.models.Node import Node


class Grid:
    """
    Classe représentant une grille contenant des noeuds hexagonaux.
    La grille est générée en utilisant des coordonnées cubiques (pour les déplacements qui seront fait par les algorithmes).
    """
    def __init__(self, rows:int, cols:int):
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
        Méthode qui permet d'ajouter les noeuds de la grille en les créants et en les connectants entre eux.
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

    def display_grid(self):
        """
        Affiche la grille en ligne de commande avec les coordonnées cubiques de chaque nœud.  
        """
        for y in range(self.rows):
            line = ""
            for x in range(self.cols):
                # Décalage des lignes impaires pour afficher les hexagones correctement
                if y % 2 == 0:
                    line += f" ({x},{y},{-x-y}) "
                else:
                    line += f"   ({x},{y},{-x-y}) "
            print(line)

    def display_neighbors(self, x:int, y:int, z:int):
        """
        Affiche les voisins d'un nœud en précisant ses coordonées (x, y, z).
        """
        node = self.get_node(x, y, z)
        if not node:
            print(f"Pas de nœud trouvé aux coordonnées ({x}, {y}, {z}).")
            return

        print(f"\nNœud ({x}, {y}, {z}): {node}")
        print("Voisins :")
        for direction, neighbor in node.voisins.items():
            print(f"  Direction {direction}: {neighbor}")

    def get_node(self, x:int, y:int, z:int):
        """
        Retourne le nœud aux coordonnées (x, y, z).
        """
        return self.nodes.get((x, y, z))