# -*- coding: utf-8 -*-

import os
import sys

def createMenu(filename):
    menu=dict()

    #ouverture fichier
    myfile = open(filename, "r")
    menu["str"]=myfile.read()
    myfile.close()
    menu["grid"]=menu['str'].splitlines()
    menu["on"]=True
    return menu

def show(menu) : 

    
    #goto
    sys.stdout.write("\033[1;1H")
        
    #couleur fond
    sys.stdout.write("\033[40m")
    
    #couleur white
    sys.stdout.write("\033[37m")
    
    #affiche
    sys.stdout.write(menu["str"])
    
def MenuOff(menu):
    menu["on"]=False