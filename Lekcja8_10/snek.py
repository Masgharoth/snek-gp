import pygame
import copy
from direction import Direction
from segment import Segment

class Snek(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.original_image = pygame.image.load("Lekcja8_10/images/head.png")
        self.image = pygame.transform.rotate(self.original_image, 0)
        self.rect = self.image.get_rect(center=(12*32+16, 9*32+16))
        self.curr_direction = Direction.UP
        self.new_direction = Direction.UP
        self.is_moving = False
        self.prev_position = None
        self.add_segment = False
        self.segments = []

    def change_direction(self, direction):
        can_change = True
        if self.curr_direction == direction:
            can_change = False

        if direction == Direction.UP and self.curr_direction == Direction.DOWN:
            can_change = False
        if direction == Direction.DOWN and self.curr_direction == Direction.UP:
            can_change = False
        if direction == Direction.RIGHT and self.curr_direction == Direction.LEFT:
            can_change = False
        if direction == Direction.LEFT and self.curr_direction == Direction.RIGHT:
            can_change = False

        if can_change or not self.is_moving:
            self.new_direction = direction

    def update(self):
        self.curr_direction = self.new_direction
        self.image = pygame.transform.rotate(self.original_image, (self.curr_direction.value*-90))

        self.prev_position = copy.deepcopy(self.rect)
        if self.curr_direction == Direction.UP:
            self.rect.move_ip(0, -32)
        if self.curr_direction == Direction.RIGHT:
            self.rect.move_ip(32, 0)
        if self.curr_direction == Direction.DOWN:
            self.rect.move_ip(0, 32)
        if self.curr_direction == Direction.LEFT:
            self.rect.move_ip(-32, 0)

        for i in range(len(self.segments)):
            if i == 0:
                self.segments[i].move(self.prev_position)
            else:
                self.segments[i].move(self.segments[i-1].prev_position)

        if self.add_segment:
            new_segment = Segment()
            new_position = None

            if len(self.segments) > 0:
                new_position = copy.deepcopy(self.segments[-1].position)
            else:
                new_position = copy.deepcopy(self.prev_position)
            new_segment.position = new_position
            self.segments.append(new_segment)
            self.add_segment = False

    def draw_segments(self, screen):
        for segment in self.segments:
            screen.blit(segment.image, segment.position)

    def eat_apple(self):
        self.add_segment = True

    def check_collision(self):

        if self.rect.top < 0 or self.rect.top >= 608:
            return True
        if self.rect.left < 0 or self.rect.left >= 800:
            return True

        return False