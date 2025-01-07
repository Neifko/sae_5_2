import customtkinter as ctk
import math

class GUI:
    def __init__(self, root, controller, rows, cols):
        self.controller = controller
        self.root = root
        self.root.title("Hexagones")
        self.root.geometry("1000x600")

        # Création des boutons de couleur
        self.color_buttons_frame = ctk.CTkFrame(self.root)
        self.color_buttons_frame.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.Y)

        colors = ["Black", "White", "Blue", "Green", "Yellow", "Départ", "Objectif"]
        for color in colors:
            button = ctk.CTkButton(self.color_buttons_frame, text=color, command=lambda c=color: print(c))
            button.pack(fill=ctk.X, padx=5, pady=2)

        # Cadre pour les zones de saisie et le switch
        self.entry_frame = ctk.CTkFrame(self.color_buttons_frame)
        self.entry_frame.pack(side=ctk.BOTTOM, padx=10, pady=10, fill=ctk.X)

        # Slider pour gérer la taille des hexagones
        self.size_slider = ctk.CTkSlider(self.entry_frame, from_=10, to=50, number_of_steps=5, orientation=ctk.HORIZONTAL, command=self.controller.update_hex_size)
        self.size_slider.pack(side=ctk.TOP, padx=2, pady=2)
        self.size_slider.set(30)  # Valeur par défaut

        # Switch pour afficher les coordonnées
        self.show_coords_label = ctk.CTkLabel(self.entry_frame, text="Afficher les coordonnées:")
        self.show_coords_label.pack(side=ctk.TOP, padx=2, pady=2)
        self.show_coords_switch = ctk.CTkSwitch(self.entry_frame, command=self.controller.toggle_coords)
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
        self.draw_button = ctk.CTkButton(self.entry_frame, text="Dessiner la grille", command=self.controller.draw_grid)
        self.draw_button.pack(side=ctk.TOP, padx=2, pady=2)

        # Bouton pour dessiner le maximum de hexagones possibles en fonction de l'écran et de la taille des hexagones
        self.max_button = ctk.CTkButton(self.entry_frame, text="Grille complète", command=self.controller.draw_max_grid)
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
        self.hex_canvas = ctk.CTkCanvas(self.main_frame, bg="black")
        self.hex_canvas.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Forcer la mise à jour de la taille du canvas
        self.hex_canvas.update_idletasks()

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
        self.hex_canvas.create_polygon(points, outline="black", fill=color, width=1)

        if label:
            self.hex_canvas.create_text(x, y, text=label, fill="black", font=("Arial", font_size))

    def clear_canvas(self):
        self.hex_canvas.delete("all")
