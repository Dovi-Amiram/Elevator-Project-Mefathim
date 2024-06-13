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

# Scroll variable


building = Building(world,
                    NUM_OF_LEVELS,
                    NUM_OF_ELEVATORS,
                    LEVEL_IMAGE,
                    ELEVATOR_IMAGE)

building.draw()


max_scroll_y = WORLD_HEIGHT - WINDOW_HEIGHT
scroll_y = max_scroll_y


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
            elif event.button == 1:
                x, y = event.pos
                building.check_calls(x, y)

    building.update()

    # Blit the world to the screen at the current scroll position
    screen.blit(world, (0, -scroll_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
