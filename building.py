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
    def handle_click(self, click_pos: tuple[int, int]) -> None:
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
            pos_y = canvas_height - WHITE_MARGIN - (ELEVATOR_HEIGHT + FLOOR_HEIGHT) // 2
            self.elevators.append(Elevator(elevator_num, (pos_x, pos_y)))

    def draw(self) -> None:
        self.canvas.fill(SWAN_WING)
        for floor in self.floors:
            floor.draw(self.canvas)
        for elevator in self.elevators:
            elevator.draw(self.canvas)

    def __elevator_arrival_call_back(self, floor_num: int) -> None:
        floor = self.floors[floor_num]
        floor.elevator_arrived()
        floor.draw(self.canvas)

    def __elevator_departure_call_back(self, floor_num: int) -> None:
        self.floors[floor_num].is_occupied = False

    def handle_click(self, click_pos: tuple[int, int]) -> None:
        for floor in self.floors:
            x, y = click_pos
            floor_x, floor_y = floor.top_left
            ordering_floor = floor.ordered_elevator((x - floor_x, y - floor_y))
            if ordering_floor:
                self.allocate_elevator(ordering_floor)
                return

    def update(self) -> None:
        for floor in self.floors:
            floor.update()
        for elevator in self.elevators:
            elevator.update(self.__elevator_arrival_call_back, self.__elevator_departure_call_back)
        self.draw()

    def allocate_elevator(self, floor_num: int) -> None:
        floor = self.floors[floor_num]
        if floor.is_occupied:
            return
        chosen_elevator = self.elevators[0]
        _, dest_y = floor.top_left
        dest_y += (FLOOR_HEIGHT - ELEVATOR_HEIGHT) // 2
        earliest_arrival_time = chosen_elevator.get_arrival_time_for_potential_trip(dest_y)
        for elevator in self.elevators:
            if elevator is not chosen_elevator:
                arrival_time = elevator.get_arrival_time_for_potential_trip(dest_y)
                if arrival_time < earliest_arrival_time:
                    earliest_arrival_time = arrival_time
                    chosen_elevator = elevator

        floor.awaiting_elevator = True
        floor.set_timer(earliest_arrival_time - get_current_time())
        chosen_elevator.add_destination(floor_num, dest_y, earliest_arrival_time)

