import math

class ButtonHandlers:
    def set_depart(self):
        self.depart_mode = True
        self.objectif_mode = False

    def set_objectif(self):
        self.depart_mode = False
        self.objectif_mode = True

    def on_canvas_click(self, event):
        # Trouver l'hexagone le plus proche du clic
        closest_hex = self.find_closest_hexagon(event.x, event.y)
        if closest_hex:
            x, y = closest_hex
            hex_id = self.hexagons[(x, y)]
            if self.depart_mode:
                if self.depart_hex:
                    self.hex_canvas.itemconfig(self.depart_hex, fill="white")
                self.depart_hex = hex_id
                self.hex_canvas.itemconfig(hex_id, fill="pink")
            elif self.objectif_mode:
                if self.objectif_hex:
                    self.hex_canvas.itemconfig(self.objectif_hex, fill="white")
                self.objectif_hex = hex_id
                self.hex_canvas.itemconfig(hex_id, fill="red")

    def find_closest_hexagon(self, click_x, click_y):
        # Trouver l'hexagone le plus proche du clic
        closest_hex = None
        min_distance = float('inf')
        for (x, y), hex_id in self.hexagons.items():
            distance = math.sqrt((click_x - x) ** 2 + (click_y - y) ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_hex = (x, y)
        return closest_hex

    def toggle_coords(self):
        if self.controller.grid:
            self.clear_canvas()
            self.controller.draw_hex_grid(self.controller.grid.rows, self.controller.grid.cols, self.controller.hex_size)
            # Restaurer les cases de départ et d'objectif
            self.restore_special_hexagons()

    def update_hex_size(self, size):
        self.controller.hex_size = int(size)
        if self.controller.grid:
            self.clear_canvas()
            self.controller.draw_hex_grid(self.controller.grid.rows, self.controller.grid.cols, self.controller.hex_size)
            # Restaurer les cases de départ et d'objectif
            self.restore_special_hexagons()

    def restore_special_hexagons(self):
        if self.depart_hex:
            self.hex_canvas.itemconfig(self.depart_hex, fill="pink")
        if self.objectif_hex:
            self.hex_canvas.itemconfig(self.objectif_hex, fill="red")
