from models.Grid import Grid
import math

class InterfaceController:
    def __init__(self):
        self.view = None
        self.grid = None

    def set_view(self, view):
        self.view = view

    def draw_grid(self):
        self.view.clear_canvas()
        rows = int(self.view.rows_entry.get())
        cols = int(self.view.cols_entry.get())
        size = 30
        self.grid = Grid(rows, cols)
        self.grid.display_grid()
        self.grid.display_neighbors(0, 1, -1)
        self.draw_hex_grid(rows, cols, size)

    def draw_hex_grid(self, rows, cols, size):
        for row in range(rows):
            for col in range(cols):
                x = 1.5 * size * col + size
                y = math.sqrt(3) * size * (row + 0.5 * (col % 2)) + size
                coord = f"({col},{row},{-col-row})"
                self.view.draw_hexagon(x, y, size, "white", coord if self.view.show_coords_switch.get() else None)