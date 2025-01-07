from models.ParcoursProfondeur import ParcoursProfondeur
from models.Grid import Grid
from models.Node import Node
from views.GUI import GUI
import customtkinter as ctk
from controllers.InterfaceController import InterfaceController

if __name__ == "__main__":

    rows, cols = 3, 3
    hex_grid = Grid(rows, cols)
    for node in hex_grid.nodes.values():
        hex_grid.display_neighbors(node.x, node.y, node.z)

    hex_grid.display_grid()
    hex_grid.display_neighbors(0, 0, 0)

    # LANCEMENT -----------------------------------------------------------
    root = ctk.CTk()
    controller = InterfaceController(rows, cols)
    gui = GUI(root, controller, rows, cols)
    controller.set_view(gui)
    root.mainloop()
    # ---------------------------------------------------------------------
