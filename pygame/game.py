import pygame
import os

#CONSTANTS
VEL = 10
PLAYERWIDTH, PLAYERHEIGHT = 77, 194
WINWIDTH, WINHEIGHT, WINTITLE = 800, 600, "My little game!"
WHITE, RED, BLACK = (255,255,255), (255,0,0), (0,0,0)
FPS = 30
WIN = pygame.display.set_mode((WINWIDTH,WINHEIGHT))
pygame.display.set_caption(WINTITLE)
STARIMAGE = pygame.image.load_extended(os.path.join('assets', 'star.png'))
AVATARIMAGE = pygame.image.load_extended(os.path.join('assets','char.png'))
PLAYERIMAGE = pygame.transform.rotate(pygame.transform.scale(AVATARIMAGE,(PLAYERWIDTH,PLAYERHEIGHT)),0)

def draw_game(player):
    WIN.fill(BLACK)
    WIN.blit(PLAYERIMAGE, (player.x, player.y))
    pygame.display.update()

def handle_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - VEL > 0:
        player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL + PLAYERWIDTH < WINWIDTH:
        player.x += VEL
    if keys_pressed[pygame.K_UP] and player.y - VEL > 0:
        player.y -= VEL
    if keys_pressed[pygame.K_DOWN] and player.y + VEL + PLAYERHEIGHT < WINHEIGHT:
        player.y += VEL

def main():
    ppos = pygame.Rect(0,WINHEIGHT-PLAYERHEIGHT,PLAYERWIDTH,PLAYERHEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed, ppos)
        draw_game(ppos)

if __name__ == '__main__':
    main()