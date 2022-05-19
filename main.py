#####################################################################
# Écrit par     : DURAISAMY ARINIDHAN
# contact       : arinidhan.duraisamy@etu.univ-lyon1.fr
# SUJET         : EVAL-FINAL PACMAN
# FICHIER       : main.py
# Version       : 0.1
#####################################################################

import core
import pygame

from PACMAN import PACMAN
from FANTOME import FANTOME
from POINTS import POINTS
from FENETRE import FENETRE

def setup():
    print("setup START---------")
    core.WINDOW_SIZE = [1080, 720]
    core.fps = 60

    core.memory("PACMAN", PACMAN())
    core.memory("FANTOME", FANTOME())
    core.memory("POINTS", POINTS())

    nb_Points = 100
    core.memory("tab_points", [])

    pac = PACMAN()
    core.memory("PACMAN", pac)

    for i in range(100, nb_Points):
        p = POINTS()
        core.memory("tab_points").append(p)

    for i in range(4, nb_FANTOME):
        core.memory("FANTOME").append(FANTOME())

    print("setup END-----------")

def run():
    core.cleanScreen()
    #lancer la partie en apuiyant sur r
    if core.getKeyPressList("r"):
        core.memory("PACMAN", PACMAN())

    for i in core.memory("POINTS"):
        i.draw(core.screen)

    for i in core.memory("FANTOME):
        i.draw(core.screen)
        i.deplacer()

    core.memory("PACMAN").show()
    core.memory("PACMAN").move()

if __name__ == '__main__':
    core.main(setup, run)
