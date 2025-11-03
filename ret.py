# jeu_tkinter_pur.py
import tkinter as tk
from tkinter import messagebox
import random
import math
import os

# ------------------ DONNÉES DU JEU ------------------
personnages = {
    "perso1": {"nom": "Chevalier Rouge", "pv": 100, "attaque": 25, "defense": 15, "vitesse": 10},
    "perso2": {"nom": "Mage Bleu", "pv": 70, "attaque": 40, "defense": 10, "vitesse": 20},
    "perso3": {"nom": "Archer Vert", "pv": 85, "attaque": 30, "defense": 12, "vitesse": 25},
}

# ------------------ UTILITAIRES ------------------
def try_load_image(path, width=None, height=None):
    """Essaie de charger une image via PhotoImage (supporte PNG/GIF). Si échec, renvoie None."""
    if not os.path.isfile(path):
        return None
    try:
        img = tk.PhotoImage(file=path)
        # PhotoImage can't easily resize without PIL; returns as is.
        return img
    except Exception:
        return None

# ------------------ CLASSE PRINCIPALE ------------------
class JeuDeCartes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jeu de cartes par May Studio")
        self.geometry("800x600")
        self.minsize(600, 400)
        self.configure(bg="#111")

        self.sauvegardeencours = ""

        # Barre de menu en haut
        self.creer_menu()

        # Frames principales
        self.frames = {}
        frame_classes = (
            MenuFrame, JouerFrame, ADMFrame, FuturParametresFrame, IUADMFrame,
            IUInGameFrame, EditorSkinFrame, MatchMaking, SkinFrame,
            CombatVsAutreFrame, CombatVsBotFrame, ParametresFrame, CreditsFrame,
            ProfilFrame
        )
        for F in frame_classes:
            frame = F(self)
            self.frames[F] = frame
            # placer sous la barre du menu (barre = 50px hauteur)
            frame.place(relx=0, rely=50/600, relwidth=1, relheight=1 - 50/600)

        self.show_frame(MenuFrame)

    # ------------------ BARRE DE MENU ------------------
    def creer_menu(self):
        menu_bar = tk.Frame(self, bg="#222", height=50)
        menu_bar.place(x=0, y=0, relwidth=1)

        def btn(x, text, cmd, fg="#eee", bg="#333"):
            b = tk.Button(menu_bar, text=text, command=cmd, bg=bg, fg=fg, bd=0)
            b.place(relx=x, rely=0.15, width=120, height=30)
            return b

        btn(0.02, "💾 Enregistrer", self.save)
        btn(0.20, "🆕 Nouvelle partie", self.newgame, bg="#444")
        btn(0.43, "📂 Charger", self.load)
        # quitter en rouge
        bquit = tk.Button(menu_bar, text="❌ Quitter", command=self.quit, bg="#aa0000", fg="white", bd=0)
        bquit.place(relx=0.86, rely=0.15, width=100, height=30)

    # ------------------ MÉTHODES DE GESTION DE SAUVEGARDE ------------------
    def save(self):
        try:
            with open("sauvegarde_jeu_de_carte_MayStudio.txt", "w", encoding="utf-8") as fichier:
                fichier.write(self.sauvegardeencours)
            print("💾 Partie enregistrée.")
            messagebox.showinfo("Sauvegarde", "Partie enregistrée.")
        except Exception as e:
            print("Erreur sauvegarde:", e)
            messagebox.showerror("Erreur", f"Impossible d'enregistrer : {e}")

    def newgame(self):
        self.sauvegardeencours = ""
        try:
            with open("sauvegarde_jeu_de_carte_MayStudio.txt", "w", encoding="utf-8") as fichier:
                fichier.write("")
            print("🎮 Nouvelle partie lancée.")
            messagebox.showinfo("Nouvelle partie", "Nouvelle partie lancée.")
        except Exception as e:
            print("Erreur:", e)
            messagebox.showerror("Erreur", f"Impossible : {e}")

    def load(self):
        try:
            with open("sauvegarde_jeu_de_carte_MayStudio.txt", "r", encoding="utf-8") as fichier:
                self.sauvegardeencours = fichier.read()
            print("📂 Partie chargée.")
            messagebox.showinfo("Chargement", "Partie chargée.")
        except FileNotFoundError:
            print("⚠️ Aucune sauvegarde trouvée.")
            messagebox.showwarning("Chargement", "Aucune sauvegarde trouvée.")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# ------------------ PAGE : MENU PRINCIPAL ------------------
class MenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="red")

        container = tk.Frame(self, bg=self["bg"])
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Jeu de cartes par May Studio",
                 font=("Arial", 32, "bold"), fg="white", bg="red").pack(pady=(0, 40))

        tk.Button(container, text="Jouer", width=30, height=2,
                  font=("Arial", 12, "bold"),
                  command=lambda: master.show_frame(JouerFrame)).pack(pady=10)

        tk.Button(container, text="Skin", width=30, height=2,
                  font=("Arial", 12, "bold"),
                  command=lambda: master.show_frame(SkinFrame)).pack(pady=10)

        tk.Button(container, text="Paramètres", width=30, height=2,
                  font=("Arial", 12, "bold"),
                  command=lambda: master.show_frame(ParametresFrame)).pack(pady=10)

        tk.Button(container, text="Crédits", width=30, height=2,
                  font=("Arial", 12, "bold"),
                  command=lambda: master.show_frame(CreditsFrame)).pack(pady=10)

        tk.Button(container, text="ADM", width=30, height=2,
                  font=("Arial", 12, "bold"),
                  command=lambda: master.show_frame(ADMFrame)).pack(pady=10)

        tk.Button(container, text="Fermer le jeu", width=30, height=2,
                  font=("Arial", 12, "bold"),
                  bg="darkred", fg="white",
                  command=master.quit).pack(pady=20)


# ------------------ PAGE : SKIN ------------------
class SkinFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")

        # ------------------ LISTE DES SKINS ------------------
        self.skins = [
            {"nom": "Skin 1", "image": "images/S1.png"},
            {"nom": "Skin 2", "image": "images/S2.png"},
        ]
        self.index_skin = 0
        self.tk_image = None  # reference pour PhotoImage

        tk.Label(self, text="Mode : Skin", font=("Arial", 28, "bold"), bg="darkred", fg="white").pack(pady=40)

        # Charger image (fallback si impossible)
        self.image_label = tk.Label(self, bg="darkred")
        self.image_label.pack(pady=10)
        self.label_skin = tk.Label(self, text="", font=("Arial", 20), bg="darkred", fg="white")
        self.label_skin.pack(pady=10)

        btn_frame = tk.Frame(self, bg="darkred")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Skin suivant", width=20, command=self.suivant_skin).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Retour au menu", width=20, command=lambda: master.show_frame(MenuFrame)).pack(side="left", padx=10)

        self.update_skin_display()

    def update_skin_display(self):
        skin = self.skins[self.index_skin]
        self.label_skin.config(text=f"Skin actuel : {skin['nom']}")
        img = try_load_image(skin["image"])
        if img:
            self.tk_image = img
            self.image_label.config(image=self.tk_image, text="")
        else:
            # fallback text (car pas de PIL / image non supportée)
            self.tk_image = None
            self.image_label.config(image="", text=f"[Image non disponible]\n{skin['image']}", fg="white")

    def suivant_skin(self):
        self.index_skin = (self.index_skin + 1) % len(self.skins)
        self.update_skin_display()


# ------------------ PAGE : ADM ------------------
class ADMFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        container = tk.Frame(self, bg="darkred")
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="ADM", font=("Arial", 32, "bold"), fg="white", bg="darkred").pack(pady=(0, 40))

        tk.Button(container, text="IU Jouer", width=30, command=lambda: master.show_frame(IUInGameFrame)).pack(pady=10)
        tk.Button(container, text="Editer Skin", width=30, command=lambda: master.show_frame(EditorSkinFrame)).pack(pady=10)
        tk.Button(container, text="Paramètres", width=30, command=lambda: master.show_frame(FuturParametresFrame)).pack(pady=10)
        tk.Button(container, text="Profil", width=30, command=lambda: master.show_frame(ProfilFrame)).pack(pady=10)
        tk.Button(container, text="IUADM", width=30, command=lambda: master.show_frame(IUADMFrame)).pack(pady=10)
        tk.Button(container, text="Fermer le jeu", width=30, bg="darkred", fg="white", command=master.quit).pack(pady=20)


