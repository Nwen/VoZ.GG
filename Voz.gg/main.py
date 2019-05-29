

#modules externes
import sys
import os
import time
import select
import tty 
import termios
import random

#mes modules
import Background 
import Tank
import Obstacle
#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

#donnee du jeu
obstacles=[]
background = None
timeStep=None


def init():
	global tank, background, timeStep, obstacles, tank2
	
	#initialisation de la partie

	timeStep=0.2
	
	# creation des elements du jeu
	
	tank=Tank.createAnimat(4,46,"tank.txt")
	tank2=Tank.createAnimat(196,46,"tank2.txt")

	background = Background.create("bg.txt")

	# interaction clavier
	tty.setcbreak(sys.stdin.fileno())

def interact():
    global tank,background, timeStep, tank2
	#gestion des evenement clavier

	#si une touche est appuyee
    if isData():
        c = sys.stdin.read(1)
        if c == '\x1b':         # x1b is ESC
            quitGame()
        elif c=='q' :
            Tank.moveLeft(tank)
        elif c=='d' :
            Tank.moveRight(tank)
        elif c=='k' :
            Tank.moveLeft(tank2)
        elif c=='m' :
            Tank.moveRight(tank2)

def isData():
	#recuperation evenement clavier
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def show():
	global background, tank,obstacles, tank2
	
	#rafraichissement de l'affichage
	
	#effacer la console
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")

	#affichage des differents elements

	Background.show(background)
	
	

	Tank.show(tank2)
	Tank.show(tank)
	
	#restoration couleur 
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")

	#deplacement curseur
	sys.stdout.write("\033[0;0H\n")


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
