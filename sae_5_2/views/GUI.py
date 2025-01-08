import customtkinter as ctk
import math
from tkinter import Canvas
from models.Grid import Grid  # Assurez-vous que cette importation est correcte

class GUI:
    def __init__(self, root, controller, rows, cols):
        self.controller = controller
        self.root = root
        self.root.title("Hexagones")
        self.root.geometry("1000x600")

        # Variable pour suivre la couleur actuelle
        self.current_color = ""  # Couleur transparente par défaut

        # Création des boutons de couleur
        self.color_buttons_frame = ctk.CTkFrame(self.root)
        self.color_buttons_frame.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.Y)

        colors = ["Black", "White", "Blue", "Green", "Yellow", "Départ", "Objectif"]
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
        self.size_slider = ctk.CTkSlider(self.entry_frame, from_=10, to=50, number_of_steps=5, orientation=ctk.HORIZONTAL, command=self.update_hex_size)
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

        actions = ["Effacer Tout", "Effacer Résultats", "Aléatoire", "Parcours en profondeur", "Parcours en largeur", "Bellman-Ford", "Dijkstra", "A*"]
        for action in actions:
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

    def draw_hexagon(self, x, y, size, color, label=None, font_size=12):
        points = []
        for i in range(6):
            angle = math.radians(60 * i)
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append(px)
            points.append(py)
        hex_id = self.hex_canvas.create_polygon(points, outline="black", fill=color, width=1)

        if label:
            self.hex_canvas.create_text(x, y, text=label, fill="black", font=("Arial", font_size))

        # Stocker l'hexagone dessiné avec ses coordonnées
        self.hexagons[(x, y)] = hex_id

    def clear_canvas(self):
        self.hex_canvas.delete("all")
        self.hexagons.clear()
        self.depart_hex = None
        self.objectif_hex = None

    def draw_grid(self):
        self.clear_canvas()
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())

        # Recréer la grille avec les nouvelles dimensions
        self.controller.grid = Grid(rows, cols)
        self.controller.draw_hex_grid(rows, cols, self.controller.hex_size)

        # Restaurer les cases de départ et d'objectif
        self.restore_special_hexagons()

    def draw_max_grid(self):
        self.clear_canvas()
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
            self.clear_canvas()
            self.controller.draw_hex_grid(self.controller.grid.rows, self.controller.grid.cols, self.controller.hex_size)
            # Restaurer les cases de départ et d'objectif
            self.restore_special_hexagons()

    def update_hex_size(self, size):
        self.controller.hex_size = int(size)
        if self.controller.grid:
            self.clear_canvas()
            self.controller.draw_hex_grid(self.controller.grid.rows, self.controller.grid.cols, self.controller.hex_size)
            # Restaurer les cases de départ et d'objectif
            self.restore_special_hexagons()

    def restore_special_hexagons(self):
        if self.depart_hex:
            hex_x, hex_y = self.depart_hex
            self.draw_hexagon(hex_x, hex_y, self.controller.hex_size, "pink")  # Rose pour le départ
        if self.objectif_hex:
            hex_x, hex_y = self.objectif_hex
            self.draw_hexagon(hex_x, hex_y, self.controller.hex_size, "red")  # Rouge pour l'objectif

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
                        self.draw_hexagon(old_hex_x, old_hex_y, self.controller.hex_size, current_color)
                    self.depart_hex = (hex_x, hex_y)
                    self.current_hex_colors[(hex_x, hex_y)] = self.hex_canvas.itemcget(hex_id, "fill")
                    self.draw_hexagon(hex_x, hex_y, self.controller.hex_size, "pink")  # Rose pour le départ
                elif self.objectif_mode:
                    if self.objectif_hex:
                        # Réinitialiser l'ancienne case d'objectif
                        old_hex_x, old_hex_y = self.objectif_hex
                        current_color = self.current_hex_colors.get((old_hex_x, old_hex_y), "")
                        self.draw_hexagon(old_hex_x, old_hex_y, self.controller.hex_size, current_color)
                    self.objectif_hex = (hex_x, hex_y)
                    self.current_hex_colors[(hex_x, hex_y)] = self.hex_canvas.itemcget(hex_id, "fill")
                    self.draw_hexagon(hex_x, hex_y, self.controller.hex_size, "red")  # Rouge pour l'objectif
                else:
                    if (hex_x, hex_y) == self.depart_hex or (hex_x, hex_y) == self.objectif_hex:
                        continue  # Ne pas changer la couleur de la case départ ou objectif
                    self.current_hex_colors[(hex_x, hex_y)] = self.current_color
                    self.draw_hexagon(hex_x, hex_y, self.controller.hex_size, self.current_color)
                break

    def on_canvas_motion(self, event):
        if not self.depart_mode and not self.objectif_mode:
            x, y = event.x, event.y
            # Vérifier si un hexagone est cliqué
            for (hex_x, hex_y), hex_id in self.hexagons.items():
                if self.hex_canvas.find_closest(x, y)[0] == hex_id:
                    if (hex_x, hex_y) == self.depart_hex or (hex_x, hex_y) == self.objectif_hex:
                        continue  # Ne pas changer la couleur de la case départ ou objectif
                    self.draw_hexagon(hex_x, hex_y, self.controller.hex_size, self.current_color)
                    break

    def on_canvas_release(self, event):
        self.depart_mode = False
        self.objectif_mode = False
