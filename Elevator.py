import pygame
from collections import deque

ELEVATOR_MARGIN = 30


class Elevator:

    def __init__(self, elevator_num, image, sapce_width=ELEVATOR_MARGIN):
        self.__space_width = sapce_width
        self.__image = image
        self.__image_width = image.get_width()
        self.__image_height = image.get_height()
        self.__num = elevator_num
        self.__current_level = 0
        self.__calls = deque()

    def draw_start_position(self, world, building_right_edge, building_deck, level_height):
        x_pos = building_right_edge + self.__space_width + (self.__image_width + self.__space_width) * self.__num
        y_pos = building_deck - level_height + ((level_height - self.__image_height) // 2)
        world.blit(self.__image, (x_pos, y_pos))

    def move_up(self, dest_level):
        pass

    def move_down(self, dest_level):
        pass
