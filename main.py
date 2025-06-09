from factory_method import *
from neighbourhood import *

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

neighbourhood = Neighbourhood()

screen = pygame.display.set_mode(
    (min(WINDOW_WIDTH, neighbourhood.canvas.get_width()), min(WINDOW_HEIGHT, neighbourhood.canvas.get_height())))
pygame.display.set_caption(CAPTION)

max_scroll_y = neighbourhood.canvas.get_height() - screen.get_height()
scroll_y = max_scroll_y

max_scroll_x = neighbourhood.canvas.get_width() - screen.get_width()
scroll_x = 0

# Main loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Mouse wheel up
                scroll_y = max(0, scroll_y - SCROLL_SPEED_Y)
            elif event.button == 5:  # Mouse wheel down
                scroll_y = min(max_scroll_y, scroll_y + SCROLL_SPEED_Y)
            elif event.button == 1:
                neighbourhood.handle_click(event.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        scroll_x = max(0, scroll_x - SCROLL_SPEED_X)
    if keys[pygame.K_RIGHT]:
        scroll_x = min(max_scroll_x, scroll_x + SCROLL_SPEED_X)

    DeltaTime().update()
    neighbourhood.update()

    # Blit the canvas to the screen at the current scroll position
    screen.blit(neighbourhood.canvas, (-scroll_x, -scroll_y))

    clock.tick(60)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
