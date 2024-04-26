import pygame
import random

class Jajo(pygame.sprite.Sprite):
    def __init__(self, nowa_pozycja):
        super().__init__()
        self.obraz = pygame.image.load("snek/snek/images/egg.png")
        self.rect = nowa_pozycja