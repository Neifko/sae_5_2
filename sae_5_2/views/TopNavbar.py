import customtkinter as ctk

class TopNavbar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        actions = ["Effacer Tout", "Effacer Résultats", "Aléatoire", "Parcours en profondeur", "Parcours en largeur",
                   "Bellman-Ford", "Dijkstra", "A*"]
        for action in actions:
            if action == "Effacer Tout":
                button = ctk.CTkButton(self, text=action, command=self.clear_canvas)
            elif action == "Effacer Résultats":
                button = ctk.CTkButton(self, text=action, command=self.clear_results)
            elif action == "Aléatoire":
                button = ctk.CTkButton(self, text=action, command=self.random_case_colors)
            elif action == "Parcours en profondeur":
                button = ctk.CTkButton(self, text=action, command=self.call_profondeur)
            else:
                button = ctk.CTkButton(self, text=action, command=lambda a=action: print(a))
            button.pack(side=ctk.LEFT, padx=5, pady=5)

    def get_controller(self):
        return self.parent.get_controller()

    def clear_canvas(self):
        self.get_controller().clear_canvas()

    def clear_results(self):
        self.get_controller().clear_results()

    def random_case_colors(self):
        self.get_controller().random_case_colors()

    def call_profondeur(self):
        self.get_controller().call_profondeur()


