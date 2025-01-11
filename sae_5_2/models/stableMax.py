import sae_5_2.models.Grid as Grid

class StableMaximumSetSolver:
    def __init__(self, grid):
        """Initialise le solveur avec une instance de Grid."""
        self.grid = grid
        self.max_set = []
        self.current_set = []

    def is_stable(self, node):
        """Vérifie si le nœud peut être ajouté à l'ensemble courant sans violer la stabilité."""
        for neighbor in node.voisins.values():
            if neighbor in self.current_set:
                return False
        return True

    def backtrack(self, nodes):
        """Fonction de backtracking pour explorer les nœuds."""
        if not nodes:
            if len(self.current_set) > len(self.max_set):
                self.max_set = self.current_set[:]
            return

        # Prendre le premier nœud
        node = nodes[0]
        remaining_nodes = nodes[1:]

        # Option 1: Ne pas inclure le nœud
        self.backtrack(remaining_nodes)

        # Option 2: Inclure le nœud si stable
        if self.is_stable(node):
            self.current_set.append(node)
            self.backtrack(remaining_nodes)
            self.current_set.pop()  # Retirer le nœud après exploration

    def find_stable_maximum_set(self):
        """Trouve un ensemble stable maximum dans la grille."""
        self.backtrack(list(self.grid.nodes.values()))
        return self.max_set 
    
    
def test_stable_maximum_set_solver():
    """Fonction de tests pour StableMaximumSetSolver."""
    # Créer une grille de test
    grid = Grid.Grid(rows=3, cols=3)  # Exemple d'une petite grille 3x3

    # Créer un solveur pour l'ensemble stable maximum
    solver = StableMaximumSetSolver(grid)

    # Trouver l'ensemble stable maximum
    max_stable_set = solver.find_stable_maximum_set()

    # Afficher l'ensemble stable maximum trouvé
    print("Ensemble stable maximum trouvé:", max_stable_set)

    # Vérifier que l'ensemble est stable
    stable = True
    for node in max_stable_set:
        for neighbor in node.voisins.values():
            if neighbor in max_stable_set:
                stable = False
                break
        if not stable:
            break

    # Afficher le résultat du test
    if stable:
        print("Test réussi: L'ensemble est stable.")
    else:
        print("Test échoué: L'ensemble n'est pas stable.")

# Appeler la fonction de tests
# test_stable_maximum_set_solver()