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
background = None
timeStep=None

def init():
    global tank, background, timeStep, tank2, menu, Fin1, Fin2
    
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
        if Menu.getOn(menu)==False and Tank.getPV(tank) > 0 and Tank.getPV(tank2) > 0:
            if c == '\x1b':         # x1b is ESC
                quitGame()
            
            if Tank.getIsPlaying(tank)==True and Tank.getPV(tank)>0 and Tank.getIsShooting(tank2)==False: #condition tank 1
                if c=='q' :
                    if Background.isValid(background,Tank.getX(tank)-3,Tank.getY(tank)):
                        if Background.isClimbable(background,Tank.getX(tank)-2,Tank.getY(tank)+2):
                            Tank.moveUpLeft(tank)
                        elif Background.canFall(background,Tank.getX(tank)-1,Tank.getY(tank)+3):
                            Tank.moveDownLeft(tank)
                        else :
                            Tank.moveLeft(tank)   
                elif c=='d' :
                    if Background.isValid(background,Tank.getX(tank)+12,Tank.getY(tank)):
                        if Background.isClimbable(background,Tank.getX(tank)+9,Tank.getY(tank)+2):
                            Tank.moveUpRight(tank)
                        elif Background.canFall(background,Tank.getX(tank)-1,Tank.getY(tank)+3):
                            Tank.moveDownRight(tank)
                        else :
                            Tank.moveRight(tank)
                elif c=='x' : 
                    Balle=Bullet.createBullet(Tank.getX(tank)+13,Tank.getY(tank)+1,26)
                    #tank["isShooting"]=True
                    Tank.setIsShooting(tank,True)
                elif c=='z' :
                    Tank.PowerUp(tank)
                elif c=='s' :
                    Tank.PowerDown(tank)
                elif c=='a' :
                    Tank.AngleDown(tank)
                elif c=='e' :
                    Tank.AngleUp(tank)
            
            if Tank.getIsPlaying(tank2)==True and Tank.getPV(tank2)>0 and Tank.getIsShooting(tank)==False: #condition tank 2
                if c=='m' :
                    if Background.isValid(background,Tank.getX(tank2)+12,Tank.getY(tank2)):
                        if Background.isClimbable(background,Tank.getX(tank2)+9,Tank.getY(tank2)+2):
                            Tank.moveUpRight(tank2)
                        elif Background.canFall(background,Tank.getX(tank2)-1,Tank.getY(tank2)+3):
                            Tank.moveDownRight(tank2)
                        else :
                            Tank.moveRight(tank2)
                elif c=='k' :
                    if Background.isValid(background,Tank.getX(tank2)-3,Tank.getY(tank2)):
                        if Background.isClimbable(background,Tank.getX(tank2)-2,Tank.getY(tank2)+2):
                            Tank.moveUpLeft(tank2)
                        elif Background.canFall(background,Tank.getX(tank2)-1,Tank.getY(tank2)+3):
                            Tank.moveDownLeft(tank2)
                        else :
                            Tank.moveLeft(tank2)
                elif c=='u' :
                    Balle=Bullet.createBullet(Tank.getX(tank2)-1,Tank.getY(tank2)+1,26)
                    #tank2["isShooting"]=True
                    Tank.setIsShooting(tank2,True)
                elif c=='o' :
                    Tank.PowerUp(tank2)
                elif c=='l' :
                    Tank.PowerDown(tank2)
                elif c=='i' :
                    Tank.AngleDown(tank2)
                elif c=='p' :
                    Tank.AngleUp(tank2)
            
        
        elif Menu.getOn(menu)==True: #Action dans le menu
            if c == '\x1b':         # x1b is ESC
                quitGame() 
        
            elif c== '\n':
                Menu.MenuOff(menu)
        
        elif Fin.getOn(Fin1)==True:
            if c== '\x1b':
                quitGame()
            elif c== 'r':
                init()
        
        elif Fin.getOn(Fin2)==True:
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
    global background, tank, tank2, menu, Fin1, Fin2
    
    #effacer la console
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")
    
    #Menu ou non
    if menu["on"]==False and Tank.getPV(tank2)>0 and Tank.getPV(tank2)>0:
    #affichage des differents elements
        Background.show(background)
        PrintVar(21,2,Tank.getV(tank))
        PrintVar(17,3,Tank.getAngle(tank))
        PrintVar(12,6,Tank.getPV(tank))
        PrintVar(186,6,Tank.getPV(tank2))
        PrintVar(194,2,Tank.getV(tank2))
        PrintVar(190,3,Tank.getAngle(tank2))
        updateBalle()
        Tank.show(tank2)
        Tank.show(tank)
    
    #Affichage du menu
    elif menu["on"]==True:
        Menu.show(menu)
    
    elif Tank.getPV(tank2)<=0:
        Fin.setOn(Fin1,True)
        Fin.show(Fin1)
    
    elif Tank.getPV(tank)<=0:
        Fin.setOn(Fin2,True)
        Fin.show(Fin2)
    
    #restoration couleur 
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    #deplacement curseur
    sys.stdout.write("\033[0;0H\n")

def updateBalle():
    global Balle
    
    if Tank.getIsShooting(tank)==True:
        Bullet.show(Balle)
        Bullet.shoot(Balle,tank,1)
        Bullet.collide(background,Balle,tank,tank2)
        #tank["isPlaying"]=False
        Tank.setIsPlaying(tank,False)
        #tank2["isPlaying"]=True
        Tank.setIsPlaying(tank2,True)
    if Tank.getIsShooting(tank2)==True:
        Bullet.show(Balle)
        Bullet.shoot(Balle,tank2,-1)
        Bullet.collide(background,Balle,tank2,tank)
        #tank2["isPlaying"]=False
        Tank.setIsPlaying(tank2,False)
        #tank["isPlaying"]=True
        Tank.setIsPlaying(tank,True)
        
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

if __name__=="__main__":
    init()
    run()
    quitGame()