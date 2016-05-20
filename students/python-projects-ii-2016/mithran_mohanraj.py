#IMPORTANT!
#Code of Mithran's Calculator. All contents of program is owned by Mithran
#Mohanraj (Excluding python and pygame script). Pictures must be in same folder
#as python program. Pygame must also be downloaded onto machine running this
#script. (c) 2016 Mithran Mohanraj
#-
#Import and Initiate pygame
import pygame
pygame.init()
#Variable Declaration.
from pygame.locals import*
calculatorskin = pygame.image.load('skin.png')
from pygame.locals import*
calculatoricon = pygame.image.load('icon.png')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PI = 3.141592653
mathProblem = []
mathProblem2 = []
mousePos = [0,0]
finishedmath = ''
finishedmath2 = ''
previousmath = ''
finalmath = ''
finalProblem = []
finalfont = 22
size = (400, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_icon(calculatoricon)
pygame.display.set_caption("Mithran's Calculator")
 
done = False
clock = pygame.time.Clock()

while not done:
    #Check for any event on computer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #Check for any keys pushed down
        if event.type == pygame.KEYDOWN:
            if event.key == K_KP1:
                if 16 >= len(mathProblem):
                    mathProblem.append("1")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("1")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP2:
                if 16 >= len(mathProblem):
                    mathProblem.append("2")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("2")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP3:
                if 16 >= len(mathProblem):
                    mathProblem.append("3")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("3")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP4:
                if 16 >= len(mathProblem):
                    mathProblem.append("4")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("4")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP5:
                if 16 >= len(mathProblem):
                    mathProblem.append("5")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("5")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP6:
                if 16 >= len(mathProblem):
                    mathProblem.append("6")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("6")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP7:
                if 16 >= len(mathProblem):
                    mathProblem.append("7")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("7")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP8:
                if 16 >= len(mathProblem):
                    mathProblem.append("8")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("8")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP9:
                if 16 >= len(mathProblem):
                    mathProblem.append("9")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("9")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP0:
                if 16 >= len(mathProblem):
                    mathProblem.append("0")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("0")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)                
            if event.key == K_KP_PERIOD:
                if 16 >= len(mathProblem):
                    mathProblem.append(".")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append(".")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP_DIVIDE:
                if 16 >= len(mathProblem):
                    mathProblem.append("/")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("/")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP_MULTIPLY:
                if 16 >= len(mathProblem):
                    mathProblem.append("*")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("*")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP_MINUS:
                if 16 >= len(mathProblem):
                    mathProblem.append("-")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("-")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP_PLUS:
                if 16 >= len(mathProblem):
                    mathProblem.append("+")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("+")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
            if event.key == K_KP_ENTER:
                finalProblem = mathProblem + mathProblem2
                #if finalProblem contains '^':
                #replace '^' with '**'
                finalinterval = 0
                for pos in finalProblem:
                    boolcheck = (pos == '^')
                    if (boolcheck):
                        finalProblem[finalinterval] = '**'
                    finalinterval = finalinterval + 1
                finalmath = ''.join(finalProblem)
                try:
                    finalmath = str(eval(finalmath))
                    finalfont = 22
                    if len(finalmath) >= 21:
                        finalfont = 16
                except:
                    finalmath = 'Error'
                if mathProblem == []:
                    finalmath = previousmath
                previousmath = finalmath
                finishedmath = ''
                finishedmath2 = ''
                print(finishedmath)
                print(finalmath)
                mathProblem = []
                print(mathProblem)
        #Mouse section below. Keyboard section above.
        if event.type == pygame.MOUSEBUTTONDOWN:
            #The max character count should be 20
            if (60 <= mousePosX <= 140) and (150 <= mousePosY <= 200):
                if 16 >= len(mathProblem):
                    mathProblem.append("1")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("1")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (160 <= mousePosX <= 240) and (150 <= mousePosY <= 200):
                if 16 >= len(mathProblem):
                    mathProblem.append("2")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("2")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (260 <= mousePosX <= 340) and (150 <= mousePosY <= 200):
                if 16 >= len(mathProblem):
                    mathProblem.append("3")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("3")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (60 <= mousePosX <= 140) and (220 <= mousePosY <= 270):
                if 16 >= len(mathProblem):
                    mathProblem.append("4")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("4")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (160 <= mousePosX <= 240) and (220 <= mousePosY <= 270):
                if 16 >= len(mathProblem):
                    mathProblem.append("5")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("5")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (260 <= mousePosX <= 340) and (220 <= mousePosY <= 270):
                if 16 >= len(mathProblem):
                    mathProblem.append("6")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("6")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (60 <= mousePosX <= 140) and (290 <= mousePosY <= 340):
                if 16 >= len(mathProblem):
                    mathProblem.append("7")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("7")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (160 <= mousePosX <= 240) and (290 <= mousePosY <= 340):
                if 16 >= len(mathProblem):
                    mathProblem.append("8")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("8")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (260 <= mousePosX <= 340) and (290 <= mousePosY <= 340):
                if 16 >= len(mathProblem):
                    mathProblem.append("9")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("9")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (60 <= mousePosX <= 140) and (360 <= mousePosY <= 410):
                if 16 >= len(mathProblem):
                    mathProblem.append("0")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("0")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (160 <= mousePosX <= 240) and (360 <= mousePosY <= 410):
                if 16 >= len(mathProblem):
                    mathProblem.append("+")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("+")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (260 <= mousePosX <= 340) and (360 <= mousePosY <= 410):
                if 16 >= len(mathProblem):
                    mathProblem.append("-")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("-")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (60 <= mousePosX <= 140) and (430 <= mousePosY <= 510):
                mathProblem = []
                finishedmath = ''
                mathProblem2 = []
                finishedmath2 = ''
                finalmath = ''
                finalProblem = []
                print(mathProblem)
            if (160 <= mousePosX <= 240) and (430 <= mousePosY <= 480):
                if 16 >= len(mathProblem):
                    mathProblem.append("*")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("*")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (260 <= mousePosX <= 340) and (430 <= mousePosY <= 480):
                if 16 >= len(mathProblem):
                    mathProblem.append("/")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("/")
                finishedmath2 = ''.join(mathProblem2) 
                finishedmath = ''.join(mathProblem)
            if (260 <= mousePosX <= 340) and (490 <= mousePosY <= 540):
                if 16 >= len(mathProblem):
                    mathProblem.append(".")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append(".")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)
            if (160 <= mousePosX <= 240) and (490 <= mousePosY <= 540):
                if 16 >= len(mathProblem):
                    mathProblem.append("^")
                elif 16 >= len(mathProblem2):
                    mathProblem2.append("^")
                finishedmath2 = ''.join(mathProblem2)
                finishedmath = ''.join(mathProblem)
                print(mathProblem)                
            if (160 <= mousePosX <= 340) and (550 <= mousePosY <= 580):
                finalProblem = mathProblem + mathProblem2
                #if finalProblem contains '^':
                #replace '^' with '**'
                finalinterval = 0
                for pos in finalProblem:
                    boolcheck = (pos == '^')
                    if (boolcheck):
                        finalProblem[finalinterval] = '**'
                    finalinterval = finalinterval + 1
                finalmath = ''.join(finalProblem)
                try:
                    finalmath = str(eval(finalmath))
                    finalfont = 22
                    if len(finalmath) >= 21:
                        finalfont = 16
                except:
                    finalmath = 'Error'
                if mathProblem == []:
                    finalmath = previousmath
                previousmath = finalmath
                finishedmath = ''
                finishedmath2 = ''
                print(finishedmath)
                print(finalmath)
                mathProblem = []
                print(mathProblem)
            
    #Game Code
    mousePosX, mousePosY = pygame.mouse.get_pos()
    #Drawing Code
    screen.fill(BLACK)
    screen.blit(calculatorskin, [0,0])
    if finishedmath != '' and finalmath != '':
        finalmath = ''
    font = pygame.font.SysFont('Bauhaus 93', 22, False, True)
    font2 = pygame.font.SysFont('Bauhaus 93', finalfont, False, True)
    displayt = font.render((finishedmath), True, BLACK)
    screen.blit(displayt, [70, 50])
    displayt2 = font.render((finishedmath2), True, BLACK)
    screen.blit(displayt2, [70, 70])
    displayt3 = font2.render((finalmath), True, BLACK)
    screen.blit(displayt3, [70, 50])    
    pygame.display.flip()
    clock.tick(60)
#Quit
pygame.quit()