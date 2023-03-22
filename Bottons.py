import pygame, sys, math


class Button():
    def __init__(self, name, startPos=[0, 0], path="Buttons/"):
        self.baseImage = pygame.image.load(path + name+"Button.png").convert()
        self.hoverImage = pygame.image.load(path + "hoverButton.png").convert()
        self.clickedImage = pygame.image.load(path + "clickedButton.png").convert()
        self.image = self.baseImage
        self.rect = self.image.get_rect(topleft=startPos)
        self.clicked = False

    def hover(self, mousePos):
        if (self.rect.left < mousePos[0] < self.rect.right and
                self.rect.top < mousePos[1] < self.rect.bottom and
                not self.clicked):
            self.image = self.hoverImage
        else:
            self.image = self.baseImage

    def clickDown(self, mousePos):
        if self.rect.left < mousePos[0] < self.rect.right:
            if self.rect.top < mousePos[1] < self.rect.bottom:
                self.image = self.clickedImage
                self.clicked = True
                return True
        self.clicked = False
        return False

    def clickUp(self, mousePos):
        if self.rect.left < mousePos[0] < self.rect.right:
            if self.rect.top < mousePos[1] < self.rect.bottom:
                self.image = self.clickedImage
                self.clicked = True
                return True
        self.clicked = False
        return False

    def reset(self):
        self.image = self.baseImage
        self.clicked = False
        








# ~ FROM https://github.com/KRHS-Game-Programming-2022/Rhythm-Smash/blob/master/Button.py
