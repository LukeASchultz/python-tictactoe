import pygame, sys, time
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Tic Tac Toe')

x = False
playing = True

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]
boardPos = [[50, 50], [150, 50], [250, 50],
            [50, 150], [150, 150], [250, 150],
            [50, 250], [150, 250], [250, 250]]

def drawX(xpos, ypos):
    pygame.draw.line(DISPLAYSURF, (255, 155, 0), (xpos - 50, ypos - 50), (xpos + 50, ypos + 50))
    pygame.draw.line(DISPLAYSURF, (255, 155, 0), (xpos + 50, ypos - 50), (xpos - 50, ypos + 50))

def drawCir(xpos, ypos):
    pygame.draw.circle(DISPLAYSURF, (0, 50, 255), (xpos, ypos), 50, 0)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (xpos, ypos), 49, 0)

def winCheck():
    if ((board[0] > 0) and(board[0] == board[1]) and (board[0] == board[2])):
        win(board[0])
    elif ((board[3] > 0) and(board[3] == board[4]) and (board[3] == board[5])):
        win(board[3])
    elif ((board[6] > 0) and(board[6] == board[7]) and (board[6] == board[8])):
        win(board[6])
        
    if ((board[0] > 0) and(board[0] == board[3]) and (board[0] == board[6])):
        win(board[0])
    elif ((board[1] > 0) and(board[1] == board[4]) and (board[1] == board[7])):
        win(board[1])
    elif ((board[2] > 0) and(board[2] == board[5]) and (board[2] == board[8])):
        win(board[2])

    if ((board[0] > 0) and(board[0] == board[4]) and (board[0] == board[8])):
        win(board[0])
    elif ((board[2] > 0) and(board[2] == board[4]) and (board[2] == board[6])):
        win(board[2])

def win(number):
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (0, 0, 300, 300))
    if number == 1:
        pygame.draw.line(DISPLAYSURF, (255, 155, 0), (0, 0), (300, 300))
        pygame.draw.line(DISPLAYSURF, (255, 155, 0), (0, 300), (300, 0))
    else:
        pygame.draw.circle(DISPLAYSURF, (0, 50, 255), (150, 150), 150, 0)
        pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (150, 150), 149, 0)

    time.sleep(2)

    for i in range(len(board)):
        board[i] = 0

while playing:
    DISPLAYSURF.fill((255, 255, 255))
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (100, 0), (100, 300))
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (200, 0), (200, 300))
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 100), (300, 100))
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 200), (300, 200))

    for i in range(len(board)):
        if board[i] > 0:
            if board[i] == 1:
                drawX(boardPos[i][0], boardPos[i][1])
            else:
                drawCir(boardPos[i][0], boardPos[i][1])
           
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            if (mouseX < 100 and mouseY < 100):
                if board[0] == 0:
                    x = not(x)
                    if (x == True):
                        board[0] = 1
                    else:
                        board[0] = 2
            elif ((mouseX > 100) and (mouseX < 200) and (mouseY < 100)):
                if board[1] == 0:
                    x = not(x)
                    if (x == True):
                        board[1] = 1
                    else:
                        board[1] = 2
            elif ((mouseX > 200) and (mouseY < 100)):
                if board[2] == 0:
                    x = not(x)
                    if (x == True):
                        board[2] = 1
                    else:
                        board[2] = 2
            elif ((mouseX < 100) and ((mouseY > 100) and (mouseY < 200))):
                if board[3] == 0:
                    x = not(x)
                    if (x == True):
                        board[3] = 1
                    else:
                        board[3] = 2
            elif ((mouseX > 100) and (mouseX < 200) and ((mouseY > 100) and (mouseY < 200))):
                if board[4] == 0:
                    x = not(x)
                    if (x == True):
                        board[4] = 1
                    else:
                        board[4] = 2
            elif ((mouseX > 200) and ((mouseY > 100) and (mouseY < 200))):
                if board[5] == 0:
                    x = not(x)
                    if (x == True):
                        board[5] = 1
                    else:
                        board[5] = 2
            elif ((mouseX < 100) and (mouseY > 200)):
                if board[6] == 0:
                    x = not(x)
                    if (x == True):
                        board[6] = 1
                    else:
                        board[6] = 2
            elif ((mouseX > 100) and (mouseX < 200) and (mouseY > 200)):
                if board[7] == 0:
                    x = not(x)
                    if (x == True):
                        board[7] = 1
                    else:
                        board[7] = 2
            elif ((mouseX > 200) and (mouseY > 200)):
                if board[8] == 0:
                    x = not(x)
                    if (x == True):
                        board[8] = 1
                    else:
                        board[8] = 2
                    
            
    winCheck()
    pygame.display.update()
