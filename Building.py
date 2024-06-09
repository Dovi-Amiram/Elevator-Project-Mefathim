import pygame
from Elevator import Elevator
from Level import Level
from settings import *


class Building:
    def __init__(self, world, num_of_levels, num_of_elevators, level_image, elevator_image, menivim=False):
        self.__level_img = level_image
        self.__elevator_img = elevator_image
        self.__levels = [Level(level_num, self.__level_img) for level_num in range(num_of_levels + 1)]
        for level in self.__levels:
            level.set_deck(world, WHITE_MARGIN)
        self.__elevators = [Elevator(elevator_num, self.__elevator_img) for elevator_num in range(num_of_elevators)]
        self.__right_edge = self.__level_img.get_width() + WHITE_MARGIN
        self.__deck = world.get_height() - WHITE_MARGIN

    def draw(self, world):
        for level in self.__levels:
            level.draw_self(world, WHITE_MARGIN)
        for elevator in self.__elevators:
            elevator.draw_start_position(world, building_right_edge, building_deck, self.__level_img.get_height())

    def get_num_of_levels(self):
        return len(self.__levels)

    def get_num_of_elevators(self):
        return len(self.__elevators)

    def get_level_img(self):
        return self.__level_img

    def get_elevator_img(self):
        return self.__elevator_img

    def allocate_elevator(self, destination):
        earliest_finnish_time = float("inf")
        optimal_elevator = None
        for elevator in self.__elevators:
            last_task = elevator.get_last_task()
            last_level, last_finnish_time = last_task if last_task else elevator.get_current_level(), 0
            travel_distance = get_travel_distance(last_level, destination, LEVEL_HEIGHT)
            potential_finnish_time = last_finnish_time + travel_distance / TRAVEL_SPEED + DELAY_AT_DESTINATION
            if potential_finnish_time < earliest_finnish_time:
                earliest_finnish_time = potential_finnish_time
                optimal_elevator = elevator
        optimal_elevator.add_task(destination, earliest_finnish_time)
