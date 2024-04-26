import pygame
import Element
pygame.init()
pygame.font.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHAR_POS_X = 270
CHAR_POS_Y = 130


my_font = pygame.font.SysFont('Monocraft', 30)
background_image = pygame.image.load('images/background.png')
base_image = pygame.image.load('images/base.png')
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
clock = pygame.time.Clock()
head = Element.HeadWear()
body = Element.BodyWear()
eyes = Element.Eyes()
weapon = Element.Weapon()

def print_text(screen, text, position):
    my_text = my_font.render(text, False, (255,255,255) )
    screen.blit(my_text, position)

game_running = True
saving = False
frame = 0
fps = 30


while game_running:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 320 < pos[0] < 460 and 180 < pos[1] < 210:
                head.chooseNext()
            if 360 < pos[0] < 450 and 210 < pos[1] < 250:
                eyes.chooseNext()
            if 330 < pos[0] < 450 and 270 < pos[1] < 330:
                body.chooseNext()
            if 470 < pos[0] < 500 and 280 < pos[1] < 310:
                weapon.chooseNext()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            if event.key == pygame.K_1:
                head.chooseNext()
            if event.key == pygame.K_2:
                eyes.chooseNext()
            if event.key == pygame.K_3:
                body.chooseNext()
            if event.key == pygame.K_4:
                weapon.chooseNext()
            if event.key == pygame.K_s:
                saving = True
        elif event.type == pygame.QUIT:
            game_running = False

    if frame == fps:
        CHAR_POS_Y -= 5
        frame = 0
    elif frame == fps//3:
        CHAR_POS_Y += 5
    char_pos = (CHAR_POS_X, CHAR_POS_Y)
    frame += 1

    screen.blit(background_image, (0, 0))
    screen.blit(base_image,char_pos)
    screen.blit(head.choosenImage(), char_pos)
    screen.blit(eyes.choosenImage(), char_pos)
    screen.blit(body.choosenImage(), char_pos)
    screen.blit(weapon.choosenImage(), char_pos)

    if saving:
        pygame.image.save(screen, 'postac.png')
        saving = False

    print_text(screen, f"[1] Head: {head.choice+1}", (100, 100) )
    print_text(screen, f"[2] Eyes: {eyes.choice+1}", (100, 140) )
    print_text(screen, f"[3] Body: {body.choice+1}", (100, 180) )
    print_text(screen, f"[4] Weapon: {weapon.choice+1}", (100, 220) )
    print_text(screen, f"[S] Zapisz", (100, 260) )

    pygame.display.flip()
    clock.tick(fps)
    pass

pygame.quit()