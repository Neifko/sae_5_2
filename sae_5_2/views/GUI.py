import customtkinter as ctk
import math
from models.Grid import Grid

class GUI:
    def __init__(self, root):
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

        # Switch pour afficher les coordonnées
        self.show_coords_label = ctk.CTkLabel(self.entry_frame, text="Afficher les coordonnées:")
        self.show_coords_label.pack(side=ctk.TOP, padx=5, pady=5)
        self.show_coords_switch = ctk.CTkSwitch(self.entry_frame, command=self.draw_grid)
        self.show_coords_switch.pack(side=ctk.TOP, padx=5, pady=5)

        # Étiquette et zone de saisie pour les lignes
        self.rows_label = ctk.CTkLabel(self.entry_frame, text="Nombre de lignes:")
        self.rows_label.pack(side=ctk.TOP, padx=5, pady=5)
        self.rows_entry = ctk.CTkEntry(self.entry_frame)
        self.rows_entry.pack(side=ctk.TOP, padx=5, pady=5)
        self.rows_entry.insert(0, "10")  # Valeur par défaut

        # Étiquette et zone de saisie pour les colonnes
        self.cols_label = ctk.CTkLabel(self.entry_frame, text="Nombre de colonnes:")
        self.cols_label.pack(side=ctk.TOP, padx=5, pady=5)
        self.cols_entry = ctk.CTkEntry(self.entry_frame)
        self.cols_entry.pack(side=ctk.TOP, padx=5, pady=5)
        self.cols_entry.insert(0, "10")  # Valeur par défaut

        # Bouton pour dessiner la grille
        self.draw_button = ctk.CTkButton(self.entry_frame, text="Dessiner la grille", command=self.draw_grid)
        self.draw_button.pack(side=ctk.TOP, padx=5, pady=5)

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

    def draw_grid(self):
        # Effacer le canvas avant de dessiner la nouvelle grille
        self.hex_canvas.delete("all")

        # Récupérer les valeurs des zones de saisie
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())
        size = 30

        # Dessiner la grille d'hexagones
        self.draw_hex_grid(rows, cols, size)

    def draw_hexagon(self, canvas, x, y, size, color, label=None):
        points = []
        for i in range(6):
            angle = math.radians(60 * i)
            px = x + size * math.cos(angle)
            py = y + size * math.sin(angle)
            points.append(px)
            points.append(py)
        canvas.create_polygon(points, outline="black", fill=color, width=1)

        if label:
            canvas.create_text(x, y, text=label, fill="black")

    def draw_hex_grid(self, rows, cols, size):
        hex_grid = Grid(rows, cols)
        hex_grid.display_grid()
        hex_grid.display_neighbors(0, 1, -1)

        for row in range(rows):
            for col in range(cols):
                x = 1.5 * size * col + size
                y = math.sqrt(3) * size * (row + 0.5 * (col % 2)) + size
                coord = f"({col},{row},{-col-row})"
                self.draw_hexagon(self.hex_canvas, x, y, size, "white", coord if self.show_coords_switch.get() else None)


