import pygame
from random import randint


class Player:
    def __init__(self, x, y):
        self.imgPlayer = pygame.image.load("core/PNG-GAME/Character4.png").convert()
        self.rect = self.imgPlayer.get_rect(x=x, y=y)
        self.speed = 1
        self.velocity = [0, 0]

        self.character = {
            'MARIO_LEFT': pygame.image.load("core/PNG-GAME/Character1.png").convert(),
            'MARIO_RIGHT': pygame.image.load("core/PNG-GAME/Character2.png").convert(),
            'MARIO_inFRONT': pygame.image.load("core/PNG-GAME/Character4.png").convert(),
            'MARIO_inFRONT_walk2': pygame.image.load("core/PNG-GAME/Character4.png").convert(),
            'MARIO_RIGHT_walk1': pygame.image.load("core/PNG-GAME/Character3.png").convert(),
            'MARIO_LEFT_walk1': pygame.image.load("core/PNG-GAME/Character10.png").convert(),
            'MARIO_UP_walk1': pygame.image.load("core/PNG-GAME/Character8.png").convert(),
            'MARIO_UP_walk2': pygame.image.load("core/PNG-GAME/Character9.png").convert(),
            'MARIO_UP': pygame.image.load("core/PNG-GAME/Character7.png").convert(),
            'MARIO_DOWN_walk1': pygame.image.load("core/PNG-GAME/Character5.png").convert(),
            'MARIO_DOWN_walk2': pygame.image.load("core/PNG-GAME/Character6.png").convert(),
        }

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        number = randint(1,2)
        if self.velocity[0] == -1:
            if number == 1:
                screen.blit(pygame.transform.scale(self.character['MARIO_LEFT'], (24, 35)), self.rect)
            if number == 2:
                screen.blit(pygame.transform.scale(self.character['MARIO_LEFT_walk1'], (24, 35)), self.rect)
            return number
        elif self.velocity[0] == 1:
            if number == 1:
                screen.blit(pygame.transform.scale(self.character['MARIO_RIGHT'], (24, 35)), self.rect)
            if number == 2:
                screen.blit(pygame.transform.scale(self.character['MARIO_RIGHT_walk1'], (24, 35)), self.rect)
            return number
        else:
            screen.blit(pygame.transform.scale(self.imgPlayer, (24, 35)), self.rect)

        if self.velocity[1] == -1:
            if number == 1:
                screen.blit(pygame.transform.scale(self.character['MARIO_UP_walk1'], (24, 35)), self.rect)
            if number == 2:
                screen.blit(pygame.transform.scale(self.character['MARIO_UP_walk2'], (24, 35)), self.rect)
            return number
        elif self.velocity[1] == 1:
            if number == 1:
                screen.blit(pygame.transform.scale(self.character['MARIO_DOWN_walk1'], (24, 35)), self.rect)
            if number == 2:
                screen.blit(pygame.transform.scale(self.character['MARIO_DOWN_walk2'], (24, 35)), self.rect)
            return number
        else:
            screen.blit(pygame.transform.scale(self.imgPlayer, (24, 35)), self.rect)