import pygame
import sys
import os
from tkinter import messagebox
from pygame_widgets.button import Button
import pygame_widgets
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
        pygame.init()  
        pygame.font.init()  
        self.load_map(map_file)
        self.button_font = pygame.font.Font(None, 36)

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

    def undo_move(self):
        if self.move_history:
            row, col, i, j = self.move_history.pop()
            self.board[row][col] = PLAYER
            if self.is_target(row, col):
                self.board[row + i][col + j] = TARGET
            else:
                self.board[row + i][col + j] = SPACE

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

def main():
    game = SokobanGame("map/game01.txt")
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Sokoban")
    window_size = (930, 400)

    screen = pygame.display.set_mode(window_size)
    screen.fill((0, 0, 0))

    game_surface_size = (720, 400)
    game_surface = pygame.Surface(game_surface_size)

    button_BFS = Button(screen,  820,  100,  100,  40, text='BFS',  fontSize=40,  margin=20,  inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=bfs )
    button_Greddy = Button(screen,  820,  50,  100,  40, text='Greedy',  fontSize=40,  margin=20,  inactiveColour=(200, 50, 0), hoverColour=(150, 0, 0), pressedColour=(0, 200, 20),  onClick=greedy )
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
                elif event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    game.undo_move()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game.draw_board(game_surface)
        screen.blit(game_surface, (0, 0))
        pygame.display.flip()
        pygame_widgets.update(events)
        pygame.display.update()

def bfs():
    messagebox.showinfo("Hello", "BFS solve!")

def greedy():
    messagebox.showinfo("Hello", "Greedy solve!")

if __name__ == "__main__":
    main()
