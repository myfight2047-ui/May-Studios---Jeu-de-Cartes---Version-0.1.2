# ------------------ IMPORTS ------------------
import tkinter as tk
import customtkinter as ctk
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
        

    
#------------------ PAGE : IUInGame ------------------
class IUInGameFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="darkred")
        ctk.CTkProgressBar(self, border_color="a").pack(pady=20)



        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                      command=lambda: master.show_frame(MenuFrame)).pack(pady=20)
        

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
                           "Graphismes : ISTOC Darius"),
                     font=("Arial", 16)).pack(pady=10)

        ctk.CTkButton(self, text="Retour au menu", width=200, height=40,
                      command=lambda: master.show_frame(MenuFrame)).pack(pady=40)


# ------------------ LANCEMENT DU PROGRAMME ------------------
if __name__ == "__main__":
    app = JeuDeCartes()
    app.mainloop()
