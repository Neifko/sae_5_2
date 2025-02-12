import math
import random
import customtkinter as ctk

from sae_5_2.models.Grid import Grid

from sae_5_2.controllers.ProfondeurController import ProfondeurController
from sae_5_2.controllers.DijkstraController import DijkstraController
from sae_5_2.controllers.BellmanFordController import BellmanFordController
from sae_5_2.controllers.AEtoileController  import AEtoileController
from sae_5_2.controllers.algoBFSController import algoBFSController
from sae_5_2.controllers.stableMaxController import stableMaxController

class MainController:
    def __init__(self, view):
        '''
        Initialise le contrôleur principal avec la vue passée en paramètre
        '''
        self.main_view = view
        self.rows = 10
        self.cols = 10
        self.hex_size = 30  # Taille initiale des hexagones

        self.grid = self.generate_grid(self.rows, self.cols)

        ### A METTRE A JOUR ###
        self.profondeur_controller = ProfondeurController()
        self.dijkstra_controller = DijkstraController()
        self.aetoile_controller = AEtoileController()
        self.bellman_ford_controller = BellmanFordController()
        self.algoBFSController = algoBFSController()
        self.stableMax = stableMaxController()

        # Variable pour suivre la couleur actuelle
        self.current_color = None  # Couleur transparente par défaut

        self.colors = ["Black", "White", "Blue", "Green", "Yellow"]

        # Forcer la mise à jour de la taille du canvas
        self.main_view.main_frame.hex_canvas.update_idletasks()

        # Variables pour suivre l'état des boutons
        self.depart_mode = False
        self.objectif_mode = False
        # Variable pour suivre si un chemin a été dessiné
        self.path_drawn = False

        # Variables pour suivre les hexagones de départ et d'objectif
        self.depart_hex = None
        self.objectif_hex = None

        # Lier les événements de clic sur le canvas
        self.main_view.main_frame.hex_canvas.bind("<Button-1>", self.on_canvas_click)
        self.main_view.main_frame.hex_canvas.bind("<B1-Motion>", self.on_canvas_motion)
        self.main_view.main_frame.hex_canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

        # Dictionnaire pour stocker les hexagones dessinés
        self.hexagons = {}
        # Dictionnaire pour stocker les couleurs précédentes des hexagones
        self.current_hex_colors = {}
        self.hex_id_get_coords = {}
        self.incoming_arrows = {}
        # Liste pour stocker les résultats (bouton effacer resultats)
        self.results = []

        self.arrow_ids = {}
        self.circle_ids = {}
        self.liste_stable = []

        # Variable pour suivre l'état du parcours en cours
        self.pathfinding_in_progress = False
        self.stop_drawing = False  # Variable pour arrêter le dessin


    ########################################## Fonctions pour la grille#################################################
    ####################################################################################################################
    
    def generate_grid(self, rows, cols):
        '''
        Génère une grille de taille rows x cols
        '''
        return Grid(rows, cols)

    def draw_hex_grid(self, rows, cols, size):
        '''
        Dessine une grille d'hexagones de taille spécifiée 
        '''
        font_size = max(8, int(size * 0.4))
        font = ("Arial", font_size)

        # Calculer les positions des hexagones en fonction de l'hexagone (0, 0, 0)
        positions = {}
        for (x, y, z), node in self.grid.nodes.items():
            if (x, y, z) not in positions:
                positions[(x, y, z)] = (0, 0)  # Position initiale

            for direction, neighbor in node.voisins.items():
                nx, ny, nz = neighbor.x, neighbor.y, neighbor.z
                if (nx, ny, nz) not in positions:
                    positions[(nx, ny, nz)] = (0, 0)  # Position initiale

                dx, dy = self.get_direction_offset(direction, size)
                positions[(nx, ny, nz)] = (
                    positions[(x, y, z)][0] + dx,
                    positions[(x, y, z)][1] + dy
                )

        # Ajuster les positions pour commencer en haut à gauche
        start_offset_x = size  # Décalage initial pour éviter de dessiner en dehors du canvas
        start_offset_y = size
        for key in positions:
            positions[key] = (
                positions[key][0] + start_offset_x,
                positions[key][1] + start_offset_y
            )

        # Dessiner les hexagones
        for (x, y, z), (px, py) in positions.items():
            self.draw_hexagon(px, py, size, "white", (x, y, z))

    def draw_grid(self):
        '''
        Dessine la grille avec les nouvelles dimensions spécifiées dans les champs de saisie
        '''
        self.clear_hexagons()
        rows = int(self.main_view.left_frame.rows_entry.get())
        cols = int(self.main_view.left_frame.cols_entry.get())

        # Recréer la grille avec les nouvelles dimensions
        self.grid = Grid(rows, cols)
        self.draw_hex_grid(rows, cols, self.hex_size)

        # Restaurer les cases de départ et d'objectif
        self.restore_special_hexagons()

    def draw_max_grid(self):
        '''
        Dessine la grille maximale qui peut tenir dans la zone de dessin en focntion de la taille des hexagones et la taille de la fenetre
        '''
        self.clear_hexagons()
        canvas_width = self.main_view.main_frame.hex_canvas.winfo_width()
        canvas_height = self.main_view.main_frame.hex_canvas.winfo_height()

        # Calcul du nombre maximum de colonnes et de rangées qui peuvent tenir dans la zone de dessin
        cols = int(canvas_width / (1.5 * self.hex_size))
        rows = int(canvas_height / (math.sqrt(3) * self.hex_size))

        # Mettre à jour les champs de saisie
        self.main_view.left_frame.rows_entry.delete(0, 'end')
        self.main_view.left_frame.rows_entry.insert(0, str(rows))
        self.main_view.left_frame.cols_entry.delete(0, 'end')
        self.main_view.left_frame.cols_entry.insert(0, str(cols))

        # Recréer la grille avec les nouvelles dimensions
        self.grid = Grid(rows, cols)
        self.draw_hex_grid(rows, cols, self.hex_size)

        # Restaurer les cases de départ et d'objectif
        self.restore_special_hexagons()
    
    def update_hex_size(self, size):
        '''
        Met à jour la taille des hexagones et redessine la grille
        '''
        self.hex_size = int(size)
        if self.grid:
            self.clear_hexagons()
            self.draw_hex_grid(self.grid.rows, self.grid.cols,
                               self.hex_size)
            # Restaurer les cases de départ et d'objectif
            self.restore_special_hexagons()

    def get_direction_offset(self, direction, size):
        '''
        Calcule le décalage en fonction de la direction et de la taille des hexagones
        '''
        if direction == "N":
            return (0, -math.sqrt(3) * size)
        elif direction == "NE":
            return (1.5 * size, -math.sqrt(3) / 2 * size)
        elif direction == "SE":
            return (1.5 * size, math.sqrt(3) / 2 * size)
        elif direction == "S":
            return (0, math.sqrt(3) * size)
        elif direction == "SW":
            return (-1.5 * size, math.sqrt(3) / 2 * size)
        elif direction == "NW":
            return (-1.5 * size, -math.sqrt(3) / 2 * size)
        else:
            return (0, 0)

    def clear_grid(self):
        '''
        Réinitialise la grille en supprimant tous les hexagones
        '''
        self.grid = Grid(0, 0)  # Réinitialiser la grille

    def axial_to_cube(self, q, r):
        '''
        Convertit les coordonnées axiales en coordonnées cubiques
        '''
        x = q
        z = r
        y = -x - z
        return (x, y, z)
    ####################################################################################################################
    ####################################################################################################################

    
    ############################ fonctions pour les algorithmes ########################################################
    ####################################################################################################################
    def call_profondeur(self):
        '''
        Exécute l'algorithme de recherche en profondeur (Depth-First Search, DFS).
        Cet algorithme explore aussi loin que possible le long de chaque branche avant de revenir en arrière.
        '''
        if self.path_drawn:
            self.stop_drawing = False
            self.clear_results()

        if not self.depart_hex or not self.objectif_hex:
            print("Veuillez définir une case de départ et une case d'objectif.")
            return

        # pour mettre à jour l'interface avec les bons résultats des variables
        self.reset_interface_state()

        depart_cubique = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
        arrive_cubique = self.hex_id_get_coords[self.hexagons[self.objectif_hex]]

        print(f"Coordonnées cubiques de départ: {depart_cubique}")
        print(f"Coordonnées cubiques d'objectif: {arrive_cubique}")

        self.profondeur_controller.set_grid(self.grid)
        path_to_target, total_path = self.profondeur_controller.execute(depart_cubique, arrive_cubique)

        if path_to_target:
            print(f"Un chemin existe entre {depart_cubique} et {arrive_cubique}.")
            print(f"Chemin vers la cible : {path_to_target}")
        else:
            print(f"Aucun chemin trouvé entre {depart_cubique} et {arrive_cubique}.")

        print(f"Chemin total parcouru : {total_path}")
        total_path = [total_path]
        # Dessiner les chemins
        self.draw_path_with_circles(path_to_target, total_path)

    def call_dijkstra(self):
        '''
        Exécute l'algorithme de Dijkstra.
        Cet algorithme trouve le chemin le plus court entre les nœuds dans un graphe, ce qui peut représenter, par exemple, les routes.
        '''
        if self.path_drawn:
            self.clear_results()

        if not self.depart_hex or not self.objectif_hex:
            print("Veuillez définir une case de départ et une case d'objectif.")
            return

        self.reset_interface_state()

        depart_cubique = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
        arrive_cubique = self.hex_id_get_coords[self.hexagons[self.objectif_hex]]

        print(f"Coordonnées cubiques de départ: {depart_cubique}")
        print(f"Coordonnées cubiques d'objectif: {arrive_cubique}")

        self.dijkstra_controller.set_grid(self.grid)
        path_to_target, all_path = self.dijkstra_controller.execute(depart_cubique, arrive_cubique)

        if path_to_target:
            print(f"Un chemin existe entre {depart_cubique} et {arrive_cubique}.")
            print(f"Chemin vers la cible : {path_to_target}")
        else:
            print(f"Aucun chemin trouvé entre {depart_cubique} et {arrive_cubique}.")

        for lst in all_path:
            print(f"Chemin total parcouru : {lst}")

        # Dessiner les chemins
        self.draw_path_with_circles(path_to_target, all_path)

    def call_aetoile(self):
        """
        Exécute l'algorithme A* (A-star).
        Cet algorithme trouve le chemin le plus court en utilisant une heuristique pour estimer le coût du chemin le plus court.
        """
        if self.path_drawn:
            self.clear_results()

        if not self.depart_hex or not self.objectif_hex:
            print("Veuillez définir une case de départ et une case d'objectif.")
            return

        self.reset_interface_state()

        depart_cubique = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
        arrive_cubique = self.hex_id_get_coords[self.hexagons[self.objectif_hex]]

        print(f"Coordonnées cubiques de départ: {depart_cubique}")
        print(f"Coordonnées cubiques d'objectif: {arrive_cubique}")

        self.aetoile_controller.set_grid(self.grid)
        path_to_target, total_path = self.aetoile_controller.execute(depart_cubique, arrive_cubique)

        if path_to_target:
            print(f"Un chemin existe entre {depart_cubique} et {arrive_cubique}.")
            print(f"Chemin vers la cible : {path_to_target}")
        else:
            print(f"Aucun chemin trouvé entre {depart_cubique} et {arrive_cubique}.")

        print(f"Chemin total parcouru : {total_path}")
        total_path = [total_path]

        # Dessiner les chemins
        self.draw_path_with_circles(path_to_target, total_path)

    def call_bellmanford(self):
        """
        Exécute l'algorithme de Bellman-Ford.
        Cet algorithme trouve le chemin le plus court à partir d'un nœud source vers tous les autres nœuds dans un graphe pondéré.
        """
        if self.path_drawn:
            self.clear_results()

        if not self.depart_hex or not self.objectif_hex:
            print("Veuillez définir une case de départ et une case d'objectif.")
            return

        self.reset_interface_state()

        depart_cubique = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
        arrive_cubique = self.hex_id_get_coords[self.hexagons[self.objectif_hex]]

        print(f"Coordonnées cubiques de départ: {depart_cubique}")
        print(f"Coordonnées cubiques d'objectif: {arrive_cubique}")

        self.bellman_ford_controller.set_grid(self.grid)
        path_to_target, total_path = self.bellman_ford_controller.execute(depart_cubique, arrive_cubique)

        if path_to_target:
            print(f"Un chemin existe entre {depart_cubique} et {arrive_cubique}.")
            print(f"Chemin vers la cible : {path_to_target}")
        else:
            print(f"Aucun chemin trouvé entre {depart_cubique} et {arrive_cubique}.")

        print(f"Chemin total parcouru : {total_path}")
        total_path = [total_path]

        # Dessiner les chemins
        self.draw_path_with_circles(path_to_target, total_path)

    def call_largeur(self):
        '''
        Exécute l'algorithme de parcours en largeur (Breadth-First Search, BFS).
        Cet algorithme explore tous les nœuds voisins à la profondeur présente avant de passer à la profondeur suivante.
        '''
        if self.path_drawn:
            self.clear_results()

        if not self.depart_hex or not self.objectif_hex:
            print("Veuillez définir une case de départ et une case d'objectif.")
            return

        self.reset_interface_state()

        depart_cubique = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
        arrive_cubique = self.hex_id_get_coords[self.hexagons[self.objectif_hex]]

        print(f"Coordonnées cubiques de départ: {depart_cubique}")
        print(f"Coordonnées cubiques d'objectif: {arrive_cubique}")

        self.algoBFSController.set_grid(self.grid)
        path_to_target, total_path = self.algoBFSController.run_bfs(depart_cubique, arrive_cubique)

        path = [(node.x, node.y, node.z) for node in path_to_target] # Convertir les nœuds en coordonnées cubiques
        total_path = [(node.x, node.y, node.z) for node in total_path]  # Convertir les nœuds en coordonnées cubiques

        if path_to_target:
            print(f"Un chemin existe entre {depart_cubique} et {arrive_cubique}.")
            print(f"Chemin vers la cible : {path}")
        else:
            print(f"Aucun chemin trouvé entre {depart_cubique} et {arrive_cubique}.")

        print(f"Chemin total parcouru : {total_path}")
        total_path = [total_path]

        # Dessiner les chemins
        self.draw_path_with_circles(path, total_path)

    def call_stableMax(self):
        '''
        Exécute l'algorithme de stabilité maximale.
        Cet algorithme identifie les nœuds les plus stables dans un graphe, souvent utilisé pour détecter les points critiques ou les centres de clusters.
        '''
        if self.path_drawn:
            self.clear_results()

        # self.reset_interface_state()

        self.stableMax.set_grid(self.grid)
        stableMax = self.stableMax.run_stableMax()
        for noeud in stableMax:
            hex_id = [key for key, value in self.hex_id_get_coords.items() if value == (noeud.x, noeud.y, noeud.z)][0]
            self.main_view.main_frame.hex_canvas.itemconfig(hex_id, fill="orange")
            self.liste_stable.append(hex_id)


    ####################################################################################################################
    ####################################################################################################################

    ###################################### Fonctions pour les cases et le dessin #######################################
    ####################################################################################################################

    def set_depart(self):
        '''
        Active le mode de sélection de la case de départ
        '''
        self.depart_mode = True
        self.objectif_mode = False
        print("Mode Départ activé")

    def set_objectif(self):
        '''
        Active le mode de sélection de la case d'objectif
        '''
        self.objectif_mode = True
        self.depart_mode = False
        print("Mode Objectif activé")

    def set_color(self, color):
        '''
        Définit la couleur actuelle
        '''
        self.current_color = color
        self.depart_mode = False
        self.objectif_mode = False
        print(f"Color set to {color}")

    def get_canvas_center(self):
        '''
        Obtient le centre du canvas
        '''
        canvas_width = self.main_view.main_frame.hex_canvas.winfo_width()
        canvas_height = self.main_view.main_frame.hex_canvas.winfo_height()
        return canvas_width / 2, canvas_height / 2

    def random_case_colors(self):
        '''
        Attribue des couleurs aléatoires à tous les hexagones de la grille actuelle
        '''
        # Parcourir tous les hexagones et leur attribuer une couleur aléatoire
        for (hex_x, hex_y), hex_id in self.hexagons.items():
            # Ne pas changer la couleur des cases de départ et d'objectif
            if (hex_x, hex_y) == self.depart_hex or (hex_x, hex_y) == self.objectif_hex:
                continue

            # Choisir une couleur aléatoire parmi les couleurs disponibles
            color = random.choice(self.colors)
            self.main_view.main_frame.hex_canvas.itemconfig(hex_id, fill=color)

            # Désactiver les cases noires
            if color == "Black":
                if self is not None:
                    grid = self.grid
                    node_modif = grid.get_node(*self.hex_id_get_coords[self.hexagons[(hex_x, hex_y)]])
                    node_modif.active = False
                    print(f"Node ({hex_x}, {hex_y}) désactivé")
            else:
                if self is not None:
                    grid = self.grid
                    node_modif = grid.get_node(*self.hex_id_get_coords[self.hexagons[(hex_x, hex_y)]])
                    node_modif.active = True
                    print(f"Node ({hex_x}, {hex_y}) activé")

            # Mettre à jour la valeur en fonction de la couleur
            self.update_node_value(node_modif, color)

    def draw_hexagon(self, x, y, size, color, coord=None, font_size=12):
        '''
        Dessine un hexagone à la position spécifiée
        '''
        points = []

        for i in range(6):
            angle = math.radians(60 * i)
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append(px)
            points.append(py)
        # TODO : verifier ce dessin
        hex_id = self.main_view.main_frame.hex_canvas.create_polygon(points, outline="black", fill=color, width=1)

        # Stocker l'hexagone dessiné avec ses coordonnées
        self.hexagons[(x, y)] = hex_id

        if coord is not None:
            coord_str = f"({coord[0]},{coord[1]},{coord[2]})"
            self.hex_id_get_coords[hex_id] = coord
        else:
            coord_str = ""

        label = coord_str if self.main_view.left_frame.show_coords_switch.get() else None

        if label:
            # TODO : verifier
            self.main_view.main_frame.hex_canvas.create_text(x, y, text=label, fill="black", font=("Arial", font_size))

    def on_canvas_click(self, event):
        '''
        Gère les événements de clic sur le canvas
        '''
        x, y = event.x, event.y
        # Vérifier si un hexagone est cliqué
        for (hex_x, hex_y), hex_id in self.hexagons.items():
            if self.main_view.main_frame.hex_canvas.find_closest(x, y)[0] == hex_id:
                if self.depart_mode:
                    if (hex_x, hex_y) == self.objectif_hex:
                        print("Vous ne pouvez pas placer la case de départ sur la case d'objectif.")
                        return
                    if self.depart_hex:
                        # Réinitialiser l'ancienne case de départ
                        old_hex_x, old_hex_y = self.depart_hex
                        current_color = self.current_hex_colors.get((old_hex_x, old_hex_y), "")
                        self.main_view.main_frame.hex_canvas.itemconfig(self.hexagons[(old_hex_x, old_hex_y)],
                                                                        fill=current_color)
                    self.depart_hex = (hex_x, hex_y)
                    self.current_hex_colors[(hex_x, hex_y)] = self.main_view.main_frame.hex_canvas.itemcget(hex_id,
                                                                                                            "fill")
                    self.main_view.main_frame.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill="pink")
                    self.depart_cube = self.axial_to_cube(hex_x, hex_y)  # Stocker les coordonnées cubiques
                elif self.objectif_mode:
                    if (hex_x, hex_y) == self.depart_hex:
                        print("Vous ne pouvez pas placer la case d'objectif sur la case de départ.")
                        return
                    if self.objectif_hex:
                        # Réinitialiser l'ancienne case d'objectif
                        old_hex_x, old_hex_y = self.objectif_hex
                        current_color = self.current_hex_colors.get((old_hex_x, old_hex_y), "")
                        self.main_view.main_frame.hex_canvas.itemconfig(self.hexagons[(old_hex_x, old_hex_y)],
                                                                        fill=current_color)
                    self.objectif_hex = (hex_x, hex_y)
                    self.current_hex_colors[(hex_x, hex_y)] = self.main_view.main_frame.hex_canvas.itemcget(hex_id,
                                                                                                            "fill")
                    self.main_view.main_frame.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill="red")
                    self.objectif_cube = self.axial_to_cube(hex_x, hex_y)  # Stocker les coordonnées cubiques
                else:
                    if (hex_x, hex_y) == self.depart_hex or (hex_x, hex_y) == self.objectif_hex:
                        continue  # Ne pas changer la couleur de la case départ ou objectif
                    self.current_hex_colors[(hex_x, hex_y)] = self.current_color
                    self.main_view.main_frame.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)],
                                                                    fill=self.current_color)
                    print(self.current_color)

                    if self is not None:
                        grid = self.grid
                        node_modif = grid.get_node(*self.hex_id_get_coords[self.hexagons[(hex_x, hex_y)]])
                        if self.current_color == "Black":
                            node_modif.active = False
                            print("Node désactivé")
                        else:
                            node_modif.active = True
                            print("Pas désactivé")

                        # Mettre à jour la valeur en fonction de la couleur
                        self.update_node_value(node_modif, self.current_color)

                break

    def on_canvas_motion(self, event):
        '''
        Gère les événements de mouvement de la souris sur le canvas, pour dessiner des lignes en restant appuyé sur le clic gauche
        '''
        if not self.depart_mode and not self.objectif_mode:
            x, y = event.x, event.y
            # Vérifier si un hexagone est cliqué
            for (hex_x, hex_y), hex_id in self.hexagons.items():
                if self.main_view.main_frame.hex_canvas.find_closest(x, y)[0] == hex_id:
                    if (hex_x, hex_y) == self.depart_hex or (hex_x, hex_y) == self.objectif_hex:
                        continue  # Ne pas changer la couleur de la case départ ou objectif
                    self.current_hex_colors[(hex_x, hex_y)] = self.current_color
                    self.main_view.main_frame.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)],
                                                                    fill=self.current_color)
                    print(self.current_color)

                    if self is not None:
                        grid = self.grid
                        node_modif = grid.get_node(*self.hex_id_get_coords[self.hexagons[(hex_x, hex_y)]])
                        if self.current_color == "Black":
                            node_modif.active = False
                            print("Node désactivé")
                        else:
                            node_modif.active = True
                            print("Pas désactivé")
                        self.update_node_value(node_modif, self.current_color)
                    break

    def draw_path_with_circles(self, path_to_target, total_path):
        '''
        Dessine le chemin avec des cercles et des flèches en fonction de la liste proposé par l'algorithme de recherche
        '''
        if not total_path:
            return

        # Dictionnaire pour stocker les identifiants des cercles
        self.circle_ids = {}

        # Variable pour suivre les nœuds visités
        visited_nodes = set()
        if self.depart_hex:
            depart_coords = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
            visited_nodes.add(depart_coords)

        # Dessiner le chemin parcouru complet avec des cercles gris
        for k in total_path:
            visited_nodes = set()
            if self.depart_hex:
                depart_coords = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
                visited_nodes.add(depart_coords)
            for coords in k:
                if self.stop_drawing:
                    self.stop_drawing = False
                    return  # Arrêter le dessin si nécessaire
                # Vérifier que les coordonnées existent dans le dictionnaire
                if coords in self.hex_id_get_coords.values():
                    hex_id = [key for key, value in self.hex_id_get_coords.items() if value == coords][0]

                    # Obtenir les sommets de l'hexagone
                    points = self.main_view.main_frame.hex_canvas.coords(hex_id)

                    if len(points) >= 12:  # Chaque hexagone doit avoir 6 sommets
                        # Calculer le centre de l'hexagone
                        center_x = sum(points[i] for i in range(0, len(points), 2)) / 6
                        center_y = sum(points[i] for i in range(1, len(points), 2)) / 6

                        # Vérifier si le nœud a déjà été visité
                        if coords not in visited_nodes and coords not in self.circle_ids.keys():
                            # Dessiner un cercle gris au centre de l'hexagone
                            circle_id = self.main_view.main_frame.hex_canvas.create_oval(
                                center_x - 5, center_y - 5, center_x + 5, center_y + 5, fill="grey"
                            )
                            self.circle_ids[coords] = circle_id
                            self.results.append(circle_id)  # Ajouter le cercle à la liste des résultats

                            # Ajouter un délai pour voir le chemin se dessiner progressivement
                            self.main_view.after(2)  # Définir le délai en millisecondes
                            self.main_view.update()

                        # Ajouter le nœud à l'ensemble des nœuds visités
                        visited_nodes.add(coords)
            self.stop_drawing = False
        # Dessiner des flèches violettes pour le chemin vers la cible
        if path_to_target:
            for i in range(len(path_to_target) - 1):
                if self.stop_drawing:
                    self.stop_drawing = False
                    return  # Arrêter le dessin si nécessaire
                coords1 = path_to_target[i]
                coords2 = path_to_target[i + 1]

                # Vérifier que les coordonnées existent dans le dictionnaire
                if coords1 in self.hex_id_get_coords.values() and coords2 in self.hex_id_get_coords.values():
                    hex_id1 = [key for key, value in self.hex_id_get_coords.items() if value == coords1][0]
                    hex_id2 = [key for key, value in self.hex_id_get_coords.items() if value == coords2][0]

                    # Obtenir les sommets des hexagones
                    points1 = self.main_view.main_frame.hex_canvas.coords(hex_id1)
                    points2 = self.main_view.main_frame.hex_canvas.coords(hex_id2)

                    if len(points1) >= 12 and len(points2) >= 12:  # Chaque hexagone doit avoir 6 sommets
                        # Calculer les centres des hexagones
                        center1_x = sum(points1[i] for i in range(0, len(points1), 2)) / 6
                        center1_y = sum(points1[i] for i in range(1, len(points1), 2)) / 6
                        center2_x = sum(points2[i] for i in range(0, len(points2), 2)) / 6
                        center2_y = sum(points2[i] for i in range(1, len(points2), 2)) / 6

                        # Dessiner une flèche violette entre les deux centres
                        arrow_id = self.main_view.main_frame.hex_canvas.create_line(
                            center1_x, center1_y, center2_x, center2_y, fill="purple", arrow=ctk.LAST, width=5
                        )
                        self.arrow_ids[(coords1, coords2)] = arrow_id
                        self.results.append(arrow_id)  # Ajouter la flèche à la liste des résultats
                        print(f"Flèche ajoutée entre {coords1} et {coords2}")

                        # Ajouter un délai pour voir le chemin se dessiner progressivement
                        self.main_view.after(2)  # Définir le délai en millisecondes
                        self.main_view.update()
            self.stop_drawing = False

        # Forcer la mise à jour de l'interface après avoir dessiné le chemin
        self.main_view.update_idletasks()

    ####################################################################################################################
    ####################################################################################################################

    ################################# Fonctions pour reinitialisation et nettoyage #####################################
    ####################################################################################################################

    def clear_canvas(self):
        '''
        Réinitialise le canvas et les variables associées pour effacer les hexagones et les résultats
        '''
        self.pathfinding_in_progress = False  # Interrompre le parcours en cours
        self.stop_drawing = True  # Arrêter le dessin
        self.reset_hexagon_colors()
        self.clear_results()
        self.reactivate_all_nodes()
        self.depart_hex = None
        self.objectif_hex = None
        self.path_drawn = False

    def reactivate_all_nodes(self):
        '''
        Réactive tous les nœuds de la grille en remettant leur valeur à 1
        '''
        if self is not None:
            grid = self.grid
            for node in grid.nodes.values():
                node.active = True
                node.valeur = 1

    def reset_interface_state(self):
        '''
        Réinitialise l'état de l'interface
        '''
        self.pathfinding_in_progress = False  # Interrompre le parcours en cours
        self.stop_drawing = False  # Arrêter le dessin
        self.path_drawn = False  # Réinitialiser l'état du chemin dessiné
        self.main_view.update_idletasks()

    def clear_results(self):
        '''
        Efface tous les résultats affichés sur le canvas (cercles et flèches) sans supprimer les cases
        '''
        self.stop_drawing = True  # Arrêter le dessin
        # Effacer tous les résultats stockés dans la liste
        for result in self.results:
            self.main_view.main_frame.hex_canvas.delete(result)

        for hex_id in self.liste_stable:
            self.main_view.main_frame.hex_canvas.itemconfig(hex_id, fill="white")
            node = self.grid.get_node(*self.hex_id_get_coords[hex_id])
            node.active = True
            node.valeur = 1
        self.liste_stable.clear()

        self.results.clear()

        # Réinitialiser les dictionnaires de flèches et de cercles
        self.arrow_ids.clear()
        self.circle_ids.clear()

        # Réinitialiser les variables de suivi des chemins
        self.path_drawn = False


    def reset_hexagon_colors(self):
        '''
        Réinitialise les couleurs des hexagones
        '''
        for (hex_x, hex_y), hex_id in self.hexagons.items():
            # TODO : verifier
            self.main_view.main_frame.hex_canvas.itemconfig(hex_id, fill="white")

        # Clear circles
        for circle_id in self.circle_ids.values():
            self.main_view.main_frame.hex_canvas.delete(circle_id)
        self.circle_ids.clear()

    def clear_hexagons(self):
        '''
        Efface tous les hexagones dessinés sur le canvas
        '''
        self.main_view.main_frame.hex_canvas.delete("all")
        self.hexagons.clear()
        self.hex_id_get_coords.clear()
        self.depart_hex = None
        self.objectif_hex = None

    def restore_special_hexagons(self):
        '''
        Restaure les hexagones de départ et d'objectif
        '''
        # TODO : verifier graphique
        if self.depart_hex:
            hex_x, hex_y = self.depart_hex
            self.main_view.main_frame.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill="pink")
        if self.objectif_hex:
            hex_x, hex_y = self.objectif_hex
            self.main_view.main_frame.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill="red")

    def on_canvas_release(self, event):
        '''
        Gère les événements de relâchement de la souris sur le canvas
        '''
        self.depart_mode = False
        self.objectif_mode = False


    ####################################################################################################################
    ####################################################################################################################

    ############################################### Autres Fonctions ###################################################
    ####################################################################################################################

    def toggle_coords(self):
        '''
        Bascule l'affichage des coordonnées sur les hexagones
        '''
        if self.grid:
            self.clear_hexagons()
            self.draw_hex_grid(self.grid.rows, self.grid.cols,
                               self.hex_size)
            # Restaurer les cases de départ et d'objectif
            self.restore_special_hexagons()

    def update_node_value(self, node, color):
        '''
        Met à jour la valeur d'un nœud en fonction de sa couleur
        '''
        if color == "Blue":
            node.valeur = 5
        elif color == "Green":
            node.valeur = 3
        elif color == "Yellow":
            node.valeur = 2
        else:
            node.valeur = 1  # Valeur par défaut pour les autres couleurs

    

    


    
