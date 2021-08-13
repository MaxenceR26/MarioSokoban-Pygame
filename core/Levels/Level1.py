"""
 ██████  ███    ██ ███████     ██      ███████ ██    ██ ███████ ██
██    ██ ████   ██ ██          ██      ██      ██    ██ ██      ██
██    ██ ██ ██  ██ █████       ██      █████   ██    ██ █████   ██
██    ██ ██  ██ ██ ██          ██      ██       ██  ██  ██      ██
 ██████  ██   ████ ███████     ███████ ███████   ████   ███████ ███████
"""

import pygame

from core.Levels.Level2 import SecondLevel

pygame.init()
from core.LevelPlayer.PlayerOne import Player

class FirstLevel:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 400))
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(75, 175)
        self.finish = False

        self.crate_x = 120
        self.crate_y = 174

        self.colors = {
            'WHITE': (255, 255, 255),
            'BLACK': (0, 0, 0)
        }

        self.comic_font = pygame.font.SysFont("comicsansms", 45, False)

        self.textWin = self.comic_font.render("Bravo !", False, self.colors['WHITE'])

        self.hitBox = {
            'CrateHitbox': pygame.Rect(self.crate_x, self.crate_y, 20, 40),
            'Border-LEFT': pygame.Rect(40, 174, 32, 40),
            'Border-RIGHT': pygame.Rect(350, 174, 32, 40)
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

        self.CrateBox = {
            'Crate_brown': pygame.image.load("core/PNG-GAME/Crate_Brown.png").convert(),
            'Crate_red': pygame.image.load("core/PNG-GAME/Crate_Red.png").convert()
        }

        self.EndPoint = pygame.image.load("core/PNG-GAME/EndPoint_Blue.png").convert()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0

    def update(self):
        if self.hitBox['CrateHitbox'].colliderect(self.player.rect):
            if self.hitBox['CrateHitbox'].colliderect(self.hitBox['Border-RIGHT']):
                NextLevel = pygame.key.get_pressed()
                if NextLevel[pygame.K_KP_ENTER]:
                    SecondLevel().run()  # Lancer le level 2
                self.crate_x += 0
                self.hitBox['CrateHitbox'] = pygame.Rect(self.crate_x, self.crate_y, 40, 40)
                self.finish = True
                if self.player.velocity[0] == 1:
                    self.player.velocity[0] = 0
                else:
                    self.player.move()
            else:
                self.crate_x += 1
                self.hitBox['CrateHitbox'] = pygame.Rect(self.crate_x, self.crate_y, 40, 40)
        ReloadLevel = pygame.key.get_pressed()
        if ReloadLevel[pygame.K_r]:
            return FirstLevel().run()
        if self.hitBox['Border-LEFT'].colliderect(self.player.rect):
            if self.player.velocity[0] == -1:
                self.player.velocity[0] = 0

                # pygame.mixer.music.load("MUSIC/cpasparla.wav")
                # pygame.mixer.music.stop()
            else:
                self.player.move()
        else:
            self.player.move()

    def display(self):
        map1 = pygame.image.load("core/PNG-MAP/map1.png")
        self.screen.blit(map1, (0, 0))
        # self.screen.blit(pygame.transform.scale(self.characters['MARIO_inFront'], (28,39)), (75,175))
        self.screen.blit(self.EndPoint, (315, 178))
        self.player.draw(self.screen)
        self.screen.blit(pygame.transform.scale(self.CrateBox['Crate_brown'], (40, 40)), (self.crate_x, self.crate_y))
        if self.finish == True:
            self.screen.blit(pygame.transform.scale(self.CrateBox['Crate_red'], (40, 40)), (self.crate_x, self.crate_y))
            pygame.draw.rect(self.screen, self.colors['BLACK'], pygame.Rect(85, 140, 225, 110), 0)
            self.screen.blit(self.textWin, (125, 160))
            for i in range(4):
                pygame.draw.rect(self.screen, self.colors['WHITE'], pygame.Rect(85 - i, 140 - i, 225, 110), 1)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_event()
            self.update()
            self.display()
            self.clock.tick(60)

pygame.quit()