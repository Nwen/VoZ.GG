# -*- coding: utf-8 -*-
import sys
import os

import math
import Tank
import Background

def createBullet(posX,posY,dmg):
    #création de la balle
    B=dict()
    B["x"]=posX
    B["y"]=posY
    B["color"]=2
    B["t"]=0
    B["p"]=0.0
    B["h"]=0.0
    B["dmg"]=dmg
    return B

def getX(b):
    return b['x']
def setX(b,x):
    b['x']=x
    
def getY(b):
    return b['y']
def setY(b,y):
    b['y']=y
    
def getColor(b):
    return b['color']
def setColor(b,c):
    b['color']=c
    
def getT(b):
    return b['t']
def setT(b,t):
    b['t']=t
    
def getP(b):
    return b['p']
def setP(b,p):
    b['p']=p
    
def getH(b):
    return b['h']
def setH(b,h):
    b['h']=h
    
def getDmg(b):
    return b['dmg']
def setDmg(b,d):
    b['dmg']=d
    

def show(a) : 
    
    #on se place a la position de la ball dans le terminal
    x=str(int(a["x"]))
    y=str(int(a["y"]))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)
    
    #couleur du fond
    sys.stdout.write("\033[40m")
    
    #couleur de la balle
    c=a["color"]
    txt="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(txt)

    #affichage de la balle : le caractere affiche est 0
    cara = "O"
    sys.stdout.write(cara)
    
def shoot(b,t,sens):
    #calcul de la position de la balle pour faire une trajectoire parabolique
    b["t"]+= 0.1
    b["h"]=sens*math.cos(math.radians(Tank.getAngle(t)))*Tank.getV(t)*b["t"]
    b["x"]+=math.ceil(b["h"])
    b["p"]=-0.5*b["t"]*b["t"]*1.5+math.sin(math.radians(Tank.getAngle(t)))*Tank.getV(t)*b["t"]
    b["y"]-=math.ceil(b["p"])
    
def collide(bg,b,shooter,target):
    #test de colision avec la balle
    x = b["x"]
    y = b["y"]
    i,j=0,0
    if Background.isValid(bg,x,y):
        if Background.getGrid(bg)[y][x]=='█':
            shooter["isShooting"]=False
            #détruire balle
        for i in range(4):
            for j in range(14):
                if x == target["x"]+j and y == target["y"]+i :
                    target["PV"]-=b["dmg"]#si la balle touche, on inflige des dégats
    else :
        shooter["isShooting"]=False