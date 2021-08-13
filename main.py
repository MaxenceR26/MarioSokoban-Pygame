
# Imports
import pygame
from random import randint
from core.Game import Game

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.Launch = False
        self.arrow = pygame.image.load("PNG/Arrow.png")
        self.EndPoint = pygame.image.load("PNG/EndPoint_Blue.png")
        self.imageCrate = {
            'CRATE_1': pygame.image.load("PNG/Crate_Brown.png").convert(),
        }

        self.character = {
            'MARIO_LEFT': pygame.image.load("PNG/Character1.png").convert(),
            'MARIO_RIGHT': pygame.image.load("PNG/Character2.png").convert(),
            'MARIO_inFRONT': pygame.image.load("PNG/Character4.png").convert(),
            'MARIO_BACK': pygame.image.load("PNG/Character7.png").convert(),
            'MARIO_inFRONT_walk1': pygame.image.load("PNG/Character6.png").convert(),
            'MARIO_inFRONT_walk2': pygame.image.load("PNG/Character4.png").convert(),
            'MARIO_BACK_walk1': pygame.image.load("PNG/Character9.png").convert(),
            'MARIO_BACK_walk2': pygame.image.load("PNG/Character8.png").convert()
        }

        self.colors = {
            'WHITE': (255,255,255)
        }

        self.comic_font = pygame.font.SysFont("comicsansms", 30, False) # Troisieme arg : Police gras = True ou False, Quatrième Arg : Police italique = True ou False

        self.texts = {
            'Title': self.comic_font.render("Mario Sokoban", False, self.colors['WHITE']),
            'Rungame': self.comic_font.render("1: Jouer", False, self.colors['WHITE']),
            'Author': self.comic_font.render("2: Author", False, self.colors['WHITE'])
        }

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.screen.blit(pygame.transform.scale(self.character['MARIO_RIGHT'], (28, 39)), (184, 87))
            pygame.display.flip()
        if keys[pygame.K_LEFT]:
            self.screen.blit(pygame.transform.scale(self.character['MARIO_LEFT'], (28, 39)), (184, 87))
            pygame.display.flip()
        if keys[pygame.K_UP]:
            number = randint(1,2)
            if number == 1:
                self.screen.blit(pygame.transform.scale(self.character['MARIO_inFRONT_walk1'], (28, 39)), (184, 87))
                pygame.display.flip()
            if number == 2:
                self.screen.blit(pygame.transform.scale(self.character['MARIO_inFRONT_walk2'], (28, 39)), (184, 87))
                pygame.display.flip()
        if keys[pygame.K_DOWN]:
            number = randint(1, 2)
            if number == 1:
                self.screen.blit(pygame.transform.scale(self.character['MARIO_BACK_walk1'], (28, 39)), (184, 87))
                pygame.display.flip()
            if number == 2:
                self.screen.blit(pygame.transform.scale(self.character['MARIO_BACK_walk2'], (28, 39)), (184, 87))
                pygame.display.flip()
        if keys[pygame.K_KP1]:
                pygame.mixer.music.stop()
                Game().runGame()


    def display(self):

        # Title

        self.screen.blit(pygame.transform.scale(self.imageCrate['CRATE_1'], (36, 36)), (45, 48))
        self.screen.blit(pygame.transform.scale(self.imageCrate['CRATE_1'], (36, 36)), (315, 48))
        self.screen.blit(self.texts['Title'], (96, 42))

        # Character (IN FRONT) below the title

        self.screen.blit(pygame.transform.scale(self.character['MARIO_inFRONT'], (28, 39)), (184, 87))

        # Text of choice

        self.screen.blit(self.texts['Rungame'], (125, 170))
        self.screen.blit(self.texts['Author'], (125, 200))

        # Exemple

        self.screen.blit(pygame.transform.scale(self.arrow,(230, 50)), (100,300))
        self.screen.blit(pygame.transform.scale(self.imageCrate['CRATE_1'], (36,36)), (75, 305))
        self.screen.blit(self.EndPoint, (315, 305))
        self.screen.blit(pygame.transform.scale(self.character['MARIO_RIGHT'], (25, 36)), (35, 305))

        pygame.display.flip()

    def run(self):
        self.display()
        while self.running:
            self.handle_event()


pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mario Sokoban")
Icon = pygame.image.load("PNG/Crate_Brown.png")
pygame.display.set_icon(Icon)
menu = Menu(screen)
menu.run()
pygame.quit()