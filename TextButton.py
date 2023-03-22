import pygame, sys, math, random

class TextButton():
    def __init__(self, name, startPos=[0, 0], bgColor=None, textColor=None):
        if bgColor == None:
            bgColor = [random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        if textColor == None:
            textColor = [random.randint(175,255),random.randint(175,255),random.randint(175,255)]
            
        self.baseImage = pygame.Surface([82,68])
        self.baseImage.fill(bgColor)
                    
        self.font = pygame.font.Font(None, 64)
        self.baseText = self.font.render(name+".)", True, textColor)
        self.textpos = self.baseText.get_rect(centerx=self.baseImage.get_width() / 2, y=10)
        self.baseImage.blit(self.baseText, self.textpos)
        
        self.hoverImage = pygame.Surface([82,68])
        self.hoverImage.fill(textColor)
        self.hoverText = self.font.render(name+".)", True, bgColor)
        self.hoverImage.blit(self.hoverText, self.textpos)
        
        self.clickedImage = pygame.Surface([82,68])
        self.clickedImage.fill((0,0,0))
        self.clickedText = self.font.render(name+".)", True, bgColor)
        self.clickedImage.blit(self.clickedText, self.textpos)
        
        
        self.rect = pygame.Rect(startPos, [82,68])
        self.image = self.baseImage
        
        self.clicked = False
        self.name = name
        
        
    def hover(self, mousePos):
        print(self.rect, mousePos)
        if (self.rect.left < mousePos[0] < self.rect.right and
                self.rect.top < mousePos[1] < self.rect.bottom):
            print("hovered")
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
            
            
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    size = [1000, 1000]
    screen = pygame.display.set_mode(size)
    
    b = TextButton("48.)", [100,100])
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                b.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:          
                b.clickDown(event.pos)
                
        screen.fill((255, 128, 64))
        screen.blit(b.image, b.rect)
        pygame.display.flip()
