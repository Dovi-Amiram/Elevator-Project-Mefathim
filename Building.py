import pygame
from Elevator import Elevator
from Level import Level

ELEVATOR_SCALE = (60, 60)
WHITE_MARGIN = 7


class Building:
    def __init__(self, num_of_levels, num_of_elevators, level_img_path, elevator_img_path, world, white_margin):
        self.__level_img = pygame.image.load(level_img_path)
        self.__image_width, self.__image_height = self.__level_img.get_size()
        self.__elevator_img = pygame.transform.scale(pygame.image.load(elevator_img_path), ELEVATOR_SCALE)
        self.__levels = [Level(level_num, self.__level_img) for level_num in range(num_of_levels + 1)]
        self.__levels[-1].mark_as_top_level()
        for level in self.__levels:
            level.set_deck(world, white_margin)
        self.__elevators = [Elevator(elevator_num, self.__elevator_img) for elevator_num in range(num_of_elevators)]

    def draw(self, world, margin, black_space, elevator_spacer):
        for level in self.__levels:
            level.draw_self(world, margin, black_space)

        building_right_edge = self.__level_img.get_width() + margin
        building_deck = world.get_height() - margin
        for elevator in self.__elevators:
            elevator.draw_start_position(world, elevator_spacer, self.__level_img, building_right_edge, building_deck)

    def get_num_of_levels(self):
        return len(self.__levels)

    def get_num_of_elevators(self):
        return len(self.__elevators)

    def get_level_img(self):
        return self.__level_img

    def get_elevator_img(self):
        return self.__elevator_img
