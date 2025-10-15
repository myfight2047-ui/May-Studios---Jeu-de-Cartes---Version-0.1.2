# ------------------ IMPORTS ------------------
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import random
import math


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
import customtkinter as ctk
from PIL import Image  # Nécessaire pour afficher les images

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
        



import customtkinter as ctk
from tkinter import messagebox
import math

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

        adv_card_border = ctk.CTkFrame(self.cards_zone, width=130, height=180,
                                       fg_color="transparent", border_color="white", border_width=3, corner_radius=10)
        adv_card_border.pack(pady=70)
        ctk.CTkLabel(adv_card_border, text="Carte adverse", text_color="white").place(relx=0.5, rely=0.5, anchor="center")

        player_card_border = ctk.CTkFrame(self.cards_zone, width=130, height=180,
                                          fg_color="transparent", border_color="white", border_width=3, corner_radius=10)
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

        # ===================== PANEL D’INFOS À DROITE (RÉDUIT) =====================
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
                player_cards_frame, text=stats["nom"],
                width=80, height=100,
                command=lambda s=stats: self.select_card(s)
            )
            carte.pack(side="left", padx=5, pady=5)
            self.cartes_joueur.append(carte)

        menu_button = ctk.CTkButton(bottom_frame, text="Retour au menu", width=200, height=40,
                                    command=lambda: master.show_frame(MenuFrame))
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
            canvas.create_text(canvas_size/2, canvas_size/2, text="Aucune carte", fill="white", font=("Arial", 12))
            return

        categories = ["Attaque", "Défense", "Magie", "Vitesse"]
        n = len(categories)
        center = canvas_size / 2
        radius = canvas_size / 2 - 30

        values = [stats[c] for c in categories]
        max_value = max(values + [10])
        avg_values = [sum(values)/n for _ in range(n)]

        # ---- Fond radar avec graduations ----
        steps = 4
        for s in range(1, steps+1):
            r = radius * s / steps
            points = []
            for i in range(n):
                angle = (i / n) * 2 * math.pi - math.pi/2
                x = center + r * math.cos(angle)
                y = center + r * math.sin(angle)
                points.append((x, y))
            for i in range(n):
                x1, y1 = points[i]
                x2, y2 = points[(i+1) % n]
                canvas.create_line(x1, y1, x2, y2, fill="#555555")
            canvas.create_text(center, max(5, center - r), text=str(int(max_value*s/steps)),
                               fill="#aaaaaa", font=("Arial", 8))

        # ---- Points carte et moyenne ----
        points_card = []
        points_avg = []
        for i, val in enumerate(values):
            angle = (i / n) * 2 * math.pi - math.pi/2
            r = (val / max_value) * radius
            x = center + r * math.cos(angle)
            y = center + r * math.sin(angle)
            points_card.append((x, y))

            r_avg = (avg_values[i] / max_value) * radius
            x_avg = center + r_avg * math.cos(angle)
            y_avg = center + r_avg * math.sin(angle)
            points_avg.append((x_avg, y_avg))

        canvas.create_polygon([coord for point in points_card for coord in point],
                              outline="#ff5555", fill="#ff555540", width=2)
        canvas.create_polygon([coord for point in points_avg for coord in point],
                              outline="#55ff55", fill="#55ff5540", width=2)

        for x, y in points_card:
            canvas.create_line(center, center, x, y, fill="#ff5555", width=1)
        for x, y in points_avg:
            canvas.create_line(center, center, x, y, fill="#55ff55", width=1)

        for i, (x, y) in enumerate(points_card):
            canvas.create_oval(x-4, y-4, x+4, y+4, fill="#ff5555")
            canvas.create_text(x, max(5, y-14), text=str(values[i]), fill="#ff5555", font=("Arial", 9, "bold"))

        for i, (x, y) in enumerate(points_avg):
            canvas.create_oval(x-4, y-4, x+4, y+4, fill="#55ff55")
            canvas.create_text(x, min(canvas_size-5, y+14), text=str(round(avg_values[i],1)),
                               fill="#55ff55", font=("Arial", 9))

        canvas.create_text(canvas_size-50, 15, text="Carte", fill="#ff5555", font=("Arial", 10))
        canvas.create_text(canvas_size-50, 30, text="Moyenne", fill="#55ff55", font=("Arial", 10))









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
