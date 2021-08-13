"""

GAME

"""

import pygame
from core.LevelPlayer.PlayerOne import Player
from core.Levels.Level2 import SecondLevel #SecondLevel().run()
from core.Levels.Level1 import FirstLevel
# Initializing pygame
pygame.init()


# Class Game

class Game:
    def runGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        FirstLevel().run()

"""

A noter :

Quand je vais ajouter le levels 2 au jeu principale j'aurais juste a rajouter au image : core/

exemple : core/PNG-MAP/map2s.png"

"""
