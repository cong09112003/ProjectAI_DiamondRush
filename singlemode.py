import pygame
import sys
import os
from tkinter import messagebox
from pygame_widgets.button import Button
from pygame_widgets.combobox import ComboBox
import pygame_widgets
import subprocess
from queue import PriorityQueue
BOX_SIZE = 36
PLAYER = "@"
TARGET = "."
SPACE = " "
BOX = "$"
BINGO = "*"
WALL = "#"
class SokobanGame:
    def __init__(self, map_file):
        self.board = []
        self.targets = []
        self.move_history = []
        self.aiStep = []
        self.listMappath = ["map/game01.txt","map/game02.txt","map/game03.txt"]
        self.curMappath = map_file
        pygame.init()  
        pygame.font.init()  
        self.load_map(map_file)
        self.button_font = pygame.font.Font(None, 36)
        self.step= len(self.move_history)

    def load_map(self, map_file):
        with open(map_file, 'r') as f:
            for line in f.read().splitlines():
                self.board.append(list(line))
        self.init_targets()

    def init_targets(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == TARGET:
                    self.targets.append((i, j))

    def all_boxes_on_targets(self):
        for target in self.targets:
            if self.board[target[0]][target[1]] != BINGO:
                return False
        return True
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

    def move_right(self):
        self.move_player(0, 1)

    def move_up(self):
        self.move_player(-1, 0)

    def move_down(self):
        self.move_player(1, 0)

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

    def get_neighbors(self, state):
        row, col = state
        neighbors = []

        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if self.is_valid_move(row + i, col + j):
                neighbors.append((row + i, col + j))

        return neighbors

    def is_valid_move(self, row, col):
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
            return False

        if self.board[row][col] == WALL:
            return False

        return True

    def cost(self, current, next_state):
        return 1

    def ucs(self):
        start_state = self.get_player_position()
        frontier = PriorityQueue()
        frontier.put((0, start_state))  
        came_from = {start_state: None}
        cost_so_far = {start_state: 0}

        while not frontier.empty():
            current = frontier.get()[1]

            if self.is_target(*current):
                break

            for next_state in self.get_neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, next_state)
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    priority = new_cost
                    frontier.put((priority, next_state))
                    came_from[next_state] = current
        print(came_from)
        return came_from, cost_so_far

def main():
    #Cưả sổ chính
    game = SokobanGame("map/game01.txt")
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Sokoban")
    window_size = (1000, 450)
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
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=ok )
    button_dfs = Button(screen,  880,  100,  100,  40, text='DFS',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=ok )
    button_ucs = Button(screen,  750,  150,  100,  40, text='UCS',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=lambda:game.ucs() )
    button_greedy = Button(screen,  880,  150,  100,  40, text='Greedy',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=ok )
    button_astar = Button(screen,  750,  200,  100,  40, text='A*',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=ok )
    button_bestfs = Button(screen,  880,  200,  100,  40, text='Best FS',  fontSize=34,  margin=20, 
                          inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=ok )
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
        game.draw_board(game_surface)
        screen.fill((41, 41, 41), (0, game_surface.get_height(), window_size[0], 50))
        steps_label = font.render(f"Steps: {game.step}", True, (255, 255, 255))
        time_label = font.render(f"Time: 0s", True, (255, 255, 255))

        screen.blit(steps_label, (80, game_surface.get_height() + 10))
        screen.blit(time_label, (360, game_surface.get_height() + 10))
        screen.blit(game_surface, (0, 0))

        pygame.display.flip()
        pygame_widgets.update(events)
        pygame.display.update()
def ok():
    messagebox.showinfo("Hello", "message")
def home():
    try:
        subprocess.Popen(["python", "menuSokoban.py"])
        sys.exit()
    except Exception as e:
        print(f"Error opening Menu.py: {e}")
if __name__ == "__main__":
    main()
