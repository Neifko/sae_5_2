import math
from models.Grid import Grid

class InterfaceController:
    def __init__(self, rows, cols):
        self.view = None
        self.grid = Grid(rows, cols)
        self.hex_size = 30  # Taille initiale des hexagones

    def set_view(self, view):
        self.view = view

    def draw_grid(self):
        self.view.clear_canvas()
        rows = int(self.view.rows_entry.get())
        cols = int(self.view.cols_entry.get())

        # Recréer la grille avec les nouvelles dimensions
        self.grid = Grid(rows, cols)
        self.draw_hex_grid(rows, cols, self.hex_size)

    def draw_max_grid(self):
        self.view.clear_canvas()
        canvas_width = self.view.hex_canvas.winfo_width()
        canvas_height = self.view.hex_canvas.winfo_height()

        # Calcul du nombre maximum de colonnes et de rangées qui peuvent tenir dans la zone de dessin
        cols = int(canvas_width / (1.5 * self.hex_size))
        rows = int(canvas_height / (math.sqrt(3) * self.hex_size))

        # Mettre à jour les champs de saisie
        self.view.rows_entry.delete(0, 'end')
        self.view.rows_entry.insert(0, str(rows))
        self.view.cols_entry.delete(0, 'end')
        self.view.cols_entry.insert(0, str(cols))

        # Recréer la grille avec les nouvelles dimensions
        self.grid = Grid(rows, cols)
        self.draw_hex_grid(rows, cols, self.hex_size)

    def draw_hex_grid(self, rows, cols, size):
        font_size = max(8, int(size * 0.4))
        font = ("Arial", font_size)

        # Obtenir les coordonnées centrales de la zone de dessin
        canvas_center_x, canvas_center_y = self.view.get_canvas_center()

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

        # Ajuster les positions pour centrer l'hexagone (0, 0, 0)
        center_offset_x, center_offset_y = positions[(0, 0, 0)]
        for key in positions:
            positions[key] = (
                positions[key][0] - center_offset_x + canvas_center_x,
                positions[key][1] - center_offset_y + canvas_center_y
            )

        # Dessiner les hexagones
        for (x, y, z), (px, py) in positions.items():
            coord = f"({x},{y},{z})"
            self.view.draw_hexagon(px, py, size, "white", coord if self.view.show_coords_switch.get() else None)

    def get_direction_offset(self, direction, size):
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

    def toggle_coords(self):
        if self.grid:
            self.view.clear_canvas()
            self.draw_hex_grid(self.grid.rows, self.grid.cols, self.hex_size)

    def update_hex_size(self, size):
        self.hex_size = int(size)
        if self.grid:
            self.view.clear_canvas()
            self.draw_hex_grid(self.grid.rows, self.grid.cols, self.hex_size)
