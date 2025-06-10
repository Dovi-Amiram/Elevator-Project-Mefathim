import pygame
from abc import ABC, abstractmethod
from typing import *

from elevator import *
from floor import *


class AbstractBuilding(ABC):
    def __init__(self, num_of_floors: int, num_of_elevators: int):
        """
        Params:
            num_of_floors (int): Total number of floors.
            num_of_elevators (int): Total number of elevators.
        """
        canvas_height = WHITE_MARGIN * 2 + FLOOR_HEIGHT * num_of_floors
        canvas_width = WHITE_MARGIN * 2 + FLOOR_WIDTH + (ELEVATOR_WIDTH + WHITE_MARGIN) * num_of_elevators
        self.canvas = pygame.Surface((canvas_width, canvas_height))

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def handle_click(self, click_pos: tuple[int, int]) -> None:
        pass


class Building(AbstractBuilding):
    def __init__(self, num_of_floors: int, num_of_elevators: int):
        """
        Params:
            num_of_floors (int): Number of floors in the building.
            num_of_elevators (int): Number of elevators in the building.
        """
        super().__init__(num_of_floors, num_of_elevators)
        canvas_height = self.canvas.get_height()

        # Create floor objects
        self.floors = []
        for level in range(num_of_floors):
            pos = (WHITE_MARGIN, canvas_height - WHITE_MARGIN - (level + 1) * FLOOR_HEIGHT)
            self.floors.append(Floor(level, pos))

        # Create elevator objects
        self.elevators = []
        for elevator_num in range(num_of_elevators):
            pos_x = WHITE_MARGIN * 2 + FLOOR_WIDTH + ELEVATOR_WIDTH * elevator_num
            pos_y = canvas_height - WHITE_MARGIN - (ELEVATOR_HEIGHT + FLOOR_HEIGHT) // 2
            self.elevators.append(Elevator(elevator_num, (pos_x, pos_y)))

    def draw(self) -> None:
        """
        Draw all building components to the canvas.
        """
        self.canvas.fill(SWAN_WING)
        for floor in self.floors:
            floor.draw(self.canvas)
        for elevator in self.elevators:
            elevator.draw(self.canvas)

    def update(self) -> None:
        """
        Update all floors and elevators and redraw the canvas.
        """
        for floor in self.floors:
            floor.update()
        for elevator in self.elevators:
            elevator.update(self.__elevator_arrival_call_back, self.__elevator_departure_call_back)
        self.draw()

    def handle_click(self, click_pos: tuple[int, int]) -> None:
        """
        Handle a mouse click to potentially order an elevator.

        Params:
            click_pos (tuple[int, int]): The click position relative to the screen.
        """
        for floor in self.floors:
            x, y = click_pos
            floor_x, floor_y = floor.top_left
            relative_click = (x - floor_x, y - floor_y)
            ordering_floor = floor.ordered_elevator(relative_click)
            if ordering_floor is not None:
                self.allocate_elevator(ordering_floor)
                return

    def allocate_elevator(self, floor_num: int) -> None:
        """
        Choose the best elevator and assign it to the given floor.

        Params:
            floor_num (int): The requested floor number.
        """
        floor = self.floors[floor_num]
        if floor.is_occupied:
            return

        # Find elevator with earliest arrival time
        chosen_elevator = self.elevators[0]
        _, dest_y = floor.top_left
        dest_y += (FLOOR_HEIGHT - ELEVATOR_HEIGHT) // 2
        earliest_arrival_time = chosen_elevator.get_arrival_time_for_potential_trip(dest_y)

        for elevator in self.elevators[1:]:
            arrival_time = elevator.get_arrival_time_for_potential_trip(dest_y)
            if arrival_time < earliest_arrival_time:
                earliest_arrival_time = arrival_time
                chosen_elevator = elevator

        floor.awaiting_elevator = True
        floor.set_timer(earliest_arrival_time - get_current_time())
        chosen_elevator.add_destination(floor_num, dest_y, earliest_arrival_time)

    def __elevator_arrival_call_back(self, floor_num: int) -> None:
        # Called when an elevator arrives at a floor
        floor = self.floors[floor_num]
        floor.elevator_arrived()
        floor.draw(self.canvas)

    def __elevator_departure_call_back(self, floor_num: int) -> None:
        # Called when an elevator leaves a floor
        self.floors[floor_num].is_occupied = False
