
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
targets=[]
root=os.path.dirname(os.path.abspath(__file__))
print(root)

def initBoard():
    with open("map/game01.txt", 'r')as f:
        for line in f.read().splitlines(): 
            board.append(list(line))
    # print(board)
            
            
            
def initTargets():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==TARGET:
                targets.append((i,j))
    print(targets)

def isTarget(row,col):
    for target in targets:
        if target[0]==row and target[1]==col:
            return True
    return False
    

   
def getScreenSize():
    j = 0
    for i in range(len(board)):
        j = len (board[i]) if len(board[i]) > j else j
    return j*BOX_SIZE, len(board) * BOX_SIZE        

def doMove(row,col,i,j):
    board[row+i][col+j]=PLAYER
    if isTarget(row,col):
        board[row][col]=TARGET
    else:
        board[row][col]=SPACE

def getPlayerPosition():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==PLAYER:
                print(i,j)
                return i,j
           

def moveLeft():
    movePlayer(0,-1)
    
def moveRight():
    movePlayer(0,1)
    
def moveUp():
    movePlayer(-1,0)
    
def moveDown():
    movePlayer(1,0)   
     
def movePlayer(i,j):
    row, col = getPlayerPosition()
    m = i*2 
    n = j*2
    # if  is_space
    if board[row+i][col+j] == SPACE:
        doMove(row,col,i,j)
        
    # if is_target
    elif board[row+i][col+j] == TARGET:
        doMove(row,col,i,j)
        
    # if is_box
    elif board[row+i][col+j] == BOX:
        if board[row+m][col+n] == SPACE:
            board[row+m][col+n] = BOX
            doMove(row,col,i,j)
            
        elif board[row+m][col+n]==TARGET:
            board[row+m][col+n]=BINGO
            doMove(row,col,i,j)
    #if is_bingo    
    elif board[row+i][col+j]==BINGO:
        if board[row+m][col+n]==SPACE:
            board[row+m][col+n]=BOX
            doMove(row,col,i,j)
            
        elif board[row+m][col+n]==TARGET:
            board[row+m][col+n]=BINGO
            doMove(row,col,i,j)
    #else is wall
    else:
        pass
def drawBoard(screen):
    # load image
    img_wall=pygame.image.load('img/wall.png').convert()
    img_box = pygame.image.load('img/box.png').convert()
    img_player = pygame.image.load('img/player.png').convert()
    img_target = pygame.image.load('img/target.png').convert()
    img_bingo = pygame.image.load('img/bingo.png').convert()
    img_space = pygame.image.load('img/space.png').convert()
    images={WALL:img_wall,SPACE:img_space,BINGO:img_bingo,
            TARGET:img_target,PLAYER:img_player,BOX:img_box}
    for i in range(len(board)):
        for j in range(len(board[i])):
            screen.blit(images[board[i][j]],(j*BOX_SIZE,i*BOX_SIZE))
    
    pygame.display.update()
            

def main():
    initBoard()
    initTargets()
    print(board)
    print(targets)
    pygame.display.init()
    pygame.display.set_caption("sokoban")
    screen=pygame.display.set_mode(getScreenSize())
    screen.fill((0,0,0))
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    moveLeft()
                elif event.key==pygame.K_RIGHT:
                    moveRight()
                elif event.key==pygame.K_UP:
                    moveUp()
                elif event.key==pygame.K_DOWN:
                    moveDown()     
                elif event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        drawBoard(screen)

if __name__ == "__main__":
    main()

