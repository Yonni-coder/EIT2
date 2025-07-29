from random import choice 

# Affiche les règles de Blackjack pour aider le joueur
def aide():
    print('''Chaque joueur reçoit initialement deux cartes face visible, tandis que le croupier reçoit une carte face visible et une carte face cachée.
Les cartes numérotées valent leur valeur nominale, les figures (valet, dame, roi) valent 10, et l'As peut valoir 1 ou 11 selon le cas.
Le but est d'obtenir une main dont la valeur totale se rapproche le plus possible de 21 sans la dépasser.
Si un joueur dépasse 21, il perd automatiquement (bust).
Après avoir reçu ses deux premières cartes, un joueur a le choix entre demander une carte supplémentaire (hit) ou rester avec sa main actuelle (stand).
Si un joueur obtient exactement 21 avec ses deux premières cartes (un as et une carte valant 10), il réalise un "Blackjack" et remporte automatiquement la partie, sauf si le croupier réalise également un Blackjack, auquel cas la partie est nulle.
Une fois que le joueur a joué, le croupier révèle sa carte face cachée et tire des cartes supplémentaires pour essayer de dépasser le total du joueur.
Le gagnant est celui qui se rapproche le plus de 21 sans la dépasser
\n \n Maintenant à vous de jouer !!\n\n''')

# Retire une carte de la liste des cartes disponibles et en retourne une autre au hasard
def efface_carte(a):
    global cartes
    cartes.remove(a)
    b = choice(cartes)
    return b

# Retourne la valeur numérique d'une carte donnée
def valeur_carte(a):
    liste_des_deux = ['Deux de pique', 'Deux de coeur', 'Deux de carreau', 'Deux de trèfle']
    liste_des_trois = ['Trois de pique', 'Trois de coeur', 'Trois de carreau', 'Trois de trèfle']
    liste_des_quatre = ['Quatre de pique', 'Quatre de coeur', 'Quatre de carreau', 'Quatre de trèfle']
    liste_des_cinq = ['Cinq de pique', 'Cinq de coeur', 'Cinq de carreau', 'Cinq de trèfle']
    liste_des_six = ['Six de pique', 'Six de coeur', 'Six de carreau', 'Six de trèfle']
    liste_des_sept = ['Sept de pique', 'Sept de coeur', 'Sept de carreau', 'Sept de trèfle']
    liste_des_huit = ['Huit de pique', 'Huit de coeur', 'Huit de carreau', 'Huit de trèfle']
    liste_des_neuf = ['Neuf de pique', 'Neuf de coeur', 'Neuf de carreau', 'Neuf de trèfle']
    liste_des_dix = ['Dix de pique', 'Dix de coeur', 'Dix de carreau', 'Dix de trèfle']
    liste_des_figures = ['Roi de pique', 'Dame de pique', 'Valet de pique',
                         'Roi de coeur', 'Dame de coeur', 'Valet de coeur',
                         'Roi de carreau', 'Dame de carreau', 'Valet de carreau',
                         'Roi de trèfle', 'Dame de trèfle', 'Valet de trèfle']
   
    b = 0
    if a in liste_des_deux:
        b = 2
    elif a in liste_des_trois:
        b = 3
    elif a in liste_des_quatre:
        b = 4
    elif a in liste_des_cinq:
        b = 5
    elif a in liste_des_six:
        b = 6
    elif a in liste_des_sept:
        b = 7
    elif a in liste_des_huit:
        b = 8
    elif a in liste_des_neuf:
        b = 9
    elif a in liste_des_dix:
        b = 10
    elif a in liste_des_figures:
        b = 10   
    return b

# Calcule la valeur d'une carte, avec une gestion spéciale pour les As
def comptage(a):
    global liste_as
    n = 0
    if a in liste_as:
        n = 11  # Un As peut valoir 11
    else:
        n = valeur_carte(a)          
    return n

# Affiche un message de défaite lorsque le total du joueur dépasse 21
def defaite():
    print ('\nVotre total a dépassé 21 (Bust)\n\n••• Vous avez perdu •••')

# Boucle de jeu pour le joueur, permettant de tirer de nouvelles cartes ou de rester
def boucle(a):
    global total
    while True:
        cartes.append(a)
        new_carte = efface_carte(a)
        try:
            option = input('\n1- Reprendre une carte (Hit)\n2- Ne pas reprendre (Stand)\n3- Comment jouer ?\n')
            if option == '2':  # Le joueur choisit de ne pas reprendre de carte
                break
            elif option == '3':  # Afficher l'aide
                aide()
            elif option != '1' and option != '2' and option != '3':  # Gérer les entrées invalides
                print('Veuillez entrer un numéro valide !')
            elif option == '1':  # Le joueur choisit de reprendre une carte
                if new_carte in liste_as and total + 11 > 21:
                    valeur_new_carte = 1  # Si l'As ferait dépasser 21, il vaut 1
                    total += 1
                    print ('\nVous avez tiré : ', new_carte)
                    print ('\nLa nouvelle valeur totale de vos cartes : ', total)
                    if total > 21:
                        defaite()
                        break
                elif new_carte in liste_as and total + 11 <= 21:
                    valeur_new_carte = 11  # Sinon, l'As vaut 11
                    total += 11
                    print ('\nVous avez tiré : ', new_carte)
                    print ('\nLa nouvelle valeur totale de vos cartes : ', total)
                    if total > 21:
                        defaite()
                        break
                else:
                    valeur_new_carte = valeur_carte(new_carte)
                    total += valeur_new_carte
                    print ('\nVous avez tiré : ', new_carte)
                    print ('\nLa nouvelle valeur totale de vos cartes : ', total)
                    if total > 21:
                        defaite()
                        break
        except Exception as e:
            print('Une erreur est survenue :', e)
            continue