# ------------------ IU INGAME (interface de jeu) ------------------
class IUInGameFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")

        # TOP : titre + barre de progression (canvas)
        top_bar = tk.Frame(self, bg=self["bg"])
        top_bar.pack(fill="x", pady=(5, 0))
        tk.Label(top_bar, text="Manche 1", font=("Arial", 20, "bold"), fg="white", bg=self["bg"]).pack(pady=(5, 3))
        self.progress_canvas = tk.Canvas(top_bar, width=300, height=12, bg="#333", highlightthickness=0)
        self.progress_canvas.pack()
        self.set_progress(50)  # 50%

        # Table de jeu
        table_frame = tk.Frame(self, bg="#5a0f0f", bd=0)
        table_frame.pack(expand=True, fill="both", padx=20, pady=10)
        tk.Label(table_frame, text="Zone de jeu", font=("Arial", 18, "bold"), bg="#5a0f0f", fg="white").place(relx=0.5, rely=0.05, anchor="center")

        # Cartes posées
        self.cards_zone = tk.Frame(table_frame, bg="#5a0f0f")
        self.cards_zone.place(relx=0.47, rely=0.5, anchor="center")

        adv_card_border = tk.Frame(self.cards_zone, width=130, height=180, bg="#5a0f0f", highlightbackground="white", highlightthickness=3)
        adv_card_border.pack(pady=10)
        adv_card_border.pack_propagate(False)
        tk.Label(adv_card_border, text="Carte adverse", bg="#5a0f0f", fg="white").place(relx=0.5, rely=0.5, anchor="center")

        player_card_border = tk.Frame(self.cards_zone, width=130, height=180, bg="#5a0f0f", highlightbackground="white", highlightthickness=3)
        player_card_border.pack(pady=10)
        player_card_border.pack_propagate(False)
        tk.Label(player_card_border, text="Votre carte", bg="#5a0f0f", fg="white").place(relx=0.5, rely=0.5, anchor="center")

        # Pioche
        self.pioche_frame = tk.Frame(table_frame, width=130, height=180, bg="#3b0a0a", highlightbackground="gold", highlightthickness=3)
        self.pioche_frame.place(relx=0.60, rely=0.5, anchor="center")
        self.pioche_frame.pack_propagate(False)
        tk.Label(self.pioche_frame, text="🂠 Pioche", font=("Arial", 14, "bold"), bg="#3b0a0a", fg="gold").place(relx=0.5, rely=0.4, anchor="center")
        self.draw_button = tk.Button(self.pioche_frame, text="Piocher", width=10, command=self.draw_card)
        self.draw_button.place(relx=0.5, rely=0.75, anchor="center")

        # Info adversaire
        adv_info = tk.Frame(table_frame, width=180, height=80, bg="#3b0a0a")
        adv_info.place(relx=0.97, rely=0.08, anchor="ne")
        adv_info.pack_propagate(False)
        tk.Label(adv_info, text="Cartes adversaire", font=("Arial", 14, "bold"), bg="#3b0a0a", fg="white").pack(pady=3)
        self.nb_cartes_adv = tk.Label(adv_info, text="Nombre : 5", font=("Arial", 16), bg="#3b0a0a", fg="white")
        self.nb_cartes_adv.pack()

        # Chat flottant (déplaçable)
        self.chat_frame = tk.Frame(self, width=220, height=170, bg="#3b0a0a", bd=0)
        self.chat_frame.place(x=40, y=100)
        self.chat_frame.pack_propagate(False)
        tk.Label(self.chat_frame, text="💬 Chat", font=("Arial", 14, "bold"), bg="#3b0a0a", fg="white").pack(anchor="w", padx=5, pady=3)
        self.chat_box = tk.Text(self.chat_frame, width=30, height=5)
        self.chat_box.pack(padx=5, pady=5)
        self.chat_entry = tk.Entry(self.chat_frame)
        self.chat_entry.insert(0, "Écrire un message...")
        self.chat_entry.bind("<Return>", self.send_message)
        self.chat_entry.bind("<FocusIn>", self._clear_placeholder)
        self.chat_entry.bind("<FocusOut>", self._restore_placeholder)
        self.chat_entry.pack(fill="x", padx=5, pady=(0, 5))
        self.chat_frame.bind("<Button-1>", self.start_move_chat)
        self.chat_frame.bind("<B1-Motion>", self.do_move_chat)

        # Panel d'infos à droite
        self.info_frame = tk.Frame(self, width=260, bg="#3b0a0a")
        self.info_frame.place(relx=0.975, rely=0.5, anchor="e", relheight=0.55)
        self.info_frame.pack_propagate(False)

        tk.Label(self.info_frame, text="📜 Carte sélectionnée", font=("Arial", 16, "bold"), bg="#3b0a0a", fg="white").pack(pady=(10, 5))
        self.card_name_label = tk.Label(self.info_frame, text="Aucune carte", font=("Arial", 15), bg="#3b0a0a", fg="white")
        self.card_name_label.pack(pady=5)
        self.card_stats_label = tk.Label(self.info_frame, text="Attaque : -\nDéfense : -\nMagie : -\nVitesse : -", font=("Arial", 13), bg="#3b0a0a", fg="white", justify="left")
        self.card_stats_label.pack(pady=5)

        # Graphique radar (canvas)
        self.graph_frame = tk.Frame(self.info_frame, bg="#4d0f0f")
        self.graph_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Bouton jouer
        self.play_button = tk.Button(self.info_frame, text="🎯 Jouer cette carte", width=25, state="disabled", command=self.play_selected_card)
        self.play_button.pack(side="bottom", pady=10)

        # Bas : vos cartes
        bottom_frame = tk.Frame(self, bg=self["bg"])
        bottom_frame.pack(side="bottom", fill="x", pady=(0, 40))
        player_cards_frame = tk.Frame(bottom_frame, bg="#3b0a0a")
        player_cards_frame.pack(side="left", padx=10)
        tk.Label(player_cards_frame, text="Vos cartes :", font=("Arial", 14, "bold"), bg="#3b0a0a", fg="white").pack(pady=5)

        self.cartes_joueur = []
        for i in range(5):
            stats = {
                "nom": f"Carte {i+1}",
                "Attaque": 10 + i * 3,
                "Défense": 5 + i * 2,
                "Magie": 7 + i,
                "Vitesse": 8 + i * 2
            }
            carte = tk.Button(player_cards_frame, text=stats["nom"], width=10, height=4, command=lambda s=stats: self.select_card(s))
            carte.pack(side="left", padx=5, pady=5)
            self.cartes_joueur.append(carte)

        menu_button = tk.Button(bottom_frame, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame))
        menu_button.pack(side="right", padx=20)

    # Progress bar (canvas)
    def set_progress(self, percent):
        self.progress_canvas.delete("all")
        w = 300
        h = 12
        self.progress_canvas.create_rectangle(0, 0, w, h, fill="#333", outline="")
        fill_w = int(w * max(0, min(100, percent)) / 100)
        self.progress_canvas.create_rectangle(0, 0, fill_w, h, fill="#55aa55", outline="")

    # Chat helpers
    def _clear_placeholder(self, event):
        if self.chat_entry.get() == "Écrire un message...":
            self.chat_entry.delete(0, "end")

    def _restore_placeholder(self, event):
        if not self.chat_entry.get().strip():
            self.chat_entry.insert(0, "Écrire un message...")

    def send_message(self, event=None):
        msg = self.chat_entry.get().strip()
        if not msg or msg == "Écrire un message...":
            messagebox.showwarning("Chat", "Message vide interdit !")
            return
        self.chat_box.insert("end", f"Vous: {msg}\n")
        self.chat_box.see("end")
        self.chat_entry.delete(0, "end")

    # Drag chat
    def start_move_chat(self, event):
        self.chat_offset_x = event.x
        self.chat_offset_y = event.y

    def do_move_chat(self, event):
        x = self.chat_frame.winfo_x() + event.x - self.chat_offset_x
        y = self.chat_frame.winfo_y() + event.y - self.chat_offset_y
        # limiter dans la fenêtre
        if x < 0: x = 0
        if y < 50: y = 50  # ne pas recouvrir la barre de menu
        self.chat_frame.place(x=x, y=y)

    # Piocher
    def draw_card(self):
        messagebox.showinfo("Pioche", "Vous avez pioché une nouvelle carte !")

    # Sélection carte
    def select_card(self, stats):
        self.card_name_label.config(text=stats["nom"])
        self.card_stats_label.config(text="\n".join([f"{k} : {v}" for k, v in stats.items() if k != "nom"]))
        self.play_button.config(state="normal")
        self.selected_card = stats
        self.update_chart(stats)

    def play_selected_card(self):
        if hasattr(self, "selected_card"):
            messagebox.showinfo("Carte jouée", f"Vous avez joué {self.selected_card['nom']} !")
            self.play_button.config(state="disabled")
            self.card_name_label.config(text="Aucune carte")
            self.card_stats_label.config(text="Attaque : -\nDéfense : -\nMagie : -\nVitesse : -")
            self.update_chart(None)
            del self.selected_card

    # Radar chart drawing
    def update_chart(self, stats):
        for w in self.graph_frame.winfo_children():
            w.destroy()
        canvas_size = 220
        canvas = tk.Canvas(self.graph_frame, width=canvas_size, height=canvas_size, bg="#4d0f0f", highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=5, pady=5)

        if not stats:
            canvas.create_text(canvas_size / 2, canvas_size / 2, text="Aucune carte", fill="white", font=("Arial", 12))
            return

        categories = ["Attaque", "Défense", "Magie", "Vitesse"]
        n = len(categories)
        center = canvas_size / 2
        radius = canvas_size / 2 - 30
        values = [stats[c] for c in categories]
        max_value = max(values + [10])
        avg_values = [sum(values) / n for _ in range(n)]

        # Fond radar
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

        # Carte et moyenne
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

        canvas.create_polygon([coord for p in points_card for coord in p], outline="#ff5555", fill="#ff5555", width=2)
        canvas.create_polygon([coord for p in points_avg for coord in p], outline="#55ff55", fill="#55ff55", width=2)

        for x, y in points_card:
            canvas.create_line(center, center, x, y, fill="#ff5555", width=1)
        for i, (x, y) in enumerate(points_card):
            canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill="#ff5555", outline="#ff5555")
            canvas.create_text(x, y - 14, text=str(values[i]), fill="#ff5555", font=("Arial", 9, "bold"))

        canvas.create_text(canvas_size - 50, 15, text="Carte", fill="#ff5555", font=("Arial", 10))
        canvas.create_text(canvas_size - 50, 30, text="Moyenne", fill="#55ff55", font=("Arial", 10))


