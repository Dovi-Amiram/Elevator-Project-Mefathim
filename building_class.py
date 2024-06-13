import pygame
from elevator_class import Elevator
from level_class import Level
from settings import *


class Building:
    def __init__(self, world, num_of_levels, num_of_elevators, level_image, elevator_image):
        self.__world = world
        self.__level_img = level_image
        self.__elevator_img = elevator_image

        self.__levels = []
        for level_num in range(num_of_levels):
            level_surface, level_rect = self.__create_level_image(level_num)
            self.__levels.append(Level(level_num, level_surface, level_rect))

        self.__elevators = []
        for elevator_num in range(num_of_elevators):
            pos = self.__calculate_elevator_pos(elevator_num)
            self.__elevators.append(Elevator(elevator_num, self.__elevator_img, pos))

    def __create_level_image(self, level_num):
        surface_height = self.__level_img.get_height() + SPACER
        level_surface = pygame.Surface((self.__level_img.get_width(), surface_height))
        level_surface.blit(self.__level_img, (0, SPACER))
        pygame.draw.rect(level_surface, pygame.Color("black"), (0, 0, self.__level_img.get_width(), SPACER))
        y_pos = self.__world.get_height() - SPACER - (level_num + 1) * surface_height
        rect = pygame.Rect(TIMER_WIDTH, y_pos, level_surface.get_width(), surface_height)
        return level_surface, rect

    def __calculate_elevator_pos(self, elevator_num):
        elevator_spacer = SPACER * 2
        x_pos = (TIMER_WIDTH + self.__level_img.get_width() + elevator_spacer
                 + elevator_num * (self.__elevator_img.get_width() + elevator_spacer))
        y_pos = self.__calculate_elevator_y_pos(0)
        return x_pos, y_pos

    def __calculate_elevator_y_pos(self, level_num):
        level = self.__levels[level_num]
        level_ceiling_y = level.get_ceiling_y()
        level_height = level.get_height()
        return level_ceiling_y + (level_height - self.__elevator_img.get_height()) // 2

    def update(self):
        for elevator in self.__elevators:
            elevator.update(self.__elevator_arrived)
        for level in self.__levels:
            level.update()
        self.draw()

    def draw(self):
        self.__world.fill(pygame.Color("white"))
        for level in self.__levels:
            level.draw(self.__world)
        for elevator in self.__elevators:
            elevator.draw(self.__world)

    def get_num_of_levels(self):
        return len(self.__levels)

    def get_num_of_elevators(self):
        return len(self.__elevators)

    def check_calls(self, x, y):
        for level in self.__levels:
            if level.check_call(x, y):
                print(level)
                self.allocate_elevator(level)

    def __elevator_arrived(self, dest_level_num):
        self.__levels[dest_level_num].elevator_arrived()

    def allocate_elevator(self, destination):
        destination_y = self.__calculate_elevator_y_pos(destination)
        earliest_finnish_time = float("inf")
        optimal_elevator = None
        for elevator in self.__elevators:
            _, last_stop_y, last_finnish_time = elevator.get_last_task()
            travel_distance = abs(last_stop_y - destination_y)
            potential_finnish_time = last_finnish_time + travel_distance / TRAVEL_SPEED + DELAY_AT_DESTINATION
            if potential_finnish_time < earliest_finnish_time:
                earliest_finnish_time = potential_finnish_time
                optimal_elevator = elevator
        optimal_elevator.add_task(destination, destination_y, earliest_finnish_time)
