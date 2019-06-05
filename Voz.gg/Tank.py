# -*- coding: utf-8 -*-
import sys
import os
import random
import Background

#le module Tank gere le type abstrait de donnee Tank

def createTank(posx,posy,filename):
    
    #creation monster
    t=dict()
    t["color"]=1
    t["x"]=posx
    t["y"]=posy
    myfile=open(filename,'r')
    t["forme"]=myfile.read()
    t["ligne"]=t["forme"].split("\n")
    t["hauteur"]=len(t["ligne"])
    t["v"]=2.0
    return t


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
    
def show(t) : 
    for l in range(0,t["hauteur"]):
        x=str(int(t["x"])-1)
        y=str(int(t["y"])+l)
        txt="\033["+y+";"+x+"H"
        sys.stdout.write(txt)
    
        #couleur fond noire
        sys.stdout.write("\033[40m")
    
        #couleur t
        c=t["color"]
        txt="\033[3"+str(c%7+1)+"m"
        sys.stdout.write(txt)

        #affichage de l t
        sys.stdout.write(t["ligne"][l])
        sys.stdout.write("\033[37m")
    
def moveRight(t):
    t["x"]+=1
    
def moveLeft(t):
    t["x"]-=1
    
def moveUpRight(t):
    t["x"]+=2
    t["y"]-=1
    
def moveUpLeft(t):
    t["x"]-=2
    t["y"]-=1
    
def moveDownRight(t):
    t["x"]+=2
    t["y"]+=1
def moveDownLeft(t):
    t["x"]-=2
    t["y"]+=1
def changeColor(a):
    a["color"]=a["color"]+1

def PowerUp(tank):
    tank["v"]+=0.1
    
def PowerDown(tank):
    tank["v"]-=0.1