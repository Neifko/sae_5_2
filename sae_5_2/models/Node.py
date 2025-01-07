class Node:
    """
    Classe représentant un nœud hexagonal dans un graphe.
    Chaque nœud a 6 voisins.
    """
    def __init__(self, x, y, z):
        self.x = x  
        self.y = y  
        self.z = z  

        self.voisins = {}       # Dictionnaire des voisins
        self.valeur = None      # Valeur ou propriété du nœud (facultatif)
        self.active = True

    def __repr__(self):
        return f"HexNode(x={self.x}, y={self.y}, z={self.z}, valeur={self.valeur})"
