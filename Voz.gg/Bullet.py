# -*- coding: utf-8 -*-
import sys
import os

import math

def createBullet(posX,posY):
    B=dict()
    B["x"]=posX
    B["y"]=posY
    B["color"]=2
    return B

def show(a) : 
    
    #on se place a la position de l ball dans le terminal
    x=str(int(a["x"]))
    y=str(int(a["y"]))
    txt="\033["+y+";"+x+"H"
    sys.stdout.write(txt)
    
    #couleur fond noire
    sys.stdout.write("\033[40m")
    
    #couleur ball
    c=a["color"]
    txt="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(txt)

    #affichage de l ball : le caractere affiche est +
    cara = "O"
    sys.stdout.write(cara)
    
def shoot(b,v,alpha,t,p):
    t= t+1.0
    h=math.cos((math.pi)/4)*5.0*t
    b["x"]+=int(h)
    p=-0.5*t*t*1+math.sin((math.pi)/4)*5.0*t
    b["y"]-=int(p)