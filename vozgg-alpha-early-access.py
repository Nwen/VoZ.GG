# -*- coding: utf-8 -*-
import random, pygame, os
#from pygame.locals import *
class Player(object):
    v=5
    gravity = 10
    velocity = 0
    isjumping = 0
    isClimbing = False
    sens = 1
    
    def __init__(self):
        self.rect = pygame.Rect(32, 620, 16, 16)
        
    def jump(self):
        self.isjumping = True
        print("jump")
        
    def climb(self) :
        self.isClimbing = True
        self.velocity = 2

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            
        
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx*self.v
        self.rect.y += dy*self.v

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    self.climb()
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    self.climb()
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    self.isjumping = False
                    self.isClimbing = False
                    self.velocity = 0
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom


                    
class Wall(object):
    
    def __init__(self, pos, size):
        #walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        
        
def Gravity(p):
    p.move(0,1.5)


def run() :
    global clock,fenetre,player,bg,running, walls
    tic = 60
    clock.tick(tic)
    delta = 1/tic
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    # Move the player if an arrow key is pressed
    Gravity(player)
    key = pygame.key.get_pressed()
    if player.isClimbing == False:
        if key[pygame.K_LEFT]:
            player.move(-1, 0)
            player.sens=-1
        if key[pygame.K_RIGHT]:
            player.move(1, 0)
            player.sens = 1

    fenetre.blit(bg,(0,0))
    for wall in walls:
        pygame.draw.rect(fenetre, (183, 142, 38), wall.rect)
        
    if player.isjumping:
        player.velocity-=player.gravity*2*delta
        player.move(0,-player.velocity)
        #print(player.velocity)
        
    if player.isClimbing == True:
        player.velocity-=player.gravity*2*delta
        player.move(player.sens, -player.velocity)
        
    pygame.draw.rect(fenetre, (255, 200, 0), player.rect)
    
    pygame.display.flip()
    
running = True
clock = pygame.time.Clock()


pygame.init()
pygame.display.set_caption("VoZ.GG alpha early access")

fenetre = pygame.display.set_mode((1080,720))

wallSize=(50,50)

bg = pygame.image.load("bg.jpg").convert()
bg = pygame.transform.scale(bg,(1080,720))
fenetre.blit(bg,(0,0))
leSol = pygame.Rect(0,620,1080,100)
coord=[(500,604),(450,588),(400,604),(1000,604),(720,604),(599,604),(140,604)]
walls=[]   
leSol=Wall((0,620),(1080,100))
walls.append(leSol)

i = 0
for e in coord :
    walls.append(Wall(e,wallSize))
    i+=1
player = Player()
   
while running :
    run()
    
pygame.quit()