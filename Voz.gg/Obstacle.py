
import sys
import os
import random
import Background

#le module Obstacle implemente le type abstrait de donnees Obstacle
#un obstacle un objet immobile avec une representation ASCII carree ('img')de cote 'size' 

def create(color,rangeX,rangeY,img=[['O']],size=1):
    
    #creation monster
    o=dict()
    o["color"]=color
    o["x"]=random.randint(2,rangeX)
    o["y"]=random.randint(2,rangeY)
    o['img']=img
    o['size']=size

    return o

def getX(o):
    return o['x']
def getY(o):
    return o['y']
def setX(o,x):
    o['x']=x
def setY(o,y):
    o['y']=y

def getColor(o):
    return o['color']
def setColor(o,c):
    o['color']=c

def getImg(o):
    return o['img']
def setImg(o,i):
    o['img']=i

def getSize(o):
    return o['size']
def setSize(o,size):
    o['size']=size

def show(a) : 
    
    #couleur fond noire
    sys.stdout.write("\033[40m")
    
    #couleur racket
    c=a["color"]
    txt="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(txt)

    #affichage de l obstacle
    #pour chaque ligne de l'image
    for j in range(len(a['img'])):
        for i in range(len(a['img'][j])):
            x=str(int(a["x"]+i))
            y=str(int(a["y"]+j))
            txt="\033["+y+";"+x+"H"
            sys.stdout.write(txt)
            sys.stdout.write(a['img'][j][i])
        
def changeColor(o):
    o["color"]=o["color"]+1

def testCollision(o,x,y):
    x=int(x)
    y=int(y)
    if o['x'] <= x  and x < o['x']+o['size'] :
        if o['y'] <= y  and y < o['y']+o['size'] :
            print o['size'],  y-o['y'],x-o['x']
            if o['img'][y-o['y']][x-o['x']]!=' ':
                return True
    return False


