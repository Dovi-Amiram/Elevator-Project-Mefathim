import pygame
from collections import deque


class Elevator:

    def __init__(self, elevator_num, image):
        self.__image = image
        self.__num = elevator_num
        self.__current_level = 0
        self.__calls = deque()

    def draw_start_position(self, world, margin, level_image, building_right_edge, building_deck):
        level_width, level_height = level_image.get_size()
        image_width = self.__image.get_width()
        image_height = self.__image.get_height()
        x_pos = building_right_edge + margin + (self.__num * image_width)
        y_pos = building_deck - (image_height + level_height // 2)
        world.blit(self.__image, (x_pos, y_pos))

    def move_up(self, dest_level):
        pass

    def move_down(self, dest_level):
        pass
