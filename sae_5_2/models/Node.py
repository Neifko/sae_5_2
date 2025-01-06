
class Node:
    def __init__(self):
        self.voisins = {
            "N":None,
            "NE":None,
            "SE":None,
            "S":None,
            "SW":None,
            "NW":None
        }
        self.couleur = None
        self.valeur = 1

    def __repr__(self):
        return f"Node(valeur={self.valeur}, couleur={self.couleur})"

