import random
import time

nombres = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As')

couleurs = ('Carreau', 'Coeur', 'Pique', 'Trêfle')

jeu = []

joueur1 = []

joueur2 = []


# fonction pour assigner une couleur à chaque carte
def creer_jeu():
    
    for n in nombres:
        for c in couleurs:
            carte = (n, c)
            jeu.append(carte)

    return(jeu)

# fonction pour mélanger le jeu
def melanger_jeu():
    random.shuffle(jeu)
    return(jeu)

# fonction pour distribuer les cartes
def distribuer_jeu():
    for carte in jeu:
        if len(joueur1) < (len(jeu)//2):
            joueur1.append(carte)
        else:
            joueur2.append(carte)
    return(joueur1, joueur2)


creer_jeu()
distribuer_jeu()
print('Joueur 1 : ', joueur1)
print('Joueur 2 : ', joueur2)


