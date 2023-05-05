import pygame, sys, math

class Wall():
    def __init__(self, image, pos=[0,0]):
        self.image = pygame.image.load("ball/" + image + ".png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "wall"
        self.hardness = .7

    def update(self, size):
        pass

    