# ------------------ EditorSkin ------------------
class EditorSkinFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        tk.Label(self, text="Mode : Editeur de skin", font=("Arial", 28, "bold"), bg="darkred", fg="white").pack(pady=40)
        tk.Button(self, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=20)


# ------------------ FuturParametres ------------------
class FuturParametresFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        tk.Label(self, text="Mode : Futur Paramètres", font=("Arial", 28, "bold"), bg="darkred", fg="white").pack(pady=10)
        entries = [
            "Sensibilité de la souris",
            "Taille de l'écran",
            "Choix de la langue",
            "Thème du jeu",
            "Attribution des touches"
        ]
        for e in entries:
            tk.Label(self, text=f"Mode : {e}", font=("Arial", 18), bg="darkred", fg="white").pack(pady=6)
        tk.Button(self, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=20)


# ------------------ Profil ------------------
class ProfilFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        tk.Label(self, text="Mode : Nom du Joueur", font=("Arial", 28, "bold"), bg="darkred", fg="white").pack(pady=10)
        tk.Label(self, text="Badges" + "🏅" * 5, font=("Arial", 20), bg="darkred", fg="white").pack(pady=10)
        tk.Label(self, text="Niveau : " + str(random.randint(1, 100)), font=("Arial", 20), bg="darkred", fg="white").pack(pady=10)
        tk.Label(self, text="Description perso " + str(random.randint(1, 10000000)), font=("Arial", 16), bg="darkred", fg="white").pack(pady=10)
        tk.Button(self, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=20)


