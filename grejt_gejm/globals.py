import pygame
from pygame.locals import *

pygame.init()

def init():
    global vel 
    vel = 5
    global enemyVel 
    enemyVel = 2.5
    global WIDTH
    WIDTH = 1200
    global HEIGHT 
    HEIGHT = 800
    global DISPLAY
    DISPLAY = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    global FramePerSec 
    FramePerSec = pygame.time.Clock()