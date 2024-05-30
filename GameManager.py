import json
import pygame
import sys
from Building import Building

# constants:

WINDOW_SIZE = 1200, 750
WHITE_MARGIN = 7
BLACK_SPACER_HEIGHT = 7
ELEVATOR_MARGIN = 30
SCROLL_BAR_WIDTH = 20
SCROLL_BAR_COLOR = (150, 150, 150)
SCROLL_BAR_BG_COLOR = (200, 200, 200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CAPTION = "Dovi's Elevator Project - Mefathim"


def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


class GameManager:

    def __init__(self, jason_file_path):
        self.window_size = WINDOW_SIZE
        data = load_json(jason_file_path)

        self.__building = Building(data['num_of_levels'],
                                   data['num_of_elevators'],
                                   data['level_image'],
                                   data['elevator_image'])

        self.world_width, self.world_height = self.__calculate_dimensions()  # Dimensions of the larger world
        self.screen = pygame.display.set_mode(self.window_size)
        self.__world = pygame.Surface(self.world_width, self.world_height)

        self.scroll_x, self.scroll_y = 0, 0
        self.max_scroll_x = self.world_width - self.window_size[0]
        self.max_scroll_y = self.world_height - self.window_size[1]
        self.scrollbar_width = SCROLL_BAR_WIDTH
        self.scrollbar_color = SCROLL_BAR_COLOR
        self.scrollbar_bg_color = SCROLL_BAR_BG_COLOR

    def __calculate_dimensions(self):
        # Calculate the total height of the world dynamically
        level_image = self.__building.get_level_img()
        level_height = level_image.get_height()  # Assuming all levels have the same height
        total_level_height = (
                self.__building.get_num_of_levels() * (level_height + BLACK_SPACER_HEIGHT) - BLACK_SPACER_HEIGHT)
        world_height = total_level_height + 2 * WHITE_MARGIN
        world_width, _ = WINDOW_SIZE
        return world_width, world_height

    def display_screen(self):
        pygame.init()
        pygame.display.set_caption(CAPTION)
        # Create a larger surface (world)
        self.__world.fill((255, 255, 255))  # Fill the world with a color (green in this case)
        self.__building.draw(self.__world, self.scrollbar_width + WHITE_MARGIN, BLACK_SPACER_HEIGHT, ELEVATOR_MARGIN)

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # Mouse wheel up
                        self.scroll_y -= 20
                    elif event.button == 5:  # Mouse wheel down
                        self.scroll_y += 20

            # Limit the scrolling to the boundaries of the world
            self.scroll_x = max(0, min(self.scroll_x, self.max_scroll_x))
            self.scroll_y = max(0, min(self.scroll_y, self.max_scroll_y))

            # Blit the world to the screen at the current scroll position
            self.screen.blit(self.world, (-self.scroll_x, -self.scroll_y))

            # Draw the scrollbar background
            pygame.draw.rect(self.screen, self.scrollbar_bg_color, (0, 0, self.scrollbar_width, self.window_size[1]))

            # Calculate the scrollbar position
            scrollbar_height = self.window_size[1] * (self.window_size[1] / self.world_height)
            scrollbar_position = (self.window_size[1] - scrollbar_height) * (self.scroll_y / self.max_scroll_y)
            pygame.draw.rect(self.screen, self.scrollbar_color,
                             (0, scrollbar_position, self.scrollbar_width, scrollbar_height))

            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()

    def run(self):
        self.display_screen()


game = GameManager("data.json")
game.run()
