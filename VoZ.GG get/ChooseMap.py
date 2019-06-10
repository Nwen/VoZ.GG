# -*- coding: utf-8 -*-

import os
import sys

def createChoix(filename):
    choix=dict()

    #ouverture fichier
    myfile = open(filename, "r")
    choix["str"]=myfile.read()
    myfile.close()
    choix["grid"]=choix['str'].splitlines()
    choix["on"]=False
    return choix

def getStr(m):
    return m["str"]
def getGrid(m):
    return m["grid"]
def getOn(m):
    return m["on"]

def setStr(m,st):
    m["str"]=st
def setGrid(m,g):
    m["grid"]=g
def setOn(m,on):
    m["on"]=on

def show(choix) : 

    
    #goto
    sys.stdout.write("\033[1;1H")
        
    #couleur fond
    sys.stdout.write("\033[40m")
    
    #couleur white
    sys.stdout.write("\033[37m")
    
    #affiche
    sys.stdout.write(choix["str"])
    
def ChoixOn(choix):
    choix["on"]=True

def ChoixOff(choix):
    choix["on"]=False