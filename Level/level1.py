import pygame, sys, math
from wall import *

def Level(lev):
    f = open(lev, 'r')
    line = f.readlines()
    f.close()
    
    print(line)
    
Level("Level/1.lvl")

