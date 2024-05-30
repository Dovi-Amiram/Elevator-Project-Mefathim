import json
import pygame
import sys
from Building import Building

# constants:

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 750
WHITE_MARGIN = 7
BLACK_SPACER_HEIGHT = 7
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


def calculate_world_height(num_of_levels, level_height):
    # Calculate the total height of the world dynamically
    total_level_height = (
            num_of_levels * (level_height + BLACK_SPACER_HEIGHT) - BLACK_SPACER_HEIGHT)
    return total_level_height + 2 * WHITE_MARGIN


class GameManager:

    def __init__(self, jason_file_path):
        self.__white_margin = WHITE_MARGIN
        data = load_json(jason_file_path)

        level_image_height = pygame.image.load(data["level_image"]).get_height()
        num_of_levels = data["num_of_levels"] + 1

        self.__world_height = (
            calculate_world_height(num_of_levels, level_image_height))  # Dimensions of the larger world

        self.__window_size = (WINDOW_WIDTH, min(self.__world_height, WINDOW_HEIGHT))
        self.__world_width = self.__window_size[0]

        self.__world = pygame.Surface((self.__world_width, self.__world_height))
        self.__building = Building(self, data['num_of_levels'],
                                   data['num_of_elevators'],
                                   data['level_image'],
                                   data['elevator_image'])

        self.__screen = pygame.display.set_mode(self.__window_size)

        self.__larger_world = self.__world_height > self.__window_size[1]

        self.__scrollbar_width = SCROLL_BAR_WIDTH if self.__larger_world else 0

        if self.__larger_world:
            self.__scroll_x, self.scroll_y = 0, 0
            self.__max_scroll_x = self.__world_width - self.__window_size[0]
            self.__max_scroll_y = self.__world_height - self.__window_size[1]
            self.__scrollbar_color = SCROLL_BAR_COLOR
            self.__scrollbar_bg_color = SCROLL_BAR_BG_COLOR

    def display_screen(self):
        pygame.init()
        pygame.display.set_caption(CAPTION)
        # Create a larger surface (world)
        x_margin = WHITE_MARGIN + self.__scrollbar_width
        self.__world.fill((255, 255, 255))  # Fill the world with a color (green in this case)
        self.__building.draw(self.__world, x_margin)

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif self.__larger_world and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:  # Mouse wheel up
                        self.scroll_y -= 20
                    elif event.button == 5:  # Mouse wheel down
                        self.scroll_y += 20

            if self.__larger_world:
                # Limit the scrolling to the boundaries of the world
                self.__scroll_x = max(0, min(self.__scroll_x, self.__max_scroll_x))
                self.scroll_y = max(0, min(self.scroll_y, self.__max_scroll_y))

                # Blit the world to the screen at the current scroll position
                self.__screen.blit(self.__world, (-self.__scroll_x, -self.scroll_y))

                # Draw the scrollbar background
                pygame.draw.rect(self.__screen, self.__scrollbar_bg_color, (0, 0, self.__scrollbar_width, self.__window_size[1]))

                # Calculate the scrollbar position
                scrollbar_height = self.__window_size[1] * (self.__window_size[1] / self.__world_height)
                scrollbar_position = (self.__window_size[1] - scrollbar_height) * (self.scroll_y / self.__max_scroll_y)
                pygame.draw.rect(self.__screen, self.__scrollbar_color,
                                 (0, scrollbar_position, self.__scrollbar_width, scrollbar_height))
            else:
                self.__screen.blit(self.__world, (0, 0))
            # Update the display
            pygame.display.flip()

        # Quit Pygame
        pygame.quit()
        sys.exit()

    def run(self):
        self.display_screen()

    def get_white_margin(self):
        return self.__white_margin

    def get_world(self):
        return self.__world


game = GameManager("data.json")
game.run()
