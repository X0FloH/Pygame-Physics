import pygame
import sys
from time import sleep

pygame.init()

play = True

white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

purple = (255, 0, 255)

gravityPull = 0.5
gravityCurrent = 0

xCurrent = 0

jumps = 0
maxJumps = 2

ypos = 100
xpos = 400

touchingObst = 0

startingXPos = [100, 100, 100, 100]
startingYPos = [200, 200, 100, 100]

level1Door = [800, 00, 100, 900]
level2Obstacle = [400, 700, 150, 100]
level3Obstacle = [400, 700, 150, 100]
level4Obstacle = [400, 700, 150, 100]

level = 1

upperLevel = 0

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jumps < maxJumps:
                    gravityCurrent = -15
                    jumps = jumps + 1
            if event.key == pygame.K_LEFT and touchingObst == 0:
                xCurrent = -15
            if event.key == pygame.K_RIGHT and touchingObst == 0:
                xCurrent = 15
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
    gravityCurrent = gravityCurrent + gravityPull
    if xCurrent > 0:
        xCurrent = xCurrent - 0.5
    if xCurrent < 0:
        xCurrent = xCurrent + 0.5
    ypos = ypos + gravityCurrent
    xpos = xpos + xCurrent
    if upperLevel == 0:
        if xpos > 950:
            xpos = 950
        if xpos < 000:
            xpos = 000
        if ypos > 750:
            ypos = 751
            gravityCurrent = 0
            jumps = 0
        if level == 4:
            if ypos < 50:
                upperLevel = 1
                ypos = 749
    else:
        if xpos > 950:
            xpos = 950
        if xpos < 000:
            xpos = 000
        if ypos > 750:
            upperLevel = 0
            ypos = 51
        if ypos < 20:
            ypos = 21
            gravityCurrent = 0
    if xpos > (level1Door[0] - (level1Door[2] / 2)) and xpos < (level1Door[0] + (level1Door[2] / 2)) and upperLevel == 0:
        level = level + 1
        jumps = 0
        xCurrent = 0
        gravityCurrent = 0
        if level == 2:
            xpos = startingXPos[1]
            ypos = startingYPos[1]
        if level == 3:
            xpos = startingXPos[2]
            ypos = startingYPos[2]
        if level == 4:
            xpos = startingXPos[3]
            ypos = startingYPos[3]
    if level == 2:
        if xpos > (level2Obstacle[0] - (level2Obstacle[2] / 2)) and xpos < (level2Obstacle[0] + (level2Obstacle[2] / 2)):
            if xpos > (level2Obstacle[0] - (level2Obstacle[2] / 2)) and ypos > (level2Obstacle[1] - (level2Obstacle[3] / 2)) and not xpos > (level2Obstacle[0] + (level2Obstacle[2] / 2)):
                touchingObst = 1
                xCurrent = 0
                xpos = xpos - 3
        else:
            touchingObst = 0
    if level == 3:
        if xpos > (level3Obstacle[0] - (level3Obstacle[2] / 2)) and xpos < (level3Obstacle[0] + (level3Obstacle[2] / 2)):
            if xpos > (level3Obstacle[0] - (level3Obstacle[2] / 2)) and ypos > (level3Obstacle[1] - (level3Obstacle[3] / 2)) and not xpos > (level3Obstacle[0] + (level3Obstacle[2] / 2)):
                xpos = level1Door[0]
                level = 2
    if level == 4:
        if xpos > (level4Obstacle[0] - (level4Obstacle[2] / 2)) and xpos < (level4Obstacle[0] + (level4Obstacle[2] / 2)):
            if xpos > (level4Obstacle[0] - (level4Obstacle[2] / 2)) and ypos > (level3Obstacle[1] - (level4Obstacle[3] / 2)) and not xpos > (level4Obstacle[0] + (level4Obstacle[2] / 2)):
                if upperLevel == 0:
                    gravityCurrent = -40
    gameDisplay = pygame.display.set_mode((1000, 800), 0, 32)
    if upperLevel == 0:
        pygame.display.set_caption('Python Physics Platformer - Level ' + str(level))
    else:
        pygame.display.set_caption('Python Physics Platformer - Level ' + str(level) + ' - Upper Level')
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, red, (xpos, ypos, 50, 50))
    pygame.font.init()
    if level == 1:
        pygame.draw.rect(gameDisplay, green, level1Door)
        myFont = pygame.font.SysFont('Futura PT Light', 60)
        textsurface = myFont.render('The Green block is a door', False, black)
        gameDisplay.blit(textsurface, (200, 700))
    if level == 2:
        myFont = pygame.font.SysFont('Avenir Light', 50)
        textsurface = myFont.render('The purple block is a Conveyor', False, purple)
        gameDisplay.blit(textsurface, (100, 100))
        pygame.draw.rect(gameDisplay, purple, level2Obstacle)
        pygame.draw.rect(gameDisplay, green, level1Door)
    if level == 3 and upperLevel == 0:
        pygame.draw.rect(gameDisplay, green, level1Door)
        pygame.draw.rect(gameDisplay, red, level3Obstacle)
        myFont = pygame.font.SysFont('Avenir Light', 50)
        textsurface = myFont.render('The red block will kill you', False, purple)
        gameDisplay.blit(textsurface, (100, 100))
    if level == 4 and upperLevel == 0:
        pygame.draw.rect(gameDisplay, blue, level4Obstacle)
        pygame.draw.rect(gameDisplay, green, level1Door)
        myFont = pygame.font.SysFont('Avenir Light', 70)
        textsurface = myFont.render('Blue bounces you up', False, purple)
        gameDisplay.blit(textsurface, (100, 100))
    if level == 4 and upperLevel == 1:
        myFont = pygame.font.SysFont('Avenir Light', 70)
        textsurface = myFont.render('This is the upper Level', False, purple)
        gameDisplay.blit(textsurface, (100, 100))
    pygame.display.update()
    sleep(0.01)
    
    
    
