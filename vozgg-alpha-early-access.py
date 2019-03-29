# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:50:57 2019
@author: nwenn
"""

import random, pygame, os
#from pygame.locals import *

pygame.init()
pygame.display.set_caption("VoZ.GG alpha early access")

fenetre = pygame.display.set_mode((1080,720))
clock = pygame.time.Clock()

running = True
bg = pygame.image.load("bg.jpg").convert()
bg = pygame.transform.scale(bg,(1080,720))
fenetre.blit(bg,(0,0))

'''img = pygame.image.load("10E.jpg").convert()
imgrect = img.get_rect()'''


class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    
class Wall(object):
    
    def __init__(self, pos, size):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        
def Gravity(p):
    p.move(0,1)

leSol = pygame.Rect(0,620,1080,100)

coord=[(500,500),(400,300),(1000,250),(720,500),(592,600),(100,100)]
walls=[]   
leSol=Wall((0,620),(1080,100))
wallSize=(50,50)
i = 0
for e in coord :
    walls.append(Wall(e,wallSize))
    i+=1
pygame.mixer.music.load('son.mp3')

player = Player()


    
while running :
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    # Move the player if an arrow key is pressed
    
    
    Gravity(player)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)
    if key[pygame.K_c]:
        fenetre.blit(bg,(0,0))
    if key[pygame.K_x]:
        pygame.mixer.music.play(0)

    for wall in walls:
        pygame.draw.rect(fenetre, (255, 0, 0), wall.rect)
    
    pygame.draw.rect(fenetre, (255, 200, 0), player.rect)

    pygame.display.flip()

pygame.quit()
