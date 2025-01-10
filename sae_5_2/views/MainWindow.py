from time import sleep

import customtkinter as ctk

from sae_5_2.controllers.MainController import MainController
from sae_5_2.views.LeftNavbar import LeftNavbar
from sae_5_2.views.MainFrame import MainFrame


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hexagones")
        self.geometry("1000x600")

        self.controller = None

        # Création des boutons de couleur
        self.left_frame = LeftNavbar(self)
        self.left_frame.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.Y)

        self.main_frame = MainFrame(self)
        self.main_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

    def set_controller(self, controller):
        print("Setting controller")
        self.controller = controller

    def get_controller(self):
        return self.controller



