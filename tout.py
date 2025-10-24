print("May Studios présente")
print("Jeu de Cartes - Version 0.1.3)

# ------------------ CONSTANTES DE TALENTS ET STATISTIQUES ------------------
BOUCLIER_BRUT = "Bouclier Brut"
EPEE_BRUTE = "Epée Brute"
DIVISION = "Division"
PIQUE_COEUR = "Pique-coeur"
IODE = "Iode"
BONUS_ROYAL = "Bonus Royal"
RESTER = "Rester"
PARA_CHUTE = "Para-Chute"
STATISTIQUE_ATTAQUE = "attaque"
STATISTIQUE_VIE = "vie"

# ------------------ IMPORTS ------------------
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import random
import math
from PIL import Image

# ------------------ DONNÉES DU JEU ------------------
personnages = {
    "perso1": {"nom": "Chevalier Rouge", "pv": 100, "attaque": 25, "defense": 15, "vitesse": 10},
    "perso2": {"nom": "Mage Bleu", "pv": 70, "attaque": 40, "defense": 10, "vitesse": 20},
    "perso3": {"nom": "Archer Vert", "pv": 85, "attaque": 30, "defense": 12, "vitesse": 25},
}


# ------------------ CONFIGURATION DE L'APPLICATION ------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ------------------ CLASSE PRINCIPALE ------------------
class JeuDeCartes(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Fenêtre principale
        self.title("Jeu de cartes par May Studio")
        self.geometry("800x600")
        self.minsize(600, 400)

        self.sauvegardeencours = ""

        # Barre de menu en haut
        self.creer_menu_ctk()

        # Frames principales
        self.frames = {}
        for F in (MenuFrame, JouerFrame, ADMFrame, FuturParametresFrame, IUADMFrame , IUInGameFrame, EditorSkinFrame , MatchMaking, SkinFrame, CombatVsAutreFrame, CombatVsBotFrame, ParametresFrame, CreditsFrame):
            frame = F(self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1, rely=0.08)  # Décalage à cause de la barre du haut

        self.show_frame(MenuFrame)

    # ------------------ BARRE DE MENU CUSTOM ------------------
    def creer_menu_ctk(self):
        menu_bar = ctk.CTkFrame(self, fg_color="#222", height=50)
        menu_bar.place(relx=0, rely=0, relwidth=1)

        # Boutons du menu
        ctk.CTkButton(menu_bar, text="💾 Enregistrer", width=120, height=30,
                    command=self.save).place(relx=0.02, rely=0.15)
        ctk.CTkButton(menu_bar, text="🆕 Nouvelle partie", width=150, height=30,
                    command=self.newgame).place(relx=0.20, rely=0.15)
        ctk.CTkButton(menu_bar, text="📂 Charger", width=120, height=30,
                    command=self.load).place(relx=0.43, rely=0.15)
        ctk.CTkButton(menu_bar, text="❌ Quitter", width=100, height=30,
                    fg_color="red", hover_color="#aa0000",
                    command=self.quit).place(relx=0.86, rely=0.15)

    # ------------------ MÉTHODES DE GESTION DE SAUVEGARDE ------------------
    def save(self):
        with open("sauvegarde_jeu_de_carte_MayStudio.txt", "w") as fichier:
            fichier.write(self.sauvegardeencours)
        print("💾 Partie enregistrée.")

    def newgame(self):
        self.sauvegardeencours = ""
        with open("sauvegarde_jeu_de_carte_MayStudio.txt", "w") as fichier:
            fichier.write("")
        print("🎮 Nouvelle partie lancée.")

    def load(self):
        try:
            with open("sauvegarde_jeu_de_carte_MayStudio.txt", "r") as fichier:
                self.sauvegardeencours = fichier.read()
            print("📂 Partie chargée.")
        except FileNotFoundError:
            print("⚠️ Aucune sauvegarde trouvée.")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# ------------------ PAGE : MENU PRINCIPAL ------------------
class MenuFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="red")

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(container, text="Jeu de cartes par May Studio",
                    font=("Arial", 32, "bold"), text_color="white").pack(pady=(0, 40))

        ctk.CTkButton(container, text="Jouer",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(JouerFrame)).pack(pady=10)
        
        ctk.CTkButton(container, text="Skin",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(SkinFrame)).pack(pady=10)

        ctk.CTkButton(container, text="Paramètres",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(ParametresFrame)).pack(pady=10)

        ctk.CTkButton(container, text="Crédits",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(CreditsFrame)).pack(pady=10)
        
        
        ctk.CTkButton(container, text="ADM",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(ADMFrame)).pack(pady=10)

        # ✅ Nouveau bouton : Fermer le jeu
        ctk.CTkButton(container, text="Fermer le jeu",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    fg_color="darkred", hover_color="#aa0000",
                    command=master.quit).pack(pady=20)
        

# ------------------ PAGE : SKIN ------------------

class SkinFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")

        # ------------------ LISTE DES SKINS ------------------
        self.skins = [
            {"nom": "Skin 1", "image": "images/S1.jpg"},
            {"nom": "Skin 2", "image": "images/S2.jpg"},
        ]
        self.index_skin = 0

        # ------------------ TITRE ------------------
        ctk.CTkLabel(self, text="Mode : Skin",
                    font=("Arial", 28, "bold")).pack(pady=40)

        # ------------------ IMAGE DU SKIN ------------------
        image = Image.open(self.skins[self.index_skin]["image"])
        image = image.resize((200, 200))  # Ajuste la taille si besoin
        self.ctk_image = ctk.CTkImage(image, size=(200, 200))

        self.image_label = ctk.CTkLabel(self, image=self.ctk_image, text="")
        self.image_label.pack(pady=10)

        # ------------------ NOM DU SKIN ------------------
        self.label_skin = ctk.CTkLabel(
            self,
            text=f"Skin actuel : {self.skins[self.index_skin]['nom']}",
            font=("Arial", 20)
        )
        self.label_skin.pack(pady=10)

        # ------------------ BOUTONS ------------------
        ctk.CTkButton(
            self,
            text="Skin suivant",
            width=200,
            height=40,
            command=self.suivant_skin
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="Retour au menu",
            width=200,
            height=40,
            command=lambda: master.show_frame(MenuFrame)
        ).pack(pady=20)

    # ------------------ CHANGEMENT DE SKIN ------------------
    def suivant_skin(self):
        """Passe au skin suivant et met à jour le visuel."""
        self.index_skin = (self.index_skin + 1) % len(self.skins)

        # Met à jour le texte
        self.label_skin.configure(
            text=f"Skin actuel : {self.skins[self.index_skin]['nom']}"
        )

        # Met à jour l’image
        image = Image.open(self.skins[self.index_skin]["image"])
        image = image.resize((200, 200))
        self.ctk_image = ctk.CTkImage(image, size=(200, 200))
        self.image_label.configure(image=self.ctk_image)


#--------------------ADM---------------------------
class ADMFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(container, text="ADM",
                    font=("Arial", 32, "bold"), text_color="white").pack(pady=(0, 40))

        ctk.CTkButton(container, text="IU Jouer",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(IUInGameFrame)).pack(pady=10)
        
        ctk.CTkButton(container, text="Editer Skin",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(EditorSkinFrame)).pack(pady=10)

        ctk.CTkButton(container, text="Paramètres",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(FuturParametresFrame)).pack(pady=10)

        ctk.CTkButton(container, text="Profil",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(ProfilFrame)).pack(pady=10)
        
        
        ctk.CTkButton(container, text="IUADM",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(IUADMFrame)).pack(pady=10)

        # ✅ Nouveau bouton : Fermer le jeu
        ctk.CTkButton(container, text="Fermer le jeu",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    fg_color="darkred", hover_color="#aa0000",
                    command=master.quit).pack(pady=20)

class IUInGameFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")

        # ===================== TITRE ET PROGRESS BAR =====================
        top_bar = ctk.CTkFrame(self, fg_color="transparent")
        top_bar.pack(fill="x", pady=(5, 0))
        ctk.CTkLabel(top_bar, text="Manche 1", font=("Arial", 20, "bold")).pack(pady=(5, 3))
        self.progress_bar = ctk.CTkProgressBar(top_bar, width=300)
        self.progress_bar.pack()
        self.progress_bar.set(0.5)

        # ===================== ZONE DE JEU =====================
        table_frame = ctk.CTkFrame(self, fg_color="#5a0f0f", corner_radius=20)
        table_frame.pack(expand=True, fill="both", padx=20, pady=10)
        ctk.CTkLabel(table_frame, text="Zone de jeu", font=("Arial", 18, "bold")).place(relx=0.5, rely=0.05, anchor="center")

        # ---- CARTES POSÉES (VERTICALES) ----
        self.cards_zone = ctk.CTkFrame(table_frame, fg_color="transparent")
        self.cards_zone.place(relx=0.5, rely=0.5, anchor="center")

        adv_card_border = ctk.CTkFrame(self.cards_zone, width=130, height=180, fg_color="transparent",
                                    border_color="white", border_width=3, corner_radius=10)
        adv_card_border.pack(pady=70)
        ctk.CTkLabel(adv_card_border, text="Carte adverse", text_color="white").place(relx=0.5, rely=0.5, anchor="center")

        player_card_border = ctk.CTkFrame(self.cards_zone, width=130, height=180, fg_color="transparent",
                                        border_color="white", border_width=3, corner_radius=10)
        player_card_border.pack(pady=70)
        ctk.CTkLabel(player_card_border, text="Votre carte", text_color="white").place(relx=0.5, rely=0.5, anchor="center")

        # ===================== INFO ADVERSAIRE =====================
        adv_info = ctk.CTkFrame(table_frame, width=180, height=80, fg_color="#3b0a0a", corner_radius=10)
        adv_info.place(relx=0.97, rely=0.08, anchor="ne")
        adv_info.pack_propagate(False)
        ctk.CTkLabel(adv_info, text="Cartes adversaire", font=("Arial", 14, "bold")).pack(pady=3)
        self.nb_cartes_adv = ctk.CTkLabel(adv_info, text="Nombre : 5", font=("Arial", 16))
        self.nb_cartes_adv.pack()

        # ===================== CHAT FLOTTANT =====================
        self.chat_frame = ctk.CTkFrame(self, width=220, height=170, fg_color="#3b0a0a", corner_radius=10)
        self.chat_frame.place(x=40, y=100)
        self.chat_frame.pack_propagate(False)
        ctk.CTkLabel(self.chat_frame, text="💬 Chat", font=("Arial", 14, "bold")).pack(anchor="w", padx=5, pady=3)
        self.chat_box = ctk.CTkTextbox(self.chat_frame, width=200, height=80)
        self.chat_box.pack(padx=5, pady=5)
        self.chat_entry = ctk.CTkEntry(self.chat_frame, placeholder_text="Écrire un message...")
        self.chat_entry.pack(fill="x", padx=5, pady=(0, 5))
        self.chat_entry.bind("<Return>", self.send_message)
        self.chat_frame.bind("<Button-1>", self.start_move_chat)
        self.chat_frame.bind("<B1-Motion>", self.do_move_chat)

        # ===================== PANEL D’INFOS À DROITE =====================
        self.info_frame = ctk.CTkFrame(self, width=260, fg_color="#3b0a0a", corner_radius=15)
        self.info_frame.place(relx=0.975, rely=0.5, anchor="e", relheight=0.55)
        self.info_frame.pack_propagate(False)

        ctk.CTkLabel(self.info_frame, text="📜 Carte sélectionnée", font=("Arial", 16, "bold")).pack(pady=(10, 5))
        self.card_name_label = ctk.CTkLabel(self.info_frame, text="Aucune carte", font=("Arial", 15))
        self.card_name_label.pack(pady=5)
        self.card_stats_label = ctk.CTkLabel(
            self.info_frame,
            text="Attaque : -\nDéfense : -\nMagie : -\nVitesse : -",
            font=("Arial", 13),
            justify="left"
        )
        self.card_stats_label.pack(pady=5)

        # ---- GRAPHIQUE RADAR COMPARATIF ----
        self.graph_frame = ctk.CTkFrame(self.info_frame, fg_color="#4d0f0f", corner_radius=10)
        self.graph_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # ---- BOUTON JOUER ----
        self.play_button = ctk.CTkButton(
            self.info_frame,
            text="🎯 Jouer cette carte",
            width=200,
            height=40,
            state="disabled",
            command=self.play_selected_card
        )
        self.play_button.pack(side="bottom", pady=10)

        # ===================== BAS : VOS CARTES =====================
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        bottom_frame.pack(side="bottom", fill="x", pady=(0, 40))
        player_cards_frame = ctk.CTkFrame(bottom_frame, fg_color="#3b0a0a", corner_radius=10)
        player_cards_frame.pack(side="left", padx=10)
        ctk.CTkLabel(player_cards_frame, text="Vos cartes :", font=("Arial", 14, "bold")).pack(pady=5)

        # --- Cartes cliquables ---
        self.cartes_joueur = []
        for i in range(5):
            stats = {
                "nom": f"Carte {i+1}",
                "Attaque": 10 + i * 3,
                "Défense": 5 + i * 2,
                "Magie": 7 + i * 1,
                "Vitesse": 8 + i * 2
            }
            carte = ctk.CTkButton(
                player_cards_frame,
                text=stats["nom"],
                width=80,
                height=100,
                command=lambda s=stats: self.select_card(s)
            )
            carte.pack(side="left", padx=5, pady=5)
            self.cartes_joueur.append(carte)

        menu_button = ctk.CTkButton(bottom_frame, text="Retour au menu", width=200, height=40,
                                    command=lambda: master.show_frame(master.frames[master.frames.keys().__iter__().__next__()]))
        menu_button.pack(side="right", padx=20)

    # ===================== CHAT =====================
    def send_message(self, event=None):
        msg = self.chat_entry.get().strip()
        if msg:
            self.chat_box.insert("end", f"Vous: {msg}\n")
            self.chat_box.see("end")
            self.chat_entry.delete(0, "end")
        else:
            messagebox.showwarning("Chat", "Message vide interdit !")

    def start_move_chat(self, event):
        self.chat_offset_x = event.x
        self.chat_offset_y = event.y

    def do_move_chat(self, event):
        x = self.chat_frame.winfo_x() + event.x - self.chat_offset_x
        y = self.chat_frame.winfo_y() + event.y - self.chat_offset_y
        self.chat_frame.place(x=x, y=y)

    # ===================== CARTE SÉLECTIONNÉE =====================
    def select_card(self, stats):
        self.card_name_label.configure(text=stats["nom"])
        self.card_stats_label.configure(
            text="\n".join([f"{k} : {v}" for k, v in stats.items() if k != "nom"])
        )
        self.play_button.configure(state="normal")
        self.selected_card = stats
        self.update_chart(stats)

    def play_selected_card(self):
        if hasattr(self, "selected_card"):
            messagebox.showinfo("Carte jouée", f"Vous avez joué {self.selected_card['nom']} !")
            self.play_button.configure(state="disabled")
            self.card_name_label.configure(text="Aucune carte")
            self.card_stats_label.configure(text="Attaque : -\nDéfense : -\nMagie : -\nVitesse : -")
            self.update_chart(None)

    # ===================== GRAPHIQUE RADAR =====================
    def update_chart(self, stats):
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        canvas_size = 220
        canvas = ctk.CTkCanvas(self.graph_frame, width=canvas_size, height=canvas_size,
                            bg="#4d0f0f", highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=5, pady=5)

        if not stats:
            canvas.create_text(canvas_size / 2, canvas_size / 2, text="Aucune carte",
                            fill="white", font=("Arial", 12))
            return

        categories = ["Attaque", "Défense", "Magie", "Vitesse"]
        n = len(categories)
        center = canvas_size / 2
        radius = canvas_size / 2 - 30
        values = [stats[c] for c in categories]
        max_value = max(values + [10])
        avg_values = [sum(values) / n for _ in range(n)]

        # ---- Fond radar ----
        steps = 4
        for s in range(1, steps + 1):
            r = radius * s / steps
            points = []
            for i in range(n):
                angle = (i / n) * 2 * math.pi - math.pi / 2
                x = center + r * math.cos(angle)
                y = center + r * math.sin(angle)
                points.append((x, y))
            for i in range(n):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % n]
                canvas.create_line(x1, y1, x2, y2, fill="#555555")
            canvas.create_text(center, max(5, center - r), text=str(int(max_value * s / steps)),
                            fill="#aaaaaa", font=("Arial", 8))

        # ---- Carte et moyenne ----
        points_card = []
        points_avg = []
        for i, val in enumerate(values):
            angle = (i / n) * 2 * math.pi - math.pi / 2
            r = (val / max_value) * radius
            x = center + r * math.cos(angle)
            y = center + r * math.sin(angle)
            points_card.append((x, y))
            r_avg = (avg_values[i] / max_value) * radius
            x_avg = center + r_avg * math.cos(angle)
            y_avg = center + r_avg * math.sin(angle)
            points_avg.append((x_avg, y_avg))

        canvas.create_polygon([coord for point in points_card for coord in point],
                            outline="#ff5555", fill="#ff5555", stipple="gray25", width=2)
        canvas.create_polygon([coord for point in points_avg for coord in point],
                            outline="#55ff55", fill="#55ff55", stipple="gray25", width=2)

        # ---- Lignes et points ----
        for x, y in points_card:
            canvas.create_line(center, center, x, y, fill="#ff5555", width=1)
        for x, y in points_avg:
            canvas.create_line(center, center, x, y, fill="#55ff55", width=1)
        for i, (x, y) in enumerate(points_card):
            canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="#ff5555")
            canvas.create_text(x, max(5, y - 14), text=str(values[i]), fill="#ff5555", font=("Arial", 9, "bold"))
        for i, (x, y) in enumerate(points_avg):
            canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="#55ff55")
            canvas.create_text(x, min(canvas_size - 5, y + 14), text=str(round(avg_values[i], 1)), fill="#55ff55", font=("Arial", 9))

        canvas.create_text(canvas_size - 50, 15, text="Carte", fill="#ff5555", font=("Arial", 10))
        canvas.create_text(canvas_size - 50, 30, text="Moyenne", fill="#55ff55", font=("Arial", 10))

