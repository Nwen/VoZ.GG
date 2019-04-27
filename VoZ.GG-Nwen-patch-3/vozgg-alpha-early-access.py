# -*- coding: utf-8 -*-
import random, pygame, os
#from pygame.locals import *
"""
Trucs à faire :
    deuxième joueur
    projectiles
    collisions joueur / projectile
    collisons joueur / joueur
    collisions projectile sol
"""


class Jeu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("VoZ.GG alpha early access")
        self.running = True
        self.clock = pygame.time.Clock()
        self.fenetre = pygame.display.set_mode((1080,720))
        self.bullets = []

        self.wallSize=(50,50)

        self.bg = pygame.image.load("bg.jpg").convert()
        self.bg = pygame.transform.scale(self.bg,(1080,720))
        self.fenetre.blit(self.bg,(0,0))
        self.leSol = pygame.Rect(0,620,1080,100)
        self.coord=[(500,604),(450,588),(400,604),(1000,604),(720,604),(599,604),(140,604)]
        self.walls=[]   
        self.leSol=Wall((0,620),(1080,100))
        self.walls.append(self.leSol)

        i = 0
        for e in self.coord :
            self.walls.append(Wall(e,self.wallSize))
            i+=1
        self.player = Player(32,620)
        self.s_player = pygame.sprite.GroupSingle(self.player)
        self.player2 = Player(1040,600)
        self.s_player2 = pygame.sprite.GroupSingle(self.player2)
        
    def mainloop(self) :
        tic = 160
        self.clock.tick(tic)
        delta = 1/tic
        player = self.player
        player2 = self.player2
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    self.running = False
            
            # Move the player if an arrow key is pressed
            player.Gravity()
            player2.Gravity()
            key = pygame.key.get_pressed()
            if player.isClimbing == False and player.isShooting == False:
                if key[pygame.K_LEFT]:
                    player.move(-1, 0)
                    player.sens=-1
                if key[pygame.K_RIGHT]:
                    player.move(1, 0)
                    player.sens = 1
                if key[pygame.K_SPACE]:
                    player.shoot()
                    self.bullets.append(Bullet((player.rect.center[0],player.rect.top[1]),(5,5)))
        
            if player2.isClimbing == False and player2.isShooting==False:
                if key[pygame.K_a]:
                    player2.move(-1,0)
                    player2.sens=-1
                if key[pygame.K_d]:
                    player2.move(1,0)
                    player2.sens = 1
        
            if player.isClimbing == True:
                player.velocity-=player.gravity*2*delta
                player.move(player.sens, -player.velocity)
            
            if player.isClimbing == True:
                player2.velocity -= player2.gravity*2*delta
                player2.move(player2.sens, -player2.velocity)

            if player.isShooting == True:
                for b in self.bullets :
                    b.update()
                    b.velocity-=b.gravity*2*delta
                    b.move(player.sens, -player.velocity)
                    pygame.draw.rect(self.fenetre, (255, 0, 0), b.rect)
                    bs = pygame.sprite.GroupSingle(self.b)
                    bs.draw(self.fenetre)
               
            self.show()

        pygame.quit()
        
    def show(self):
        self.fenetre.blit(self.bg,(0,0))
        for wall in self.walls:
            pygame.draw.rect(self.fenetre, (183, 142, 38), wall.rect)
         
        self.s_player.draw(self.fenetre)
        self.s_player2.draw(self.fenetre)
        #pygame.draw.rect(self.fenetre, (255, 200, 0), self.player.rect)
        pygame.display.flip()
    
                
class Player(pygame.sprite.Sprite):

    v=1
    gravity = 10
    velocity = 0
    isClimbing = False
    isShooting = False
    sens = 1
    
    def __init__(self, posx, posy):
        '''self.image = pygame.image.load("tank.png")
        self.image = pygame.transform.scale(self.image, (32,16))
        self.rect = self.image.get_rect()'''
        self.rect = pygame.Rect(posx, posy, 32, 16)
        pygame.sprite.Sprite.__init__(self)
    def climb(self) :
        self.isClimbing = True
        self.velocity = 2

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            
        if self.sens == 1 :
            self.image = pygame.image.load("tank.png")
            self.image = pygame.transform.scale(self.image, (32,16))
        if self.sens == -1 :
            self.image = pygame.image.load("tank.png")
            self.image = pygame.transform.scale(self.image, (32,16))
            self.image = pygame.transform.flip(self.image, True, False)
            
        
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx*self.v
        self.rect.y += dy*self.v

        # If you collide with a wall, move out based on velocity
        for wall in jeu.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    self.climb()
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    self.climb()
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    self.isClimbing = False
                    self.velocity = 0
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    
    def shoot(self):
        self.isShooting = True
        
    def Gravity(self):
        self.move(0,1.5)
        

        
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, posx, posy, vit, ang):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load("bullet.png")
        self.posx = posx
        self.posy = posy
        self.vit = vit
        
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
        for wall in jeu.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                    
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                    
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                    self.velocity = 0
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    
    def update(self):
        #à faire
        print('o no')

                    
class Wall(pygame.sprite.Sprite):
    
    def __init__(self, pos, size):
        #walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        #self.rect = self.image.get_rect()
        
jeu = Jeu()
jeu.mainloop()