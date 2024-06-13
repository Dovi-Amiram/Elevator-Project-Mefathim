import time
import pygame
from collections import deque


class Elevator:

    def __init__(self, elevator_num, image, position):
        self.__num = elevator_num
        self.__image = image
        self.__x, self.__y = position
        self.__resting = False
        self.__current_level = 0
        self.__tasks = deque([])
        self.__current_dest_level = None
        self.__current_dest_y = None
        self.__departure_time = None
        self.__departure_y = self.__y
        self.__current_task_finnish_time = 0

    def update(self, elevator_arrived):
        if self.__resting:
            self.__wait()
        elif self.__current_dest_y:
            self.__move(elevator_arrived)
        else:
            self.__config_task()

    def __wait(self):
        current_time = time.time()
        if current_time >= self.__current_task_finnish_time:
            self.__config_task()

    def __move(self, elevator_arrived):
        if self.__y != self.__current_dest_y:
            distance = self.__current_dest_y - self.__y
            direction = distance / abs(distance)
            elapsed_time = time.time() - self.__departure_time
            new_y = self.__departure_y + direction * elapsed_time
            if abs(self.__y - new_y) < abs(self.__y - self.__current_dest_y):
                self.__y = new_y
            else:
                elevator_arrived(self.__current_dest_level)
                self.__y = self.__current_dest_y
                self.__config_task()

    def __config_task(self):
        if len(self.__tasks) > 0:
            self.__resting = False
            self.current_dest_level, self.__current_dest_y, self.__current_task_finnish_time = self.__tasks.popleft()
            self.__departure_y = self.__y
            self.__departure_time = time.time()
        else:
            self.__resting = True
            self.__current_dest_y = None
            self.__current_task_finnish_time = 0
            self.__current_dest_level = None

    def draw(self, world):
        rect = self.__image.get_rect()
        rect.x = self.__x
        rect.y = self.__y
        world.blit(self.__image, rect)

    def add_task(self, destination_level, destination_y, finnish_time):
        self.__tasks.append((destination_level, destination_y, finnish_time))

    def get_last_task(self):
        return self.__tasks[-1] if len(self.__tasks) > 0 else self.__y, 0
