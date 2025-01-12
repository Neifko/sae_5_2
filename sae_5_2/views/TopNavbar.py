import tkinter as tk
import customtkinter as ctk

class TopNavbar(ctk.CTkFrame):
    def __init__(self, parent):
        # Obtenir le mode actuel (clair ou sombre)
        appearance_mode = ctk.get_appearance_mode()

        # Définir la couleur de fond en fonction du mode actuel
        if appearance_mode == "Dark":
            bg_color = "#2B2B2B"  # Couleur de fond pour le mode sombre
        else:
            bg_color = "white"  # Couleur de fond pour le mode clair

        super().__init__(parent, fg_color=bg_color)

        self.parent = parent

        # Créer un tk.Frame pour contenir le tk.Canvas
        self.frame = tk.Frame(self, bg=bg_color)
        self.frame.pack(fill="x", expand=False)

        # Créer un tk.Canvas dans le tk.Frame
        self.canvas = tk.Canvas(self.frame, bg=bg_color, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Lier l'événement de défilement de la molette au Canvas
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)  # Pour Windows
        self.canvas.bind_all("<Button-4>", self.on_mouse_wheel)    # Pour Linux (molette vers le haut)
        self.canvas.bind_all("<Button-5>", self.on_mouse_wheel)    # Pour Linux (molette vers le bas)

        # Créer un tk.Frame dans le tk.Canvas pour contenir les boutons
        self.inner_frame = tk.Frame(self.canvas, bg=bg_color)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        actions = ["Effacer Tout", "Effacer Résultats", "Aléatoire", "Parcours en profondeur", "Parcours en largeur",
                   "Bellman-Ford", "Dijkstra", "A*"]
        for action in actions:
            if action == "Effacer Tout":
                button = ctk.CTkButton(self.inner_frame, text=action, command=self.clear_canvas)
            elif action == "Effacer Résultats":
                button = ctk.CTkButton(self.inner_frame, text=action, command=self.clear_results)
            elif action == "Aléatoire":
                button = ctk.CTkButton(self.inner_frame, text=action, command=self.random_case_colors)
            elif action == "Parcours en profondeur":
                button = ctk.CTkButton(self.inner_frame, text=action, command=self.call_profondeur)
            elif action == "Parcours en largeur":
                button = ctk.CTkButton(self.inner_frame, text=action, command=self.call_largeur)
            else:
                button = ctk.CTkButton(self.inner_frame, text=action, command=lambda a=action: print(a))
            button.pack(side=tk.LEFT, padx=5, pady=5)

        # Mettre à jour la zone de défilement après avoir ajouté les boutons
        self.inner_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Ajuster la hauteur du frame et du canvas en fonction de la hauteur des boutons
        button_height = button.winfo_height()
        extra_margin = 10  # Marge supplémentaire
        total_height = button_height + extra_margin
        self.frame.config(height=total_height)
        self.canvas.config(height=total_height)

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

    def on_mouse_wheel(self, event):
        # Défiler horizontalement en fonction de l'événement de la molette
        if event.delta:  # Pour Windows
            self.canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
        else:  # Pour Linux
            if event.num == 4:
                self.canvas.xview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.xview_scroll(1, "units")

    def call_largeur(self):
        self.get_controller().call_largeur()
