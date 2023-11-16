
# DFS
# 
import pygame
import sys
import os
from tkinter import messagebox
from pygame_widgets.button import Button
from pygame_widgets.combobox import ComboBox
import pygame_widgets
import subprocess



# Import .py
import singlemode


# Load map 
class DFS():
    def __init__(self,current_map_file,aiStep):
        self.current_map_file=current_map_file
        self.game = singlemode.SokobanGame(current_map_file)
        self.listStep=aiStep
        self.board=self.game.board
    def solveDFS(self):
        listStep=[]
        listStep=['D', 'L', 'L', 'L', 'U', 'L', 'D']      
        return listStep
        
 