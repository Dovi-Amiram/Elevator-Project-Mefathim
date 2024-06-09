import pygame
import sys
from settings import *
from building_class import Building

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(CAPTION)

# Create a larger surface (world)
world = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
world.fill((255, 255, 255))  # Fill the world with a white color

# Scroll variable
scroll_y = 0
max_scroll_y = WORLD_HEIGHT - WINDOW_HEIGHT

building = Building(world,
                    NUM_OF_LEVELS,
                    NUM_OF_ELEVATORS,
                    LEVEL_IMAGE,
                    ELEVATOR_IMAGE,
                    WHITE_MARGIN)
building.draw(world)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Mouse wheel up
                scroll_y = max(0, scroll_y - 20)
            elif event.button == 5:  # Mouse wheel down
                scroll_y = min(max_scroll_y, scroll_y + 20)

    # Blit the world to the screen at the current scroll position
    screen.blit(world, (0, -scroll_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
