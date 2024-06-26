"""
File: sprites.py
Author: Crystal Diamond, Oliver Tzeng, 314hello
Email: hsnu.crc46th@gmail.com
Github: https://github.com/hsnucrc46
Description: Sprites(objects) declaration
"""

from random import randint

import pygame
import src.lib


class spaceship:
    """
    The player
    """

    def __init__(self, game):
        self.game = game
        self.pos_x = src.lib.width * 0.45
        self.pos_y = src.lib.height * 0.75
        self.speed_x = 50
        self.direction_x = 0
        self.ispaceship = pygame.image.load("src/spaceship.png")
        self.rect = self.ispaceship.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.health = src.lib.health

    def healthbar(self, screen):
        pygame.draw.rect(
                screen, (255, 0, 0), (50, 50, 200, 50)
                )  # Draw a background bar
        pygame.draw.rect(
                screen, (0, 255, 0), (50, 50, int((self.health / 100) * 200), 50)
                )

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.direction_x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction_x = 1
        else:
            self.direction_x = 0

        self.pos_x += self.direction_x * self.speed_x
        if self.pos_x <= 0:
            self.pos_x = 0
        elif self.pos_x >= src.lib.width - 100:
            self.pos_x = src.lib.width - 100
        self.rect.topleft = (self.pos_x, self.pos_y)

    def draw(self, screen):
        self.game.screen.blit(self.ispaceship, (self.pos_x, self.pos_y))
        self.healthbar(screen)


class comet:
    """
    The enemy
    """

    def __init__(self, game):
        self.game = game
        self.pos_x = randint(0, src.lib.width)
        self.pos_y = -50
        self.speed_y = 0
        self.acceleration_y = 9.8 / src.lib.FPS
        self.icomet = pygame.image.load("src/comet.png")
        self.rect = self.icomet.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)

    def update(self):
        self.speed_y += self.acceleration_y
        self.pos_y += self.speed_y
        self.rect.topleft = (self.pos_x, self.pos_y)

    def draw(self):
        self.game.screen.blit(self.icomet, (self.pos_x, self.pos_y))
