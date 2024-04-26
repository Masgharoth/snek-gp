import pygame
import copy

class Segment(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("Lekcja8_10/images/segment.png")
        self.position = pygame.Rect(-32, -32, 32, 32)
        self.prev_position = None

    def move(self, new_position):
        self.prev_position = copy.deepcopy(self.position)
        self.position = copy.deepcopy(new_position)