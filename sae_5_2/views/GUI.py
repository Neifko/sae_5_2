import customtkinter as ctk
import math
import random
import tkinter as tk
from tkinter import Canvas
from sae_5_2.controllers.InterfaceController import InterfaceController
from sae_5_2.controllers.ProfondeurController import ProfondeurController
from sae_5_2.controllers.algoBFSController import algoBFSController
from sae_5_2.models.Grid import Grid  # Assurez-vous que cette importation est correcte
from sae_5_2.views.LeftNavbar import LeftNavbar


class GUI:
    def __init__(self, root, controller, rows, cols):
        self.controller = controller
        self.root = root
        self.root.title("Hexagones")
        self.root.geometry("1000x600")

        self.interface_controller = None

        self.profondeur_controller = ProfondeurController()
        self.algoBFSController = algoBFSController()

        # Variable pour suivre la couleur actuelle
        self.current_color = None  # Couleur transparente par défaut

        # Création des boutons de couleur
        self.color_buttons_frame = ctk.CTkFrame(self.root)
        self.color_buttons_frame.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.Y)

        colors = ["Black", "White", "Blue", "Green", "Yellow", "Départ", "Objectif"]
        self.colors = ["Black", "White", "Blue", "Green", "Yellow"]
        for color in colors:
            if color == "Départ":
                button = ctk.CTkButton(self.color_buttons_frame, text=color, command=self.set_depart)
            elif color == "Objectif":
                button = ctk.CTkButton(self.color_buttons_frame, text=color, command=self.set_objectif)
            else:
                button = ctk.CTkButton(self.color_buttons_frame, text=color, command=lambda c=color: self.set_color(c))
            button.pack(fill=ctk.X, padx=5, pady=2)

        # Cadre pour les zones de saisie et le switch
        self.entry_frame = ctk.CTkFrame(self.color_buttons_frame)
        self.entry_frame.pack(side=ctk.BOTTOM, padx=10, pady=10, fill=ctk.X)

        # Slider pour gérer la taille des hexagones
        self.size_slider = ctk.CTkSlider(self.entry_frame, from_=10, to=50, number_of_steps=5,
                                         orientation=ctk.HORIZONTAL, command=self.update_hex_size)
        self.size_slider.pack(side=ctk.TOP, padx=2, pady=2)
        self.size_slider.set(30)  # Valeur par défaut

        # Switch pour afficher les coordonnées
        self.show_coords_label = ctk.CTkLabel(self.entry_frame, text="Afficher les coordonnées:")
        self.show_coords_label.pack(side=ctk.TOP, padx=2, pady=2)
        self.show_coords_switch = ctk.CTkSwitch(self.entry_frame, command=self.toggle_coords)
        self.show_coords_switch.pack(side=ctk.TOP, padx=2, pady=2)

        # Étiquette et zone de saisie pour les lignes
        self.rows_label = ctk.CTkLabel(self.entry_frame, text="Nombre de lignes:")
        self.rows_label.pack(side=ctk.TOP, padx=5, pady=5)
        self.rows_entry = ctk.CTkEntry(self.entry_frame)
        self.rows_entry.pack(side=ctk.TOP, padx=5, pady=5)
        self.rows_entry.insert(0, str(rows))  # Valeur par défaut

        # Étiquette et zone de saisie pour les colonnes
        self.cols_label = ctk.CTkLabel(self.entry_frame, text="Nombre de colonnes:")
        self.cols_label.pack(side=ctk.TOP, padx=5, pady=5)
        self.cols_entry = ctk.CTkEntry(self.entry_frame)
        self.cols_entry.pack(side=ctk.TOP, padx=5, pady=5)
        self.cols_entry.insert(0, str(cols))  # Valeur par défaut

        # Bouton pour dessiner la grille
        self.draw_button = ctk.CTkButton(self.entry_frame, text="Dessiner la grille", command=self.draw_grid)
        self.draw_button.pack(side=ctk.TOP, padx=2, pady=2)

        # Bouton pour dessiner le maximum de hexagones possibles en fonction de l'écran et de la taille des hexagones
        self.max_button = ctk.CTkButton(self.entry_frame, text="Grille complète", command=self.draw_max_grid)
        self.max_button.pack(side=ctk.TOP, padx=5, pady=5)

        # Cadre principal pour les boutons et la zone de dessin
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Création des boutons d'action
        self.action_buttons_frame = ctk.CTkFrame(self.main_frame)
        self.action_buttons_frame.pack(side=ctk.TOP, fill=ctk.X, padx=10, pady=5)

        actions = ["Effacer Tout", "Effacer Résultats", "Aléatoire", "Parcours en profondeur", "Parcours en largeur",
                   "Bellman-Ford", "Dijkstra", "A*"]
        for action in actions:
            if action == "Effacer Tout":
                button = ctk.CTkButton(self.action_buttons_frame, text=action, command=self.clear_canvas)
            elif action == "Effacer Résultats":
                button = ctk.CTkButton(self.action_buttons_frame, text=action, command=self.clear_results)
            elif action == "Aléatoire":
                button = ctk.CTkButton(self.action_buttons_frame, text=action, command=self.random_case_colors)
            elif action == "Parcours en profondeur":
                button = ctk.CTkButton(self.action_buttons_frame, text=action, command=self.call_profondeur)
            elif action == "Parcours en largeur":
                button = ctk.CTkButton(self.action_buttons_frame, text=action, command=self.call_largeur)
            else:
                button = ctk.CTkButton(self.action_buttons_frame, text=action, command=lambda a=action: print(a))
            button.pack(side=ctk.LEFT, padx=5, pady=5)

        # Zone de dessin des hexagones
        self.hex_canvas = Canvas(self.main_frame, bg="grey")
        self.hex_canvas.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Forcer la mise à jour de la taille du canvas
        self.hex_canvas.update_idletasks()

        # Variables pour suivre l'état des boutons
        self.depart_mode = False
        self.objectif_mode = False
        # Variable pour suivre si un chemin a été dessiné
        self.path_drawn = False

        # Variables pour suivre les hexagones de départ et d'objectif
        self.depart_hex = None
        self.objectif_hex = None

        # Lier les événements de clic sur le canvas
        self.hex_canvas.bind("<Button-1>", self.on_canvas_click)
        self.hex_canvas.bind("<B1-Motion>", self.on_canvas_motion)
        self.hex_canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

        # Dictionnaire pour stocker les hexagones dessinés
        self.hexagons = {}
        # Dictionnaire pour stocker les couleurs précédentes des hexagones
        self.current_hex_colors = {}
        self.hex_id_get_coords = {}
        self.incoming_arrows = {}

    def axial_to_cube(self, q, r):
        x = q
        z = r
        y = -x - z
        return (x, y, z)

    def call_profondeur(self):
        if self.path_drawn:
            self.clear_results()    

        if not self.depart_hex or not self.objectif_hex:
            print("Veuillez définir une case de départ et une case d'objectif.")
            return

        depart_cubique = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
        arrive_cubique = self.hex_id_get_coords[self.hexagons[self.objectif_hex]]

        print(f"Coordonnées cubiques de départ: {depart_cubique}")
        print(f"Coordonnées cubiques d'objectif: {arrive_cubique}")

        self.profondeur_controller.set_grid(self.controller.grid)
        path_to_target, total_path = self.profondeur_controller.execute(depart_cubique, arrive_cubique)

        if path_to_target:
            print(f"Un chemin existe entre {depart_cubique} et {arrive_cubique}.")
            print(f"Chemin vers la cible : {path_to_target}")
        else:
            print(f"Aucun chemin trouvé entre {depart_cubique} et {arrive_cubique}.")

        print(f"Chemin total parcouru : {total_path}")

        # Dessiner les chemins
        self.draw_path(path_to_target, total_path)

    def call_largeur(self):
        print("oui")
        if self.path_drawn:
            self.clear_results()

        if not self.depart_hex or not self.objectif_hex:
            print("Veuillez définir une case de départ et une case d'objectif.")
            return

        depart_cubique = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
        arrive_cubique = self.hex_id_get_coords[self.hexagons[self.objectif_hex]]

        print(f"Coordonnées cubiques de départ: {depart_cubique}")
        print(f"Coordonnées cubiques d'objectif: {arrive_cubique}")

        self.algoBFSController.set_grid(self.controller.grid)
        path_to_target, total_path = self.algoBFSController.run_bfs(depart_cubique, arrive_cubique)

        path = [(node.x, node.y, node.z) for node in path_to_target] # Convertir les nœuds en coordonnées cubiques
        total_path = [(node.x, node.y, node.z) for node in total_path]  # Convertir les nœuds en coordonnées cubiques

        # print(path)

        if path_to_target:
            print(f"Un chemin existe entre {depart_cubique} et {arrive_cubique}.")
            print(f"Chemin vers la cible : {path}")
        else:
            print(f"Aucun chemin trouvé entre {depart_cubique} et {arrive_cubique}.")

        print(f"Chemin total parcouru : {total_path}")

        # Dessiner les chemins
        self.draw_path(path_to_target, total_path)


    def random_case_colors(self):
        # Parcourir tous les hexagones et leur attribuer une couleur aléatoire
        for (hex_x, hex_y), hex_id in self.hexagons.items():
            # Ne pas changer la couleur des cases de départ et d'objectif
            if (hex_x, hex_y) == self.depart_hex or (hex_x, hex_y) == self.objectif_hex:
                continue

            # Choisir une couleur aléatoire parmi les couleurs disponibles
            color = random.choice(self.colors)
            self.hex_canvas.itemconfig(hex_id, fill=color)

            # Désactiver les cases noires
            if color == "Black":
                if self.interface_controller is not None:
                    grid = self.interface_controller.grid
                    node_modif = grid.get_node(*self.hex_id_get_coords[self.hexagons[(hex_x, hex_y)]])
                    node_modif.active = False
                    print(f"Node ({hex_x}, {hex_y}) désactivé")
            else:
                if self.interface_controller is not None:
                    grid = self.interface_controller.grid
                    node_modif = grid.get_node(*self.hex_id_get_coords[self.hexagons[(hex_x, hex_y)]])
                    node_modif.active = True
                    print(f"Node ({hex_x}, {hex_y}) activé")


    def draw_arrow(self, x1, y1, x2, y2, color="#9900CC"):
        self.hex_canvas.create_line(x1, y1, x2, y2, fill=color, arrow=tk.LAST, width=5)
    def draw_arrow2(self, x1, y1, x2, y2, color="grey"):
        self.hex_canvas.create_line(x1, y1, x2, y2, fill=color, arrow=tk.LAST, width=5)

    def draw_path(self, path_to_target, total_path):
        if not total_path:
            return

        # Dictionnaire pour stocker les identifiants des flèches grises
        self.arrow_ids = {}

        # Variable pour suivre les nœuds visités
        visited_nodes = set()
        if self.depart_hex:
            depart_coords = self.hex_id_get_coords[self.hexagons[self.depart_hex]]
            visited_nodes.add(depart_coords)

        # Dessiner le chemin parcouru complet avec des flèches grises
        for i in range(len(total_path) - 1):
            coords1 = total_path[i]
            coords2 = total_path[i + 1]

            # Vérifier que les coordonnées existent dans le dictionnaire
            if coords1 in self.hex_id_get_coords.values() and coords2 in self.hex_id_get_coords.values():
                hex_id1 = [key for key, value in self.hex_id_get_coords.items() if value == coords1][0]
                hex_id2 = [key for key, value in self.hex_id_get_coords.items() if value == coords2][0]

                # Obtenir les sommets des hexagones
                points1 = self.hex_canvas.coords(hex_id1)
                points2 = self.hex_canvas.coords(hex_id2)

                if len(points1) >= 12 and len(points2) >= 12:  # Chaque hexagone doit avoir 6 sommets
                    # Calculer les centres des hexagones
                    center1_x = sum(points1[i] for i in range(0, len(points1), 2)) / 6
                    center1_y = sum(points1[i] for i in range(1, len(points1), 2)) / 6
                    center2_x = sum(points2[i] for i in range(0, len(points2), 2)) / 6
                    center2_y = sum(points2[i] for i in range(1, len(points2), 2)) / 6

                    # Vérifier si le nœud suivant a déjà été visité
                    if coords2 not in visited_nodes:
                        # Dessiner une flèche grise entre les deux centres
                        arrow_id = self.hex_canvas.create_line(center1_x, center1_y, center2_x, center2_y, fill="grey", arrow=tk.LAST, width=5)
                        self.arrow_ids[(coords1, coords2)] = arrow_id

                        # Ajouter un délai pour voir le chemin se dessiner progressivement
                        self.root.after(5)  # Définir le délai en millisecondes
                        self.root.update()

                    # Ajouter le nœud suivant à l'ensemble des nœuds visités
                    visited_nodes.add(coords2)

        # Modifier la couleur des flèches existantes en violet pour le chemin vers la cible
        if path_to_target:
            for i in range(len(path_to_target) - 1):
                coords1 = path_to_target[i]
                coords2 = path_to_target[i + 1]
                print(coords1, coords2)
                print(self.arrow_ids)

                # Vérifier que les coordonnées existent dans le dictionnaire
                if (coords1, coords2) in self.arrow_ids:
                    print("oui")
                    arrow_id = self.arrow_ids[(coords1, coords2)]
                    # Modifier la couleur de la flèche en violet
                    self.hex_canvas.itemconfig(arrow_id, fill="purple")

                    # Ajouter un délai pour voir le chemin se dessiner progressivement
                    self.root.after(2)  # Définir le délai en millisecondes
                    self.root.update()

    def set_depart(self):
        self.depart_mode = True
        self.objectif_mode = False
        print("Mode Départ activé")

    def set_objectif(self):
        self.objectif_mode = True
        self.depart_mode = False
        print("Mode Objectif activé")

    def set_color(self, color):
        self.current_color = color
        self.depart_mode = False
        self.objectif_mode = False
        print(f"Color set to {color}")

    def get_canvas_center(self):
        canvas_width = self.hex_canvas.winfo_width()
        canvas_height = self.hex_canvas.winfo_height()
        return canvas_width / 2, canvas_height / 2

    def draw_hexagon(self, x, y, size, color, coord=None, font_size=12):
        points = []

        for i in range(6):
            angle = math.radians(60 * i)
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append(px)
            points.append(py)
        hex_id = self.hex_canvas.create_polygon(points, outline="black", fill=color, width=1)

        # Stocker l'hexagone dessiné avec ses coordonnées
        self.hexagons[(x, y)] = hex_id

        if coord is not None:
            coord_str = f"({coord[0]},{coord[1]},{coord[2]})"
            self.hex_id_get_coords[hex_id] = coord
        else:
            coord_str = ""

        label = coord_str if self.show_coords_switch.get() else None

        if label:
            self.hex_canvas.create_text(x, y, text=label, fill="black", font=("Arial", font_size))

    def clear_canvas(self):
        self.reset_hexagon_colors()
        self.clear_arrows()
        self.reactivate_all_nodes()
        self.depart_hex = None  
        self.objectif_hex = None
        self.path_drawn = False

    def reactivate_all_nodes(self):
        if self.interface_controller is not None:
            grid = self.interface_controller.grid
            for node in grid.nodes.values():
                node.active = True

    def clear_results(self):
        self.clear_arrows()
        self.path_drawn = False

    def reset_hexagon_colors(self):
        for (hex_x, hex_y), hex_id in self.hexagons.items():
            self.hex_canvas.itemconfig(hex_id, fill="white")

    def clear_arrows(self):
        for arrow_id in self.arrow_ids.values():
            self.hex_canvas.delete(arrow_id)
        self.arrow_ids.clear()

    def clear_hexagons(self):
        self.hex_canvas.delete("all")
        self.hexagons.clear()
        self.hex_id_get_coords.clear()
        self.depart_hex = None
        self.objectif_hex = None

    def draw_grid(self):
        self.clear_hexagons()
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())

        # Recréer la grille avec les nouvelles dimensions
        self.controller.grid = Grid(rows, cols)
        self.controller.draw_hex_grid(rows, cols, self.controller.hex_size)

        # Restaurer les cases de départ et d'objectif
        self.restore_special_hexagons()

    def draw_max_grid(self):
        self.clear_hexagons()
        canvas_width = self.hex_canvas.winfo_width()
        canvas_height = self.hex_canvas.winfo_height()

        # Calcul du nombre maximum de colonnes et de rangées qui peuvent tenir dans la zone de dessin
        cols = int(canvas_width / (1.5 * self.controller.hex_size))
        rows = int(canvas_height / (math.sqrt(3) * self.controller.hex_size))

        # Mettre à jour les champs de saisie
        self.rows_entry.delete(0, 'end')
        self.rows_entry.insert(0, str(rows))
        self.cols_entry.delete(0, 'end')
        self.cols_entry.insert(0, str(cols))

        # Recréer la grille avec les nouvelles dimensions
        self.controller.grid = Grid(rows, cols)
        self.controller.draw_hex_grid(rows, cols, self.controller.hex_size)

        # Restaurer les cases de départ et d'objectif
        self.restore_special_hexagons()

    def toggle_coords(self):
        if self.controller.grid:
            self.clear_hexagons()
            self.controller.draw_hex_grid(self.controller.grid.rows, self.controller.grid.cols,
                                          self.controller.hex_size)
            # Restaurer les cases de départ et d'objectif
            self.restore_special_hexagons()

    def update_hex_size(self, size):
        self.controller.hex_size = int(size)
        if self.controller.grid:
            self.clear_hexagons()
            self.controller.draw_hex_grid(self.controller.grid.rows, self.controller.grid.cols,
                                          self.controller.hex_size)
            # Restaurer les cases de départ et d'objectif
            self.restore_special_hexagons()

    def restore_special_hexagons(self):
        if self.depart_hex:
            hex_x, hex_y = self.depart_hex
            self.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill="pink")
        if self.objectif_hex:
            hex_x, hex_y = self.objectif_hex
            self.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill="red")

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        # Vérifier si un hexagone est cliqué
        for (hex_x, hex_y), hex_id in self.hexagons.items():
            if self.hex_canvas.find_closest(x, y)[0] == hex_id:
                if self.depart_mode:
                    if self.depart_hex:
                        # Réinitialiser l'ancienne case de départ
                        old_hex_x, old_hex_y = self.depart_hex
                        current_color = self.current_hex_colors.get((old_hex_x, old_hex_y), "")
                        self.hex_canvas.itemconfig(self.hexagons[(old_hex_x, old_hex_y)], fill=current_color)
                    self.depart_hex = (hex_x, hex_y)
                    self.current_hex_colors[(hex_x, hex_y)] = self.hex_canvas.itemcget(hex_id, "fill")
                    self.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill="pink")
                    self.depart_cube = self.axial_to_cube(hex_x, hex_y)  # Stocker les coordonnées cubiques
                elif self.objectif_mode:
                    if self.objectif_hex:
                        # Réinitialiser l'ancienne case d'objectif
                        old_hex_x, old_hex_y = self.objectif_hex
                        current_color = self.current_hex_colors.get((old_hex_x, old_hex_y), "")
                        self.hex_canvas.itemconfig(self.hexagons[(old_hex_x, old_hex_y)], fill=current_color)
                    self.objectif_hex = (hex_x, hex_y)
                    self.current_hex_colors[(hex_x, hex_y)] = self.hex_canvas.itemcget(hex_id, "fill")
                    self.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill="red")
                    self.objectif_cube = self.axial_to_cube(hex_x, hex_y)  # Stocker les coordonnées cubiques
                else:
                    if (hex_x, hex_y) == self.depart_hex or (hex_x, hex_y) == self.objectif_hex:
                        continue  # Ne pas changer la couleur de la case départ ou objectif
                    self.current_hex_colors[(hex_x, hex_y)] = self.current_color
                    self.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill=self.current_color)
                    print(self.current_color)

                    if self.interface_controller is not None:
                        grid = self.interface_controller.grid
                        node_modif = grid.get_node(*self.hex_id_get_coords[self.hexagons[(hex_x, hex_y)]])
                        if self.current_color == "Black":
                            node_modif.active = False
                            print("Node désactivé")
                        else:
                            node_modif.active = True
                            print("Pas desactivé")

                break

    def on_canvas_motion(self, event):
        if not self.depart_mode and not self.objectif_mode:
            x, y = event.x, event.y
            # Vérifier si un hexagone est cliqué
            for (hex_x, hex_y), hex_id in self.hexagons.items():
                if self.hex_canvas.find_closest(x, y)[0] == hex_id:
                    if (hex_x, hex_y) == self.depart_hex or (hex_x, hex_y) == self.objectif_hex:
                        continue  # Ne pas changer la couleur de la case départ ou objectif
                    self.current_hex_colors[(hex_x, hex_y)] = self.current_color
                    self.hex_canvas.itemconfig(self.hexagons[(hex_x, hex_y)], fill=self.current_color)
                    print(self.current_color)

                    if self.interface_controller is not None:
                        grid = self.interface_controller.grid
                        node_modif = grid.get_node(*self.hex_id_get_coords[self.hexagons[(hex_x, hex_y)]])
                        if self.current_color == "Black":
                            node_modif.active = False
                            print("Node désactivé")
                        else:
                            node_modif.active = True
                            print("Pas désactivé")

                    break

    def on_canvas_release(self, event):
        self.depart_mode = False
        self.objectif_mode = False


