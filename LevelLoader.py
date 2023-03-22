import pygame, sys, math
from wall import *

def loadLevel(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
        
    tiles = []
    
    scale = 50
    for y, line in enumerate(lines):
        for x, char in enumerate(line): 
            if char == '-':
                tiles += [Wall("wall1", [x*scale, y*scale])]
                tiles += [Wall("wall2", [x*scale, y*scale])]
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

