# -*- coding: utf-8 -*-

import os
import sys

def createFin(filename):
    fin=dict()

    #ouverture fichier
    myfile = open(filename, "r")
    fin["str"]=myfile.read()
    myfile.close()
    fin["grid"]=fin['str'].splitlines()
    fin["on"]=False
    return fin

def show(fin) : 

    
    #goto
    sys.stdout.write("\033[1;1H")
        
    #couleur fond
    sys.stdout.write("\033[40m")
    
    #couleur white
    sys.stdout.write("\033[37m")
    
    #affiche
    sys.stdout.write(fin["str"])
    
def FinOn(fin):
    fin["on"]=True