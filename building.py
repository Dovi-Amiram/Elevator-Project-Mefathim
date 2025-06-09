import pygame
from elevator import *
from floor import *
from abc import ABC, abstractmethod


class AbstractBuilding(ABC):

    def __init__(self, num_of_floors, num_of_elevators):
        canvas_height = WHITE_MARGIN * 2 + FLOOR_HEIGHT * num_of_floors
        canvas_width = WHITE_MARGIN * 2 + FLOOR_WIDTH + (ELEVATOR_WIDTH + WHITE_MARGIN) * num_of_elevators
        self.canvas = pygame.Surface((canvas_width, canvas_height))

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def handle_click(self, click_pos) -> None:
        pass


class Building(AbstractBuilding):
    def __init__(self, num_of_floors, num_of_elevators):
        super().__init__(num_of_floors, num_of_elevators)

        canvas_height = self.canvas.get_height()

        # create floors
        self.floors = []
        for level in range(num_of_floors):
            pos = (WHITE_MARGIN, canvas_height - WHITE_MARGIN - (level + 1) * FLOOR_HEIGHT)
            self.floors.append(Floor(level, pos))

        # create elevators
        self.elevators = []
        for elevator_num in range(num_of_elevators):
            pos_x = WHITE_MARGIN * 2 + FLOOR_WIDTH + ELEVATOR_WIDTH * elevator_num
            pos_y = canvas_height - WHITE_MARGIN - ELEVATOR_HEIGHT // 2 - FLOOR_HEIGHT // 2
            self.elevators.append(Elevator(elevator_num, (pos_x, pos_y)))

    def draw(self) -> None:
        self.canvas.fill(SWAN_WING)
        for floor in self.floors:
            floor.draw(self.canvas)
        for elevator in self.elevators:
            elevator.draw(self.canvas)

    def __elevator_call_back(self, floor_num) -> None:
        floor = self.floors[floor_num]
        floor.elevator_arrived()
        floor.draw(self.canvas)

    def handle_click(self, click_pos) -> None:
        for floor in self.floors:
            ordering_floor = floor.ordered_elevator(click_pos)
            if ordering_floor:
                self.allocate_elevator(ordering_floor)

    def update(self) -> None:
        for floor in self.floors:
            floor.update()
        for elevator in self.elevators:
            elevator.update(self.__elevator_call_back)
        self.draw()

    def allocate_elevator(self, floor_num: int) -> None:
        pass