# ------------------ IUADM ------------------
class IUADMFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        tk.Button(self, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=20)


# ------------------ MATCHMAKING ------------------
class MatchMaking(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        tk.Label(self, text="Mode : Matchmaking", font=("Arial", 28, "bold"), bg="darkred", fg="white").pack(pady=20)
        tk.Button(self, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=10)

        # Animation (canvas)
        self.canvas_size = 150
        self.canvas = tk.Canvas(self, width=self.canvas_size, height=self.canvas_size, bg="darkred", highlightthickness=0)
        self.canvas.pack(pady=30)
        self.angle = 0
        self.line_length = 60
        self.center = self.canvas_size // 2
        self.line = self.canvas.create_line(self.center, self.center, self.center + self.line_length, self.center, width=4, fill="white", capstyle="round")
        self.animate_circle()

    def animate_circle(self):
        rad = math.radians(self.angle)
        x = self.center + self.line_length * math.cos(rad)
        y = self.center + self.line_length * math.sin(rad)
        self.canvas.coords(self.line, self.center, self.center, x, y)
        self.angle = (self.angle + 5) % 360
        self.after(50, self.animate_circle)


# ------------------ JOUER ------------------
class JouerFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        container = tk.Frame(self, bg="darkred")
        container.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(container, text="Mode de jeu", font=("Arial", 28, "bold"), bg="darkred", fg="white").pack(pady=40)

        tk.Button(container, text="Combat vs autre (phase de test)", width=30, command=lambda: master.show_frame(MatchMaking)).pack(pady=10)
        tk.Button(container, text="Combat vs bot (phase de test)", width=30, command=lambda: master.show_frame(CombatVsBotFrame)).pack(pady=10)
        tk.Button(container, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=40)


# ------------------ COMBAT VS AUTRE ------------------
class CombatVsAutreFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        tk.Label(self, text="Mode : Combat contre un autre joueur", font=("Arial", 28, "bold"), bg="darkred", fg="white").pack(pady=40)
        tk.Button(self, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=20)


# ------------------ COMBAT VS BOT ------------------
class CombatVsBotFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        tk.Label(self, text="Mode : Combat contre le bot", font=("Arial", 28, "bold"), bg="darkred", fg="white").pack(pady=40)
        perso = personnages["perso2"]
        tk.Label(self, text=f"{perso['nom']} — PV: {perso['pv']} | ATQ: {perso['attaque']} | DEF: {perso['defense']} | VIT: {perso['vitesse']}",
                 font=("Arial", 16), bg="darkred", fg="white").pack(pady=10)
        tk.Button(self, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=40)


# ------------------ PARAMETRES ------------------
class ParametresFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="darkred")
        tk.Label(self, text="Paramètres", font=("Arial", 28, "bold"), bg="darkred", fg="white").pack(pady=40)

        tk.Label(self, text="Volume du jeu :", font=("Arial", 16), bg="darkred", fg="white").pack(pady=10)
        self.scale_vol = tk.Scale(self, from_=0, to=100, orient="horizontal")
        self.scale_vol.pack(pady=10)

        tk.Label(self, text="Nom du joueur :", font=("Arial", 16), bg="darkred", fg="white").pack(pady=10)
        self.entry_pseudo = tk.Entry(self)
        self.entry_pseudo.insert(0, "Entrez votre pseudo")
        self.entry_pseudo.bind("<FocusIn>", lambda e: self._clear_if_placeholder(e, "Entrez votre pseudo"))
        self.entry_pseudo.bind("<FocusOut>", lambda e: self._restore_if_empty(e, "Entrez votre pseudo"))
        self.entry_pseudo.pack(pady=10)

        tk.Button(self, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=40)

    def _clear_if_placeholder(self, event, text):
        if event.widget.get() == text:
            event.widget.delete(0, "end")

    def _restore_if_empty(self, event, text):
        if not event.widget.get().strip():
            event.widget.insert(0, text)


# ------------------ CREDITS ------------------
class CreditsFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="black")
        tk.Label(self, text="Crédits", font=("Arial", 28, "bold"), bg="black", fg="white").pack(pady=30)
        tk.Label(self, text=("Développé par May Studio (2025)\n"
                             "Merci d'avoir joué !\n\n"
                             "Version 0.1 (phase de test)\n\n"
                             "Code : Myfight\n"
                             "Graphismes : ISTOC Darius\n"
                             "une petite donnation ne lui ferait pas de mal :\n"
                             "buymeacoffee.com/DARIUSISTOC1\n"
                             "protodev : Brunet Aaron"),
                 font=("Arial", 16), bg="black", fg="white").pack(pady=10)
        tk.Button(self, text="Retour au menu", width=25, command=lambda: master.show_frame(MenuFrame)).pack(pady=40)


# ------------------ LANCEMENT DU PROGRAMME ------------------
if __name__ == "__main__":
    app = JeuDeCartes()
    app.mainloop()
