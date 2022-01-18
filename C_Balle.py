# Roze Corentin
# 18/01/2021
# Classe Balle Pong
# V0.0.1

from pygame.math import Vector2
import core
import pygame
import random
import math
from C_Raquette_D import C_Raquette_D
from C_Raquette_G import C_Raquette_G

class C_Balle:

    def __init__(self):

        self.centredecercle = pygame.Vector2(500, 300)
        self.centredecercle = pygame.Vector2(self.centredecercle.x, self.centredecercle.y)
        self.rayonducercle = 10
        self.couleurducercle = (255, 255, 255)
        self.gravity_x = 10
        self.gravity_y = 10

        self.couleur_T_D = (0, 0, 255)
        self.score_D = '0'
        self.pos_score_D = pygame.Vector2(750, 10)

        self.couleur_T_G = (255, 0, 0)
        self.score_G = '0'
        self.pos_score_G = pygame.Vector2(250, 10)

        self.cpt_G = 0
        self.cpt_D = 0

    def draw (self):
        pygame.draw.circle(core.screen, self.couleurducercle, self.centredecercle,  self.rayonducercle)
        core.Draw.text(self.couleur_T_D, self.score_D, self.pos_score_D, 30)
        core.Draw.text(self.couleur_T_G, self.score_G, self.pos_score_G, 30)

    def move(self):

        # Hors limite X
        if self.centredecercle.x > core.WINDOW_SIZE[0] - self.rayonducercle:
            self.gravity_x = -10
            self.score_G = 'Point'
            self.cpt_G = self.cpt_G + 1
            print("Le score est de ", self.cpt_G, "contre ", self.cpt_D)

        if self.centredecercle.x < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayonducercle:
            self.gravity_x = 10
            self.score_D = 'Point'
            self.cpt_D = self.cpt_D + 1
            print("Le score est de ", self.cpt_G, "contre ", self.cpt_D)



        # Hors limite Y
        if self.centredecercle.y > core.WINDOW_SIZE[1] - self.rayonducercle:
            self.gravity_y = -10

        if self.centredecercle.y < core.WINDOW_SIZE[0] - core.WINDOW_SIZE[0] + self.rayonducercle:
            self.gravity_y = 10
            #self.couleurducercle = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Reset
        if core.getKeyPressList("r"):
            self.centredecercle = pygame.Vector2(200, 200)
            self.gravity_x = 0
            self.gravity_y = 0

        self.centredecercle = pygame.Vector2(self.centredecercle.x + self.gravity_x , self.centredecercle.y + self.gravity_y)

    def degager(self):
            self.gravity_x = -self.gravity_x


