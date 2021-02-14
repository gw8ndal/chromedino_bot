from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *

# coordonnées du bouton recommencer et du dino
replay_button = (960, 525)
dino = (127, 620)

# fonction pour redémarrer la partie qui se lance au début
def restart():
    pyautogui.click(replay_button)
    print('jeu démarré')

# créer une box pour checker un changement de couleur
def image_grab():
    box = (dino[0]+120, dino[1], dino[0]+200, dino[1]+20)
    image = ImageGrab.grab(box)
    imageGris = ImageOps.grayscale(image)
    a = array(imageGris.getcolors())
    print(a.sum())
    return a.sum()

def appuyerEspace():
    pyautogui.keyDown('space')


# attendre 5 secondes pour aller sur la bonne fenetre
time.sleep(5)
restart()


# variable mode jour ou nuit
mode = 'Jour'
while True:
    image_grab()
    # checker si il fait jour ou nuit
    if (image_grab() == 483):
        mode = 'Nuit'

    elif (image_grab() == 705):
        mode = 'Jour'
    print(mode)

    # checker si il y a un cactus
    if mode == 'Jour' and (image_grab() == 1115):
        print('Cactus dans la journée !')
        appuyerEspace()
        sleep(0.1)

    elif mode == 'Nuit' and (image_grab() == 661):
        print('Cactus dans la nuit !')
        appuyerEspace()
        sleep(0.1)
