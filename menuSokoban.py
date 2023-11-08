import pygame
import time
pygame.init()

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
                
screen = pygame.display.set_mode((1448, 758))
pygame.display.set_caption("Sokoban")
backgroundmenu = pygame.image.load("img/background.jpg")

backgroundGame = pygame.image.load("img/backgroundGameNau.jpg")

def startMenu_game():
    print("Start the game")
    
def endMenu_game():
    global running
    print("End the game")
    running = False
    
# Nut start game   
start_time = None
step_count = 0
game_states = []
def startPlayer_game():
    global start_time
    global step_count
    print("Go game")
    # Record the start time
    start_time = time.time()
    step_count = 0
def undo():
    global game_states
    if game_states:
        # Remove the last game state
        game_states.pop()
        print("Undo last step")
# Nut end game
def endPlayer_game():
    global current_interface
    print("End game")
    current_interface = "menu"
    
def toggle_mode():
    if mode_button.text == "Player Mode":
        mode_button.text = "AI Mode"
        print("Switched to AI Mode")
    else:
        mode_button.text = "Player Mode"
        print("Switched to Player Mode")
#giao dien       
def switch_interface():
    global current_interface
    if current_interface == "menu":
        current_interface = "player"
    else:
        current_interface = "menu"
#next level
def next_level():
    print("Next level")
    
current_interface = "menu"
#Button for Menu
switch_button = Button(1100, 400, 140, 75, (255, 255, 255), "Player", switch_interface)
startMenu_button = Button(1100, 300, 125, 75, (255, 255, 255), "Start", startMenu_game)
endMenu_button = Button(1100, 500, 125, 75, (255, 255, 255), "Quit", endMenu_game)

mode_button = Button(1100, 400, 125, 75, (255, 255, 255), "Mode", toggle_mode)

#Button for Mode Player
startPlayer_button = Button(1200, 200, 125, 75, (255, 255, 255), "StartGame", startPlayer_game)
endPlayer_button = Button(1200, 300, 125, 75, (255, 255, 255), "QuitGame", endPlayer_game)
next_button = Button(1200, 400, 125, 75, (255, 255, 255), "Next", next_level)
undo_button = Button(1200, 500, 125, 75, (255, 255, 255), "Undo", undo)
#label time
font = pygame.font.Font(None, 36)
#Map game
# Get the size of the game window
window_width, window_height = screen.get_size()

# Set the size of the game map
map_width, map_height = 500, 500
#Chay game 
running = True

while running:
    if current_interface == "menu":
        # Draw interface 1
        screen.blit(backgroundmenu, (0, 0))
        startMenu_button.draw(screen)
        endMenu_button.draw(screen)
        switch_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                startMenu_button.handle_event(event)
                endMenu_button.handle_event(event)
                switch_button.handle_event(event)

    else:
        screen.blit(backgroundGame, (0, 0))
        startPlayer_button.draw(screen)
        endPlayer_button.draw(screen)
        next_button.draw(screen)
        undo_button.draw(screen)


        # vi tri map
        map_x = (window_width - map_width) // 2
        map_y = (window_height - map_height) // 2

        # ve map
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(map_x, map_y, map_width, map_height), 2)

        if start_time is not None:
            # Tinh thoi gian
            elapsed_time = time.time() - start_time

            # chuyen doi thoi gian
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)

            # Render the time as a Surface
            time_surface = font.render(f"{minutes}:{seconds}", True, (255, 255, 255))

            # Render the label as a Surface
            label_surface = font.render("Time:", True, (255, 255, 255))
            step_surface = font.render(f"Step: {step_count}", True, (255, 255, 255))
            # Draw the label and the time onto the screen
            screen.blit(label_surface, (120, 50))
            screen.blit(time_surface, (200, 50))
            screen.blit(step_surface, (120, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                startPlayer_button.handle_event(event)
                endPlayer_button.handle_event(event)
                next_button.handle_event(event)
                undo_button.handle_event(event)


    pygame.display.update()
pygame.quit()