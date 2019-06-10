# -*- coding: utf-8 -*-
import sys
import os
import random
import Background

#le module Tank gere le type abstrait de donnee Tank

def createTank(posx,posy,filename,isPlaying):
    
    #creation tank
    t=dict()
    t["color"]=1
    t["x"]=posx
    t["y"]=posy
    t["PV"]=25
    myfile=open(filename,'r')
    t["forme"]=myfile.read()
    t["ligne"]=t["forme"].split("\n")
    t["hauteur"]=len(t["ligne"])
    t["v"]=2.0
    t["isShooting"]=False
    t["isPlaying"]=isPlaying
    t["angle"]=45
    return t


def getX(t):
    return t['x']
def setX(t,x):
    t['x']=x

def getY(t):
    return t['y']
def setY(t,y):
    t['y']=y

def getColor(t):
    return t['color']
def setColor(t,c):
    t['color']=c
    
def getPV(t):
    return t['PV']
def setPV(t,pv):
    t['PV']=pv
    
def getV(t):
    return t['v']
def setV(t,v):
    t['v']=v
    
def getIsShooting(t):
    return t["isShooting"]
def setIsShooting(t,isShooting):
    t['isShooting']=isShooting
    
def getIsPlaying(t):
    return t["isPlaying"]
def setIsPlaying(t,isPlaying):
    t['isPlaying']=isPlaying
    
def getAngle(t):
    return t['angle']
def setAngle(t,angle):
    t['angle']=angle
    
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
    
def AngleUp(tank):
    tank["angle"]+=1
    
def AngleDown(tank):
    tank["angle"]-=1