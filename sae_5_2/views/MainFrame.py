import customtkinter as ctk

from sae_5_2.views.GridCanvas import GridCanvas
from sae_5_2.views.TopNavbar import TopNavbar


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # Création des boutons d'action
        self.top_navbar = TopNavbar(self)
        self.top_navbar.pack(side=ctk.TOP, fill=ctk.X, padx=10, pady=5)

        # Zone de dessin des hexagones
        self.hex_canvas = GridCanvas(self)
        self.hex_canvas.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

    def get_controller(self):
        return self.parent.get_controller()
