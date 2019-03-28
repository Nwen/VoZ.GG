# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:10:51 2019

@author: gwend,Nwen
"""
import random, pygame, os
#from pygame.locals import *

pygame.init()
pygame.display.set_caption("VoZ.GG alpha early access")

fenetre = pygame.display.set_mode((1540,794))
clock = pygame.time.Clock()

running = True
bg = pygame.image.load("bg.jpg").convert()
bg = pygame.transform.scale(bg,(1540,794))
fenetre.blit(bg,(0,0))

img = pygame.image.load("10E.jpg").convert()
imgrect = img.get_rect()

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
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)
        
coord=[(500,500),(400,300),(1000,250),(720,500),(592,600),(100,100)]
walls=[]        
i = 0
for e in coord :
    walls.append(Wall(e))
    i+=1

player = Player()

while running :
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    # Move the player if an arrow key is pressed
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
    
    for wall in walls:
        pygame.draw.rect(fenetre, (255, 255, 255), wall.rect)
        
    pygame.draw.rect(fenetre, (255, 200, 0), player.rect)
    
    pygame.display.flip()
