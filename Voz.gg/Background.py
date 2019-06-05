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
    if y>len(bg['grid'])-1:
        return False
    if x>len(bg['grid'][0])-1:
        return False
    if bg['grid'][y][x]=='█':
        return True
    else:
        return False
    
def canFall(bg,x,y):
    for i in range(12):
        if bg['grid'][y+i][x+i]==' ' and bg['grid'][y+i][x+i]!='█':
            return True
        else:
            return False
        i+=1

    
def show(bg) : 

    
    #goto
    sys.stdout.write("\033[1;1H")
        
    #couleur fond
    sys.stdout.write("\033[40m")
    
    #couleur white
    sys.stdout.write("\033[37m")
    
    #affiche
    sys.stdout.write(bg["str"])



    
