from sae_5_2.models.Grid import Grid
from sae_5_2.models.ParcoursProfondeur import ParcoursProfondeur


class ComposantesConnexes:

    def __init__(self, grid):
        self.grid = grid

    def find_connected_components(self):
        """
        Trouve les composantes connexes de la grille.
        Une composante connexe est un ensemble de nœuds reliés directement ou indirectement entre eux
        :return: Set des composantes connexes (chaque composante est une liste de nœuds).
        """
        visited = set()  # Ensemble des nœuds visités
        components = []  # Liste des composantes connexes
        dfs = ParcoursProfondeur(self.grid)

        for node_coords, node in self.grid.nodes.items():
            if node_coords not in visited and node.active:
                _, component = dfs.parcours(node_coords, None)
                if component:
                    visited.update(component)
                    component_nodes = [self.grid.nodes[coords] for coords in component]
                    print(visited, component)
                    components.append(component_nodes)

        return components
