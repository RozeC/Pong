# Roze Corentin
# 18/01/2021
# Classe Fond Pong
# V0.0.1

from pygame.math import Vector2
import core
import pygame
import random
import math
from C_Raquette_D import C_Raquette_D
from C_Raquette_G import C_Raquette_G

class C_Fond:

    def __init__(self):

        self.couleur_R = (192, 192, 192)
        self.Longueur_R = 10
        self.Largeur_R = 1000
        self.pos_x = 490
        self.pos_y = 0

    def draw (self):
        pygame.draw.rect(core.screen, self.couleur_R, (self.pos_x, self.pos_y, self.Longueur_R, self.Largeur_R))





