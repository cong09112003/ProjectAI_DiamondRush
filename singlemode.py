import pygame
import sys
import os
from tkinter import messagebox
from pygame_widgets.button import Button
from pygame_widgets.combobox import ComboBox
import pygame_widgets
import subprocess
import DFS
import time
BOX_SIZE = 36
PLAYER = "@"
TARGET = "."
SPACE = " "
BOX = "$"
BINGO = "*"
WALL = "#"
FPS=30
window_size = (1000, 600)
  
class SokobanGame:
    def __init__(self, map_file):
        self.board = []
        self.targets = []
        self.move_history = []
        self.aiStep = []
        self.playerStep=[]
        self.clock=pygame.time.Clock()
        self.listMappath = ["map/game01.txt","map/game02.txt","map/game03.txt"]
        self.curMappath = map_file
        self.DeadLocks=[]
        pygame.init()  
        pygame.font.init()  
        self.load_map(map_file)
        self.button_font = pygame.font.Font(None, 36)
        self.step= len(self.move_history)
        self.state="..."
        if self.is_success==True:
            self.state="Win"
    def load_map(self, map_file):
        with open(map_file, 'r') as f:
            for line in f.read().splitlines():
                self.board.append(list(line))
        self.init_targets()
        print(f"targets:{self.targets}")
        self.init_deadblock()
        print(f"dealocks:{self.DeadLocks}")
    def is_success(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == TARGET:
                    return False
        return True
    # i!=0 and j!=0 and i!=len(self.board[0])-1 and j!=len(self.board[1])-1 and
    # ((self.board[i-1][j]==WALL and self.board[i][j-1]==WALL) or
    # (self.board[i-1][j]==WALL and self.board[i][j+1]==WALL) or
    # (self.board[i+1][j]==WALL and self.board[i][j-1]==WALL) or
    # (self.board[i+1][j]==WALL and self.board[i][j+1]==WALL))
    def init_deadblock(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if  self.board[i][j] == SPACE or self.board[i][j] == PLAYER :
                    # print(i,j)
                    if i-1 >= 0 and j-1 >= 0 and i+1 <= len(self.board) and j+1 <= len(self.board[0]):
                        if self.board[i-1][j]==WALL and self.board[i][j-1]==WALL:
                            self.DeadLocks.append((i,j))  
                        elif self.board[i-1][j]==WALL and self.board[i][j+1]==WALL:
                            self.DeadLocks.append((i,j))  
                        elif self.board[i+1][j]==WALL and self.board[i][j-1]==WALL:
                            self.DeadLocks.append((i,j))
                        elif self.board[i+1][j]==WALL and self.board[i][j+1]==WALL:
                            self.DeadLocks.append((i,j))                     
    def is_deadblock(self,row,col):
        for dealbock in self.DeadLocks:
            if dealbock[0] == row and dealbock[1] == col:
                return True
        return False
    def init_targets(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == TARGET:
                    self.targets.append((i, j))

    def is_target(self, row, col):
        for target in self.targets:
            if target[0] == row and target[1] == col:
                return True
        return False

    def get_screen_size(self):
        j = 0
        for i in range(len(self.board)):
            j = len(self.board[i]) if len(self.board[i]) > j else j
        return j * BOX_SIZE, len(self.board) * BOX_SIZE

    def do_move(self, row, col, i, j):
        self.move_history.append((row, col, i, j))
        self.board[row + i][col + j] = PLAYER
        if self.is_target(row, col):
            self.board[row][col] = TARGET
        else:
            self.board[row][col] = SPACE
        self.step = len(self.move_history)

    def get_player_position(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == PLAYER:
                    return i, j

    def move_left(self):
        self.move_player(0, -1)
        self.playerStep.append('L')

    def move_right(self):
        self.move_player(0, 1)
        self.playerStep.append('R')

    def move_up(self):
        self.move_player(-1, 0)
        self.playerStep.append('U')

    def move_down(self):
        self.move_player(1, 0)
        self.playerStep.append('D')

    def move_player(self, i, j):
        row, col = self.get_player_position()
        m, n = i * 2, j * 2

        if self.board[row + i][col + j] == SPACE:
            self.do_move(row, col, i, j)

        elif self.board[row + i][col + j] == TARGET:
            self.do_move(row, col, i, j)

        elif self.board[row + i][col + j] == BOX:
            if self.board[row + m][col + n] == SPACE:
                self.board[row + m][col + n] = BOX
                self.do_move(row, col, i, j)

            elif self.board[row + m][col + n] == TARGET:
                self.board[row + m][col + n] = BINGO
                self.do_move(row, col, i, j)

        elif self.board[row + i][col + j] == BINGO:
            if self.board[row + m][col + n] == SPACE:
                self.board[row + m][col + n] = BOX
                self.do_move(row, col, i, j)

            elif self.board[row + m][col + n] == TARGET:
                self.board[row + m][col + n] = BINGO
                self.do_move(row, col, i, j)

    def load_map_from_file(self, map_file):
        self.board = []
        self.targets = []
        self.move_history = []
        self.load_map(map_file)
        self.init_targets()

    
    def draw_board(self, surface):
        img_wall = pygame.image.load('img/wall.png').convert()
        img_box = pygame.image.load('img/box.png').convert()
        img_player = pygame.image.load('img/player.png').convert()
        img_target = pygame.image.load('img/target.png').convert()
        img_bingo = pygame.image.load('img/bingo.png').convert()
        img_space = pygame.image.load('img/space.png').convert()
        images = {WALL: img_wall, SPACE: img_space, BINGO: img_bingo,
                  TARGET: img_target, PLAYER: img_player, BOX: img_box}
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                surface.blit(images[self.board[i][j]], (j * BOX_SIZE, i * BOX_SIZE))
    def reset(self):
        self.board = []  
        self.targets = []  
        self.move_history = []  
        self.load_map_from_file(self.curMappath)
        self.init_targets()
        self.step = 0
        font = pygame.font.Font(None, 36)
        steps_label = font.render(f"Steps: {self.step}", True, (255, 255, 255))
        time_label = font.render(f"Time: 0s", True, (255, 255, 255))
        return steps_label, time_label

    def load_next_map(self,gamesur):
        gamesur.fill((41,41,41))
        index = self.listMappath.index(self.curMappath)
        if index < len(self.listMappath) - 1:
            self.curMappath = self.listMappath[index + 1]
            self.load_map_from_file(self.curMappath)

    def load_previous_map(self,gamesur):
        gamesur.fill((41,41,41))
        index = self.listMappath.index(self.curMappath)
        if index > 0:
            self.curMappath = self.listMappath[index - 1]
            self.load_map_from_file(self.curMappath)
    def printStep(self):
        print (f"AI Step:{self.aiStep}")
        print (f"Player step: {self.playerStep}")
    def solve_DFS(self,gamsurface):
        dfs=DFS.DFS(self.curMappath,self.aiStep)
        self.aiStep=dfs.solveDFS()
        for i in (self.aiStep):
            if i == 'L': 
                self.move_left()
            if i == 'R':
                self.move_right()
            if i == 'U':
                self.move_up()
            if i == 'D':
                self.move_down()
            self.draw_board(pygame.display.get_surface())
            pygame.display.flip()
            pygame.time.delay(250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        self.draw_board(pygame.display.get_surface())
        pygame.display.flip()
            
def main():
    #Cưả sổ chính
    game = SokobanGame("map/game01.txt")
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Sokoban")
    
    screen = pygame.display.set_mode(window_size)
    screen.fill((41,41,41))

    #Game surface hiện trò chơi
    game_surface_size = (720, 400)
    game_surface = pygame.Surface(game_surface_size)
    game_surface.fill((41,41,41))

    font = pygame.font.Font(None, 36)
    #Button trong game
    button_reset = Button(screen,  815,  50,  100,  40, text='Reset',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=lambda: game.reset() )
    
    button_bfs = Button(screen,  750,  100,  100,  40, text='BFS',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=bfs )
    button_dfs = Button(screen,  880,  100,  100,  40, text='DFS',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=lambda:game.solve_DFS(game_surface) )
    button_ucs = Button(screen,  750,  150,  100,  40, text='UCS',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=bfs )
    button_greedy = Button(screen,  880,  150,  100,  40, text='Greedy',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=bfs )
    button_astar = Button(screen,  750,  200,  100,  40, text='A*',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=bfs )
    button_bestfs = Button(screen,  880,  200,  100,  40, text='Best FS',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=bfs )
    button_nextlevel = Button(screen,  880,  350,  100,  40, text='Next',  fontSize=34,  margin=20, 
                               inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=lambda: game.load_next_map(game_surface) )
    button_previouslevel = Button(screen,  750,  350,  100,  40, text='Previous',  fontSize=34,  margin=20,  
                                  inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=lambda: game.load_previous_map(game_surface) )
    button_Home = Button(screen,  815,  300,  100,  40, text='Home',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=lambda: home() )

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                elif event.key == pygame.K_UP:
                    game.move_up()
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if game.is_success(): 
            game.state = 'win'
            game.printStep()
            
        game.draw_board(game_surface)
        screen.fill((41, 41, 41), (0, game_surface.get_height(), window_size[0], 50))
        steps_label = font.render(f"Steps: {game.step}", True, (255, 255, 255))
        time_label = font.render(f"Time: 0s", True, (255, 255, 255))

        
        state_label=font.render(f"State: {game.state}", True, (255, 255, 255))
        screen.blit(steps_label, (80, game_surface.get_height() + 10))
        screen.blit(time_label, (360, game_surface.get_height() + 10))
        screen.blit(state_label, (500, game_surface.get_height() + 10))
        screen.blit(game_surface, (0, 0))

        pygame.display.flip()
        pygame_widgets.update(events)
        pygame.display.update()
        game.clock.tick(FPS)
    
def bfs():
    messagebox.showinfo("Hello", "BFS solve!")
def home():
    try:
        subprocess.Popen(["python", "menuSokoban.py"])
        sys.exit()
    except Exception as e:
        print(f"Error opening Menu.py: {e}")
if __name__ == "__main__":
    main()
    