class Chainon :
    """
    Élément de la file (chaîné).
    """
    def __init__(self, valeur, suivant=None) :
        self.valeur = valeur
        self.suivant = suivant


class File :
    """
    Implémentation d'une file (FIFO).
    """
    def __init__(self) :
        self.tete = None    # Premier élément de la file
        self.queue = None   # Dernier élément de la file

    def est_vide(self) :
        """Vérifie si la file est vide."""
        return self.tete is None

    def enfiler(self, v) :
        """Ajoute un élément à la fin de la file."""
        # Créer un nouveau chainon avec la valeur donnée
        nouveau_chainon = Chainon(v)
        
        # Si la file est vide, le nouvel élément est à la fois la tête et la queue
        if self.est_vide() :
            self.tete = self.queue = nouveau_chainon
        else : 
            # Sinon, on ajoute à la fin de la file
            self.queue.suivant = nouveau_chainon
            self.queue = nouveau_chainon

    def defiler(self) :
        """Retire et renvoie l'élément en tête de la file."""
        if self.est_vide():
            raise IndexError("La file est vide, impossible de défiler.")
        
        # On récupère la valeur à la tête de la file
        valeur = self.tete.valeur
        
        # Déplace la tête de la file vers le suivant
        self.tete = self.tete.suivant
        
        # Si la file devient vide après le défilage, on met la queue à None
        if self.tete is None:
            self.queue = None

        return valeur
