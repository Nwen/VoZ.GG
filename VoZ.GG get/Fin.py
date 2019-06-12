# -*- coding: utf-8 -*-
import os
import sys

def createFin(filename):
    #création de l'écran de fin
    fin=dict()

    #ouverture fichier
    myfile = open(filename, "r")
    fin["str"]=myfile.read()
    myfile.close()
    fin["grid"]=fin['str'].splitlines()
    fin["on"]=False
    return fin

def getStr(f):
    return f["str"]
def getGrid(f):
    return f['grid']
def getOn(f):
    return f['on']

def setStr(f,st):
    f['str']=st
def setGrid(f,g):
    f['grid']=g
def setOn(f,on):
    f['on']=on

def show(fin) :
    #affichage de l'écran de fin

    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[40m")
    sys.stdout.write("\033[37m")
    sys.stdout.write(fin["str"])
    
def FinOn(fin):
    fin["on"]=True