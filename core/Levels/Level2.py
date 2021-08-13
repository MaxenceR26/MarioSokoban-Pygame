"""
███████ ███████  ██████  ██████  ███    ██ ██████      ██      ███████ ██    ██ ███████ ██
██      ██      ██      ██    ██ ████   ██ ██   ██     ██      ██      ██    ██ ██      ██
███████ █████   ██      ██    ██ ██ ██  ██ ██   ██     ██      █████   ██    ██ █████   ██
     ██ ██      ██      ██    ██ ██  ██ ██ ██   ██     ██      ██       ██  ██  ██      ██
███████ ███████  ██████  ██████  ██   ████ ██████      ███████ ███████   ████   ███████ ███████
"""

from core.LevelPlayer.PlayerTwo import Player
import pygame

pygame.init()

class SecondLevel:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 400))
        self.running = True
        self.RedCrateOne = False
        self.player = Player(50, 64)
        self.clock = pygame.time.Clock()
        self.RedCrateTwo = False
        self.NextLevels = False

        self.EndPoint = pygame.image.load("core/PNG-GAME/EndPoint_Blue.png")

        self.leftBorder = pygame.image.load("core/PNG-MAP/map2-element/left.png")
        self.leftBorderHitBox = pygame.Rect(0, 80, 45, 3)

        self.upBorder = pygame.image.load("core/PNG-MAP/map2-element/up.png")
        self.upBorderHitBox = pygame.Rect(0, 0, 450, 64)

        self.downBorder = pygame.image.load("core/PNG-MAP/map2-element/down.png")
        self.downBorderHitBox = pygame.Rect(0, 121, 300, 65)

        self.leftDownBorder = pygame.image.load("core/PNG-MAP/map2-element/leftdown.png")
        self.leftDownBorderHitBox = pygame.Rect(297, 20, 10, 310)

        self.rightBorder = pygame.image.load("core/PNG-MAP/map2-element/right.png")
        self.rightBorderHitBox = pygame.Rect(386, 15, 40, 460)

        self.rightDownBorder = pygame.image.load("core/PNG-MAP/map2-element/rightdown.png")
        self.rightDownBorderHitBox = pygame.Rect(352, 257, 63, 65)

        self.DownDownBorder = pygame.image.load("core/PNG-MAP/map2-element/downdown.png")
        self.DownDownBorderHitBox = pygame.Rect(0, 345, 450, 65)

        self.colors = {
            'WHITE': (255, 255, 255),
            'BLACK': (0, 0, 0)
        }

        self.comic_font = pygame.font.SysFont("comicsansms", 45, False)

        self.textWin = self.comic_font.render("Bravo !", False, self.colors['WHITE'])

        self.cratex = 304
        self.cratey = 100

        self.cratexX = 340
        self.crateyY = 100

        self.CrateHitBox = {
            'crateone': pygame.Rect(320, self.cratey - 20, 1, 1),
            'cratetwo': pygame.Rect(360, self.crateyY, 1, -3),
            'collisionBoxTwo': pygame.Rect(340, 280, 50, 5)
        }

        self.CrateBox = {
            'Crate_brown': pygame.image.load("core/PNG-GAME/Crate_Brown.png").convert(),
            'Crate_red': pygame.image.load("core/PNG-GAME/Crate_Red.png").convert()
        }

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
        elif keys[pygame.K_LEFT]:
            self.player.velocity[0] = -1
        else:
            self.player.velocity[0] = 0
        if keys[pygame.K_UP]:
            self.player.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.player.velocity[1] = 1
        else:
            self.player.velocity[1] = 0

        if keys[pygame.K_e]:
            self.player.speed = 5

    def update(self):
        if self.leftBorderHitBox.colliderect(self.player.rect):
            # Regarder les directions des joueurs ( Pour les box gauches )
            if self.player.velocity[0] == -1:
                self.player.velocity[0] = 0
            elif self.player.velocity[1] == -1:
                self.player.velocity[0] = 0
            elif self.player.velocity[1] == 1:
                self.player.velocity[0] = 0
            else:
                self.player.move()
        elif self.upBorderHitBox.colliderect(self.player.rect):
            # Regarder la direction du joueur pour la box du haut
            if self.player.velocity[1] == -1:
                self.player.velocity[0] = 0
            elif self.rightBorderHitBox.colliderect(self.player.rect):
                if self.player.velocity[0] == 1:
                    self.player.velocity[0] = 0
                else:
                    self.player.move()
            else:
                self.player.move()
        elif self.downBorderHitBox.colliderect(self.player.rect):
            # Regarder la direction du joueur pour la box du bas
            if self.player.velocity[1] == 1:
                self.player.velocity[0] = 0

            else:
                self.player.move()
        elif self.leftDownBorderHitBox.colliderect(self.player.rect):
            if self.player.velocity[0] == -1:
                self.player.velocity[0] = 0
            elif self.player.velocity[1] == -1:
                self.player.move()
            elif self.DownDownBorderHitBox.colliderect(self.player.rect):
                if self.player.velocity[1] == 1:
                    self.player.velocity[0] = 0
                    self.RedCrateOne = True
            elif self.CrateHitBox['crateone'].colliderect(self.player.rect):
                if self.player.velocity[1] == 1:
                    self.player.move()
                    self.cratey += 1
                    self.CrateHitBox['crateone'] = pygame.Rect(320, self.cratey + 23, 1, 1)
            elif self.CrateHitBox['cratetwo'].colliderect(self.player.rect):
                if self.player.velocity[1] == 1:
                    self.player.move()
                    self.crateyY += 1
                    self.CrateHitBox['cratetwo'] = pygame.Rect(320+40, self.crateyY - 30, 1, -3)
                elif self.player.velocity[0] == -1:
                    self.player.move()
                elif self.player.velocity[1] == -1:
                    self.player.velocity[0] = 0
                else:
                    self.player.move()
            else:
                self.player.move()
        elif self.rightBorderHitBox.colliderect(self.player.rect):
            if self.player.velocity[0] == 1:
                self.player.velocity[0] = 0
            elif self.rightDownBorderHitBox.colliderect(self.player.rect):
                if self.player.velocity[1] == 1:
                    self.player.velocity[0] = 0
            elif self.CrateHitBox['cratetwo'].colliderect(self.player.rect):
                if self.player.velocity[1] == 1:
                    self.player.move()
                    self.crateyY += 1
                    self.CrateHitBox['cratetwo'] = pygame.Rect(320 + 40, self.crateyY + 25, -14, -3)
                else:
                    self.player.move()
            elif self.CrateHitBox['cratetwo'].colliderect(self.rightDownBorderHitBox):
                if self.player.velocity[1] == 1:
                    self.player.velocity[0] = 0
                else:
                    self.player.velocity[0] = 0
            else:
                self.player.move()
        elif self.rightDownBorderHitBox.colliderect(self.player.rect):
            if self.player.velocity[0] == 1:
                self.player.velocity[0] = 0
            elif self.player.velocity[1] == 1:
                self.player.velocity[0] = 0
                self.RedCrateTwo = True
            elif self.player.velocity[1] == -1:
                self.player.move()
            else:
                self.player.move()
        elif self.DownDownBorderHitBox.colliderect(self.player.rect):
            if self.player.velocity[1] == 1:
                self.player.velocity[0] = 0
            else:
                self.player.move()

        elif self.CrateHitBox['crateone'].colliderect(self.player.rect):
            if self.player.velocity[1] == 1:
                self.player.move()
                self.cratey += 1
                self.CrateHitBox['crateone'] = pygame.Rect(320+11, self.cratey - 23, 4, 1)
            elif self.player.velocity[0] == -1:
                self.player.move()
            elif self.player.velocity[0] == 1:
                self.player.move()
            else:
                self.player.move()

        elif self.CrateHitBox['cratetwo'].colliderect(self.player.rect):
            if self.player.velocity[1] == 1:
                self.player.move()
                self.crateyY += 1
                self.CrateHitBox['cratetwo'] = pygame.Rect(320+40, self.crateyY + 25, -14, -3)
            elif self.player.velocity[0] == -1:
                self.player.move()
            elif self.player.velocity[0] == 1:
                self.player.move()
            else:
                self.player.move()
        else:
            self.player.move()

    def display(self):
        #   Affichage élément de la map
        self.screen.blit(self.leftBorder, (0, 0))
        self.screen.blit(self.upBorder, (0, 0))
        self.screen.blit(self.downBorder, (0, 0))
        self.screen.blit(self.leftDownBorder, (0, 0))
        self.screen.blit(self.rightBorder, (0, 0))
        self.screen.blit(self.rightDownBorder, (0, 0))
        self.screen.blit(self.DownDownBorder, (0, 0))
        #   Affichage de la map
        map2 = pygame.image.load("core/PNG-MAP/map2.png")
        self.screen.blit(map2, (0, 0))
        # Autre, box, point..
        self.player.draw(self.screen)
        self.screen.blit(pygame.transform.scale(self.EndPoint, (28, 28)), (307, 325))
        self.screen.blit(pygame.transform.scale(self.EndPoint, (28, 28)), (345, 238))
        self.screen.blit(pygame.transform.scale(self.CrateBox['Crate_brown'], (33, 33)),
                         (304, self.cratey))  # 322 pour qu'il soit nickel sur le point
        self.screen.blit(pygame.transform.scale(self.CrateBox['Crate_brown'], (33, 33)),
                         (340, self.crateyY))  # 235 pour qu'il soit nickel sur le point

        if self.RedCrateOne == True:
            if self.RedCrateTwo == True:
                self.screen.blit(pygame.transform.scale(self.CrateBox['Crate_red'], (33, 33)),
                                 (304, self.cratey))  # 322 pour qu'il soit nickel sur le point
                self.screen.blit(pygame.transform.scale(self.CrateBox['Crate_red'], (33, 33)),
                                (340, self.crateyY))  # 235 pour qu'il soit nickel sur le point
                # Bientot...
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_event()
            self.update()
            self.display()
            self.clock.tick(60)

pygame.quit()


"""
Parti du code bientôt modifier car beaucoup de bug niveau collision.

-- Katsu'hi
"""