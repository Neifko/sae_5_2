import customtkinter as ctk

# Fenêtre principale
window = ctk.CTk()
window.title("Hexagones")
window.geometry("1000x600")

# Création des boutons de couleur
color_buttons_frame = ctk.CTkFrame(window)
color_buttons_frame.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.Y)

colors = ["Black", "White", "Blue", "Green", "Yellow", "Départ", "Objectif"]
for color in colors:
    button = ctk.CTkButton(color_buttons_frame, text=color, command=lambda c=color: print(c))
    button.pack(fill=ctk.X, padx=5, pady=2)

# Cadre principal pour les boutons et la zone de dessin
main_frame = ctk.CTkFrame(window)
main_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

# Création des boutons d'action
action_buttons_frame = ctk.CTkFrame(main_frame)
action_buttons_frame.pack(side=ctk.TOP, fill=ctk.X, padx=10, pady=5)

actions = ["Effacer Tout", "Effacer Résultats", "Aléatoire", "Parcours en profondeur", "Parcours en largeur", "Bellman-Ford", "Dijkstra", "A*"]
for action in actions:
    button = ctk.CTkButton(action_buttons_frame, text=action, command=lambda a=action: print(a))
    button.pack(side=ctk.LEFT, padx=5, pady=5)

# Zone de dessin des hexagones (pour l'instant vide)
hex_canvas = ctk.CTkCanvas(main_frame, bg="white")
hex_canvas.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# Lancer la fenêtre principale
window.mainloop()
