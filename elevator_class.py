import time

import pygame
from collections import deque

ELEVATOR_MARGIN = 30


class Elevator:

    def __init__(self, elevator_num, image):
        self.__image = image
        self.__image_width = image.get_width()
        self.__image_height = image.get_height()
        self.__num = elevator_num
        self.__current_level = 0
        self.__tasks = deque([])
        self.__x = 0
        self.__y = 0
        self.__departure_time = 0
        self.__departure_y = 0

    def draw_start_position(self, world, building_right_edge, building_deck, level_height):
        x_pos = building_right_edge + self.__space_width + (self.__image_width + self.__space_width) * self.__num
        y_pos = building_deck - level_height + ((level_height - self.__image_height) // 2)
        world.blit(self.__image, (x_pos, y_pos))

    def move(self):
        if len(self.__tasks) > 0:
            dest, _ = self.__tasks.popleft()
            dest_y =
            if self.__y != dest_y:
                distance = dest_y - self.__y
                direction = distance / abs(distance)
                elapsed_time = time.time() - self.__departure_time
                new_y = self.__departure_y +

    def draw(self, world):
        world.blit(self.__image, (self.__x, self.__y))

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

    def set_coordinates(self, x, y):
        self.__x = x
        self.__y = y

    def get_num(self):
        return self.__num

    def get_width(self):
        return self.__image_width

    def get_height(self):
        return self.__image_height

    def set_y(self, y):
        self.__y = y