#------------------ PAGE : EditorSkin ------------------
class EditorSkinFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")
        ctk.CTkLabel(self, text="Mode : Editeur de skin",
                    font=("Arial", 28, "bold")).pack(pady=40)

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                    command=lambda: master.show_frame(MenuFrame)).pack(pady=20)
        

#------------------ PAGE : FuturParametres ------------------
class FuturParametresFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")
        ctk.CTkLabel(self, text="Mode : Futur Paramètres",
                    font=("Arial", 28, "bold")).pack(pady=40)
        
        ctk.CTkLabel(self, text="Mode : ensibilité de la souris",
                    font=("Arial", 28, "bold")).pack(pady=40)
        
        ctk.CTkLabel(self, text="Mode : Taille de l'ecran",
                    font=("Arial", 28, "bold")).pack(pady=40)
        
        ctk.CTkLabel(self, text="Mode : Choix de la langue",
                    font=("Arial", 28, "bold")).pack(pady=40)
        
        ctk.CTkLabel(self, text="Mode : Thème du jeu",
                    font=("Arial", 28, "bold")).pack(pady=40)
        
        ctk.CTkLabel(self, text="Mode : Atribution des touches",
                    font=("Arial", 28, "bold")).pack(pady=40)

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                    command=lambda: master.show_frame(MenuFrame)).pack(pady=20)


#------------------ PAGE : Profil ------------------
class ProfilFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")
        ctk.CTkLabel(self, text="Mode : Nom du Joueur",
                    font=("Arial", 28, "bold")).pack(pady=40)
        
        ctk.CTkLabel(self, text="Badges" + "🏅" * 5,
                    font=("Arial", 28, "bold")).pack(pady=40)
        
        ctk.CTkLabel(self, text="Niveau : " + str(random.randint(1, 100)),
                    font=("Arial", 28, "bold")).pack(pady=40)
        
        ctk.CTkLabel(self, text="Description perso"+str(random.randint(1, 10000000)),
                    font=("Arial", 28, "bold")).pack(pady=40)

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                    command=lambda: master.show_frame(MenuFrame)).pack(pady=20)


# ---------------PAGE : IUADM -----------------
class IUADMFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                    command=lambda: master.show_frame(MenuFrame)).pack(pady=20)




# ---------------- PAGE : MATCHMAKING ---------------
class MatchMaking(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")
        ctk.CTkLabel(self, text="Mode : Matchmaking",
                    font=("Arial", 28, "bold")).pack(pady=40)

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                    command=lambda: master.show_frame(MenuFrame)).pack(pady=20)

        # --- Canvas pour l'animation ---
        self.canvas_size = 150
        self.canvas = ctk.CTkCanvas(self, width=self.canvas_size, height=self.canvas_size, bg="darkred", highlightthickness=0)
        self.canvas.pack(pady=30)

        self.angle = 0  # angle initial
        self.line_length = 60
        self.center = self.canvas_size // 2

        # Dessiner le cercle de rotation
        self.line = self.canvas.create_line(self.center, self.center,
                                            self.center + self.line_length, self.center,
                                            width=4, fill="white", capstyle="round")
        self.animate_circle()

    def animate_circle(self):
        # Calculer nouvelle position du bout du trait
        rad = math.radians(self.angle)
        x = self.center + self.line_length * math.cos(rad)
        y = self.center + self.line_length * math.sin(rad)

        # Mettre à jour la ligne
        self.canvas.coords(self.line, self.center, self.center, x, y)

        # Avancer l'angle
        self.angle = (self.angle + 5) % 360

        # Refaire l'animation toutes les 50ms
        self.after(50, self.animate_circle)


# ------------------ PAGE : JOUER ------------------
class JouerFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(container, text="Mode de jeu", font=("Arial", 28, "bold")).pack(pady=40)

        ctk.CTkButton(container, text="Combat vs autre (phase de test)",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(MatchMaking)).pack(pady=10)

        ctk.CTkButton(container, text="Combat vs bot (phase de test)",
                    width=300, height=50, font=("Arial", 18, "bold"),
                    command=lambda: master.show_frame(CombatVsBotFrame)).pack(pady=10)

        ctk.CTkButton(container, text="Retour au menu", width=200, height=40,
                        command=lambda: master.show_frame(MenuFrame)).pack(pady=40)
            



# ------------------ PAGE : COMBAT CONTRE UN AUTRE JOUEUR ------------------
class CombatVsAutreFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")
        ctk.CTkLabel(self, text="Mode : Combat contre un autre joueur",
                    font=("Arial", 28, "bold")).pack(pady=40)

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                    command=lambda: master.show_frame(MenuFrame)).pack(pady=20)


# ------------------ PAGE : COMBAT CONTRE BOT ------------------
class CombatVsBotFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")
        ctk.CTkLabel(self, text="Mode : Combat contre le bot",
                    font=("Arial", 28, "bold")).pack(pady=40)

        perso = personnages["perso2"]
        ctk.CTkLabel(self, text=f"{perso['nom']} — PV: {perso['pv']} | ATQ: {perso['attaque']} | DEF: {perso['defense']} | VIT: {perso['vitesse']}",
                    font=("Arial", 16)).pack(pady=10)

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                    command=lambda: master.show_frame(MenuFrame)).pack(pady=40)


# ------------------ PAGE : PARAMÈTRES ------------------
class ParametresFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")

        ctk.CTkLabel(self, text="Paramètres", font=("Arial", 28, "bold")).pack(pady=40)

        ctk.CTkLabel(self, text="Volume du jeu :", font=("Arial", 16)).pack(pady=10)
        ctk.CTkSlider(self, from_=0, to=100).pack(pady=10)

        ctk.CTkLabel(self, text="Nom du joueur :", font=("Arial", 16)).pack(pady=10)
        ctk.CTkEntry(self, placeholder_text="Entrez votre pseudo").pack(pady=10)

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                    command=lambda: master.show_frame(MenuFrame)).pack(pady=40)


# ------------------ PAGE : CRÉDITS ------------------
class CreditsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="black")

        ctk.CTkLabel(self, text="Crédits", font=("Arial", 28, "bold")).pack(pady=30)

        ctk.CTkLabel(self,
                    text=("Développé par May Studio (2025)\n"
                        "Merci d'avoir joué !\n\n"
                        "Version 0.1 (phase de test)\n\n"
                        "Code : Myfight\n"
                        "Graphismes : ISTOC Darius\n"
                        "une petite donnation ne lui ferait pas de mal :\n"
                        "buymeacoffee.com/DARIUSISTOC1\n"),
                    font=("Arial", 16)).pack(pady=10)

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                    command=lambda: master.show_frame(MenuFrame)).pack(pady=40)


# ------------------ LANCEMENT DU PROGRAMME ------------------
if __name__ == "__main__":
    app = JeuDeCartes()
    app.mainloop()

# ------------------ FIN DARIUS

