# -*- coding: utf-8 -*-
import sys
import os
import random
import Background

def init(pos,c,imgfile) :
    t=dict()
    t["color"]=c
    t["pos"]=pos
    
    img = open(imgfile, "r")
    t["img"]=img.read()
    img.close()
    t["grid"]=t["str"].splitlines()
    
    return t

def getX(t):
	return t["pos"][0]
def setX(t,x):
	t["pos"][0]=x

def getY(t):
	return t["pos"][1]
def setY(t,y):
	t["pos"][1]=y

def getColor(t):
	return t["color"]
def setColor(t,c):
	t["color"]=c
    
def show(t) : 
    
    #couleur du fond
    sys.stdout.write("\033[40m")
    
    c=t["color"]
    txt="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(txt)

    #affichage du tank pour chaque ligne
    for j in range(len(t["img"])):
        for i in range(len(t["img"][j])):
            x=str(int(t["x"]+i))
            y=str(int(t["y"]+j))
            txt="\033["+y+";"+x+"H"
            sys.stdout.write(txt)
            sys.stdout.write(t["img"][j][i])