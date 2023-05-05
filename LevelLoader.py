import pygame, sys, math
from wall import *

def loadLevel(lev):
    print(lev)
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
        
    tiles = []
    
    scale = 100
    for y, line in enumerate(lines):
        for x, char in enumerate(line): 
            if char == '-':
                tiles += [Wall("wall-horizontal", [x*scale+scale/2, y*scale+scale/2])]
            if char == '|':
                tiles += [Wall("wall-vertical", [x*scale+scale/2, y*scale+scale/2])]
            if char == 'x':
                tiles += [Wall("wall-floor", [500, y*scale+50])]
            if char == 'g':
                tiles += [Wall("wall-goal", [300, y*scale+50])]
            if char == 'b':
                tiles += [Wall("wall-brick", [300, y*scale+50])]
    return tiles
    
    
    
# ~ def loadLevel2(lev):
    # ~ f = open(lev, 'r')
    # ~ lines = f.readlines()
    # ~ f.close()
        
    # ~ tiles = []
    
    # ~ scale = 50
    # ~ for y, line in enumerate(lines):
        # ~ for x, char in enumerate(line):
            # ~ if char == '-':
                # ~ tiles += [Wall("wall1", [x*scale, y*scale])]
                
    
    
    # ~ return tiles

