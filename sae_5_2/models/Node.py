class Node:
    """
    Classe représentant un nœud hexagonal dans un graphe.
    Chaque nœud a 6 voisins.
    """
    def __init__(self, x:int, y:int, z:int):
        """
        Constructeur de la classe Node qui prend en paramètre les coordonnées cubique du noeud.
        """
        self.x = x              
        self.y = y              
        self.z = z              
        self.voisins = {}           # Dictionnaire des voisins
        self.valeur = None          # Valeur ou propriété du nœud (facultatif)
        self.active = True          # Indicateur pour dire si le noeud est un obstacle ou non (si False, il s'agit d'un obstacle)

    def __repr__(self):
        return f"HexNode(x={self.x}, y={self.y}, z={self.z}, valeur={self.valeur})"