# Boucle de jeu pour le croupier, qui tire des cartes jusqu'à atteindre ou dépasser le total du joueur
def boucle_croupier(a):
    global total_croupier
    global total
    global total_maj
    global carte_cachée
    cartes.append(a)
    new_carte_croupier = efface_carte(a)
    
    total_maj = 0
    while total_maj < 17:
        new_carte_croupier = efface_carte(new_carte_croupier)
        print ('\nLe croupier a tiré : ', new_carte_croupier)
        
        if new_carte_croupier in liste_as and total_croupier + 11 > 21:
            val_new_carte = 1  # Si l'As ferait dépasser 21, il vaut 1
            total_maj = total_croupier + 1
            total_croupier = total_maj
        elif new_carte_croupier in liste_as and total_croupier + 11 <= 21:
            val_new_carte = 11  # Sinon, l'As vaut 11
            total_maj = total_croupier + 11
            total_croupier = total_maj
        else:
            val_new_carte_croupier = valeur_carte(new_carte_croupier)
            total_maj = total_croupier + val_new_carte_croupier
            total_croupier = total_maj
            print ('\nNouvelle valeur des cartes du croupier: ', total_maj)
    
    if total_maj > 21:
        print ('\nLe croupier a dépassé 21\n\n••• Félicitations !! vous avez gagné !! •••')
    elif total_maj > total and total_maj <= 21:
        print ('\n•• Dommage, le croupier a gagné •• ')
    elif total > total_maj and total <= 21:
        print ('\n••• Félicitations !! Vous avez gagné !! •••')  
    elif total_maj == total:
        print ('\n•• Match nul !! ••')

# Fonction principale du jeu de Blackjack
def jouer_blackjack():
    print ('     \n ************ BLACKJACK ************\n\n')
    global cartes, liste_as, total, total_croupier, total_maj, carte_cachée

    # Liste de toutes les cartes nécessaires pour jouer à Blackjack 
    cartes = ['As de pique', 'Roi de pique', 'Dame de pique', 'Valet de pique',
              'Deux de pique', 'Trois de pique', 'Quatre de pique', 'Cinq de pique', 'Six de pique', 'Sept de pique', 'Huit de pique', 'Neuf de pique', 'Dix de pique',
              'As de coeur', 'Roi de coeur', 'Dame de coeur', 'Valet de coeur',
              'Deux de coeur', 'Trois de coeur', 'Quatre de coeur', 'Cinq de coeur', 'Six de coeur', 'Sept de coeur', 'Huit de coeur', 'Neuf de coeur', 'Dix de coeur',
              'As de carreau', 'Roi de carreau', 'Dame de carreau', 'Valet de carreau',
              'Deux de carreau', 'Trois de carreau', 'Quatre de carreau', 'Cinq de carreau', 'Six de carreau', 'Sept de carreau', 'Huit de carreau', 'Neuf de carreau', 'Dix de carreau',
              'As de trèfle', 'Roi de trèfle', 'Dame de trèfle', 'Valet de trèfle',
              'Deux de trèfle', 'Trois de trèfle', 'Quatre de trèfle', 'Cinq de trèfle', 'Six de trèfle', 'Sept de trèfle', 'Huit de trèfle', 'Neuf de trèfle', 'Dix de trèfle']

    liste_as = ['As de pique', 'As de coeur', 'As de carreau', 'As de trèfle']
    total = 0
    total_croupier = 0
    total_maj = 0
    carte_cachée = 0
    
    print('Règle : 1- La valeur des figures (valet, dame, roi) est 10 \n\t2- Les autres cartes gardent leur valeur numérique\n\t3- As vaut 1 ou 11\n')
    
    # Distribution des premières cartes pour le joueur et le croupier
    a = choice(cartes)
    cartes.remove(a)
    b = choice(cartes)
    cartes.remove(b)
    c = choice(cartes)
    cartes.remove(c)
    d = choice(cartes)
    cartes.remove(d)
    
    total += comptage(a) + comptage(b)
    carte_cachée += comptage(d)
    total_croupier += comptage(c) 
    
    print('Votre première carte :', a)
    print('Votre deuxième carte :', b)
    print('La carte du croupier :', c)
    print('Le total de vos cartes :', total)
    3
    if total == 21:
        print('••• Félicitations !! Blackjack, vous avez gagné •••')
    else:
        boucle(b)
        if total <= 21:
            print('\nLe croupier révèle sa carte cachée : ', d)
            total_croupier += carte_cachée
            print('\nLe total des cartes du croupier : ', total_croupier)
            if total_croupier == 21:
                print('\nLe croupier a fait un Blackjack !! \n\n•• Vous avez perdu !! •• ')
            else:
                boucle_croupier(d)

# Fonction main pour gérer la boucle principale du jeu
def main():
    while True:
        jouer_blackjack()
        try:
            choix = input('\nVoulez-vous jouer une nouvelle partie ? (1 pour rejouer, autre touche pour quitter): ')
            if choix != '1':  # L'utilisateur choisit de quitter en entrant autre chose que "1"
                print("Merci d'avoir joué ! À la prochaine.")
                break
        except Exception as e:
            print('Une erreur est survenue :', e)
            continue

# Point d'entrée du programme
if __name__ == "__main__":
    main()
    