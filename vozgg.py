# -*- coding: utf-8 -*-
#modules externes
import sys
import os
import time
import select
import tty 
import termios

#nos modules
import Background 
import Tank
import Bullet
import Menu
import Fin
import ChooseMap
#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

#donnee du jeu
background = None
timeStep = None

def init():
    global tank, background, timeStep, tank2, menu, Fin1, Fin2, choixmap
    
    #initialisation de la partie

    timeStep=0.05
    
    # creation des elements du jeu
    
    tank=Tank.createTank(4,46,"tank.txt",True)
    tank2=Tank.createTank(196,46,"tank2.txt",False)
    choixmap = ChooseMap.createChoix("ChoixMap.txt")
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
        if Menu.getOn(menu)==False and Tank.getPV(tank) > 0 and Tank.getPV(tank2) > 0 and background!=None and ChooseMap.getOn(choixmap)==False:
            if c == '\x1b':         # x1b = échap
                quitGame()
            
            if Tank.getIsPlaying(tank)==True and Tank.getPV(tank)>0 and Tank.getIsShooting(tank2)==False: #condition pour jouer tank 1
                if c=='q' :
                    if Background.isValid(background,Tank.getX(tank)-3,Tank.getY(tank)):
                        if Background.isClimbable(background,Tank.getX(tank)-2,Tank.getY(tank)+2): #si le tank peut grimper
                            Tank.moveUpLeft(tank) #monter et avancer à gauche
                        elif Background.canFall(background,Tank.getX(tank)-1,Tank.getY(tank)+3): #si le tank peut tomber
                            Tank.moveDownLeft(tank) #descendre et avancer à gauche
                        else :
                            Tank.moveLeft(tank) # avancer à gauche
                elif c=='d' :
                    if Background.isValid(background,Tank.getX(tank)+12,Tank.getY(tank)):
                        if Background.isClimbable(background,Tank.getX(tank)+9,Tank.getY(tank)+2):
                            Tank.moveUpRight(tank) #monter et avancer à droite
                        elif Background.canFall(background,Tank.getX(tank)-1,Tank.getY(tank)+3):
                            Tank.moveDownRight(tank) #descendre et avancer à droite
                        else :
                            Tank.moveRight(tank) # avancer à droite
                elif c=='x' : 
                    Balle=Bullet.createBullet(Tank.getX(tank)+13,Tank.getY(tank)+1,5)
                    Tank.setIsShooting(tank,True)
                elif c=='z' : #augmenter la puissance de tir
                    Tank.PowerUp(tank)
                elif c=='s' : #diminuer la puissance de tir
                    Tank.PowerDown(tank)
                elif c=='a' : #diminuer l'angle de tir
                    Tank.AngleDown(tank)
                elif c=='e' : #augmenter l'angle de tir
                    Tank.AngleUp(tank)
            
            if Tank.getIsPlaying(tank2)==True and Tank.getPV(tank2)>0 and Tank.getIsShooting(tank)==False: #condition pour jouer tank 2
                if c=='m' :
                    if Background.isValid(background,Tank.getX(tank2)+12,Tank.getY(tank2)):
                        if Background.isClimbable(background,Tank.getX(tank2)+11,Tank.getY(tank2)+2):
                            Tank.moveUpRight(tank2) #monter et avancer à gauche
                        elif Background.canFall(background,Tank.getX(tank2),Tank.getY(tank2)+3):
                            Tank.moveDownRight(tank2) #descendre et avancer à gauche
                        else :
                            Tank.moveRight(tank2) # avancer à gauche
                elif c=='k' :
                    if Background.isValid(background,Tank.getX(tank2)-3,Tank.getY(tank2)):
                        if Background.isClimbable(background,Tank.getX(tank2)-2,Tank.getY(tank2)+2):
                            Tank.moveUpLeft(tank2) #monter et avancer à droite
                        elif Background.canFall(background,Tank.getX(tank2)-1,Tank.getY(tank2)+3):
                            Tank.moveDownLeft(tank2) #descendre et avancer à droite
                        else :
                            Tank.moveLeft(tank2) # avancer à droite
                elif c=='u' :
                    Balle=Bullet.createBullet(Tank.getX(tank2)-1,Tank.getY(tank2)+1,5)
                    Tank.setIsShooting(tank2,True)
                elif c=='o' : #augmenter la puissance de tir
                    Tank.PowerUp(tank2)
                elif c=='l' : #diminuer la puissance de tir
                    Tank.PowerDown(tank2)
                elif c=='i' : #diminuer l'angle de tir
                    Tank.AngleDown(tank2)
                elif c=='p' : #augmenter l'angle de tir
                    Tank.AngleUp(tank2)
            
        
        elif Menu.getOn(menu)==True: #Action dans le menu
            if c == '\x1b':         # x1b = échap
                quitGame() 
        
            elif c== '\n': #enlever le menu et choisir la carte et la couleur
                Menu.MenuOff(menu)
                ChooseMap.ChoixOn(choixmap)
            
        elif ChooseMap.getOn(choixmap)==True:
            if c== '\x1b': #x1b is ESC
                quitGame()
            
            elif c== 'g': #choix map 1
                background = Background.create("bg.txt")
                Tank.setY(tank,46)
                Tank.setY(tank2,46)
                
            elif c== 'h': #choix map 2
                background = Background.create("bg1.txt")
                Tank.setY(tank,18)
                Tank.setY(tank2,18)
            
            elif c== '\n': #enlever le choix de la carte de la couleur
                ChooseMap.ChoixOff(choixmap)
                
            elif c== 'c': #changer la couleur du tank 1
                Tank.changeColor(tank)
            
            elif c== 'v': #changer la couleur du tank 2
                Tank.changeColor(tank2)
        
        elif Fin.getOn(Fin1)==True:
            if c== '\x1b':
                quitGame()
            elif c== 'r': #recommencer un partie
                init()
        
        elif Fin.getOn(Fin2)==True:
            if c== '\x1b':
                quitGame()
            elif c== 'r': #recommencer un partie
                init()

