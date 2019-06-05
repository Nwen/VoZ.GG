# -*- coding: utf-8 -*-
#modules externes
import sys
import os
import time
import select
import tty 
import termios
import random
import math

#mes modules
import Background 
import Tank
import Bullet
#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

#donnee du jeu
obstacles=[]
background = None
timeStep=None
t=0.0
m=0
p=0.0
h=0.0

def init():
    global tank, background, timeStep, obstacles, tank2
    
    #initialisation de la partie

    timeStep=0.05
    
    # creation des elements du jeu
    
    tank=Tank.createTank(4,46,"tank.txt")
    tank2=Tank.createTank(196,46,"tank2.txt")
    background = Background.create("bg.txt")

    # interaction clavier
    tty.setcbreak(sys.stdin.fileno())

def interact():
    global tank,background, timeStep, tank2,m, Balle
    #gestion des evenement clavier

    #si une touche est appuyee
    if isData():
        c = sys.stdin.read(1)
        if c == '\x1b':         # x1b is ESC
            quitGame()
        if c=='q' :
            if Background.isValid(background,tank["x"]-3,tank["y"]):
                if Background.isClimbable(background,tank["x"]-2,tank["y"]+1):
                    Tank.moveUpLeft(tank)
                elif Background.canFall(background,tank["x"]+10,tank["y"]+2):
                    Tank.moveDownRight(tank)
                else :
                    Tank.moveLeft(tank)
        elif c=='d' :
            if Background.isValid(background,tank["x"]+12,tank["y"]):
                if Background.isClimbable(background,tank["x"]+9,tank["y"]+1):
                    Tank.moveUpRight(tank)
                elif Background.canFall(background,tank["x"]-1,tank["y"]+2):
                    Tank.moveDownRight(tank)
                else :
                    Tank.moveRight(tank)
        elif c=='k' :
            if Background.isValid(background,tank2["x"]-3,tank2["y"]):#gestion collision avec les bords de la map
                if Background.isClimbable(background,tank2["x"]-2,tank2["y"]+1):#si un bloc est devant, le tank monte
                    Tank.moveUpLeft(tank2)
                elif Background.canFall(background,tank2["x"]+12,tank2["y"]-1): #si il peut tomber, il tombe
                    Tank.moveDownLeft(tank2)
                else :
                    Tank.moveLeft(tank2)
        elif c=='m' :
            if Background.isValid(background,tank2["x"]+12,tank2["y"]):
                if Background.isClimbable(background,tank2["x"]+9,tank2["y"]+1):
                    Tank.moveUpRight(tank2)
                elif Background.canFall(background,tank2["x"]+12,tank2["y"]-1):
                    Tank.moveDownRight(tank2)
                else :
                    Tank.moveRight(tank2)
        elif c=='v' : 
            Balle=Bullet.createBullet(tank["x"],tank["y"])
            m=1
        elif c=='z' :
            Tank.PowerUp(tank)
        elif c=='s' :
            Tank.PowerDown(tank)

def isData():
    #recuperation evenement clavier
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def PrintVar(y,x,var):
    X=str(int(x))
    Y=str(int(y))
    sys.stdout.write("\033["+X+";"+Y+"H")
    sys.stdout.write("\033[40m")
    sys.stdout.write(str(var))
    sys.stdout.write("\033[37m")

def show():
    global background, tank,obstacles, tank2
    
    #rafraichissement de l'affichage
    
    #effacer la console
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")

    #affichage des differents elements
    
    Background.show(background)
    PrintVar(21,2,tank["v"])
    showBalle()
    Tank.show(tank2)
    Tank.show(tank)
    
    #restoration couleur 
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    #deplacement curseur
    sys.stdout.write("\033[0;0H\n")

def showBalle():
    global Balle,t,p,v
    
    if m==1:
        Bullet.show(Balle)
        t= t+1.0
        h=math.cos((math.pi)/4)*5.0*t
        Balle["x"]+=int(h)
        p=-0.5*t*t*1+math.sin((math.pi)/4)*tank["v"]*t
        Balle["y"]-=int(p)
        
        
def run():
    global timeStep
    
    #Boucle de simulation    
    while 1:
        interact()
        show()
        time.sleep(timeStep)

def quitGame():    
    
    #restoration parametres terminal
    global old_settings
    
    #couleur white
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")
    
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    sys.exit()

######################################


init()
#try:
run()
#finally:
quitGame()