import customtkinter as ctk

class TopNavbar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

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

    def clear_canvas(self):
        pass

    def clear_results(self):
        pass

    def random_case_colors(self):
        pass

    def call_profondeur(self):
        pass


