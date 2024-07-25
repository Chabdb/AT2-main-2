# AT2
import pygame, sys
from settings import *
from map import Map

# Initialize pygame
pygame.init()

# Screen dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dungeon Game')

# Create a Map instance
game_map = Map(window)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle map events
    action = game_map.handle_events()
    if action == 'quit':
        running = False
    
    # Draw the map and elements
    game_map.draw()
    
    # Update the display
    pygame.display.flip()
    
    # Frame rate
    pygame.time.Clock().tick(60)

pygame.quit()# AT2-main-2