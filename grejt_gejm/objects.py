from email.mime import image
import pygame, globals
from pygame.locals import *

globals.init()
pygame.init()

class Player:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("chuju1.jpg")
        self.rotImage = pygame.transform.rotate(self.image, 0)
        self.resetPos()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_d]:
            self.x += globals.vel
            self.rotImage = pygame.transform.rotate(self.image, 270)
        if keys[K_a]:
            self.x -= globals.vel
            self.rotImage = pygame.transform.rotate(self.image, 90)
        if keys[K_w]:
            self.y -= globals.vel
            self.rotImage = pygame.transform.rotate(self.image, 0)
        if keys[K_s]:
            self.y += globals.vel
            self.rotImage = pygame.transform.rotate(self.image, 180)


    def draw(self):
        globals.DISPLAY.blit(self.rotImage, (self.x, self.y))

    def getPos(self, xy):
        if xy == "x":
            return(self.x)
        elif xy == "y":
            return(self.y)
    def resetPos(self):
        self.x = globals.WIDTH / 2
        self.y = globals.HEIGHT / 2

P1 = Player()


class Enemak1():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemak1.jpg")
        self.resetPos()
    
    def update(self):
        if(self.x - P1.getPos("x")) < 0 and (self.x - P1.getPos("x")) != 0:
            self.x += globals.enemyVel
        elif(self.x - P1.getPos("x")) > 0 and (self.x - P1.getPos("x")) != 0:
            self.x -= globals.enemyVel

        if(self.y - P1.getPos("y")) < 0 and (self.y - P1.getPos("y")) != 0:
            self.y += globals.enemyVel
        elif(self.y - P1.getPos("y")) > 0 and (self.y - P1.getPos("y")) != 0:
            self.y -= globals.enemyVel
        

    def draw(self):
        globals.DISPLAY.blit(self.image, (self.x, self.y))
    
    def getPos(self, xy):
        if xy == "x":
            return(self.x)
        elif xy == "y":
            return(self.y)

    def resetPos(self):
        self.x = 128
        self.y = 128

E1 = Enemak1()


class Projectiles():
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        self.image = pygame.image.load("fula.jpg")
    
    def draw(self):
        globals.DISPLAY.blit(self.image, (self.x, self.y))


Pr = Projectiles(1, 600, 400)