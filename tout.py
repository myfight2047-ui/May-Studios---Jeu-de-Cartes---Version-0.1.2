import random
import tkinter as tk
import easyapip
import math

print("May Studios présente")
print("Jeu de Cartes V.0.1.2")





    #---------------------------FIN DARIUS

class Cartes:
    def Cartes(self, carte, nom, rarete, type_carte, attaque_de_base, vitesse_de_base, defense_de_base, vie_de_base, puissance_de_base, cout, talent, talent_facultatif = None, artefact = None, capacite = None, specialite = None, attaque = None, attaque_deux = None, attaque_trois = None, attaque_quatre = None, attaque_cinq = None, vitesse = None, vitesse_deux = None, vitesse_trois = None, vitesse_quatre = None, vitesse_cinq = None, defense = None, defense_deux = None, defense_trois = None, defense_quatre = None, defense_cinq = None, vie = None, vie_deux = None, vie_trois = None, vie_quatre = None, vie_cinq = None, puissance = None, puissance_deux = None, puissance_trois = None, puissance_quatre = None, puissance_cinq = None):
        self.carte = carte
        self.adverse = adverse
        self.possedee = possedee
        
        self.nom = nom
        self.rarete = rarete
        self.type_carte = type_carte
        self.specialite = specialite
        
        self.attaque = attaque
        self.vitesse = vitesse
        self.defense = defense
        self.vie = vie
        self.puissance = puissance

        self.de_base = vitesse_de_base
        self.deux = vitesse_deux
        self.trois = vitesse_trois
        self.quatre = vitesse_quatre
        self.cinq = vitesse_cinq

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
        self.roulement = roulement
        self.seconde = seconde
        seconde = vie*125
        
    class bibliotheque_de_cartes:  
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
            def Aura_Sphere(self):  
                self.nom = "Aura-Sphère"
                self.numero = "8"
                self.rarete = "Mythique"
                self.type_carte = "Foudre"
                self.attaque.de_base = 100
                self.vitesse.de_base = 1.25
                self.defense.de_base = 0
                self.vie.de_base = self.seconde.Aura_Sphere
                self.seconde.Aura_Sphere = 10
                self.puissance.de_base = 5
                self.cout = 5
                self.talent = "Rester"
                
        class Guerrier_Aerien:   
            def Guerrier_Aerien(self):  
                self.nom = "Guerrier Aérien"
                self.numero = "9"
                self.rarete = "Epique"
                self.type_carte = "Royauté"
                self.attaque.de_base = 225
                self.vitesse.de_base = 1
                self.defense.de_base = 6
                self.vie.de_base = 1500
                self.puissance.de_base = 6
                self.cout = 4
                self.talent = "Para-Chute" # Augmente la vie de 50%, seulement au premier tour
                
        class Roue_Gobeline:   
            def Roue_Gobeline(self):  
                self.nom = "Roue Gobeline"
                self.numero = "10"
                self.rarete = "Rare"
                self.type_carte = "Technologie"
                self.attaque.de_base = 125
                self.attaque.deux = 75
                self.vitesse.de_base = 1
                self.vitesse.deux = 3
                self.defense.de_base = 10
                self.defense.deux = 4
                self.vie.de_base = 0
                self.vie.deux = 250
                self.puissance.de_base = 3
                self.cout = 4
                self.talent = "Bonus Royal"
                
        class Chat_de_Compagnie:   
            def Chat_de_Compagnie(self):  
                self.nom = "Chat de Compagnie"
                self.numero = "11"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 300
                self.attaque.deux = 150
                self.vitesse.de_base = 1
                self.vitesse.deux = 1.5
                self.defense.de_base = 6
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Système Tactique" # Le joueur peut choisir la statistique qu'il préfère lorsque celle-ci se décline sur 2 à 5 plans, parmi toutes les valeurs chiffrées de la carte
                
        class Chien_de_Compagnie:   
            def Chien_de_Compagnie(self):  
                self.nom = "Chien de Compagnie"
                self.numero = "12"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 550
                self.attaque.deux = 225
                self.vitesse.de_base = 1
                self.vitesse.deux = 0.75
                self.defense.de_base = 6
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Système Tactique"
                
        class Guerriers_Elite:   
            def Guerriers_Elite(self):  
                self.nom = "Guerriers d'Elite"
                self.numero = "13"
                self.rarete = "Epique"
                self.type_carte = "Royauté"
                self.attaque.de_base = 225
                self.vitesse.de_base = 2
                self.defense.de_base = 6
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 6
                self.talent = "Epée Brute" 
                
        class Phonosort:   
            def Phonosort(self):  
                self.nom = "Phonosort"
                self.numero = "14"
                self.rarete = "Mythique"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 150
                self.vitesse.de_base = 1
                self.defense.de_base = 0
                self.vie.de_base = 250
                self.puissance.de_base = 2
                self.cout = 2
                self.talent = "Rester"
                
        class Tornade:   
            def Tornade(self):  
                self.nom = "Tornade"
                self.numero = "15"
                self.rarete = "Epique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 200
                self.vitesse.de_base = 1
                self.defense.de_base = 10
                self.vie.de_base = 625
                self.puissance.de_base = 3
                self.cout = 3
                self.talent = "Emport" # Remplace la carte adverse par une carte aléatoire ayant une statistique aléatoire la plus forte de son deck
                
        class Drone:   
            def Drone(self):  
                self.nom = "Drone"
                self.numero = "16"
                self.rarete = "Mythique"
                self.type_carte = "Technologie"
                self.attaque.de_base = 300
                self.vitesse.de_base = 0.75
                self.defense.de_base = 6
                self.vie.de_base = 1750
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Statique" # Oppose la statistique prévue telle qu'à l'origine et ce peu importe les protections mises en place par l'adversaire
                
        class Incendie:   
            def Incendie(self):  
                self.nom = "Incendie"
                self.numero = "17"
                self.rarete = "Légendaire"
                self.type_carte = "Feu"
                self.attaque.de_base = 200
                self.vitesse.de_base = 0.5
                self.defense.de_base = 0
                self.vie.de_base = 625
                self.puissance.de_base = 3
                self.cout = 3
                self.talent = "Bonus Royal"
                
        class Prison:   
            def Prison(self):  
                self.nom = "Prison"
                self.numero = "18"
                self.rarete = "Légendaire"
                self.type_carte = "Mystère"
                self.attaque.de_base = 25
                self.vitesse.de_base = 1
                self.defense.de_base = 6
                self.vie.de_base = 2000
                self.puissance.de_base = 4
                self.cout = 4
                self.talent = "Rester"
                
        class Elektromanipulatrice:   
            def Elektromanipulatrice(self):  
                self.nom = "Elektromanipulatrice"
                self.numero = "19"
                self.rarete = "Mythique"
                self.type_carte = "Foudre"
                self.attaque.de_base = 750
                self.vitesse.de_base = 0.25
                self.defense.de_base = 6
                self.vie.de_base = 2000
                self.puissance.de_base = 7
                self.cout = 7
                self.talent = "Division"
                
        class Bombe:   
            def Bombe(self):  
                self.nom = "Bombe"
                self.numero = "20"
                self.rarete = "Commune"
                self.type_carte = "Technologie"
                self.attaque.de_base = 300
                self.vitesse.de_base = 1
                self.defense.de_base = 0
                self.vie.de_base = 0
                self.puissance.de_base = 5
                self.cout = 3 
                self.talent = "Fibulatio" # Crée une zone de brûlure qui réduit temporairement la vie de chaque carte adverse posée sur le terrain de 15% pendant leur tour, et ce pendant 3 tours. L'effet du talent est cumulable à l'infini
                
        class Cage_Elite:   
            def Cage_Elite(self):  
                self.nom = "Cage_Elite"
                self.numero = "21"
                self.rarete = "Commune"
                self.type_carte = "Royauté"
                self.attaque.de_base = 0
                self.attaque.deux = 225
                self.vitesse.de_base = 0
                self.vitesse.deux = 1
                self.attaque_privilegiee.couverture_explosive = self.attaque.deux
                self.defense.de_base = 6
                self.vie.de_base = self.seconde.Cage_Elite
                self.seconde.Cage_Elite = 15
                self.vie.deux = 1500
                self.puissance.de_base = 3
                self.cout = 4
                self.talent = "Couverture Explosive" # A chaque retour à l'attaque désignée comme "privilégiée", inflige des dégâts de zone à hauteur de 5% multiplié par le nombre de tours passés par chaque carte adverse sur le terrain depuis le début de la partie, cumulable à l'infini. Si la vie atteint 0 (100% de dégâts, 20 tours passés sur le terrain), la carte adverse est gagnée, et ce même si elle n'est pas jouée actuellement. Si le talent se repète au cours de la partie, il ne fait qu'ajouter 5% de dégâts à chaque carte déjà touchée, et applique la première logique aux cartes qui ne l'ont pas subi. L'effet ne s'annule que lorsqu'une carte est regagnée, et ne se réactive pas si cette même carte est reperdue
                
        class Cow_Boy:   
            def Cow_Boy(self):  
                self.nom = "Cow-Boy"
                self.numero = "22"
                self.rarete = "Mythique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 100
                self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Mirage" # Après avoir été posée, augmente à chaque tour la chance de l'adversaire de rater son attaque de 2.5%, cumulable jusqu'à 100%, avec 2.5% comme valeur initiale au tour 0. Si l'attaque rate, le talent reste actif, mais se réinitialise à 2.5%. Si l'attaque réussit, le talent rajoute 2.5% à la valeur actuelle. Le talent se désactive si la carte est perdue, mais reste réactivable par l'adversaire s'il rejoue la carte, lui attribuant alors l'effet. Si elle est regagnée, elle réapplique la même logique entre chaque joueur.
                
        class Lianes:   
            def Lianes(self):  
                self.nom = "Lianes"
                self.numero = "23"
                self.rarete = "Commune"
                self.type_carte = "Mystère"
                self.attaque.de_base = 200
                self.vitesse.de_base = 1
                self.defense.de_base = 6
                self.vie.de_base = self.seconde.Lianes
                self.seconde.Lianes = 5
                self.puissance.de_base = 4
                self.cout = 3 
                self.talent = "Rester"
                
        class Cyclope:   
            def Cyclope(self):  
                self.nom = "Cyclope"
                self.numero = "24"
                self.rarete = "Rare"
                self.type_carte = "Mystère"
                self.attaque.de_base = 250
                self.vitesse.de_base = 0.75
                self.defense.de_base = 6
                self.vie.de_base = 2000
                self.puissance.de_base = 5
                self.cout = 5
                self.talent = "Maladresse" # A 20% de chance de rater son attaque, mais si cette dernière loupe, elle est doublée pour les 2 tours suivants. Si au cours de ces 2 tours, l'attaque rate à nouveau, elle est à nouveau multipliée par 2 pour les 2 tours suivants, et ainsi de suite jusqu'à l'infini et de façon exponentielle. Si l'attaque réussit, le talent se réinitialise à l'attaque de base, et garde la probabilité de 20%. Le talent se désactive si la carte est perdue, mais reste réactivable par l'adversaire s'il rejoue la carte, lui attribuant alors l'effet. Si elle est regagnée, elle réapplique la même logique entre chaque joueur.
                
        class Avion_Elite:   
            def Avion_Elite(self):  
                self.nom = "Avion d'Elite"
                self.numero = "25"
                self.rarete = "Epique"
                self.type_carte = "Royauté"
                self.attaque.de_base = 400
                self.attaque.deux = 225
                self.vitesse.de_base = 1
                self.vitesse.deux = 3
                self.defense_de_base = 6
                self.vie_de_base = 2000
                self.vie_deux = 1500
                self.puissance_de_base = 6 
                self.cout = 7
                self.talent = "Largage Progressif" # Lors de son premier tour, commence avec une attaque égale à 200% de son attaque de base, puis diminue de 25% à chaque tour, jusqu'à atteindre 100% de son attaque de base au 5ème tour. A partir du 6ème tour, l'attaque reste à 100% de son attaque de base. Si la carte est perdue, le talent se réinitialise.

        class Oléomage:   
            def Oléomage(self):  
                self.nom = "Oléomage"
                self.numero = "26"
                self.rarete = "Epique"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 200
                self.vitesse.de_base = 0.5
                self.defense.de_base = 5
                self.vie.de_base = 2000
                self.puissance.de_base = 4
                self.cout = 3
                self.talent = "Emport"

        class Tour_Energie:   
            def Tour_Energie(self):  
                self.nom = "Tour d'Energie"
                self.numero = "27"
                self.rarete = "Mythique"
                self.type_carte = "Mystère"
                self.attaque.de_base = 350
                self.vitesse.de_base = 0.5
                self.defense.de_base = 6
                self.vie.de_base = 3000
                self.puissance.de_base = 3
                self.cout = 6
                self.talent = "Signal" # Lors de son premier tour, marque la carte adverse posée avec un "signal" : peu importe ce que les deux cartes deviennent, ce lien est gardé de façon à ce que si la carte porteuse du signal est opposée à une carte du deck du possesseur originel de la carte disposant du talent Signal, peu importe la statistique qu'on lui oppose, elle perdra obligatoirement. De ce fait, si la carte possédant le talent Signal est perdue, son talent reste lié à son possesseur d'origine, et n'est donc d'aucune utilité pour l'adversaire

        class Orage:   
            def Orage(self):  
                self.nom = "Orage"
                self.numero = "28"
                self.rarete = "Epique"
                self.type_carte = "Foudre"
                self.attaque.de_base = 200
                self.vitesse.de_base = 1
                self.defense.de_base = 0
                self.vie.de_base = 0
                self.puissance.de_base = 5
                self.cout = 2
                self.talent = "Division"

        class Garde_Glace:   
            def Garde_Glace(self):  
                self.nom = "Garde-Glace"
                self.numero = "29"
                self.rarete = "Mythique"
                self.type_carte = "Royauté"
                self.attaque.de_base = 250
                self.vitesse.de_base = 0.75
                self.defense.de_base = 6
                self.vie.de_base = 3000
                self.puissance.de_base = 3
                self.cout = 4
                self.talent = "Cryogénisation" #  Réduit la vitesse de la carte adverse posée de 25% pendant 3 tours si cette dernière est conservée par l'adversaire. En cas de répétition du talent via la même carte ou une autre ayant le même talent face à une carte différente de la carte déjà touchée, le talent s'applique pareillement à la carte, et n'est pas affecté par le nombre de cartes touchées adverses, le nombre de tours restants, ou le nombre de cartes impactées par la même carte possesseuse du talent. Le talent se désactive si la carte est perdue, mais reste réactivable par l'adversaire s'il rejoue la carte, lui attribuant alors l'effet. Si elle est regagnée, elle réapplique la même logique entre chaque joueur. 

        class Vent_Glacial:   
            def Vent_Glacial(self):  
                self.nom = "Vent Glacial"
                self.numero = "30"
                self.rarete = "Mythique"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 100
                self.vitesse.de_base = 1
                self.defense.de_base = 0
                self.vie.de_base = self.seconde.Vent_Glacial
                self.seconde.Vent_Glacial = 5
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Cryogénisation"

        class Pyromancien:   
            def Pyromancien(self):  
                self.nom = "Pyromancien"
                self.numero = "31"
                self.rarete = "Légendaire"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 200
                self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Fibulatio"

        class Cryomancien:   
            def Cryomancien(self):  
                self.nom = "Cryomancien"
                self.numero = "32"
                self.rarete = "Légendaire"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 150
                self.vitesse.de_base = 0.75
                self.defense.de_base = 5
                self.vie.de_base = 1500
                self.puissance_de_base = 5
                self.cout = 3
                self.talent = "Cryogénisation"

        class Electromancien:   
            def Electromancien(self):  
                self.nom = "Electromancien"
                self.numero = "33"
                self.rarete = "Légendaire"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 75
                self.vitesse.de_base = 2
                self.defense.de_base = 5
                self.vie.de_base = 1500
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Rester"

        class Statue:   
            def Statue(self):  
                self.nom = "Statue"
                self.numero = "34"
                self.rarete = "Rare"
                self.type_carte = "Mystère"
                self.attaque.de_base = 200
                self.vitesse.de_base = 1
                self.defense.de_base = 6
                self.vie.de_base = 3000
                self.puissance.de_base = 6
                self.cout = 5
                self.talent = "Rester"

        class Guérisseur:   
            def Guérisseur(self):  
                self.nom = "Guérisseur"
                self.numero = "35"
                self.rarete = "Commune"
                self.type_carte = "Sorts et soins"
                self.attaque.de_base = 50
                self.vitesse.de_base = 1
                self.defense.de_base = 5
                self.vie.de_base = 3000
                self.puissance.de_base = 5
                self.cout = 3
                self.talent = "Volatile" # Augmente la vie d'une carte aléatoire de son deck de 200% des dégâts qu'il inflige lors des tours où la carte possesseuse du talent est jouée, cumulable à l'infini. Si la carte est perdue, elle est réutilisable par l'adversaire s'il rejoue la carte, lui attribuant alors l'effet, mais les bonus de vie déjà acquis ne peuvent être perdus par simple changement de camp. Si elle est regagnée, elle réapplique la même logique entre chaque joueur.

        class Tour_des_Archers:   
            def Tour_des_Archers(self):  
                self.nom = "Tour des Archers"
                self.numero = "36"
                self.rarete = "Commune"
                self.type_carte = "Royauté"
                self.attaque.de_base = 75
                self.vitesse.de_base = 2
                self.defense.de_base = 6
                self.vie.de_base = 3000
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Bouclier Brut"

        class Tour_Canoniere:   
            def Tour_Canoniere(self):  
                self.nom = "Tour Canonière"
                self.numero = "37"
                self.rarete = "Commune"
                self.type_carte = "Royauté"
                self.attaque.de_base = 100
                self.vitesse.de_base = 2
                self.defense.de_base = 6
                self.vie.de_base = 2500
                self.puissance.de_base = 5
                self.cout = 4
                self.talent = "Epée Brute"

        class Glaciere:   
            def Glaciere(self):  
                self.nom = "Glacière"
                self.numero = "38"
                self.rarete = "Rare"
                self.type_carte = "Eau"
                self.attaque.de_base = 0
                self.attaque.deux = 50
                self.vitesse.de_base = 0
                self.vitesse.deux = nombre_cartes_adverses # Voir talent Relié (La vitesse de la carte en unités est égale au nombre de cartes possedées par l'adversaire durant le tour en cours)
                self.defense.de_base = 5
                self.vie.de_base = self.seconde.Glaciere
                self.seconde.Glaciere = 15
                self.puissance.de_base = 3
                self.cout = 2
                self.talent = "Relié" # La vitesse de la carte en unités est égale au nombre de cartes possedées par l'adversaire durant le tour en cours multipliée par une valeur variable prédéfinie pour chaque carte. Si l'adversaire possède plus de 5 cartes, la limite du facteur s'arrête à 5. A chaque tour où le nombre de cartes adverses varie, même si non jouée, la vitesse de la carte est mise à jour en arrière-plan. Si la carte est perdue, le talent et la vitesse de base de la carte se réinitialisent, mais le talent reste réactivable par l'adversaire s'il rejoue la carte, lui attribuant alors l'effet. Si elle est regagnée, elle réapplique la même logique entre chaque joueur.

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
                self.vitesse.de_base = 0.25 < (nombre_cartes_adverses*0.05 + 0.25) <= 0.5
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
                    self.carte.attaque = carte.attaque*1.25
                    self.carte.vitesse = carte.vitesse + 0.5
                    self.carte.defense = carte.defense + 1
                    self.carte.vie = carte.vie*1.25
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
                self.vitesse.de_base = 0.5 =< (nombre_cartes_adverses*0.5)
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
                self.attaque.de_base = self.attaque_initiale - (self.attaque_initiale*(1 - 0.2*carte.nombre_tours_joues))
                self.vitesse.de_base = 0.25
                self.defense_initiale = 8
                self.defense.de_base = self.defense_initiale - (self.defense_initiale*(1 - 0.25*carte.nombre_tours_joues))
                self.vie.de_base = 3250
                self.puissance.de_base = 8
                self.cout = 6
                self.talent = "Instinct" # Active automatiquement sa capacité lorsque celle-ci est disponible si la carte adverse est plus puissante en termes d'attaque ou de défense lorsque viennent ces statistiques à être en vigueur.
                self.champion = True
                self.capacite = "Recharge Energétique"
                if self.carte.capacite = True:
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

        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :   
            def (self):  
                self.nom = ""
                self.numero = ""
                self.rarete = ""
                self.type_carte = ""
                self.attaque.de_base = 
                self.vitesse.de_base = 
                self.defense.de_base = 
                self.vie.de_base = 
                self.puissance.de_base = 
                self.cout = 
                self.talent = "" 
        class :