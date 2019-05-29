
import sys
import os
import random
import Background

#le module Monster gere le type abstrait de donnee Monster
#un monster est un objet qui se deplace dans le terminal de maniere aleatoire

def createAnimat(posx,posy,filename):
	
	#creation monster
    animat=dict()
    animat["color"]=1
    animat["x"]=posx
    animat["y"]=posy
    myfile=open(filename,'r')
    animat["forme"]=myfile.read()
    animat["ligne"]=animat["forme"].split("\n")
    animat["hauteur"]=len(animat["ligne"])
    return animat


def getX(m):
    return m['x']
def setX(m,x):
	m['x']=x

def getY(m):
	return m['y']
def setY(m,y):
	m['y']=y

def getColor(m):
	return m['color']
def setColor(m,c):
	m['color']=c
	
def show(animat) : 
    for l in range(0,animat["hauteur"]):
        x=str(int(animat["x"])-1)
        y=str(int(animat["y"])+l)
        txt="\033["+y+";"+x+"H"
        sys.stdout.write(txt)
	
    	#couleur fond noire
        sys.stdout.write("\033[40m")
	
    	#couleur animat
        c=animat["color"]
        txt="\033[3"+str(c%7+1)+"m"
        sys.stdout.write(txt)

    	#affichage de l animat
        sys.stdout.write(animat["ligne"][l])
        sys.stdout.write("\033[37m")
    
def moveRight(animat):
    animat["x"]+=1
    
def moveLeft(animat):
    animat["x"]-=1
    
def changeColor(a):
	a["color"]=a["color"]+1
