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
        self.__tasks = deque([])
        self.__x = 0
        self__y = 0

    def draw_start_position(self, world, building_right_edge, building_deck, level_height):
        x_pos = building_right_edge + self.__space_width + (self.__image_width + self.__space_width) * self.__num
        y_pos = building_deck - level_height + ((level_height - self.__image_height) // 2)
        world.blit(self.__image, (x_pos, y_pos))

    def move(self):
        if len(self.__tasks) > 0:
            pass

    def draw(self):
        pass

    def update(self):
        pass

    def get_current_level(self):
        return self.__current_level

    def set_current_level(self, level):
        self.__current_level = level

    def add_task(self, destination, finnish_time):
        self.__tasks.append((destination, finnish_time))

    def get_last_task(self):
        if len(self.__tasks) > 0:
            return self.__tasks[-1]
