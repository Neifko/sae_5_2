import customtkinter as ctk
from customtkinter import *

class LeftNavbar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.rows = 10
        self.cols = 10

        self.parent = parent

        colors = ["Black", "White", "Blue", "Green", "Yellow", "Départ", "Objectif", "Stable Maximum"]

        for color in colors:
            button = ctk.CTkButton(
                self,
                text=color,
                corner_radius=32,
                fg_color="transparent",
                hover_color="#5A1E9C",
                border_width=2,
                border_spacing=5,
                border_color="#671D67"
            )

            if color == "Départ":
                button.configure(command=self.set_depart)
            elif color == "Objectif":
                button.configure(command=self.set_objectif)
            else:
                button.configure(command=lambda c=color: self.set_color(c))

            button.pack(fill=ctk.X, padx=5, pady=2)

        # Cadre pour les zones de saisie et le switch
        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.pack(side=ctk.BOTTOM, padx=10, pady=10, fill=ctk.X)

        # Slider pour gérer la taille des hexagones
        self.size_slider = ctk.CTkSlider(
            self.entry_frame,
            from_=10,
            to=50,
            number_of_steps=5,
            orientation=ctk.HORIZONTAL,
            command=self.update_hex_size,
            button_color="#5A1E9C",
            hover=False
        )
        self.size_slider.pack(side=ctk.TOP, padx=2, pady=2)
        self.size_slider.set(30)  # Valeur par défaut

        # Switch pour afficher les coordonnées
        self.show_coords_label = ctk.CTkLabel(self.entry_frame, text="Afficher les coordonnées:")
        self.show_coords_label.pack(side=ctk.TOP, padx=2, pady=2)
        self.show_coords_switch = ctk.CTkSwitch(
            self.entry_frame,
            progress_color="#5A1E9C",
            command=self.toggle_coords,
        )
        self.show_coords_switch.pack(side=ctk.TOP, padx=2, pady=2)

        # Étiquette et zone de saisie pour les lignes
        self.rows_label = ctk.CTkLabel(self.entry_frame, text="Nombre de lignes:")
        self.rows_label.pack(side=ctk.TOP, padx=5, pady=5)
        self.rows_entry = ctk.CTkEntry(self.entry_frame)
        self.rows_entry.pack(side=ctk.TOP, padx=5, pady=5)
        self.rows_entry.insert(0, str(self.rows))  # Valeur par défaut

        # Étiquette et zone de saisie pour les colonnes
        self.cols_label = ctk.CTkLabel(self.entry_frame, text="Nombre de colonnes:")
        self.cols_label.pack(side=ctk.TOP, padx=5, pady=5)
        self.cols_entry = ctk.CTkEntry(self.entry_frame)
        self.cols_entry.pack(side=ctk.TOP, padx=5, pady=5)
        self.cols_entry.insert(0, str(self.cols))  # Valeur par défaut

        # Bouton pour dessiner la grille
        self.draw_button = ctk.CTkButton(
            self.entry_frame,
            text="Dessiner la grille",
            command=self.draw_grid,
            corner_radius=32,
            fg_color="transparent",
            hover_color="#5A1E9C",
            border_width=2,
            border_spacing=5,
            border_color="#671D67"
        )
        self.draw_button.pack(side=ctk.TOP, padx=2, pady=2)

        # Bouton pour dessiner le maximum de hexagones possibles en fonction de l'écran et de la taille des hexagones
        self.max_button = ctk.CTkButton(
            self.entry_frame,
            text="Grille complète",
            command=self.draw_max_grid,
            corner_radius=32,
            fg_color="transparent",
            hover_color="#5A1E9C",
            border_width=2,
            border_spacing=5,
            border_color="#671D67"
        )
        self.max_button.pack(side=ctk.TOP, padx=5, pady=5)

    def get_controller(self):
        return self.parent.get_controller()

    def set_depart(self):
        self.get_controller().set_depart()

    def set_objectif(self):
        self.get_controller().set_objectif()

    def set_color(self, c):
        self.get_controller().set_color(c)

    def update_hex_size(self, size):
        self.get_controller().update_hex_size(size)

    def toggle_coords(self):
        self.get_controller().toggle_coords()

    def draw_grid(self):
        self.get_controller().draw_grid()

    def draw_max_grid(self):
        self.get_controller().draw_max_grid()

    def call_stableMax(self):
        self.get_controller().call_stableMax()
