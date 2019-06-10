# -*- coding: utf-8 -*-
#modules externes
import sys
import os
import time
import select
import tty 
import termios

#mes modules
import Background 
import Tank
import Bullet
import Menu
import Fin
#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

#donnee du jeu
obstacles=[]
background = None
timeStep=None

def init():
    global tank, background, timeStep, obstacles, tank2, menu, Fin1, Fin2
    
    #initialisation de la partie

    timeStep=0.05
    
    # creation des elements du jeu
    
    tank=Tank.createTank(4,46,"tank.txt",True)
    tank2=Tank.createTank(196,46,"tank2.txt",False)
    background = Background.create("bg.txt")
    menu = Menu.createMenu("menu.txt")
    Fin1= Fin.createFin("Win_1.txt")
    Fin2= Fin.createFin("Win_2.txt")

    # interaction clavier
    tty.setcbreak(sys.stdin.fileno())

def interact():
    global tank,background, timeStep, tank2, Balle, menu
    #gestion des evenement clavier

    #si une touche est appuyee
    if isData():
        c = sys.stdin.read(1)
        if menu["on"]==False and tank["PV"]>0 and tank2["PV"]>0:
            if c == '\x1b':         # x1b is ESC
                quitGame()
            
            if tank["isPlaying"]==True and tank["PV"]>0 and tank2["isShooting"]==False: #condition tank 1
                if c=='q' :
                    if Background.isValid(background,tank["x"]-3,tank["y"]):
                        if Background.isClimbable(background,tank["x"]-2,tank["y"]+2):
                            Tank.moveUpLeft(tank)
                        elif Background.canFall(background,tank["x"]-1,tank["y"]+3):
                            Tank.moveDownLeft(tank)
                        else :
                            Tank.moveLeft(tank)   
                elif c=='d' :
                    if Background.isValid(background,tank["x"]+12,tank["y"]):
                        if Background.isClimbable(background,tank["x"]+9,tank["y"]+2):
                            Tank.moveUpRight(tank)
                        elif Background.canFall(background,tank["x"]-1,tank["y"]+3):
                            Tank.moveDownRight(tank)
                        else :
                            Tank.moveRight(tank)
                elif c=='x' : 
                    Balle=Bullet.createBullet(tank["x"]+13,tank["y"]+1,5)
                    tank["isShooting"]=True
                elif c=='z' :
                    Tank.PowerUp(tank)
                elif c=='s' :
                    Tank.PowerDown(tank)
                elif c=='a' :
                    Tank.AngleDown(tank)
                elif c=='e' :
                    Tank.AngleUp(tank)
            
            if tank2["isPlaying"]==True and tank2["PV"]>0 and tank["isShooting"]==False: #condition tank 2
                if c=='m' :
                    if Background.isValid(background,tank2["x"]+12,tank2["y"]):
                        if Background.isClimbable(background,tank2["x"]+9,tank2["y"]+2):
                            Tank.moveUpRight(tank2)
                        elif Background.canFall(background,tank2["x"]-1,tank2["y"]+3):
                            Tank.moveDownRight(tank2)
                        else :
                            Tank.moveRight(tank2)
                elif c=='k' :
                    if Background.isValid(background,tank2["x"]-3,tank2["y"]):
                        if Background.isClimbable(background,tank2["x"]-2,tank2["y"]+2):
                            Tank.moveUpLeft(tank2)
                        elif Background.canFall(background,tank2["x"]-1,tank2["y"]+3):
                            Tank.moveDownLeft(tank2)
                        else :
                            Tank.moveLeft(tank2)
                elif c=='u' :
                    Balle=Bullet.createBullet(tank2["x"]-1,tank2["y"]+1,5)
                    tank2["isShooting"]=True
                elif c=='o' :
                    Tank.PowerUp(tank2)
                elif c=='l' :
                    Tank.PowerDown(tank2)
                elif c=='i' :
                    Tank.AngleDown(tank2)
                elif c=='p' :
                    Tank.AngleUp(tank2)
            
        
        elif menu["on"]==True: #Action dans le menu
            if c == '\x1b':         # x1b is ESC
                quitGame() 
        
            elif c== '\n':
                Menu.MenuOff(menu)
        
        elif Fin1["on"]==True:
            if c== '\x1b':
                quitGame()
            elif c== 'r':
                init()
        
        elif Fin2["on"]==True:
            if c== '\x1b':
                quitGame()
            elif c== 'r':
                init()
      

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
    global background, tank,obstacles, tank2, menu
    
    #effacer la console
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")
    
    #Menu ou non
    if menu["on"]==False and tank["PV"]>0 and tank2["PV"]>0:
    #affichage des differents elements
        Background.show(background)
        PrintVar(21,2,tank["v"])
        PrintVar(17,3,tank["angle"])
        PrintVar(12,6,tank["PV"])
        PrintVar(186,6,tank2["PV"])
        PrintVar(194,2,tank2["v"])
        PrintVar(190,3,tank2["angle"])
        PrintVar(190,4,Fin1["on"])
        showBalle()
        Tank.show(tank2)
        Tank.show(tank)
    
    #Affichage du menu
    elif menu["on"]==True:
        Menu.show(menu)
    
    elif tank2["PV"]<=0:
        Fin.FinOn(Fin1)
        Fin.show(Fin1)
    
    elif tank["PV"]<=0:
        Fin.FinOn(Fin2)
        Fin.show(Fin2)
    
    #restoration couleur 
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    #deplacement curseur
    sys.stdout.write("\033[0;0H\n")

def showBalle():
    global Balle
    
    if tank["isShooting"]==True:
        Bullet.show(Balle)
        Bullet.shoot(Balle,tank,1)
        Bullet.collide(background,Balle,tank,tank2)
        tank["isPlaying"]=False
        tank2["isPlaying"]=True
    if tank2["isShooting"]==True:
        Bullet.show(Balle)
        Bullet.shoot(Balle,tank2,-1)
        Bullet.collide(background,Balle,tank2,tank)
        tank2["isPlaying"]=False
        tank["isPlaying"]=True
        
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