class Cartes:
    def __init__(self, carte, nom, rarete, type_carte, attaque, vitesse, defense, vie, puissance, cout, talent, de_base=None, deux=None, trois=None, quatre=None, cinq=None, eau = None, feu = None, foudre = None, technologie = None, royaute = None, sorts_et_soins = None, mystere = None, chaos = None, apothicaire = None, terres_de_l_au_dela = None, monde_magique = None, talent_facultatif=None, artefact=None, capacite=None, specialite=None, statistique=None, statistique_en_cours=None, statistique_en_vigueur=None, roulement=None, statistique_privilegiee=None, statistique_par_type=None, compteur_de_tours = None, tour_actuel = None, carte_possedee = None, carte_adverse = None, valeur_tiree = None):
        self.carte = carte
        self.nom = nom
        self.rarete = rarete
        self.type_carte = type_carte
        self.specialite = specialite

        self.eau = eau
        self.feu = feu
        self.foudre = foudre
        self.technologie = technologie
        self.royaute = royaute
        self.sorts_et_soins = sorts_et_soins
        self.mystere = mystere

        self.chaos = chaos
        self.terres_de_l_au_dela = terres_de_l_au_dela
        self.apothicaire = apothicaire
        self.monde_magique = monde_magique

        self.attaque = attaque
        self.vitesse = vitesse
        self.defense = defense
        self.vie = vie
        self.puissance = puissance
        self.de_base = de_base

        self.deux = deux
        self.trois = trois
        self.quatre = quatre
        self.cinq = cinq

        self.cout = cout
        self.talent = talent
        self.talent_facultatif = talent_facultatif
        self.artefact = artefact
        self.capacite = capacite

        self.statistique = statistique
        self.statistique_en_cours = statistique_en_cours
        self.statistique_en_vigueur = statistique_en_vigueur
        self.statistique_privilegiee = statistique_privilegiee
        self.statistique_par_type = statistique_par_type
        self.valeur_tiree = valeur_tiree

        self.roulement = roulement
        self.seconde = vie * 125

        self.compteur_de_tours = compteur_de_tours
        self.tour_actuel = tour_actuel
        self.carte_possedee = carte_possedee
        self.carte_adverse = carte_adverse

    def bibliotheque_de_types(self):
        types = {
            self.eau : "Eau",
            self.feu : "Feu",
            self.foudre : "Foudre",
            self.technologie : "Technologie",
            self.royaute : "Royauté",
            self.sorts_et_soins : "Sorts et soins",
            self.mystere : "Mystère"
        }
    
    def bibliotheque_de_rarete(self):
        rarete = {
            self.commune : "Commune",
            self.rare : "Rare",
            self.epique : "Epique",
            self.mythique : "Mythique",
            self.legendaire : "Légendaire",
            self.champion : "Champion"
        }
        
       
    class bibliotheque_de_carte:  
        class Tireur_Aquatique:   
            def Tireur_Aquatique(self):  
                self.nom = "Tireur Aquatique"
                self.numero = "1"
                self.rarete = "Commune"
                self.type_carte = "Eau"
                self.attaque.de_base = 150
                self.vitesse.de_base = 1.25
                self.defense.de_base = 5
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Bouclier Brut"
                
        class Tireur_de_Lave:   
            def Tireur_de_Lave(self):  
                self.nom = "Tireur de Lave"
                self.numero = "2"
                self.rarete = "Commune"
                self.type_carte = "Feu"
                self.attaque.de_base = 200
                self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Epée Brute"
        
        class Chasseuse_Orage:   
            def Chasseuse_Orage(self):  
                self.nom = "Chasseuse d'Orage"
                self.numero = "3"
                self.rarete = "Rare"
                self.type_carte = "Foudre"
                self.attaque.de_base = 100
                self.vitesse.de_base = 2
                self.defense.de_base = 6
                self.vie.de_base = 2000
                self.puissance.de_base = 4
                self.cout = 5
                self.talent = "Division"
                
        class Araignee_Mecanique:   
            def Araignee_Mecanique(self):  
                self.nom = "Araignée Mécanique"
                self.numero = "4"
                self.rarete = "Commune"
                self.type_carte = "Technologie"
                self.attaque.de_base = 100
                self.vitesse.de_base = 1
                self.defense.de_base = 8
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Goutte Empoisonnée"
                
        class Chevalier:   
            def Chevalier(self):  
                self.nom = "Chevalier"
                self.numero = "5"
                self.rarete = "Rare"
                self.type_carte = "Royauté"
                self.attaque.de_base = 100
                self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 3000
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Pique-coeur"
                
        class Tsunami:   
            def Tsunami(self):  
                self.nom = "Tsunami"
                self.numero = "6"
                self.rarete = "Rare"
                self.type_carte = "Eau"
                self.attaque.de_base = 300
                self.vitesse.de_base = 1
                self.defense.de_base = 0
                self.vie.de_base = 0
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Iode"
                
        class Dragon:   
            def Dragon(self):  
                self.nom = "Dragon"
                self.numero = "7"
                self.rarete = "Légendaire"
                self.type_carte = "Feu"
                self.attaque.de_base = 500
                self.vitesse.de_base = 0.5
                self.defense.de_base = 3
                self.vie.de_base = 2000
                self.puissance.de_base = 5
                self.cout = 6
                self.talent = "Bonus Royal"
                
        class Aura_Sphere:
            def __init__(self):
                self.nom = "Aura-Sphère"
                self.numero = "8"
                self.rarete = "Mythique"
                self.type_carte = "Foudre"
                self.attaque = 100
                self.vitesse = 1.25
                self.defense = 0
                self.vie = 10
                self.puissance = 5
                self.cout = 5
                self.talent = "Rester"
                
        class Guerrier_Aerien:
            def __init__(self):
                self.nom = "Guerrier Aérien"
                self.numero = "9"
                self.rarete = "Epique"
                self.type_carte = "Royauté"
                self.attaque = 225
                self.vitesse = 1
                self.defense = 6
                self.vie = 1500
                self.puissance = 6
                self.cout = 4
                self.talent = "Para-Chute"
                
        class Roue_Gobeline:
            def __init__(self):
                self.nom = "Roue Gobeline"
                self.numero = "10"
                self.rarete = "Rare"
                self.type_carte = "Technologie"
                self.attaque = 125
                self.attaque_deux = 75
                self.vitesse = 1
                self.vitesse_deux = 3
                self.defense = 10
                self.defense_deux = 4
                self.vie = 0
                self.vie_deux = 250
                self.puissance = 3
                self.cout = 4
                self.talent = "Bonus Royal"
                
        class Chat_de_Compagnie:
            def __init__(self):
                self.nom = "Chat de Compagnie"
                self.numero = "11"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque = 300
                self.attaque_deux = 150
                self.vitesse = 1
                self.vitesse_deux = 1.5
                self.defense = 6
                self.vie = 1500
                self.puissance = 5
                self.cout = 3
                self.talent = "Système Tactique"
                
        class Chien_de_Compagnie:
            def __init__(self):
                self.nom = "Chien de Compagnie"
                self.numero = "12"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque = 550
                self.attaque_deux = 225
                self.vitesse = 1
                self.vitesse_deux = 0.75
                self.defense = 6
                self.vie = 1500
                self.puissance = 5
                self.cout = 3
                self.talent = "Système Tactique"
                
        class Guerriers_Elite:
            def __init__(self):
                self.nom = "Guerriers d'Elite"
                self.numero = "13"
                self.rarete = "Epique"
                self.type_carte = "Royauté"
                self.attaque = 225
                self.vitesse = 2
                self.defense = 6
                self.vie = 1500
                self.puissance = 5
                self.cout = 6
                self.talent = "Epée Brute"
                
        class Phonosort:
            def __init__(self):
                self.nom = "Phonosort"
                self.numero = "14"
                self.rarete = "Mythique"
                self.type_carte = "Sorts et soins"
                self.attaque = 150
                self.vitesse = 1
                self.defense = 0
                self.vie = 250
                self.puissance = 2
                self.cout = 2
                self.talent = "Rester"
                
        class Tornade:
            def __init__(self):
                self.nom = "Tornade"
                self.numero = "15"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque = 200
                self.vitesse = 1
                self.defense = 10
                self.vie = 625
                self.puissance = 3
                self.cout = 3
                self.talent = "Emport"
                
        class Drone:
            def __init__(self):
                self.nom = "Drone"
                self.numero = "16"
                self.rarete = "Mythique"
                self.type_carte = "Technologie"
                self.attaque = 300
                self.vitesse = 0.75
                self.defense = 6
                self.vie = 1750
                self.puissance = 5
                self.cout = 4
                self.talent = "Statique"
                
        class Incendie:
            def __init__(self):
                self.nom = "Incendie"
                self.numero = "17"
                self.rarete = "Légendaire"
                self.type_carte = "Feu"
                self.attaque = 200
                self.vitesse = 0.5
                self.defense = 0
                self.vie = 625
                self.puissance = 3
                self.cout = 3
                self.talent = "Bonus Royal"
                
        class Prison:
            def __init__(self):
                self.nom = "Prison"
                self.numero = "18"
                self.rarete = "Légendaire"
                self.type_carte = "Mystère"
                self.attaque = 25
                self.vitesse = 1
                self.defense = 6
                self.vie = 2000
                self.puissance = 4
                self.cout = 4
                self.talent = "Rester"
                
        class Elektromanipulatrice:
            def __init__(self):
                self.nom = "Elektromanipulatrice"
                self.numero = "19"
                self.rarete = "Mythique"
                self.type_carte = "Foudre"
                self.attaque = 750
                self.vitesse = 0.25
                self.defense = 6
                self.vie = 2000
                self.puissance = 7
                self.cout = 7
                self.talent = "Division"
                
        class Bombe:
            def __init__(self):
                self.nom = "Bombe"
                self.numero = "20"
                self.rarete = "Commune"
                self.type_carte = "Technologie"
                self.attaque = 300
                self.vitesse = 1
                self.defense = 0
                self.vie = 0
                self.puissance = 5
                self.cout = 3
                self.talent = "Fibulatio"
                
        class Cage_Elite:
            def __init__(self):
                self.nom = "Cage_Elite"
                self.numero = "21"
                self.rarete = "Commune"
                self.type_carte = "Royauté"
                self.attaque = 0
                self.attaque_deux = 225
                self.vitesse = 0
                self.vitesse_deux = 1
                self.defense = 6
                self.vie = 15
                self.vie_deux = 1500
                self.puissance = 3
                self.cout = 4
                self.talent = "Couverture Explosive"
                
        class Cow_Boy:
            def __init__(self):
                self.nom = "Cow-Boy"
                self.numero = "22"
                self.rarete = "Mythique"
                self.type_carte = "Mystère"
                self.attaque = 100
                self.vitesse = 1
                self.defense = 5
                self.vie = 1500
                self.puissance = 5
                self.cout = 4
                self.talent = "Mirage"
                
        class Lianes:
            def __init__(self):
                self.nom = "Lianes"
                self.numero = "23"
                self.rarete = "Commune"
                self.type_carte = "Mystère"
                self.attaque = 200
                self.vitesse = 1
                self.defense = 6
                self.vie = 5
                self.puissance = 4
                self.cout = 3
                self.talent = "Rester"
                
        class Cyclope:
            def __init__(self):
                self.nom = "Cyclope"
                self.numero = "24"
                self.rarete = "Rare"
                self.type_carte = "Mystère"
                self.attaque = 250
                self.vitesse = 0.75
                self.defense = 6
                self.vie = 2000
                self.puissance = 5
                self.cout = 5
                self.talent = "Maladresse"
                
        class Avion_Elite:
            def __init__(self):
                self.nom = "Avion d'Elite"
                self.numero = "25"
                self.rarete = "Epique"
                self.type_carte = "Royauté"
                self.attaque = 400
                self.attaque_deux = 225
                self.vitesse = 1
                self.vitesse_deux = 3
                self.defense = 6
                self.vie = 2000
                self.vie_deux = 1500
                self.puissance = 6
                self.cout = 7
                self.talent = "Largage Progressif"

        class Oleomage:
            def __init__(self):
                self.nom = "Oléomage"
                self.numero = "26"
                self.rarete = "Epique"
                self.type_carte = "Sorts et soins"
                self.attaque = 200
                self.vitesse = 0.5
                self.defense = 5
                self.vie = 2000
                self.puissance = 4
                self.cout = 3
                self.talent = "Emport"

        class Tour_Energie:
            def __init__(self):
                self.nom = "Tour d'Energie"
                self.numero = "27"
                self.rarete = "Mythique"
                self.type_carte = "Mystère"
                self.attaque = 350
                self.vitesse = 0.5
                self.defense = 6
                self.vie = 3000
                self.puissance = 3
                self.cout = 6
                self.talent = "Signal"

        class Orage:
            def __init__(self):
                self.nom = "Orage"
                self.numero = "28"
                self.rarete = "Epique"
                self.type_carte = "Foudre"
                self.attaque = 200
                self.vitesse = 1
                self.defense = 0
                self.vie = 0
                self.puissance = 5
                self.cout = 2
                self.talent = "Division"

        class Garde_Glace:
            def __init__(self):
                self.nom = "Garde-Glace"
                self.numero = "29"
                self.rarete = "Mythique"
                self.type_carte = "Royauté"
                self.attaque = 250
                self.vitesse = 0.75
                self.defense = 6
                self.vie = 3000
                self.puissance = 3
                self.cout = 4
                self.talent = "Cryogénisation"

        class Vent_Glacial:
            def __init__(self):
                self.nom = "Vent Glacial"
                self.numero = "30"
                self.rarete = "Mythique"
                self.type_carte = "Sorts et soins"
                self.attaque = 100
                self.vitesse = 1
                self.defense = 0
                self.vie = 5
                self.puissance = 5
                self.cout = 3
                self.talent = "Cryogénisation"

        class Pyromancien:
            def __init__(self):
                self.nom = "Pyromancien"
                self.numero = "31"
                self.rarete = "Légendaire"
                self.type_carte = "Sorts et soins"
                self.attaque = 200
                self.vitesse = 1
                self.defense = 5
                self.vie = 1500
                self.puissance = 5
                self.cout = 3
                self.talent = "Fibulatio"

        class Cryomancien:
            def __init__(self):
                self.nom = "Cryomancien"
                self.numero = "32"
                self.rarete = "Légendaire"
                self.type_carte = "Sorts et soins"
                self.attaque = 150
                self.vitesse = 0.75
                self.defense = 5
                self.vie = 1500
                self.puissance = 5
                self.cout = 3
                self.talent = "Cryogénisation"

        class Electromancien:
            def __init__(self):
                self.nom = "Electromancien"
                self.numero = "33"
                self.rarete = "Légendaire"
                self.type_carte = "Sorts et soins"
                self.attaque = 75
                self.vitesse = 2
                self.defense = 5
                self.vie = 1500
                self.puissance = 5
                self.cout = 3
                self.talent = "Rester"

        class Statue:
            def __init__(self):
                self.nom = "Statue"
                self.numero = "34"
                self.rarete = "Rare"
                self.type_carte = "Mystère"
                self.attaque = 200
                self.vitesse = 1
                self.defense = 6
                self.vie = 3000
                self.puissance = 6
                self.cout = 5
                self.talent = "Rester"

        class Guerisseur:
            def __init__(self):
                self.nom = "Guérisseur"
                self.numero = "35"
                self.rarete = "Commune"
                self.type_carte = "Sorts et soins"
                self.attaque = 50
                self.vitesse = 1
                self.defense = 5
                self.vie = 3000
                self.puissance = 5
                self.cout = 3
                self.talent = "Volatile"

        class Tour_des_Archers:
            def __init__(self):
                self.nom = "Tour des Archers"
                self.numero = "36"
                self.rarete = "Commune"
                self.type_carte = "Royauté"
                self.attaque = 75
                self.vitesse = 2
                self.defense = 6
                self.vie = 3000
                self.puissance = 5
                self.cout = 4
                self.talent = "Bouclier Brut"

        class Tour_Canoniere:
            def __init__(self):
                self.nom = "Tour Canonière"
                self.numero = "37"
                self.rarete = "Commune"
                self.type_carte = "Royauté"
                self.attaque = 100
                self.vitesse = 2
                self.defense = 6
                self.vie = 2500
                self.puissance = 5
                self.cout = 4
                self.talent = "Epée Brute"

        class Glaciere:
            def __init__(self):
                self.nom = "Glacière"
                self.numero = "38"
                self.rarete = "Rare"
                self.type_carte = "Eau"
                self.attaque = 0
                self.attaque_deux = 50
                self.vitesse = 0
                self.vitesse_deux = None # à définir dynamiquement
                self.defense = 5
                self.vie = 15
                self.puissance = 3
                self.cout = 2
                self.talent = "Relié"

        class Esprit_Empoisonné:   
            def Esprit_Empoisonné(self):  
                self.nom = "Esprit Empoisonné"
                self.numero = "39"
                self.rarete = "Mythique"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 25*self.seconde.Esprit_Empoisonné
                self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 200
                self.seconde.Esprit_Empoisonné = 5
                self.puissance_de_base = 3
                self.cout = 2
                self.talent = "Poison" # Lors du premier tour où la carte est jouée, son talent poison s'attache à la carte adverse posée si celle-ci est conservée par l'adversaire (si ce n'est pas le cas, le talent ne s'active pas jusqu'à ce qu'une carte adverse finisse par être conservée, et par extension, la remporte), lui infligeant des dégâts à hauteur de 5% de sa vie à chaque tour, cumulable jusqu'à 100% de sa vie, auquel cas la carte est regagnée par le possesseur originel de la carte possesseuse du talent. Si la carte est perdue, le talent devient inutilisable pour l'adversaire puisqu'attaché à son possesseur originel, et ce jusqu'à ce que la carte soit éventuellement regagnée, mais ces changements de camp n'affectent pas le talent déjà appliqué à une carte adverse. Lorsque la carte adverse touchée par le poison est regagnée, le talent se désactive et ne peut se réenclencher jusqu'à la fin de la partie, et ce pour les deux joueurs.

        class Drone:   
            def Drone(self):  
                self.nom = "Drone"
                self.numero = "40"
                self.rarete = "Rare"
                self.type_carte = "Technologie"
                self.attaque.de_base = 200
                self.vitesse.de_base = 1.25
                self.defense.de_base = 6
                self.vie.de_base = 1000
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Epée Brute"

        class Mr_Boomerang:   
            def Mr_Boomerang(self):  
                self.nom = "Mr. Boomerang"
                self.numero = "41"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 100
                self.vitesse.de_base = 2
                self.defense.de_base = 5
                self.vie.de_base = 2000
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Retour de Flamme" # En cas de parade de l'attaque, cette dernière est renvoyée à l'adversaire à hauteur de 200% de l'attaque initiale sur ses points de vie, avec en plus un effet de brûlure qui entraîne une baisse de 5% de la vie totale de la carte adverse à chaque tour pendant 3 tours. Si la vie de la carte adverse tombe à 0, elle est regagnée par le possesseur originel de la carte possesseuse du talent. Si la carte est perdue, le talent se réinitialise, mais reste réactivable par l'adversaire s'il rejoue la carte, lui attribuant alors l'effet. Si elle est regagnée, elle réapplique la même logique entre chaque joueur.

        class Magicien:
            def Magicien(self):
                self.nom = "Magicien"
                self.numero = "42"
                self.rarete = "Rare"
                self.type_carte = "Sorts et soins"
                self.attaque.deux = 75
                self.attaque.trois = 150
                self.attaque.quatre = 200
                self.liste_attaques = [self.attaque.deux, self.attaque.trois, self.attaque.quatre]
                random.shuffle(self.liste_attaques)
                self.attaque.de_base = self.liste_attaques[0]
                self.vitesse.deux = 2
                self.vitesse.trois = 0.75
                self.vitesse.quatre = 1
                if self.attaque.de_base == self.attaque.deux:
                    self.vitesse.de_base = self.vitesse.deux
                elif self.attaque.de_base == self.attaque.trois:
                    self.vitesse.de_base = self.vitesse.trois
                elif self.attaque.de_base == self.attaque.quatre:
                    self.vitesse.de_base = self.vitesse.quatre
                else:
                    self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 3000
                self.puissance.de_base = 4
                self.cout = 5
                self.talent = "Triple-attaque" # Possède 3 attaques différentes, dont une seule est choisie aléatoirement à chaque tour. Chaque attaque a une vitesse différente, et la vitesse de la carte est donc fonction de l'attaque choisie. Si la carte est perdue, le talent se réinitialise, mais reste réactivable par l'adversaire s'il rejoue la carte, lui attribuant alors l'effet. Si elle est regagnée, elle réapplique la même logique entre chaque joueur.

        class Excitation:   
            def Excitation(self):  
                self.nom = "Excitation"
                self.numero = "43"
                self.rarete = "Epique"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 0
                self.vitesse.de_base = 0
                self.defense.de_base = 0
                self.vie.de_base = 0
                self.puissance.de_base = 6
                self.puissance.deux = 5
                self.cout = 2
                self.talent = "Relié"
                self.artefact = self.artefact_excitation
                self.artefact_excitation = True
                if self.carte.artefact == self.artefact_excitation:
                    self.carte.attaque = self.carte.attaque * 1.25
                    self.carte.vitesse = self.carte.vitesse * 2
                    self.carte.defense = self.carte.defense
                    self.carte.vie = self.carte.vie + self.vie.artefact_excitation
                    self.carte.puissance = (self.carte.puissance + self.puissance_deux)//2
                    self.cout = self.cout.carte + self.cout.artefact_excitation
                    self.talent_facultatif = self.talent.artefact_excitation
                else:
                    return    
                     
        class Forgeron_Excite:   
            def Forgeron_Excite(self):  
                self.nom = "Forgeron Excité"
                self.numero = "44"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 100
                self.vitesse.de_base = 2
                self.defense.de_base = 5
                self.vie.de_base = 2000
                self.puissance.de_base = 6
                self.cout = 4
                self.talent = "Ivresse" # Une fois perdue puis regagnée, augmente toutes ses statistiques de 25%. Utilisable uniquement par le possesseur originel de la carte (lien avec soi-même, verrouillage de talent similaire à celui de Rester)

        class Catapulte:   
            def Catapulte(self):  
                self.nom = "Catapulte"
                self.numero = "45"
                self.rarete = "Rare"
                self.type_carte = "Royauté"
                self.attaque.de_base = 300
                self.vitesse.de_base = 0.25 < (self.nombre_cartes_adverses*0.05 + 0.25) <= 0.5
                self.defense.de_base = 6
                self.vie.de_base = 2000
                self.puissance.de_base = 7
                self.cout = 4
                self.talent = "Relié"

        class Enserreur:   
            def Enserreur(self):  
                self.nom = "Enserreur"
                self.numero = "46"
                self.rarete = "Légendaire"
                self.type_carte = "Mystère"
                if self.vitesse == self.vitesse.de_base:
                    self.attaque.de_base = 150
                elif self.vitesse == self.vitesse.deux:
                    self.attaque.de_base = 300
                else:
                    return
                self.vitesse.de_base = 3
                self.vitesse.deux = 2
                self.defense.de_base = 5
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 5
                self.talent = "Système tactique"

        class Guerrier_Supreme:   
            def Guerrier_Supreme(self):  
                self.nom = "Guerrier Suprême"
                self.numero = "47"
                self.rarete = "Légendaire"
                self.type_carte = "Royauté"
                self.attaque.de_base = 300
                self.vitesse.de_base = 0.75
                self.defense.de_base = 6
                self.vie.de_base = 3000
                self.puissance.de_base = 6
                self.cout = 7
                self.talent = "Altérations" # Invulnérable aux altérations de talents adverses

        class Guerrier_Excite:   
            def Guerrier_Excite(self):  
                self.nom = "Guerrier Excité"
                self.numero = "48"
                self.rarete = "Légendaire"
                self.type_carte = "Royauté"
                self.attaque.de_base = 225
                self.vitesse.de_base = 2
                self.defense.de_base = 6
                self.vie.de_base = 1250
                self.puissance.de_base = 6
                self.cout = 5
                self.talent = "Ivresse"

        class Centrale_Recyclage:   
            def Centrale_Recyclage(self):  
                self.nom = "Centrale de Recyclage"
                self.numero = "49"
                self.rarete = "Rare"
                self.type_carte = "Technologie"
                self.attaque.de_base = 0
                self.attaque.deux = 25*self.seconde.Centrale_Recyclage
                self.vitesse.de_base = 0.25
                self.vitesse.deux = 1
                self.defense.de_base = 6
                self.vie.de_base = 3000
                self.vie.deux = self.seconde.Centrale_Recyclage
                self.seconde.Centrale_Recyclage = 5
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Aura" # Augmente l'attaque de toutes les cartes alliées de même type de 25 points d'attaque par tour passé sur le terrain

        class Grand_Archer:   
            def Grand_Archer(self):  
                self.nom = "Grand Archer"
                self.numero = "50"
                self.rarete = "Légendaire"
                self.type_carte = "Mystère"
                self.attaque.de_base = 200
                self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Travers" # Enlève à la vie de la dernière carte adverse conservée l'équivalent de l'attaque de la carte, peu importe si cette dernière venait de lui ou du possesseur de la carte talent, peu importe le nombre de tours écoulés depuis la dernière défaite. Si aucune carte n'a été perdue depuis le début de la partie, inflige les dégâts à une carte adverse aléatoire

        class Fantôme:   
            def Fantôme(self):  
                self.nom = "Fantôme"
                self.numero = "51"
                self.rarete = "Légendaire"
                self.type_carte = "Mystère"
                self.attaque.de_base = 300
                self.vitesse.de_base = 0.5
                self.defense.de_base = 6
                self.vie.de_base = 0
                self.vie.deux = 500
                self.puissance.de_base = 3
                self.cout = 5
                self.talent = "Attaque Surprise" #Enlève autant de points de vie à la carte adverse que la hauteur de l'attaque de la carte multiplié par le nombre de tours où elle fut jouée, si les points de vie de la carte adverse arrivent à 0, elle revient au joueur peu importe les affectation du résultat de la manche, la carte possédant le talent n'étant pas impactée/La vitesse de la carte est telle qu'aucune autre valeur qu'elle même ne peut l'atteindre, seule sa propre valeur s'érige en son égale

        class Geyser:   
            def Geyser(self):  
                self.nom = "Geyser"
                self.numero = "52"
                self.rarete = "Rare"
                self.type_carte = "Eau"
                self.attaque.de_base = 300
                self.vitesse.de_base = 0.25
                self.defense.de_base = 0
                self.vie.de_base = self.seconde.Geyser
                self.seconde.Geyser = 24
                self.puissance.de_base = 3
                self.cout = 3
                self.talent = "Crash" #Projette la carte adverse en l'air, infligeant des dégats égaux à la hauteur de 15% de la vie de la carte adverse, la carte étant rendue inutilisable pour les 2 tours à venir en cas de conservation

        class Garde:   
            def Garde(self):  
                self.nom = "Garde"
                self.numero = "53"
                self.rarete = "Commune"
                self.type_carte = "Royauté"
                self.attaque.de_base = 100
                self.attaque.deux = 225
                self.vitesse.de_base = 1
                self.vitesse.deux = 1.25
                self.defense.de_base = 6
                self.vie.de_base = 500
                self.vie.deux = 1250
                self.puissance.de_base = 4
                self.cout = 2
                self.talent = "Protection" # Applique l'attaque de base jusqu'à ce qu'elle soit perdue puis regagnée, auquel cas elle applique l'attaque deux, et ainsi de suite. La carte ne peut revenir sur une attaque déjà passé, ainsi si elle arrivé à sa dernière attaque dans la liste, elle gardera cette attaque jusqu'à la fin de la partie, et ce peu importe les changements de camps. Lorsqu'elle change de camp, elle garde l'attaque précédente, cette dernière ne change que lorsque la carte est regagnée par son possesseur originel, ainsi l'adversaire ne peut en tirer parti et ne peut donc pas réinitialiser les valeurs d'attaque de la carte pour tirer profit du talent. 

        class Generateur_Pieces:   
            def Generateur_Pieces(self):  
                self.nom = "Générateur de Pièces"
                self.numero = "54"
                self.rarete = "Commune"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 0
                self.vitesse.de_base = 0.25
                self.defense.de_base = 5
                self.vie.de_base = self.seconde.Generateur_Pieces
                self.seconde.Generateur_Pieces = 24
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Bouclier Brut" 

        class Mur_Royal:   
            def Mur_Royal(self):  
                self.nom = "Mur Royal"
                self.numero = "55"
                self.rarete = "Commune"
                self.type_carte = "Royauté"
                self.attaque.de_base = 75
                self.vitesse.de_base = 5
                self.defense.de_base = 6
                self.vie.de_base = 2000
                self.puissance.de_base = 7
                self.cout = 5
                self.talent = "Bouclier Brut"

        class Bombardier:   
            def Bombardier(self):  
                self.nom = "Bombardier"
                self.numero = "56"
                self.rarete = "Commune"
                self.type_carte = "Mystère"
                self.attaque.de_base = 300
                self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 750
                self.puissance.de_base = 4
                self.cout = 3
                self.talent = "Cadeau d'Adieu" # Si la carte est perdue, elle inflige à la carte adverse qui la remporte des dégâts sur sa vie à hauteur de 300% de son attaque en vigueur. Si la vie de cette dernière tombe en dessous de 0, elle est remportée par le joueur possesseur de la carte ayant le talent, mais cette dernière sera tout de même remportée par l'adversaire, qui pourra réutiliser le talent à son tour.

        class Chevalier_Verre:   
            def Chevalier_Verre(self):  
                self.nom = "Chevalier de Verre"
                self.numero = "57"
                self.rarete = "Rare"
                self.type_carte = "Mystère"
                self.attaque.de_base = 350
                self.attaque.deux = 175
                self.vitesse.de_base = 1
                self.vitesse.deux = 1.25
                self.defense.de_base = 6
                self.defense.deux = 5
                self.vie.de_base = 1000
                self.vie.deux = 1500
                self.puissance.de_base = 4
                self.cout = 4
                self.talent = "Charge" # Tant que la vie n'est pas affectée de façon à ce qu'elle soit inférieure à sa valeur de base, les statistiques de base restent en vigueur. Si une baisse de la vie devait advenir, les statistiques secondaires entreraient en vigueur, et ce par paliers de 20% de la vie.

        class Reproduction:   
            def Reproduction(self):  
                self.nom = "Reproduction"
                self.numero = "59"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 0
                self.vitesse.de_base = 0
                self.defense.de_base = 0
                self.vie.de_base = 0
                self.puissance.de_base = 7
                self.cout = 3
                self.talent = "Bonus Royal"
                self.artefact = self.artefact_reproduction
                self.artefact_reproduction = True
                if self.carte.artefact == self.artefact_reproduction:
                    self.carte.attaque = self.carte.attaque*1.25
                    self.carte.vitesse = self.carte.vitesse + 0.5
                    self.carte.defense = self.carte.defense + 1
                    self.carte.vie = self.carte.vie*1.25
                    self.carte.puissance = (self.carte.puissance + self.artefact_reproduction.puissance)//2
                    self.carte.cout = self.carte.cout + self.artefact_reproduction.cout
                    self.carte.talent_facultatif = self.artefact_reproduction.talent
                else:
                    return

        class Empoisonneur:   
            def Empoisonneur(self):  
                self.nom = "Empoisonneur"
                self.numero = "59"
                self.rarete = "Rare"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 50
                self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 2000
                self.puissance.de_base = 7
                self.cout = 4
                self.talent = "Poison"

        class Tour_Acide:   
            def Tour_Acide(self):  
                self.nom = "Tour d'Acide"
                self.numero = "60"
                self.rarete = "Mythique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 250
                self.vitesse.de_base = 0.5
                self.defense.de_base = 5
                self.vie.de_base = 2000
                self.puissance.de_base = 6
                self.cout = 5
                self.talent = "Cadeau d'Adieu"

        class Pluie_Epees:   
            def Pluie_Epees(self):  
                self.nom = "Pluie d'Epées"
                self.numero = "61"
                self.rarete = "Mythique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 25
                self.vitesse.de_base = 15
                self.defense.de_base = 0
                self.vie.de_base = 0
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Epicentre" # L'Attaque inflige des dégâts de zone à hauteur de l'attaque en vigueur multipliée par la vitesse en vigueur de la carte possesseuse du talent sur l'ensemble des cartes déjà parues en jeu actuellement dans le deck de l'adversaire (perdues ou conservées). Si la vie de certaines cartes tombe à 0, elles sont remportées par le possesseur de la carte possesseuse du talent Epicentre. La vie perdue par les cartes adverses est regagnée équitablement à hauteur de 25% pour chaque tour qui passe jusqu'à 100% de vie recouverte. Si le talent est rejoué entre-temps, ses effets ne se cumulent pas tels qu'entendus, mais la valeur de recouvrement de vie adverse est réinitialisée à 0% du déficit engendré par la carte à l'origine du déficit.

        class Guerrier_Indigène:   
            def Guerrier_Indigène(self):  
                self.nom = "Guerrier Indigène"
                self.numero = "62"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 250
                self.vitesse.de_base = 0.5 <= (self.nombre_cartes_adverses*0.5)
                self.defense.de_base = 3
                self.vie.de_base = 2000
                self.puissance.de_base = 0
                self.cout = 4
                self.talent = "Relié"
 
        class Bouc:   
            def Bouc(self):  
                self.nom = "Bouc"
                self.numero = "63"
                self.rarete = "Rare"
                self.type_carte = "Mystère"
                self.attaque.de_base = 350
                self.attaque.deux = 175
                self.vitesse.de_base = 1
                self.defense.de_base = 6
                self.vie.de_base = 1500
                self.puissance.de_base = 2
                self.cout = 4
                self.talent = "Onde de Choc" # Altère les vitesses de toutes les cartes d'une valeur compris entre +0 et +0.25 pour les cartes alliés de la carte possédant le talent, et de -0 à -0.25 pour les cartes adverses, et ce pendant 3 tours.

        class Circul_X:   
            def Circul_X(self):  
                self.nom = "Circul-X"
                self.numero = "64"
                self.rarete = "Epique"
                self.type_carte = "Technologie"
                self.attaque.de_base = 175
                self.vitesse.de_base = 2
                self.defense.de_base = 6
                self.vie.de_base = 2000
                self.vie.deux = 500
                self.puissance.de_base = 6
                self.cout = 5
                self.talent = "Travers"

        class Technoguerrier:   
            def Technoguerrier(self):  
                self.nom = "Technoguerrier"
                self.numero = "65"
                self.rarete = "Champion"
                self.type_carte = "Technologie"
                self.attaque_initiale = 300
                self.attaque.de_base = self.attaque_initiale - (self.attaque_initiale*(1 - 0.2*self.carte.nombre_tours_joues))
                self.vitesse.de_base = 0.25
                self.defense_initiale = 8
                self.defense.de_base = self.defense_initiale - (self.defense_initiale*(1 - 0.25*self.carte.nombre_tours_joues))
                self.vie.de_base = 3250
                self.puissance.de_base = 8
                self.cout = 6
                self.talent = "Instinct" # Active automatiquement sa capacité lorsque celle-ci est disponible si la carte adverse est plus puissante en termes d'attaque ou de défense lorsque viennent ces statistiques à être en vigueur.
                self.champion = True
                self.capacite = "Recharge Energétique"
                if self.carte.capacite == True:
                    self.attaque = self.attaque_initiale
                    self.defense = self.defense_initiale
                else:
                    return
        
        class Extralazer:   
            def Extralazer(self):  
                self.nom = "Extralazer"
                self.numero = "66"
                self.rarete = "Mythique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 125
                self.vitesse.de_base = 1.75
                self.defense.de_base = 6
                self.vie.de_base = 1750
                self.puissance.de_base = 5
                self.cout = 5
                self.talent = "Entrave du Poulpe" # Tant que la carte possesseuse du talent appartient à son propriétaire d'origine, chaque confrontation qui mènera à une conservation marquera la carte adverse remportée en face d'une entrave qui réduira à néant une de ses statistiques aléatoires pour le reste de la partie, et ce peu importe son propriétaire. Si une carte vient à subir cet effet une seconde fois, alors une autre de ses statistiques sera entravée, et ce jusqu'à anéantissement de chacune de ses statistiques (à noter qu'un anéantissement de statistique ne peut entraîner un changement de camp). Si la carte est perdue, son talent se désactive pour toujours et ce même si elle est regagnée par la suite.

        class La_Massue:   
            def La_Massue(self):  
                self.nom = '"La Massue"'
                self.numero = "67"
                self.rarete = "Légendaire"
                self.type_carte = "Mystère"
                self.attaque.de_base = 450
                self.vitesse.de_base = 0.25
                self.defense.de_base = 6
                self.vie.de_base = 3000
                self.puissance.de_base = 7
                self.cout = 6
                self.talent = "Os Maudits" # Toute carte remportée durant sa présence dans le deck est "Maudite" : Dès lors, si elle est regagnée par l'adversaire, elle comportera un malus de 20% sur l'ensemble de ses statistiques. Cet effet peut être annulé si la carte possesseuse du talent est gagnée à son tour (à compter que cette dernière est maudite en permanence pour chaque utilisateur autre que son propriétaire d'origine) : elle restera maudite envers son précédent propriétaire uniquement, mais ses avantages pourront être réactivés pour son nouveau propriétaire lors de sa relance en jeu.

        class Lance_Pierre:   
            def Lance_Pierre(self):  
                self.nom = "Lance-Pierre"
                self.numero = "68"
                self.rarete = "Commune"
                self.type_carte = "Technologie"
                self.attaque.de_base = 100
                self.vitesse.de_base = 1
                self.defense.de_base = 3
                self.vie.de_base = 1000
                self.puissance.de_base = 5 
                self.cout = 2
                self.talent = "Sans pitié" # La carte dispose d'une "cartouche" de talent : lorsqu'elle est censée perdre durant un tour où la vie ou la défense sont en vigueur, elle dégaine cette cartouche de façon à ce que sa vie soit égale à sa vie initiale plus 5% de la vie de l'adversaire volée multipliée par le nombre de tours passés depuis le début de la partie, et +0.25 points de défense par tour passé depuis le début de la partie, arrondi à l'unité. Une fois cette cartouche utilisée (automatiquement), le talent devient inactif et le reste jusqu'à ce qu'une "cartouche" soit regagnée pour ce talent (encore à définir)

        class Base_Elite:   
            def Base_Elite(self):  
                self.nom = "Base d'Elite"
                self.numero = "69"
                self.rarete = "Epique"
                self.type_carte = "Royauté"
                self.attaque.de_base = 0
                self.attaque.deux = 150
                self.vitesse.de_base = 0.25
                self.vitesse.trois = 4
                self.defense.de_base = 3 
                self.vie.de_base = self.seconde.Base_Elite
                self.seconde.Base_Elite = 12
                self.vie.deux = 1250
                self.puissance.de_base = 0
                self.cout = 5
                self.talent = "Bonus Royal"

        class Pyromane:   
            def Pyromane(self):  
                self.nom = "Pyromane"
                self.numero = "70"
                self.rarete = "Mythique"
                self.type_carte = "Feu"
                self.attaque.de_base = 300 
                self.vitesse.de_base = 0.25
                self.defense.de_base = 6
                self.vie.de_base = 2250
                self.puissance.de_base = 6 
                self.cout = 5
                self.talent = "Brûlure" # Brûle la carte adverse. Cette dernière garde la trace pendant 3 tours, cette dernière lui infligeant 15% des dégâts de l'attaque de la carte possédant le talent. Si cette carte entre en contact avec une autre carte entre temps, elle lui transmet la marque. La marque s'arrête pour toutes les cartes au bout de 9 tours.

        class Jongleur:   
            def Jongleur(self):  
                self.nom = "Jongleur"
                self.numero = "71"
                self.rarete = "Rare"
                self.type_carte = "Mystère"
                self.attaque.de_base = 150
                self.vitesse.de_base = 1.25
                self.defense.de_base = 5
                self.vie.de_base = 1750
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Détournement d'Attention" # A des chances de détourner l'attention de l'adversaire de façon à ce que celui-ci soit "distrait" et ait à son tour ses chances exponentielles de se tromper de cible et d'être incapable d'appliquer sa statistique. Cet effet s'annule entièrement lorsque l'une des deux cartes (Distryante et Distraite) change de camp

        class Tue_Loup:   
            def Tue_Loup(self):  
                self.nom = "Tue-Loup"
                self.numero = "72"
                self.rarete = "Commune"
                self.type_carte = "Technologie"
                self.attaque.de_base = 50
                self.vitesse.de_base = 1
                self.defense.de_base = 0
                self.vie.de_base = 0
                self.puissance.de_base = 0
                self.cout = 4
                self.talent = "Malédiction Eternelle" # Chaque carte adverse jouée contre la carte porteuse du talent tant que celle-ci appartient à son propriétaire d'origine

        class Scorpion_Geant:   
            def Scorpion_Geant(self):  
                self.nom = "Scorpion Géant"
                self.numero = "73"
                self.rarete = "Rare"
                self.type_carte = "Mystère"
                self.attaque.de_base = 250
                self.vitesse.de_base = 0.75
                self.defense.de_base = 6
                self.vie.de_base = 2750
                self.puissance.de_base = 7 
                self.cout = 6
                self.talent = "Goutte Empoisonnée"

        class Grand_Chasseur:   
            def Grand_Chasseur(self):  
                self.nom = "Grand Chasseur"
                self.numero = "76"
                self.rarete = "Champion"
                self.type_carte = "Mystère"
                self.attaque.de_base = 200
                self.vitesse.de_base = 0.75
                self.defense.de_base = 5
                self.vie.de_base = 3000
                self.puissance.de_base = 6 
                self.cout = 6
                self.talent = "Entretien de Puissance" # Tant qu'il appartient à son propriétaire d'origine, chaque confrontation remportée lui attribue un supplément de 25% arrondi de la statistique en cours de la carte vaincue
                self.champion = True
                self.capacite = "Protection Energétique" # Perd l'entiereté de sa statistique en cours qui vient se soustraire à celle de son adversaire : au tour en cours, on compare alors l'ancienne statistique avant sacrifice et celle devenue après soustraction de l'adversaire. Nombre de tours de recharge : 3. Coût : 1.

        class Tesla:   
            def Tesla(self):  
                self.nom = "Tesla"
                self.numero = "77"
                self.rarete = "Commune"
                self.type_carte = "Foudre"
                self.attaque.de_base = 200
                self.vitesse.de_base = 0.25
                self.defense.de_base = 6
                self.vie.de_base = 2000
                self.puissance.de_base = 0
                self.cout = 4
                self.talent = "Accumulation" # Tant qu'il appartient à son propriétaire d'origine, chaque confrontation gagnée augmente son niveau d'accumualtion : celui-ci détermine comment ses statistiques augmentent de façon exponentielle. Lors de sa défaite, ce sont ces statistiques qu'il inflige à la carte qui le vainc tandis que son niveau d'accumulation revient à 0

        class Machine_Antique:   
            def Machine_Antique(self):  
                self.nom = "Machine Antique"
                self.numero = "78"
                self.rarete = "Mythique"
                self.type_carte = "Technologie"
                self.attaque.de_base = 200
                self.vitesse.de_base = 1.25
                self.defense.de_base = 6
                self.vie.de_base = 2000
                self.puissance.de_base = 4
                self.cout = 4
                self.talent = "Esprit Vengeur" # Augmente ses statistiques d'attaque et de vitesse de 25% pour chaque carte manquante du nombre de cartes originel

        class Mine:   
            def Mine(self):  
                self.nom = "Mine"
                self.numero = "79"
                self.rarete = "Rare"
                self.type_carte = "Mystère"
                self.attaque.de_base = 0
                self.vitesse.de_base = 0.2
                self.defense.de_base = 8
                self.vie.de_base = self.seconde.Mine
                self.seconde.Mine = 24
                self.puissance.de_base = 5 
                self.cout = 5
                self.talent = "Relance Economique" # Choisit une carte aléatoire de son jeu dont le coût diminue d'un point, puis le reverse à une carte adverse aléatoire. L'effet peut se cumuler jusqu'à l'infini potentiel, mais si la carte est perdue tous ses effets s'annulent.

        class Montagne_Golemites:   
            def Montagne_Golemites(self):  
                self.nom = "Montagne aux Golemites"
                self.numero = "80"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 0
                self.attaque.deux = 125
                self.vitesse.de_base = 0.2
                self.vitesse.deux = 0.25
                self.defense.de_base = 8
                self.defense.deux = 7
                self.vie.de_base = self.seconde.Montagne_Golemites
                self.seconde.Montagne_Golemites = 24
                self.vie.deux = 750
                self.puissance.de_base = 5
                self.puissance.deux = 3  
                self.cout = 6
                self.talent = "Instabilité" # Initie son roulement aléatoirement pour chaque statistique séparément

        class Moulin_Vent:   
            def Moulin_Vent(self):  
                self.nom = "Moulin à Vent"
                self.numero = "81"
                self.rarete = "Légendaire"
                self.type_carte = "Technologie"
                self.attaque.de_base = 0
                self.attaque.deux = 50
                self.attaque.trois = 75
                self.attaque.quatre = 100
                self.vitesse.de_base = 0.2
                self.defense.de_base = 3
                self.vie.de_base = 1500
                if self.vie.de_base <= 1000:
                    self.roulement = False
                    self.attaque_en_vigueur = self.attaque.de_base
                self.puissance.de_base = 0 
                self.cout = 4
                self.talent = "Interrupteur" # Tant que le roulement est actif, le talent agit même lorsqu'il n'est pas présent, faisant chuter progressivement la défense adverse et augmentant la vitesse alliée (temporairement à chaque tour, potentiellement indéfini au cours de la partie jusqu'à prise de la carte possédant le talent)

        class Electrons:   
            def Electrons(self):  
                self.nom = "Electrons"
                self.numero = "82"
                self.rarete = "Légendaire"
                self.type_carte = "Foudre"
                self.attaque.de_base = 75
                self.vitesse.de_base = 3
                self.defense.de_base = 3
                self.vie.de_base = 2250
                self.puissance.de_base = 5 
                self.cout = 3
                self.talent = "Conduction" # Attribue le type Foudre à la carte posée au tour suivant, en plus de son type connu, seulement pour ce tour

        class Malediction:   
            def Malediction(self):  
                self.nom = "Malédiction"
                self.numero = "83"
                self.rarete = "Mythique"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 50*self.seconde.Malediction*self.vitesse
                self.vitesse.de_base = 1
                self.defense.de_base = 0
                self.vie.de_base = self.seconde.Malediction
                self.seconde.Malediction = 12
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Assombrissement" # La carte adverse ne peut plus être jouée qu'une fois tous les 3 tours. Un seul lien permis.

        class Sorciere_Mystique:   
            def Sorciere_Mystique(self):  
                self.nom = "Sorcière Mystique"
                self.numero = "84"
                self.rarete = "Epique"
                self.type_carte = "Chaos"
                self.attaque.de_base = 200
                self.attaque.deux = 25
                self.vitesse.de_base = 1.25
                self.vitesse.deux = 1 
                self.defense.de_base = 5
                self.defense.deux = 1 
                self.vie.de_base = 1500
                self.vie.deux = 25
                self.puissance.de_base = 7
                self.cout = 4
                self.talent = "Maîtrise Magique" # Est insensible aux attributs des cartes de type Monde Magique     
            
    class Talents:
        def Talents(self):
            Talents = {
                self.bouclier_brut : "Bouclier Brut",
                self.epee_brute : "Epée Brute",
                self.division : "Division",
                self.goutte_empoisonnee : "Goutte Empoisonnée",
                self.pique_coeur : "Pique-coeur",
                self.iode : "Iode",
                self.bonus_royal : "Bonus Royal",
                self.rester : "Rester",
                self.para_chute : "Para-chute",
                self.systeme_tactique : "Système Tactique",
                self.emport : "Emport",
                self.statique : "Statique",
                self.couverture_explosive : "Couverture Explosive",
                self.mirage : "Mirage",
                self.maladresse : "Maladresse",
                self.larguage_progressif : "Larguage Progressif",
                self.cryogenisation : "Cryogénisation",
                self.fibulatio : "Fibulatio",
                self.volatile : "Volatile",
                self.relie : "Relié",
                self.poison_mortel : "Poison Mortel",
                self.retour_de_flamme : "Retour de Flammes",
                self.triple_attaque : "Triple-attaque",
                self.ivresse : "Ivresse",
                self.alterations : "Altérations",
                self.aura : "Aura",
                self.travers : "Travers",
                self.attaque_surprise : "Attaque Surprise",
                self.crash : "Crash",
                self.protection : "Protection",
                self.cadeau_adieu : "Cadeau d'Adieu",
                self.charge : "Charge",
                self.epicentre : "Epicentre",
                self.onde_choc : "Onde de Choc",
                self.instinct : "Instinct",
                self.entrave_poulpe : "Entrave du Poulpe",
                self.os_maudits : "Os Maudits",
                self.sans_pitie : "Sans pitié",
                self.brulure : "Brûlure",
                self.malediction_eternelle : "Malédiction Eternelle"   
                }
            
    class Bibliothèque_De_Talents:
        def bibliotheque_de_cartes(self):
                if carte.talent == "Bouclier Brut":
                    if self.statistique_en_cours == self.attaque:
                        probabilite_bouclier_brut = random.randint(1, 5)
                        if probabilite_bouclier_brut == 1:
                            carte_adverse.attaque = carte_adverse.attaque_initiale
                            carte_adverse.attaque = 0
                            print("Le talent Bouclier Brut de",carte," est actif ! L'attaque de",carte_adverse.nom," est nulle !")
                            if self.compteur_de_tours > self.tour_actuel:
                                carte_adverse.attaque_initiale = carte_adverse.attaque
                                self.tour_actuel = self.compteur_de_tours
                            else:
                                return
                        else:
                            print("Le talent Bouclier Brut de",carte.nom," est inactif.")
                    else:
                        return
                elif carte.talent == "Epée Brute":
                    if self.statistique_en_cours == self.attaque:
                        probabilite_epee_brute = random.randint(1, 5)
                        if probabilite_epee_brute == 1:
                            carte.attaque = carte.attaque_initiale
                            carte.attaque = carte.attaque*2
                            print("Le talent Epée Brute de",carte.nom," est actif ! Son attaque vient de doubler !")
                            if self.compteur_de_tours > self.tour_actuel:
                                carte.attaque_initiale = carte.attaque
                                self.tour_actuel = self.compteur_de_tours
                            else:
                                return
                        else:
                            print("Le talent Epée Brute de",carte.nom," est inactif.")
                    else:
                        return
                elif carte.talent == "Division":
                    carte.attaque = carte.attaque_division
                    carte.attaque_division = carte.attaque_division//2
                    if self.compteur_de_tours > self.tour_actuel:
                        carte = self.carte_tour_suivant
                        carte.attaque = self.carte_tour_suivant.attaque + carte.attaque_division
                        print("Le talent Division de",carte.nom,"est actif ! L'attaque de",carte.talent.division.nom," vient d'augmenter !")
                        self.tour_actuel = self.compteur_de_tours
                    else:
                        return
                elif carte.talent == "Pique-coeur":
                    if self.statistique_en_cours == self.vie:
                        carte.vie = carte.vie_initiale
                        carte_adverse.vie = carte_adverse.vie_initiale
                        carte.vie = carte.vie + carte_adverse.vie*0.15
                        carte_adverse.vie = carte_adverse.vie*0.85
                        print("Le talent Pique-Coeur de",carte.nom," est actif ! La vie de",carte_adverse.nom," est drainée à hauteur de 15% !")
                        if self.compteur_de_tours > self.tour_actuel:
                            carte.vie_initiale = carte.vie
                            carte_adverse.vie_intiale = carte_adverse.vie
                            self.tour_actuel = self.compteur_de_tours
                        else:
                            return
                    else:
                        return
                elif carte.talent == "Iode":
                    if self.statistique_en_cours == self.statistique_attaque:
                        if carte_adverse.type_carte == self.feu:
                            carte.attaque = carte.attaque_initiale
                            carte.attaque = carte.attaque*3
                            print("Le talent Iode de",carte.nom," est actif ! Son attaque vient de tripler !")
                            if self.compteur_de_tours > self.tour_actuel:
                                carte.attaque_initiale = carte.attaque
                                self.tour_actuel = self.compteur_de_tours
                            else:
                                return
                        else:
                            return
                elif carte.talent == "Bonus Royal":
                    if carte_adverse.type_carte == "Royauté":
                        carte.attaque_initiale = carte.attaque
                        carte.vitesse_initiale = carte.vitesse
                        carte.defense_initiale = carte.defense
                        carte.vie_initiale = carte.vie
                        carte.puissance_initiale = carte.puissance
                        carte.attaque = carte.attaque*1.25
                        carte.vitesse = carte.vitesse*1.25
                        carte.defense = carte.defense*1.25
                        carte.vie = carte.vie*1.25
                        carte.puissance = carte.puissance*1.25
                        print("Le talent Bonus Royal de",carte.nom," est actif ! Ses statistiques augmentent de 25%.")
                        if self.compteur_de_tours > self.tour_actuel:
                            carte.attaque = carte.attaque_initiale
                            carte.vitesse = carte.vitesse_initiale
                            carte.defense = carte.defense_initiale
                            carte.vie = carte.vie_initiale
                            carte.puissance = carte.puissance_initiale
                            self.tour_actuel = self.compteur_de_tours
                        else:
                            return
                    else:
                        return
                elif carte.talent == "Rester":
                    if carte_adverse.talent != "Rester":
                        carte_adverse = carte_adverse_rester
                        carte = self.carte_rester
                        print("Le talent Rester de",carte.nom," est actif sur",carte_adverse.nom," !")
                        if carte_adverse_rester.carte.statistique_en_cours > self.carte_rester.carte.statistique_en_cours:
                            self.carte_rester.carte = carte_adverse_perdue_rester.carte
                            carte_adverse.carte = carte_adverse_rester.carte
                            while carte_adverse_perdue_rester.carte != carte_adverse:
                                break
                            while carte_adverse_rester.carte != carte_adverse:
                                break
                            if carte_adverse_perdue_rester.carte == carte_adverse:
                                print("La carte",carte_adverse_perdue_rester.carte.nom," liée à la carte", carte_adverse_rester.carte.nom," est jouée ! Le talent Rester est réactif !")
                                if carte.statistique_en_cours > carte_adverse_perdue_rester.carte.statistique_en_cours:
                                    carte_adverse_perdue_rester.carte = carte_possedee in self.cartes_possedees
                                    carte_adverse_rester.carte = carte_possedee in self.cartes_possedees
                                    print("Le talent Rester s'active ! Les cartes liées",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," sont regagnées !")
                                    print("Le talent Rester n'est plus actif. Les cartes",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," ne sont plus liées.")
                                elif carte.statistique_en_cours < carte_adverse_perdue_rester.carte.statistique_en_cours:
                                    carte_adverse_perdue_rester = carte_adverse in self.cartes_adverses
                                    carte_adverse_rester = carte_adverse in self.cartes_adverses
                                    print("Le talent Rester ne s'active pas. Les cartes",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," sont conservées.")
                                    print("Le talent Rester n'est plus actif. Les cartes",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," ne sont plus liées.")
                                else:
                                    while carte.statistique_en_cours == carte_adverse.statistique_en_cours:
                                        for carte_possedee in self.cartes_possedees:
                                            carte = random.shuffle(self.cartes_possedees)
                                        for carte_adverse in self.carte_adverses:
                                            carte_adverse = random.shuffle(self.cartes_adverses)
                                        if carte.statistique_en_cours > carte_adverse.statistique_en_cours:
                                            carte = carte_possedee in self.cartes_possedees
                                            carte_adverse = carte_possedee in self.cartes_possedees
                                            carte_adverse_rester = carte_possedee in self.cartes_possedees
                                            carte_adverse_perdue_rester = carte_possedee in self.cartes_possedees
                                            print("Le talent Rester s'active ! Les cartes liées",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," sont regagnées !")
                                            print("Le talent Rester n'est plus actif. Les cartes",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," ne sont plus liées.")
                                        elif carte.statistique_en_cours < carte_adverse.statistique_en_cours:
                                            carte = carte_adverse in self.cartes_adverses
                                            carte_adverse = carte_adverse in self.cartes_adverses
                                            carte_adverse_rester = carte_adverse in self.cartes_adverses
                                            carte_adverse_perdue_rester = carte_adverse in self.cartes_adverses
                                            print("Le talent Rester ne s'active pas. Les cartes",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," sont conservées.")
                                            print("Le talent Rester n'est plus actif. Les cartes",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," ne sont plus liées.")
                                        else:
                                            break
                            else:
                                return
                        elif carte_adverse_rester.carte.statistique_en_cours > self.carte_rester.carte.statistique_en_cours:
                            carte = carte_possedee_rester
                            carte_adverse = carte_adverse_possedee_rester
                            while carte != carte_possedee_rester:
                                break
                            while carte != carte_adverse_possedee_rester:
                                break
                            if carte_possedee_rester == carte:
                                print("La carte",carte_possedee_rester.carte.nom," liée à la carte", carte_adverse_possedee_rester.carte.nom," est jouée ! Le talent Rester est réactif !")
                                if carte_possedee_rester.statistique_en_cours > carte_adverse.statistique_en_cours:
                                    carte_possedee_rester = carte_possedee in self.cartes_possedees
                                    carte_adverse_possedee_rester = carte_possedee in self.cartes_possedees
                                    carte_adverse = carte_possedee in self.cartes_possedees
                                    print("Le talent Rester s'active ! Les cartes liées",carte_possedee_rester.carte.nom," et",carte_adverse_possedee_rester.carte.nom," sont conservées !")
                                    print("Le talent Rester n'est plus actif. Les cartes",carte_possedee_rester.carte.nom," et",carte_adverse_possedee_rester.carte.nom," ne sont plus liées.")
                                elif carte_possedee_rester.statistique_en_cours < carte_adverse.statistique_en_cours:
                                    carte_possedee_rester = carte_adverse_rester in self.cartes_adverses
                                    carte_adverse = carte_adverse in self.cartes_adverses
                                    print("Le talent Rester s'active ! La carte",carte_possedee_rester.nom," est perdue. La carte",carte_adverse_possedee_rester.nom," est conservée.")
                                    print("Le talent Rester reste actif. Les cartes",carte_possedee_rester.nom," et",carte_adverse_possedee_rester.nom," sont toujours liées.")
                                    if self.compteur_de_tours > self.tour_actuel:
                                        while carte_adverse != carte_adverse_rester:
                                            break
                                        while carte != carte_adverse_possedee_rester:
                                            break
                                        if carte_adverse == carte_adverse_rester:
                                            if carte.statistique_en_cours > carte_adverse_rester.statistique_en_cours:
                                                carte = carte_possedee in self.cartes_possedees
                                                carte_adverse_rester = carte_possedee in self.cartes_possedees
                                                print("Le talent Rester s'active ! La carte",carte_adverse_rester.carte.nom," liée à la carte",carte_adverse_possedee_rester.carte.nom," est regagnée !")
                                                print("Le talent Rester n'est plus actif. Les cartes",carte_adverse_rester.carte.nom," et",carte_adverse_possedee_rester.carte.nom," ne sont plus liées.")
                                            elif carte.statistique_en_cours < carte_adverse_rester.statistique_en_cours:
                                                carte = carte_adverse in self.cartes_adverses
                                                carte_adverse_rester in self.cartes_adverses
                                                carte_adverse_possedee_rester = carte_possedee in self.cartes_possedees
                                                print("Le talent Rester ne s'active pas. La carte",carte_adverse_rester.nom," n'est pas regagnée. La carte",carte_adverse_possedee_rester.nom," est conservée.")
                                                print("Le talent Rester n'est plus actif. Les cartes",carte_adverse_rester.nom," et",carte_adverse_possedee_rester.nom," ne sont plus liées.")
                                            else:
                                                while carte.statistique_en_cours == carte_adverse.statistique_en_cours:
                                                    for carte_possedee in self.cartes_possedees:
                                                        carte = random.shuffle(self.cartes_possedees)
                                                    for carte_adverse in self.cartes_adverses:
                                                        carte_adverse = random.shuffle(self.cartes_adverses)
                                                    if carte.statistique_en_cours > carte_adverse.statistique_en_cours:
                                                        carte = carte_possedee in self.cartes_possedees
                                                        carte_adverse = carte_possedee in self.cartes_possedees
                                                        carte_adverse_rester = carte_possedee in self.cartes_possedees
                                                        carte_adverse_possedee_rester = carte_possedee in self.cartes_possedees
                                                        print("Le talent Rester s'active ! Les cartes liées",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," sont regagnées !")
                                                        print("Le talent Rester n'est plus actif. Les cartes",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," ne sont plus liées.")
                                                    elif carte.statistique_en_cours < carte_adverse.statistique_en_cours:
                                                        carte = carte_adverse in self.cartes_adverses
                                                        carte_adverse = carte_adverse in self.cartes_adverses
                                                        carte_adverse_rester = carte_adverse in self.cartes_adverses
                                                        carte_adverse_possedee_rester = carte_possedee in self.cartes_possedees
                                                        print("Le talent Rester ne s'active pas. Les cartes",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," sont conservées.")
                                                        print("Le talent Rester n'est plus actif. Les cartes",carte_adverse_perdue_rester.carte.nom," et",carte_adverse_rester.carte.nom," ne sont plus liées.")
                                                    else:
                                                        break
                                                    self.tour_actuel = self.compteur_de_tours
                                    else:
                                        return
                                else:
                                    while carte_possedee_rester.statistique_en_cours == carte_adverse.statistique_en_cours:
                                        for carte_possedee in self.cartes_possedees:
                                            carte = random.shuffle(self.cartes_possedees)
                                        for carte_adverse in self.carte_adverses:
                                            carte_adverse = random.shuffle(self.cartes_adverses)
                                        if carte_possedee_rester.statistique_en_cours > carte_adverse.statistique_en_cours:
                                            carte_possedee_rester = carte_possedee in self.cartes_possedees
                                            carte_adverse = carte_possedee in self.cartes_possedees
                                            carte_adverse_rester = carte_possedee in self.cartes_possedees
                                            print("Le talent Rester s'active ! La carte",carte_possedee_rester.carte.nom," liée à la carte",carte_adverse_possedee_rester.carte.nom," est regagnée !")
                                            print("Le talent Rester n'est plus actif. Les cartes",carte_possedee_rester.carte.nom," et",carte_adverse_possedee_rester.carte.nom," ne sont plus liées.")
                                        elif carte_possedee_rester.statistique_en_cours < carte_adverse.statistique_en_cours:
                                            carte_possedee_rester = carte_adverse in self.cartes_adverses
                                            carte_adverse = carte_adverse in self.cartes_adverses
                                            carte_adverse_rester = carte_adverse in self.cartes_adverses
                                            print("Le talent Rester ne s'active pas. La carte",carte_possedee_rester.carte.nom," n'est pas regagnée. La carte",carte_adverse_possedee_rester.carte.nom," est conservée.")
                                            print("Le talent Rester n'est plus actif. Les cartes",carte_possedee_rester.carte.nom," et",carte_adverse_possedee_rester.carte.nom," ne sont plus liées.")
                                        else:
                                            break
                            elif carte_adverse_possedee_rester == carte:
                                print("La carte",carte_possedee_rester.carte.nom," liée à la carte", carte_adverse_possedee_rester.carte.nom," est jouée ! Le talent Rester est réactif !")
                                if carte_adverse_possedee_rester.statistique_en_cours > carte.statistique_en_cours:
                                    carte_adverse_possedee_rester = carte_possedee in self.cartes_possedees
                                    carte = carte_possedee in self.cartes_possedees
                                    carte_adverse_rester = carte_possedee in self.cartes_possedees
                                    print("Le talent Rester s'active ! Les cartes liées",carte_adverse_possedee_rester.carte.nom," et",carte_adverse_rester.carte.nom," sont conservées !")
                                    print("Le talent Rester n'est plus actif. Les cartes",carte_adverse_possedee_rester.carte.nom," et",carte_adverse_rester.carte.nom," ne sont plus liées.")
                                elif carte_adverse_possedee_rester.statistique_en_cours < carte.statistique_en_cours:
                                    carte_adverse_possedee_rester = carte_adverse_rester in self.cartes_adverses
                                    carte = carte_adverse in self.cartes_adverses
                                    print("Le talent Rester s'active ! La carte",carte_adverse_possedee_rester.nom," est perdue. La carte",carte_adverse_rester.nom," est conservée.")
                                    print("Le talent Rester reste actif. Les cartes",carte_adverse_possedee_rester.nom," et",carte_adverse_rester.nom," sont toujours liées.")
                                    if self.compteur_de_tours > self.tour_actuel:
                                        while carte != carte_possedee_rester:
                                            break
                                        while carte_adverse != carte_adverse_rester:
                                            break
                                        if carte == carte_possedee_rester:
                                            if carte.statistique_en_cours > carte_adverse_rester.statistique_en_cours:
                                                carte = carte_possedee in self.cartes_possedees
                                                carte_adverse_rester = carte_possedee in self.cartes_possedees
                                                print("Le talent Rester s'active ! La carte",carte_possedee_rester.carte," liée à la carte",carte_adverse_rester.carte," est regagnée !")
                                                print("Le talent Rester n'est plus actif. Les cartes",carte_possedee_rester.carte," et",carte_adverse_rester.carte," ne sont plus liées.")
                                            elif carte.statistique_en_cours < carte_adverse_rester.statistique_en_cours:
                                                carte = carte_adverse in self.cartes_adverses
                                                carte_adverse_rester in self.cartes_adverses
                                                carte_adverse_possedee_rester = carte_possedee in self.cartes_possedees
                                                print("Le talent Rester ne s'active pas. La carte",carte_possedee_rester," n'est pas regagnée. La carte",carte_adverse_rester," est conservée.")
                                                print("Le talent Rester n'est plus actif. Les cartes",carte_possedee_rester," et",carte_adverse_rester," ne sont plus liées.")
                                            else:
                                                while carte.statistique_en_cours == carte_adverse.statistique_en_cours:
                                                    for carte_possedee in self.cartes_possedees:
                                                        carte = random.shuffle(self.cartes_possedees)
                                                    for carte_adverse in self.cartes_adverses:
                                                        carte_adverse = random.shuffle(self.cartes_adverses)
                                                    if carte.statistique_en_cours > carte_adverse.statistique_en_cours:
                                                        carte = carte_possedee in self.cartes_possedees
                                                        carte_adverse = carte_possedee in self.cartes_possedees
                                                        carte_adverse_rester = carte_possedee in self.cartes_possedees
                                                        carte_adverse_perdue_rester = carte_possedee in self.cartes_possedees
                                                        print("Le talent Rester s'active ! La carte ... (truncated in archive)")
                                                    self.tour_actuel = self.compteur_de_tours
                
                elif carte.talent == "Para-chute":
                    if carte.talent.para_chute == carte.premiere_fois:
                        carte.talent.para_chute.vie_initiale = carte.talent.para_chute.vie
                        carte.talent.para_chute.vie = carte.talent.para_chute.vie*1.5
                        print("Le talent Para-chute de la carte",carte.talent.para_chute.nom," est actif ! Sa vie augmente de 50% pour ce tour !")
                        if self.compteur_de_tours == self.compteur_de_tours + 1:
                            carte.talent.para_chute.vie = carte.talent.para_chute.vie_initiale
                            print("Le talent Para-chute de la carte",carte.talent.para_chute.nom," n'est plus actif. La vie de la carte",carte.talent.para_chute.nom," revient à sa valeur initiale.")
                        else:
                            return
                    else:
                        return
                    
                elif carte.talent == "Système Tactique":
                    carte.roulement = False
                    if carte.talent.systeme_tactique == carte:
                        statistique_choisie = int(input("Quelle statistique de",carte.statistique_en_cours,"souhaitez-vous jouer ?"))
                        if statistique_choisie == 1:
                            carte.statistique_en_cours = carte.statistique_choisie.de_base
                            print("La statistique choisie est",carte.talent.systeme_tactique.statistique_choisie," !")
                        elif statistique_choisie == 2:
                            if self.statistique_en_cours.deux == True:
                                carte.statistique_en_cours = carte.statistique_choisie.deux
                                print("La statistique choisie est",carte.talent.systeme_tactique.statistique_choisie," !")
                            else:
                                print("La statistique choisie n'existe pas ! Choisissez-en une autre.")
                                return
                        elif statistique_choisie == 3:
                            if self.statistique_en_cours.trois == True:
                                carte.statistique_en_cours = carte.statistique_choisie.trois
                                print("La statistique choisie est",carte.talent.systeme_tactique.statistique_choisie," !")
                            else:
                                print("La statistique choisie n'existe pas ! Choisissez-en une autre.")
                                return
                        elif statistique_choisie == 4:
                            if self.statistique_en_cours.quatre == True:
                                carte.statistique_en_cours = carte.statistique_choisie.quatre
                                print("La statistique choisie est",carte.talent.systeme_tactique.statistique_choisie," !")
                            else:
                                print("La statistique choisie n'existe pas ! Choisissez-en une autre.")
                        elif statistique_choisie == 5:
                            if self.statistique_en_cours.cinq == True:
                                carte.statistique_en_cours = carte.statistique_choisie.cinq
                                print("La statistique choisie est",carte.talent.systeme_tactique.statistique_choisie," !")
                            else:
                                print("La statistique choisie n'existe pas ! Choisissez-en une autre.")
                        else:
                            print("La statistique choisie n'existe pas ! Choisissez-en une autre.")
                    else:
                        return
                
                elif carte.talent == "emport":
                    carte_adverse_ignoree = carte_adverse
                    if carte_adverse_ignoree in self.cartes_adverses:
                        self.cartes_adverses.remove(carte_adverse_ignoree)
                        print("Le talent Emport de la carte",carte.talent.emport.nom," est actif ! La carte",carte_adverse_ignoree.nom," est sur le point de se faire remplacer !")
                        print("Tirage au sort en cours...")
                        if len(self.cartes_adverses) > 0:
                            max_attaque = 0
                            max_vitesse = 0
                            max_defense = 0
                            max_vie = 0
                            max_puissance = 0
                            for carte_adverse in self.cartes_adverses:
                                if carte_adverse.attaque > max_attaque:
                                    max_attaque = carte_adverse.attaque
                                elif carte_adverse.vitesse > max_vitesse:
                                    max_vitesse = carte_adverse.vitesse
                                elif carte_adverse.defense > max_defense:
                                    max_defense = carte_adverse.defense
                                elif carte_adverse.vie > max_vie:
                                    max_vie = carte_adverse.vie
                                elif carte_adverse.puissance > max_puissance:
                                    max_puissance = carte_adverse.puissance
                            meilleures_statistiques = [
                                ("attaque", max_attaque),
                                ("vitesse", max_vitesse),
                                ("defense", max_defense),
                                ("vie", max_vie),
                                ("puissance", max_puissance)
                            ]
                            statistique_tiree = random.choice(meilleures_statistiques)
                            for carte_adverse in self.cartes_adverses:
                                if self.statistique.nom == "attaque" and carte_adverse.attaque == self.valeur_tiree:
                                    carte_choisie = carte_adverse
                                if self.statistique.nom == "vitesse" and carte_adverse.vitesse == self.valeur_tiree:
                                    carte_choisie = carte_adverse
                                if self.statistique.nom == "defense" and carte_adverse.defense == self.valeur_tiree:
                                    carte_choisie = carte_adverse
                                if self.statistique.nom == "vie" and carte_adverse.vie == self.valeur_tiree:
                                    carte_choisie = carte_adverse
                                if self.statistique.nom == "puissance" and carte_adverse.puissance == self.valeur_tiree:
                                    carte_choisie = carte_adverse
                                print(f"Tirage au sort effectué ! La carte",carte_adverse_ignoree.nom," est remplacée par",carte_choisie.nom," .")
                                if self.compteur_de_tours > self.tour_actuel:
                                    self.cartes_adverses.append(carte_adverse_ignoree)
                                    print("Le talent Emport n'est plus actif. La carte",carte_adverse_ignoree.nom," est réintégrée parmi les cartes adverses.")
                                    self.tour_actuel = self.compteur_de_tours
                                else:
                                    return
                        else:
                            return
                    else:
                        return
                elif carte.talent == "Statique":
                    if carte == carte.talent.statique:
                        carte_adverse = self.carte_statique
                        print("Le talent Statique de la carte",carte.talent.statique.nom," est actif ! La carte",self.carte_statique," est impactée.")
                        if carte == carte.talent.statique and carte_adverse == self.carte_statique:
                            self.carte_statique.statistique_en_vigueur = 0
                            print("Le talent Statique de la carte",carte.talent.statique.nom," s'active ! La statistique",carte.statistique_en_cours," de la carte",carte.statique," est annulée !")
                            if self.compteur_de_tours > self.tour_actuel:
                                if carte.statistique_en_cours > carte_adverse.statistique_en_cours:
                                    carte_statique = carte_possedee in self.cartes_possedees
                                elif carte.statistique_en_cours < carte_adverse.statistique_en_cours:
                                    carte_statique = carte_adverse in self.cartes_adverses
                                else:
                                    while carte.statistique_en_cours == carte_adverse.statistique_en_cours:
                                        for carte_possedee in self.cartes_possedees:
                                            carte = random.shuffle(self.cartes_possedees)
                                        for carte_adverse in self.cartes_adverses:
                                            carte_adverse = random.shuffle(self.cartes_adverses)
                                            if carte.statistique_en_cours > carte_adverse.statistique_en_cours:
                                                carte = carte_possedee in self.cartes_possedees
                                                carte_adverse = carte_possedee in self.cartes_possedees
                                                carte.statique = carte_possedee in self.cartes_possedees
                                            elif carte.statistique_en_cours < carte_adverse.statistique_en_cours:        
                                                carte = carte_adverse in self.cartes_adverses
                                                carte_adverse = carte_adverse in self.cartes_adverses
                                                carte.statique = carte_adverse in self.cartes_adverses
                                            else:
                                                break
                                            self.tour_actuel = self.compteur_de_tours
                            else:
                                return
                        else:
                            return
                    else:
                        return
                elif carte.talent == "Fibulatio":
                    if carte.talent == "Fibulatio":
                        print("Le talent Fibulatio de la carte", carte.nom, "est actif !")
                        if self.effet_fibulatio == 0:
                            self.effet_fibulatio = 3
                            self.tour_debut_fibulatio = self.compteur_de_tours + 1
                            print("L'effet Fibulatio s'enclenche pour les 3 prochains tours à partir du tour suivant.")
                        elif self.effet_fibulatio > 0:
                            self.effet_fibulatio += 3
                            print("Le talent Fibulatio est réactivé ! L'effet se prolonge de 3 tours supplémentaires !")
                            print("Nombre de tours restants :", self.effet_fibulatio)
                        if self.compteur_de_tours >= self.tour_debut_fibulatio:
                            carte_adverse.vie_initiale = carte_adverse.vie
                            carte_adverse.vie = carte_adverse.vie * 0.85
                            print("La vie de la carte adverse", carte_adverse.nom, "est réduite de 15% pour ce tour.")
                            if self.compteur_de_tours > self.tour_actuel:
                                carte_adverse.vie = carte_adverse.vie_initiale
                                print("L'effet Fibulatio cesse pour ce tour, la carte", carte_adverse.nom, "retrouve sa vie initiale.")
                                self.tour_actuel = self.compteur_de_tours
                                self.effet_fibulatio -= 1
                                if self.effet_fibulatio <= 0:
                                    self.effet_fibulatio = 0
                                    print("Le talent Fibulatio n'est plus actif.")
                                else:
                                    print("Tours restants pour l'effet Fibulatio :", self.effet_fibulatio)
                            else:
                                return
                        else:
                            print("L'effet Fibulatio commencera au prochain tour.")
                    else:
                        return
