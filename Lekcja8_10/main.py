import pygame
import random
import time
from apple import Apple
from snek import Snek
from direction import Direction

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGH = 608
FPS = 30

screenBg = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGH))

for i in range(25):
    for j in range(19):
        bckgr = pygame.image.load("Lekcja8_10/images/background.png")
        mask = (random.randrange(0,20),random.randrange(0,20),random.randrange(0,20))
        bckgr.fill(mask, special_flags=pygame.BLEND_ADD)
        screenBg.blit(bckgr, (i*32, j*32))

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGH])
clock = pygame.time.Clock()

snek = Snek()
MOVE_SNEK = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNEK, 200)

apple = Apple()
apples = pygame.sprite.Group()
apples.add(apple)

game_runs = True
game_started = False

while game_runs:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_runs = False
            if event.key == pygame.K_w:
                snek.change_direction(Direction.UP)
                game_started = True
            if event.key == pygame.K_s:
                snek.change_direction(Direction.DOWN)
                game_started = True
            if event.key == pygame.K_a:
                snek.change_direction(Direction.LEFT)
                game_started = True
            if event.key == pygame.K_d:
                snek.change_direction(Direction.RIGHT)
                game_started = True
        elif event.type == pygame.QUIT:
            game_runs = False
        elif event.type == MOVE_SNEK:
            if game_started == True:
                snek.is_moving = True
                snek.update()

    collision_apple = pygame.sprite.spritecollideany(snek, apples)

    if collision_apple != None:
        collision_apple.kill()
        snek.eat_apple()
        apple = Apple()
        apples.add(apple)

    screen.blit(screenBg, (0,0))

    snek.draw_segments(screen)

    for apple in apples:
        screen.blit(apple.image, apple.rect)
    screen.blit(snek.image, snek.rect)

    if snek.check_collision():
        game_runs = False

    pygame.display.flip()

    clock.tick(FPS)

time.sleep(2)
pygame.quit()

'''
+ rysownie tła
+ jabłko
+ main snek
+ kierowanie
- jedzenia jabłka
- dodawanie segmentów
- dodawanie jabłek
- endgame condition
    - kolizja ściana
    - kolizja ogon
- punkty
- tekst końcowy
'''