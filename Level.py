import pygame

BLACK = (0, 0, 0)


def draw_black_space(world, left, top, width, height):
    pygame.draw.rect(world, BLACK, (left, top, width, height))


class Level:

    def __init__(self, level_num, image):
        self.__image = image
        self.__num = level_num
        self.__top_level = False
        self.__deck = 0

    def draw_self(self, world, x_margin, black_space):
        level_height = self.__image.get_height()
        level_width = self.__image.get_width()

        # Calculate the position of the level in the world
        x_pos = x_margin
        y_pos = world.get_height() - (self.__num + 1) * (level_height + black_space)

        if not self.__top_level:
            draw_black_space(world, x_pos, y_pos - black_space, level_width, level_height)
        # Draw the level image
        world.blit(self.__image, (x_pos, y_pos))

        # Draw the 7-pixel black line at the bottom of the level

    def display_timer(self, world):
        pass

    def handle_event(self, event):
        pass

    def call_elevator(self):
        pass

    def mark_as_top_level(self):
        self.__top_level = True

    def set_deck(self, world, white_margin):
        world_height = world.get_height()
        self.__deck = world_height - white_margin - (self.__image.get_height() * (self.__num + 1))

    def get_deck(self):
        return self.__deck

    def get_num(self):
        return self._num
