# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 23:23:00 2023

@author: Tris Anh
"""
import pygame # Import pygame module
class Button():
    def __init__(self, x, y, width, height, color, text, onclick):
        self.x = x # The x coordinate of the button
        self.y = y # The y coordinate of the button
        self.width = width # The width of the button
        self.height = height # The height of the button
        self.color = color # The color of the button
        self.text = text # The text on the button
        self.onclick = onclick # The function to call when the button is clicked
        self.surface = pygame.Surface((self.width, self.height)) # The surface of the button
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) # The rectangle of the button
        self.font = pygame.font.SysFont("Arial", 32) # The font of the text
        self.text_surf = self.font.render(self.text, True, (0, 0, 0)) # The surface of the text
    def draw(self, screen):
        self.surface.fill(self.color) # Fill the surface with the color
        self.surface.blit(self.text_surf, (self.width // 2 - self.text_surf.get_width() // 2, self.height // 2 - self.text_surf.get_height() // 2)) # Blit the text on the center of the surface
        screen.blit(self.surface, (self.x, self.y)) # Blit the surface on the screen at the position
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: # If the event is pressing the mouse button
            mouse_pos = pygame.mouse.get_pos() # Get the mouse position
            if self.rect.collidepoint(mouse_pos): # If the mouse position is on the button
                self.onclick() # Call the function

  

   
