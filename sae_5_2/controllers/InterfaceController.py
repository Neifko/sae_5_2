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

        self.draw_hex_grid(rows, cols, self.hex_size)

    def draw_hex_grid(self, rows, cols, size):
        font_size = max(8, int(size * 0.4))
        font = ("Arial", font_size)
        for row in range(rows):
            for col in range(cols):
                x = 1.5 * size * col + size
                y = math.sqrt(3) * size * (row + 0.5 * (col % 2)) + size
                coord = f"({col},{row},{-col-row})"
                self.view.draw_hexagon(x, y, size, "white", coord if self.view.show_coords_switch.get() else None)

    def toggle_coords(self):
        if self.grid:
            self.view.clear_canvas()
            self.draw_hex_grid(self.grid.rows, self.grid.cols, self.hex_size)

    def update_hex_size(self, size):
        self.hex_size = int(size)
        if self.grid:
            self.view.clear_canvas()
            self.draw_hex_grid(self.grid.rows, self.grid.cols, self.hex_size)
