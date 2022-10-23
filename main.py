import pygame
from pygame.locals import *
import numpy
import sys

pygame.init()
grid = 30
width, height = 1280, 720
resolution = (width, height)
gridW, gridH = width // grid , height // grid 
display = pygame.display.set_mode(resolution)
cells = numpy.zeros((gridW,gridH))    
# initialize 2d datastructure, every row is one array, inside that array is 0 or 1 to indicate life
# board = []
# for j in range (0, gridH):
#     for i in range(0, gridW):
#         board= [[i], j]
board=[]
def initializeDataStructure(array):
    for i in range(0, gridH):
        row = []
        for j in range(0,gridW):
            # would be cool in the future to implement simplex noise to generate randomness, that way more cells survive
            row.append(numpy.random.randint(0,2))
        array.append(row)

# for x in range(0, width):
#     for y in range(0,height):
#         board[x] = (numpy.random.randint(0,1))
# draw the grids
def drawGrid():
    for x in range(0, width, grid):
        pygame.draw.line(display, 'gray', (x,0), (x,height))
    for y in range(0, height, grid):
        pygame.draw.line(display, 'gray',(0,y), (width,y))
#populate the cells
# what data structure to use? array with (x,y) coordinates two dimensional array?

# draw cells
# def drawCells():
    # test, draw all grids

initializeDataStructure(board)
while True:    
    drawGrid()
    for x in range(0,len(board[1]) -1): # length of column
        for y in range(0,len(board) -1): #length of rows
            if board[y][x] == 1:
                pygame.draw.rect(display, 'gray', (x * grid , y * grid , grid, grid))
    # count alive neighbors... hmmm...
    for x in range(0,len(board[1]) -1):
        for y in range(0,len(board) -1):
            sum = 0
            sum+= board[y-1][x-1]
            sum+= board[y][x-1]
            sum+= board[y-1][x]
            sum+= board[y+1][x+1]
            sum+= board[y+1][x]
            sum+= board[y][x+1]
            sum+= board[y-1][x+1]
            sum+= board[y+1][x-1]
            # if sum > 3 delete it overpopulation
            # if sum < 1 delete it as well

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
