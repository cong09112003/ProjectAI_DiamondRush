
import pygame
import sys
import os
BOX_SIZE=36
PLAYER="@"
TARGET="."
SPACE=" "
BOX="$"
BINGO="*"
WALL="#"
board=[]
target=[]
root=os.path.dirname(os.path.abspath(__file__))
def initBoard():
    with open(root+"map/game01.txt", 'r')as f:
        for line in f.read().splitlines(): 
            board.append(list(line))
            
            
            
def initTargets():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==TARGET:
                target.append((i,j))

def isTargets():
    for i in range(len)
        

