import pygame, objects, globals
from pygame.locals import *

globals.init()
pygame.init()

colorWhite = (255,255,255)
colorBlack = (0, 0, 0)
font = pygame.font.Font('Arial.ttf', 32)

def checkColision():
    P1x = objects.P1.getPos("x")
    P1y = objects.P1.getPos("y")
    E1x = objects.E1.getPos("x")
    E1y = objects.E1.getPos("y")

    if (P1x - E1x) in range(-128,128) and (P1y - E1y) in range(-128,128):
        text = font.render("Nupko stlac R alebo ESC", True, colorWhite)
        globals.DISPLAY.blit(text, (globals.WIDTH/2, globals.HEIGHT/2))
        pygame.display.update()
        objects.P1.resetPos()
        objects.E1.resetPos()

        while True:
            globals.FramePerSec.tick(20)
            keys = pygame.key.get_pressed()
            if keys[K_r]:
                break
            if keys[K_ESCAPE]:
                pygame.quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()