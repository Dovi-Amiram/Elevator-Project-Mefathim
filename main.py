from config import *
from building import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(CAPTION)

# Create a larger surface (canvas)
canvas_height = max(WHITE_MARGIN * 3 + NUM_OF_FLOORS * FLOOR_HEIGHT, WINDOW_HEIGHT)
canvas = pygame.Surface((WINDOW_WIDTH, canvas_height))

# Scroll variable
max_scroll_y = canvas_height - WINDOW_HEIGHT
scroll_y = max_scroll_y

# create building instance
building = Building(NUM_OF_FLOORS, NUM_OF_ELEVATORS, canvas_height)

# Main loop
run = True
while run:
    canvas.fill(SWAN_WING)
    pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Mouse wheel up
                scroll_y = max(0, scroll_y - SCROLL_SPEED)
            elif event.button == 5:  # Mouse wheel down
                scroll_y = min(max_scroll_y, scroll_y + SCROLL_SPEED)
            elif event.button == 1:
                pos = event.pos
                for floor in building.floors:
                    level = floor.button_pressed(pos)
                    if level is not None:
                        floor.button_compressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            for floor in building.floors:
                if floor.button_compressed:
                    building.allocate_elevator(floor.level)
                    floor.button_compressed = False

    building.update()
    building.draw(canvas)

    # Blit the canvas to the screen at the current scroll position
    screen.blit(canvas, (0, -scroll_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
