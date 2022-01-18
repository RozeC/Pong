# Roze Corentin
# 18/01/2021
# Classe RD Pong
# V0.0.1

from pygame.math import Vector2
import core
import pygame
import random
import math

class C_Raquette_D:

    def __init__(self):

        self.couleur_R = (255, 255, 255)
        self.Longueur_R = 10
        self.Largeur_R = 70
        self.pos_x = 980
        self.pos_y = 300

    def draw(self):
        pygame.draw.rect(core.screen, self.couleur_R, (self.pos_x, self.pos_y, self.Longueur_R, self.Largeur_R))

    def move(self):

        print(core.getkeyPressValue())

        #Hors limite Y
        if self.pos_y > core.WINDOW_SIZE[1] - self.Largeur_R:
            self.pos_y = 530

        if self.pos_y < 0:
            self.pos_y = 0

        # Up
        if core.getKeyPressList("p"):
            self.pos_y = self.pos_y - 10

        # Down
        if core.getKeyPressList("m"):
            self.pos_y = self.pos_y + 10
