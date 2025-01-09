from sae_5_2.models.Grid import Grid
from sae_5_2.models.ParcoursProfondeur import ParcoursProfondeur


def find_connected_components(grid):
    """
    Trouve les composantes connexes de la grille.
    Une composante connexe est un ensemble de nœuds reliés directement ou indirectement entre eux
    :param grid: Instance de Grid
    :return: Liste des composantes connexes (chaque composante est une liste de nœuds)
    """
    visited = set()  # Ensemble des nœuds visités
    components = []  # Liste des composantes connexes

    def parcours(node, component):
        """Parcours en profondeur pour explorer une composante connexe."""
        dfs = ParcoursProfondeur(grid)
        path, total_path = dfs.parcours((node.x, node.y, node.z), None)
        for coords in total_path:
            n = grid.get_node(*coords)
            if n and n.active:
                visited.add(n)
                component.append(coords)

    # Parcourir tous les nœuds de la grille
    for node in grid.nodes.values():
        if node not in visited and node.active:
            component = []  # Nouvelle composante connexe
            parcours(node, component)
            components.append(component)

    return components

# Exemple d'utilisation
if __name__ == "__main__":
    grid = Grid(4, 4)

    # Désactivation de quelques nœuds pour avoir plusieurs composantes connexes
    grid.get_node(1, 0, -1).active = False
    grid.get_node(2, 1, -3).active = False
    grid.get_node(2, 0, -2).active = False
    grid.get_node(3, 1, -4).active = False
    grid.get_node(0, 2, -2).active = False
    grid.get_node(1, 2, -3).active = False

    connected_components = find_connected_components(grid)

    print("Composantes connexes :")
    for i, component in enumerate(connected_components):
        print(f"Composante {i + 1}: {component}")