def isData():
    #recuperation evenement clavier
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def PrintVar(y,x,var): 
    #afficher une variable
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
    if Menu.getOn(menu)==False and Tank.getPV(tank2)>0 and Tank.getPV(tank2)>0 and ChooseMap.getOn(choixmap)==False:
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
    elif Menu.getOn(menu)==True:
        Menu.show(menu)
    
    #affichage choix map et couleur
    elif ChooseMap.getOn(choixmap)==True:
        ChooseMap.show(choixmap)
        if background != None:
            Tank.show(tank)
            Tank.show(tank2)
    
    #affichage fin1, tank1 a gagné
    elif Tank.getPV(tank2)<=0:
        Fin.setOn(Fin1,True)
        Fin.show(Fin1)
    
    #affichage fin2, tank2 a gagné
    elif Tank.getPV(tank)<=0:
        Fin.setOn(Fin2,True)
        Fin.show(Fin2)
    
    #restoration couleur 
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    #deplacement curseur
    sys.stdout.write("\033[0;0H\n")

def updateBalle():
    #mise à jour de la balle, gestion du tour en fonction de la situation de la balle
    global Balle
    
    if Tank.getIsShooting(tank)==True:
        Bullet.show(Balle)
        Bullet.shoot(Balle,tank,1)
        Bullet.collide(background,Balle,tank,tank2)
        Tank.setIsPlaying(tank,False)
        Tank.setIsPlaying(tank2,True)
    if Tank.getIsShooting(tank2)==True:
        Bullet.show(Balle)
        Bullet.shoot(Balle,tank2,-1)
        Bullet.collide(background,Balle,tank2,tank)
        Tank.setIsPlaying(tank2,False)
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
    
def main() :
    init()
    run()
    quitGame()


if __name__=="__main__":
    main()