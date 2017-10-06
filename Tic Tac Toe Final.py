import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((300, 350))
pygame.display.set_caption('Tic Tac Toe')
pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 50)

x = False
xWins = 0
oWins = 0
wins = []

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0] #The value of each box. 0 means blank, 1 means X, 2 means O
boardPos = [[50, 50], [150, 50], [250, 50],
            [50, 150], [150, 150], [250, 150],
            [50, 250], [150, 250], [250, 250]] #The positions for drawing shapes in each box

def drawX(xpos, ypos): #Function for drawing X
    pygame.draw.line(DISPLAYSURF, (255, 155, 0), (xpos - 50, ypos - 50), (xpos + 50, ypos + 50))
    pygame.draw.line(DISPLAYSURF, (255, 155, 0), (xpos + 50, ypos - 50), (xpos - 50, ypos + 50))

def drawCir(xpos, ypos): #Function for drawing O
    pygame.draw.circle(DISPLAYSURF, (0, 50, 255), (xpos, ypos), 50, 0)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (xpos, ypos), 49, 0)

def checkDraw(): #Checks for a draw between players
    draw = True

    for i in range(len(board)):
        if (board[i] == 0):
            draw = False

    if draw == True:
        win(3, xWins, oWins, x)

def winCheck(): #Check every possible 3-in-a-row to see if someone won
    if ((board[0] > 0) and (board[0] == board[1]) and (board[0] == board[2])):
        win(board[0], xWins, oWins, x)
    elif ((board[3] > 0) and (board[3] == board[4]) and (board[3] == board[5])):
        win(board[3], xWins, oWins, x)
    elif ((board[6] > 0) and (board[6] == board[7]) and (board[6] == board[8])):
        win(board[6], xWins, oWins, x)
        
    if ((board[0] > 0) and (board[0] == board[3]) and (board[0] == board[6])):
        win(board[0], xWins, oWins, x)
    elif ((board[1] > 0) and (board[1] == board[4]) and (board[1] == board[7])):
        win(board[1], xWins, oWins, x)
    elif ((board[2] > 0) and (board[2] == board[5]) and (board[2] == board[8])):
        win(board[2], xWins, oWins, x)

    if ((board[0] > 0) and (board[0] == board[4]) and (board[0] == board[8])):
        win(board[0], xWins, oWins, x)
    elif ((board[2] > 0) and (board[2] == board[4]) and (board[2] == board[6])):
        win(board[2], xWins, oWins, x)

def win(number, xWins, oWins, x): #Adds to the win array, and resets the board
    wins.append(number)

    for i in range(len(board)):
        board[i] = 0 #Sets each box on the board to be blank

while True:
    xText = font.render(("X=" + str(xWins)), False, (0, 0, 0))
    oText = font.render(("O=" + str(oWins)), False, (0, 0, 0)) #These set up the win counters in the bottom
    xWins = 0
    oWins = 0 #Set to zero every loop to stop them from continuing to increase

    DISPLAYSURF.fill((255, 255, 255))
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (100, 0), (100, 300))
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (200, 0), (200, 300))
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 100), (300, 100))
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 200), (300, 200))
    pygame.draw.line(DISPLAYSURF, (0, 0, 0), (0, 300), (300, 300)) #Draws the grid

    DISPLAYSURF.blit(xText, (0, 300))
    DISPLAYSURF.blit(oText, (210, 300)) #Places the win counters

    for i in range(len(board)): #Checks the value of each box, and draws a shape where applicable
        if board[i] > 0:
            if board[i] == 1:
                drawX(boardPos[i][0], boardPos[i][1])
            else:
                drawCir(boardPos[i][0], boardPos[i][1])
           
    for event in pygame.event.get():
        if event.type == QUIT: #Quits the game
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            mouseX, mouseY = event.pos #Updates the mouse positions, used for finding out where the mouse was pressed
        if event.type == pygame.MOUSEBUTTONUP:
            if (mouseX < 100 and mouseY < 100): #Checks which box the mouse is over
                if board[0] == 0: #If the box is empty
                    x = not(x) #Change which piece is being pressed
                    if (x == True):
                        board[0] = 1 #Changes the box to hold an X
                    else:
                        board[0] = 2 #Changes the box to hold an O
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
                    
    for i in range(len(wins)): #Used to see how many wins each player has
        if (wins[i] == 1):
            xWins += 1
        elif (wins[i] == 2):
            oWins += 1

    winCheck()
    checkDraw()

    pygame.display.update() #Updates the game state
