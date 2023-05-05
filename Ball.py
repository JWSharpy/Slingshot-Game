import pygame, math

class Ball():
    def __init__(self, speed=0, angle=0, startPos=[50,50]):
        self.image = pygame.image.load("ball/ball5.png")
        self.rect = self.image.get_rect(center=startPos)
        
        self.angle=angle
        self.vel=speed
        self.veloffset=10
        self.velscale = 100
        self.speedx = math.cos(math.radians(self.angle))*self.vel
        self.speedy = -math.sin(math.radians(self.angle))*self.vel
        self.speed = [self.speedx, self.speedy]
        
        self.posx= startPos[0]
        self.posy= startPos[1]
        self.pos = [self.posx, self.posy]
        
        self.didBounceX = False 
        self.didBounceY = False
        
        self.gravity=.4
        self.atBottom = False
        
    def go(self, pos):
        xdiff=pos[0]-self.rect.centerx
        ydiff=pos[1]-self.rect.centery
        mouseangle=-math.degrees(math.atan2(ydiff, xdiff))
        if mouseangle<0:
            mouseangle+=360
        self.angle=mouseangle
        
        dis=math.dist(pos,self.rect.center)
        
        self.vel=(dis/self.velscale)**(1/2)+10
        print(dis, self.vel)
        self.speedx = math.cos(math.radians(self.angle))*self.vel
        self.speedy = -math.sin(math.radians(self.angle))*self.vel
        if self.atBottom:
            self.speedy += 5
        self.speed = [self.speedx, self.speedy]
        print(self.vel,self.speed)
        self.move()
        
    def update(self, size):
        self.speedy+=self.gravity
        self.didBounceX = False 
        self.didBounceY = False 
        
        self.atBottom = False
        
        self.move()
        self.screenCollide(size)

    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.posx+= self.speedx
        self.posy+= self.speedy
        self.pos = [self.posx, self.posy]
        
        self.rect.center = [int(self.posx), int(self.posy)]
        
    def didCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        return True
        return False
        
    def wallCollide(self, other):
        if self.didCollide(other):
            if self.rect.centery < other.rect.centery: # above halfway
                ydiff = self.rect.bottom - other.rect.top
                if self.rect.centerx < other.rect.centerx: # left of halfway
                    xdiff = self.rect.right - other.rect.left
                else:                                      # right of halfway
                    xdiff = other.rect.right - self.rect.left
            else:                                      # below halfway
                ydiff = other.rect.bottom - self.rect.top
                if self.rect.centerx < other.rect.centerx: # left of halfway
                    xdiff = self.rect.right - other.rect.left
                else:                                      # right of halfway
                    xdiff = other.rect.right - self.rect.left

            if xdiff < ydiff:      #side colision
                self.speedx = -self.speedx*other.hardness
                self.didBounceX = True 
                while self.didCollide(other):
                    print(self.rect, other.rect)
                    self.move()
            else:
                if self.rect.centery > other.rect.centery:  #top colision
                    self.speedy = -self.speedy*other.hardness
                    self.didBounceY = True 
                else:
                    self.speedy = -self.speedy*other.hardness
                    self.didBounceY = True 
                    self.move()
                    if self.rect.bottom > other.rect.top:
                        self.rect.bottom=other.rect.top
                        self.atBottom = True
        return False
        
        
    def screenCollide(self, size):
        width = size[0]
        height = size[1]
        hardness=.8
        if not self.didBounceY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy*hardness
                self.didBounceY = True 
                self.move()
                if self.rect.bottom > height:
                    self.rect.bottom=height
                    self.atBottom = True
                
            if self.rect.top < 0:
                self.speedy = -self.speedy*hardness
                self.didBounceY = True 
        if not self.didBounceX:
            if self.rect.right > width:
                self.speedx = -self.speedx*hardness
                self.didBounceX = True 
            if self.rect.left < 0:
                self.speedx = -self.speedx*hardness
                self.didBounceX = True 


