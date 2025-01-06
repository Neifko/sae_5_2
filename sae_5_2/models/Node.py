class Node:
    """
    Classe représentant un nœud hexagonal dans un graphe.
    Chaque nœud a 6 voisins.
    """
    def __init__(self, x, y, z):
        self.x = x  # Coordonnée x (cubique)
        self.y = y  # Coordonnée y (cubique)
        self.z = z  # Coordonnée z (cubique)
        self.voisins = {}  # Dictionnaire des voisins
        self.valeur = 1  # Valeur ou propriété du nœud (facultatif)

    def __repr__(self):
        return f"HexNode(x={self.x}, y={self.y}, z={self.z}, valeur={self.valeur})"
