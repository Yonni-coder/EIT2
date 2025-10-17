from random import shuffle

class Blackjack:
    def __init__(self):
        self.couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        self.valeurs = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'Valet': 10, 'Dame': 10, 'Roi': 10, 'As': 11
        }
        self.paquet = self.creer_paquet()
        self.main_joueur = []
        self.main_croupier = []
        self.score_joueur = 0
        self.score_croupier = 0

    def creer_paquet(self):
        """Crée et mélange un paquet de cartes"""
        paquet = []
        for couleur in self.couleurs:
            for valeur in self.valeurs.keys():
                paquet.append(f"{valeur} de {couleur}")
        shuffle(paquet)
        return paquet

    def calculer_score(self, main):
        """Calcule le score d'une main en gérant intelligemment les As"""
        score = 0
        as_count = 0
        
        for carte in main:
            valeur = carte.split(' de ')[0]
            score += self.valeurs[valeur]
            if valeur == 'As':
                as_count += 1
        
        # Ajuste la valeur des As si nécessaire
        while score > 21 and as_count > 0:
            score -= 10  # Change un As de 11 à 1
            as_count -= 1
            
        return score

    def tirer_carte(self):
        """Tire une carte du paquet"""
        if len(self.paquet) == 0:
            self.paquet = self.creer_paquet()
        return self.paquet.pop()

    def afficher_main(self, main, cachee=False):
        """Affiche une main de cartes"""
        if cachee and len(main) > 1:
            print(f"[{main[0]}, **Carte cachée**]")
        else:
            print("[", end="")
            print(", ".join(main), end="")
            print("]")

    def afficher_etat(self, tour_joueur=True):
        """Affiche l'état actuel du jeu"""
        print("\n" + "="*50)
        print(f"Votre main : ", end="")
        self.afficher_main(self.main_joueur)
        print(f"Votre score : {self.score_joueur}")
        
        print(f"\nMain du croupier : ", end="")
        if tour_joueur:
            self.afficher_main(self.main_croupier, cachee=True)
        else:
            self.afficher_main(self.main_croupier)
            print(f"Score du croupier : {self.score_croupier}")
        print("="*50)

    def distribuer_cartes_initiales(self):
        """Distribue les cartes initiales"""
        self.main_joueur = [self.tirer_carte(), self.tirer_carte()]
        self.main_croupier = [self.tirer_carte(), self.tirer_carte()]
        
        self.score_joueur = self.calculer_score(self.main_joueur)
        self.score_croupier = self.calculer_score(self.main_croupier)

    def tour_joueur(self):
        """Gère le tour du joueur"""
        while self.score_joueur < 21:
            self.afficher_etat(tour_joueur=True)
            
            choix = input("\n1- Tirer une carte (Hit)\n2- Rester (Stand)\n3- Règles\nVotre choix : ")
            
            if choix == '1':
                nouvelle_carte = self.tirer_carte()
                self.main_joueur.append(nouvelle_carte)
                self.score_joueur = self.calculer_score(self.main_joueur)
                print(f"\nVous avez tiré : {nouvelle_carte}")
                
            elif choix == '2':
                break
            elif choix == '3':
                self.afficher_regles()
            else:
                print("Choix invalide ! Veuillez choisir 1, 2 ou 3.")
        
        return self.score_joueur

    def tour_croupier(self):
        """Gère le tour du croupier"""
        print("\n*** Tour du croupier ***")
        self.afficher_etat(tour_joueur=False)
        
        # Le croupier révèle sa carte cachée
        print(f"\nLe croupier révèle sa carte cachée : {self.main_croupier[1]}")
        
        # Le croupier tire jusqu'à avoir au moins 17
        while self.score_croupier < 17:
            nouvelle_carte = self.tirer_carte()
            self.main_croupier.append(nouvelle_carte)
            self.score_croupier = self.calculer_score(self.main_croupier)
            print(f"Le croupier tire : {nouvelle_carte}")
            print(f"Nouveau score du croupier : {self.score_croupier}")
        
        return self.score_croupier

    def determiner_gagnant(self):
        """Détermine le gagnant de la partie"""
        print("\n" + "="*50)
        print("*** RÉSULTAT FINAL ***")
        self.afficher_etat(tour_joueur=False)
        
        if self.score_joueur > 21:
            print("\n💥 Vous avez dépassé 21 ! Vous perdez.")
            return "croupier"
        elif self.score_croupier > 21:
            print("\n🎉 Le croupier a dépassé 21 ! Vous gagnez !")
            return "joueur"
        elif self.score_joueur > self.score_croupier:
            print("\n🎉 Vous avez un meilleur score ! Vous gagnez !")
            return "joueur"
        elif self.score_croupier > self.score_joueur:
            print("\n💥 Le croupier a un meilleur score ! Vous perdez.")
            return "croupier"
        else:
            print("\n🤝 Égalité ! Match nul.")
            return "nul"

    def verifier_blackjack(self):
        """Vérifie si quelqu'un a un Blackjack initial"""
        blackjack_joueur = (self.score_joueur == 21 and len(self.main_joueur) == 2)
        blackjack_croupier = (self.score_croupier == 21 and len(self.main_croupier) == 2)
        
        if blackjack_joueur and blackjack_croupier:
            print("\n🤝 Double Blackjack ! Match nul.")
            return True
        elif blackjack_joueur:
            print("\n🎉 Blackjack ! Vous gagnez !")
            return True
        elif blackjack_croupier:
            print("\n💥 Le croupier a un Blackjack ! Vous perdez.")
            return True
        return False

    def afficher_regles(self):
        """Affiche les règles du jeu"""
        print('''
📋 RÈGLES DU BLACKJACK :
• Chaque joueur reçoit 2 cartes, le croupier a une carte cachée
• Les cartes numérotées valent leur valeur, les figures valent 10
• L'As vaut 1 ou 11 automatiquement (le meilleur score est choisi)
• But : avoir un score ≤ 21 et supérieur à celui du croupier
• Blackjack : As + carte à 10 points (victoire automatique)
• Si vous dépassez 21, vous perdez automatiquement
• Le croupier doit tirer jusqu'à avoir au moins 17
        ''')

    def jouer_partie(self):
        """Joue une partie complète de Blackjack"""
        print("\n" + "🎰" * 15)
        print("     BLACKJACK")
        print("🎰" * 15)
        
        # Réinitialiser le jeu
        self.paquet = self.creer_paquet()
        self.distribuer_cartes_initiales()
        
        # Vérifier les Blackjack initiaux
        if self.verifier_blackjack():
            return
        
        # Tour du joueur
        score_final_joueur = self.tour_joueur()
        
        if score_final_joueur <= 21:
            # Tour du croupier
            self.tour_croupier()
        
        # Résultat final
        self.determiner_gagnant()

def main():
    """Fonction principale du jeu"""
    print("Bienvenue au Blackjack !")
    
    while True:
        jeu = Blackjack()
        jeu.jouer_partie()
        
        rejouer = input("\nVoulez-vous jouer une autre partie ? (o/n) : ").lower()
        if rejouer not in ['o', 'oui', 'y', 'yes']:
            print("\nMerci d'avoir joué ! À bientôt !")
            break

if __name__ == "__main__":
    main()