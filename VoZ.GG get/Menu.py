# -*- coding: utf-8 -*-

import os
import sys

def createMenu(filename):
    #création menu
    menu=dict()

    #ouverture fichier
    myfile = open(filename, "r")
    menu["str"]=myfile.read()
    myfile.close()
    menu["grid"]=menu['str'].splitlines()
    menu["on"]=True
    return menu

def getStr(m):
    return m["str"]
def getGrid(m):
    return m['grid']
def getOn(m):
    return m['on']

def setStr(m,st):
    m['str']=st
def setGrid(m,g):
    m['grid']=g
def setOn(m,on):
    m['on']=on
    
def show(menu) : 
    #affichage menu

    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[40m")
    sys.stdout.write("\033[37m")
    sys.stdout.write(menu["str"])
    
def MenuOff(menu):
    setOn(menu,False)