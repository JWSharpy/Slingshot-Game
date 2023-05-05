import pygame, sys, math, random
from Ball import *    
from LevelLoader import *
from wall import *
from Bottons import *
from TextButton import *
pygame.init() 
pygame.font.init()
clock = pygame.time.Clock();


size = [1000, 1000]
screen = pygame.display.set_mode(size)


mode = "title"
mode = "MainMenu"
lev = 1
backList = ["MainMenu"]
while True:
    #-----START SCREEN------
    if mode == "MainMenu":
        bgImage = pygame.image.load("MainMenu.png").convert()
        bgRect = bgImage.get_rect()
        levelsButton = Button("levels", [200, 250])
        quitButton = Button("quit", [200, 550])
        creditsButton = Button("credits", [200, 450])
        descriptionButton = Button("description", [200, 350])

    while mode == "MainMenu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                levelsButton.hover(event.pos)
                quitButton.hover(event.pos)
                creditsButton.hover(event.pos)
                descriptionButton.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:          
                levelsButton.clickDown(event.pos)
                quitButton.clickDown(event.pos)
                creditsButton.clickDown(event.pos)
                descriptionButton.clickDown(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if levelsButton.clickUp(event.pos):
                    mode = "LevelSelect"
                    backList += ["LevelSelect"]
                if quitButton.clickUp(event.pos):
                    sys.exit()
                if creditsButton.clickUp(event.pos):
                    mode = "Credits"
                    backList += ["Credits"]
                if descriptionButton.clickUp(event.pos):
                    mode = "Description"
                    backList += ["Description"]
        screen.fill((255, 128, 64))
        screen.blit(bgImage, bgRect)
        screen.blit(levelsButton.image, levelsButton.rect)
        screen.blit(quitButton.image, quitButton.rect)
        screen.blit(creditsButton.image, creditsButton.rect)
        screen.blit(descriptionButton.image, descriptionButton.rect)
        pygame.display.flip()
        clock.tick(60)
    
   
   
   
    #-----Credits SCREEN------
    if mode == "Credits":
        bgImage = pygame.image.load("Credits.png").convert()
        bgRect = bgImage.get_rect()
        quitButton = Button("quit", [225, 750])
        backButton = Button("back", [75, 750])
                 
                        
    while mode == "Credits":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                levelsButton.hover(event.pos)
                quitButton.hover(event.pos)
                creditsButton.hover(event.pos)
                descriptionButton.hover(event.pos)
                backButton.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:          
                levelsButton.clickDown(event.pos)
                quitButton.clickDown(event.pos)
                creditsButton.clickDown(event.pos)
                descriptionButton.clickDown(event.pos)
                backButton.clickDown(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if quitButton.clickUp(event.pos):
                    sys.exit()
                if backButton.clickUp(event.pos):
                    backList.remove(backList[-1])
                    mode = backList[-1]
        screen.fill((255, 128, 64))
        screen.blit(bgImage, bgRect)
        screen.blit(quitButton.image, quitButton.rect)
        screen.blit(backButton.image, backButton.rect)
        pygame.display.flip()
        clock.tick(60)



 #-----DESCRIPTION SCREEN------
    if mode == "Description":
        bgImage = pygame.image.load("Description.png").convert()
        bgRect = bgImage.get_rect()
        quitButton = Button("quit", [225, 750])
        backButton = Button("back", [75, 750])  

    while mode == "Description":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                levelsButton.hover(event.pos)
                quitButton.hover(event.pos)
                creditsButton.hover(event.pos)
                descriptionButton.hover(event.pos)
                backButton.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:          
                levelsButton.clickDown(event.pos)
                quitButton.clickDown(event.pos)
                creditsButton.clickDown(event.pos)
                descriptionButton.clickDown(event.pos)
                backButton.clickDown(event.pos)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if quitButton.clickUp(event.pos):
                    sys.exit()
                if backButton.clickUp(event.pos):
                    backList.remove(backList[-1])
                    mode = backList[-1]
        screen.fill((255, 128, 64))
        screen.blit(bgImage, bgRect)
        screen.blit(quitButton.image, quitButton.rect)
        screen.blit(backButton.image, backButton.rect)
        pygame.display.flip()
        clock.tick(60)
                        

#----------Levels-----------

    if mode == "LevelSelect":
        bgImage = pygame.image.load("LevelSelect.png").convert()
        bgRect = bgImage.get_rect()
        quitButton = Button("quit", [800, 900])
        backButton = Button("back", [650, 900]) 
        levelButtons =[]
        x = 200
        y = 200
        for num in range(48):
            levelButtons += [TextButton(str(num+1), [x,y])]
            x+= 100
            if (num+1)%6 == 0:
                y+= 75
                x = 200

    while mode == "LevelSelect":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                levelsButton.hover(event.pos)
                quitButton.hover(event.pos)
                creditsButton.hover(event.pos)
                descriptionButton.hover(event.pos)
                backButton.hover(event.pos)
                
                for lb in levelButtons:
                    lb.hover(event.pos)
                
            if event.type == pygame.MOUSEBUTTONDOWN:          
                levelsButton.clickDown(event.pos)
                quitButton.clickDown(event.pos)
                creditsButton.clickDown(event.pos)
                descriptionButton.clickDown(event.pos)
                backButton.clickDown(event.pos)
                
                for lb in levelButtons:
                    lb.clickDown(event.pos)
               

            if event.type == pygame.MOUSEBUTTONUP:
                if quitButton.clickUp(event.pos):
                    sys.exit()
                
                for lb in levelButtons:
                    if lb.clickUp(event.pos):
                        lev = lb.name
                        print(lev)
                        mode = "game" 
                
                if backButton.clickUp(event.pos):
                    backList.remove(backList[-1])
                    mode = backList[-1]
                
                
        screen.fill((255, 128, 64))
        screen.blit(bgImage, bgRect)
        screen.blit(quitButton.image, quitButton.rect)
        screen.blit(backButton.image, backButton.rect)
        for lb in levelButtons:
            screen.blit(lb.image, lb.rect)
        pygame.display.flip()
        clock.tick(60)

    
    
    #-----GAME------
    ball=Ball(1,350,[1000/2,1000/2])
    walls = loadLevel("Level/"+str(lev)+".lvl")
    
    while mode == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            if event.type==pygame.MOUSEBUTTONDOWN:
                ball.go(event.pos)
        
        ball.update(size)
        
        
        for wall in walls:
            ball.wallCollide(wall)
        
        screen.fill((64, 128, 255))
        screen.blit(ball.image, ball.rect)
        for wall in walls:
            screen.blit(wall.image, wall.rect)
            screen.blit(wall.image, wall.rect)
        
        pygame.display.flip()
        clock.tick(60)



