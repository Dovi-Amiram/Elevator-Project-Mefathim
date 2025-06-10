from config import *
from typing import *

from time_keeper import get_current_time, DeltaTime


class Elevator:

    def __init__(self, num: int, pos: tuple[int, int]):
        self.num = num
        self.x, self.y = pos
        self.image = pygame.transform.scale(pygame.image.load(ELEVATOR_IMAGE_PATH), ELEVATOR_SIZE)
        self.is_moving = False
        self.current_dest_y = None
        self.queue = []
        self.current_dest_floor = 0
        self.doors_open = False
        self.rest_time = DELAY_AT_DESTINATION
        self.time_when_free = get_current_time()
        self.position_when_free = 0, self.y
        self.current_direction = -1  # initial direction set to UP (because all elevators start at the entrance floor)

    def draw(self, canvas) -> None:
        canvas.blit(self.image, (self.x, self.y))

    def add_destination(self, dest_floor_num: int, dest_y: int, arrival_time: float) -> None:
        self.position_when_free = dest_floor_num, dest_y
        self.time_when_free = arrival_time + DELAY_AT_DESTINATION
        self.queue.append(self.position_when_free)

    def __set_next_trip(self) -> None:
        self.position_when_free = self.queue[-1]
        self.current_dest_floor, self.current_dest_y = self.queue.pop(0)
        self.is_moving = True
        pos_difference = self.current_dest_y - self.y
        self.current_direction = pos_difference // abs(pos_difference)  # will be -1 if up, and 1 if down


    def __arrived(self) -> None:
        self.is_moving = False
        self.doors_open = True
        # TODO: ding

    def get_arrival_time_for_potential_trip(self, dest_y) -> float:
        _, y_when_free = self.position_when_free
        trip_distance = abs(y_when_free - dest_y)
        trip_time = trip_distance * TRAVEL_TIME_PER_FLOOR / FLOOR_HEIGHT
        return self.time_when_free + trip_time

    def update(self, arrival_call_back: Callable, departure_call_back: Callable) -> None:

        if self.is_moving:
            absolute_travel_distance = min(round((FLOOR_HEIGHT / TRAVEL_TIME_PER_FLOOR) * DeltaTime().dt),
                                           abs(self.y - self.current_dest_y))
            self.y += self.current_direction * absolute_travel_distance

            if self.y == self.current_dest_y:
                self.__arrived()
                arrival_call_back(self.current_dest_floor)

        elif self.doors_open:
            self.rest_time -= DeltaTime().dt
            if self.rest_time <= 0:
                self.doors_open = False
                self.rest_time = DELAY_AT_DESTINATION

        elif self.queue:
            departure_call_back(self.current_dest_floor)
            self.__set_next_trip()

        else:
            self.current_dest_floor, self.current_dest_y = self.position_when_free
            self.time_when_free = get_current_time()
