# Roze Corentin
# 18/01/2021
# main Pong
# V0.0.1

from pygame.math import Vector2
import core
import pygame
import random
from C_Raquette_D import C_Raquette_D
from C_Raquette_G import C_Raquette_G
from C_Balle import C_Balle
from C_Fond import C_Fond


def setup():
    print("Setup START---------")

    pygame.display.set_caption("Pong")

    core.memory("L", 1000)
    core.memory("H", 600)

    core.fps = 30
    core.WINDOW_SIZE = [core.memory("L"), core.memory("H")]

    core.memory("Fond", C_Fond())
    core.memory("Joueur_D", C_Raquette_D())
    core.memory("Joueur_G", C_Raquette_G())
    core.memory("Balle", C_Balle())

    print("Setup END-----------")


def run():
    core.cleanScreen()
    pygame.display.set_caption("Pong")

    core.memory("Fond").draw()

    core.memory("Joueur_D").draw()
    core.memory("Joueur_D").move()

    core.memory("Joueur_G").draw()
    core.memory("Joueur_G").move()

    core.memory("Balle").draw()
    core.memory("Balle").move()

    if (core.memory("Balle").centredecercle.x + 10) >= core.memory("Joueur_D").pos_x and (core.memory("Balle").centredecercle.y + 10) >= core.memory("Joueur_D").pos_y and (core.memory("Balle").centredecercle.y + 10) <= core.memory("Joueur_D").pos_y + 70:
        core.memory("Balle").degager()

    if (core.memory("Balle").centredecercle.x) <= (core.memory("Joueur_G").pos_x + 10) and (core.memory("Balle").centredecercle.y + 10) >= core.memory("Joueur_G").pos_y and (core.memory("Balle").centredecercle.y + 10) <= core.memory("Joueur_G").pos_y + 70:
        core.memory("Balle").degager()


core.main(setup, run)
