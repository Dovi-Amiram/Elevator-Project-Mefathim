from neighbourhood import *

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

neighbourhood = Neighbourhood()

fullscreen = False


def get_screen(fullscreen: bool) -> pygame.Surface:
    if fullscreen:
        return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        return pygame.display.set_mode(
            (min(WINDOW_WIDTH, neighbourhood.canvas.get_width()),
             min(WINDOW_HEIGHT, neighbourhood.canvas.get_height()))
        )


screen = get_screen(fullscreen)

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
                x, y = event.pos
                neighbourhood.handle_click((x + scroll_x, y + scroll_y))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                screen = get_screen(fullscreen)

                # Recalculate scroll limits
                max_scroll_y = neighbourhood.canvas.get_height() - screen.get_height()
                max_scroll_x = neighbourhood.canvas.get_width() - screen.get_width()

                scroll_y = min(scroll_y, max_scroll_y)
                scroll_x = min(scroll_x, max_scroll_x)

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
