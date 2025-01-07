from models.ParcoursProfondeur import ParcoursProfondeur
from models.Grid import Grid
from models.Node import Node
from views.GUI import GUI
import customtkinter as ctk
from controllers.InterfaceController import InterfaceController

if __name__ == "__main__":
    # Exemple d'utilisation
    rows, cols = 10, 10  # Taille de la grille
    hex_grid = Grid(rows, cols)
    hex_grid.display_grid()
    hex_grid.display_neighbors(0, 1, -1)  # Coordonnées (x=2, y=2, z=-4)



    # LANCEMENT -----------------------------------------------------------
    root = ctk.CTk()
    controller = InterfaceController()
    gui = GUI(root, controller)
    controller.set_view(gui)
    root.mainloop()
    # ---------------------------------------------------------------------
