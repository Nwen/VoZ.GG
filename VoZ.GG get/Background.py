# -*- coding: utf-8 -*-
import sys
import os

def create(filename):
    #creation du fond
    bg=dict()

    #ouverture fichier
    myfile = open(filename, "r")
    bg["str"]=myfile.read()
    myfile.close()
    bg["grid"]=bg['str'].splitlines()
    return bg

def getStr(b):
    return b['str']
def setStr(b,st):
    b['str']=st
    
def getGrid(b):
    return b['grid']
def setV(b,grid):
    b['grid']=grid

def isValid(bg,x,y):
	if y>len(bg['grid'])-1:
		return False
	if x>len(bg['grid'][0])-1:
		return False
	if bg['grid'][y][x]==' ':
		return True
	else:
		return False

def isClimbable(bg,x,y) :
    if bg['grid'][y][x]=='█':
        return True
    else:
        return False
    
def canFall(bg,x,y):
    k,i=0,0
    for i in range(10):
        if bg['grid'][y][x+i]!=' ' and bg['grid'][y][x+i]=='█':
            k+=1
    if k != 0:
        return False
    else :
        return True

    
def show(bg) : 
    #affichage du background
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[40m")
    sys.stdout.write("\033[37m")
    sys.stdout.write(bg["str"])