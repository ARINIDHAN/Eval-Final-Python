#####################################################################
# Écrit par     : DURAISAMY ARINIDHAN
# contact       : arinidhan.duraisamy@etu.univ-lyon1.fr
# SUJET         : EVAL-FINAL PACMAN
# FICHIER       : PACMAN.py
# Version       : 0.1
#####################################################################

import core
import FENETRE

class PACMAN():
    x = 0
    y = 0
    def __init__(self):
        self.vitesse= Vector2
        self.rayon = 10
        self.x = x
        self.y = y
        self.nom = "PACMAN"
        self.couleur =(255,255,0)#couleur JAUNE

    def show(self):
        core.Draw.circle(self.couleur,[self.x,self.y],self.r)

    def move(self):
        if core.getKeyPress("z"):
            self.y = self.y-1
        if core.getKeyPressList("s"):
            self.y = self.y+1
        if core.getKeyPressList("q"):
            self.x = self.x-1
        if core.getKeyPressList("d"):
            self.x = self.x+1
        self.edge()

    def edge(self):
        if self.x - self.rayon <= 0:
            self.x = self.rayon
        if self.x + self.rayon >= core.WINDOW_SIZE[0]:
            self.x = core.WINDOW_SIZE[0] - self.rayon
        if self.y - self.rayon <= 0:
            self.y = self.rayon
        if self.y + self.rayon >= core.WINDOW_SIZE[1]:
            self.y = core.WINDOW_SIZE[1] - self.rayon
    def mourir(self):
    #Le rayon du fantome sera toujours superieur a pacman, si le fantome touche pacman il meurt. GAME OVER
        if i.core.memory("PACMAN").rayon < i.core.memory("FANTOME").rayon
            core.memory("pacman").mourir()
            print("GAME OVER PACMAN")
