import Grid as Grid

class DynamicProgrammingStableMaximumSetSolver:
    def __init__(self, grid):
        """Initialise le solveur avec une instance de Grid."""
        self.grid = grid
        self.max_set = []

    def is_stable(self, node, included_nodes):
        """Vérifie si le nœud peut être ajouté à l'ensemble courant sans violer la stabilité."""
        for neighbor in node.voisins.values():
            if neighbor in included_nodes:
                return False
        return True

    def find_stable_maximum_set(self):
        """Trouve un ensemble stable maximum dans la grille en utilisant la programmation dynamique."""
        nodes = list(self.grid.nodes.values())
        n = len(nodes)

        # Dictionnaire pour stocker les résultats des sous-problèmes
        dp = [0] * (n + 1)
        included = [set() for _ in range(n + 1)]

        for i in range(n):
            node = nodes[i]
            # Vérifier si le nœud peut être inclus
            for j in range(i):
                if self.is_stable(node, included[j]):
                    if dp[j] + 1 > dp[i + 1]:
                        dp[i + 1] = dp[j] + 1
                        included[i + 1] = included[j].copy()
                        included[i + 1].add(node)

        # Trouver l'ensemble stable maximum
        max_size = max(dp)
        self.max_set = included[dp.index(max_size)]
        return self.max_set

def test_dynamic_programming_stable_maximum_set_solver():
    """Fonction de tests pour DynamicProgrammingStableMaximumSetSolver."""
    # Créer une grille de test
    grid = Grid.Grid(rows=10, cols=10)  # Exemple d'une petite grille 5x5

    # Créer un solveur pour l'ensemble stable maximum
    solver = DynamicProgrammingStableMaximumSetSolver(grid)

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
test_dynamic_programming_stable_maximum_set_solver()