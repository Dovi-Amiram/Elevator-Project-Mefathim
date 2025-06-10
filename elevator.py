from config import *
from typing import *

from time_keeper import get_current_time, DeltaTime


class Elevator:
    def __init__(self, num: int, pos: tuple[int, int]):
        """
        Params:
            num (int): Elevator ID.
            pos (tuple[int, int]): Initial (x, y) position on the canvas.
        """
        self.num = num

        # Position and visual representation
        self.x, self.y = pos
        self.image = pygame.transform.scale(pygame.image.load(ELEVATOR_IMAGE_PATH), ELEVATOR_SIZE)

        # Movement state
        self.is_moving = False
        self.doors_open = False
        self.current_direction = -1  # Starts moving upward by default

        # Destination and queue
        self.current_dest_y = None
        self.current_dest_floor = 0
        self.queue = []

        # Timing
        self.rest_time = DELAY_AT_DESTINATION
        self.time_when_free = get_current_time()
        self.position_when_free = 0, self.y

    def draw(self, canvas) -> None:
        """
        Params:
            canvas (pygame.Surface): The surface to draw the elevator on.
        """
        canvas.blit(self.image, (self.x, self.y))

    def add_destination(self, dest_floor_num: int, dest_y: int, arrival_time: float) -> None:
        """
        Add a new destination to the elevator's queue.

        Params:
            dest_floor_num (int): Floor number to reach.
            dest_y (int): Y-position of the destination.
            arrival_time (float): Time at which the elevator was assigned the task.
        """
        self.position_when_free = dest_floor_num, dest_y
        self.time_when_free = arrival_time + DELAY_AT_DESTINATION
        self.queue.append(self.position_when_free)

    def get_arrival_time_for_potential_trip(self, dest_y: int) -> float:
        """
        Calculate expected arrival time if elevator were to go to dest_y.

        Params:
            dest_y (int): Y-position of the target floor.

        Returns:
            float: Estimated time of arrival in seconds.
        """
        _, y_when_free = self.position_when_free
        trip_distance = abs(y_when_free - dest_y)
        trip_time = trip_distance * TRAVEL_TIME_PER_FLOOR / FLOOR_HEIGHT
        return self.time_when_free + trip_time

    def update(self, arrival_call_back: Callable, departure_call_back: Callable) -> None:
        """
        Update elevator state (movement, door timing, queue).

        Params:
            arrival_call_back (Callable): Called when elevator arrives at a floor.
            departure_call_back (Callable): Called when elevator departs for a floor.
        """
        if self.is_moving:
            # Move elevator incrementally toward destination
            speed = (FLOOR_HEIGHT / TRAVEL_TIME_PER_FLOOR) * DeltaTime().dt
            step = min(round(speed), abs(self.y - self.current_dest_y))
            self.y += self.current_direction * step

            if self.y == self.current_dest_y:
                self.__arrived()
                arrival_call_back(self.current_dest_floor)

        elif self.doors_open:
            # Count down rest time while doors are open
            self.rest_time -= DeltaTime().dt
            if self.rest_time <= 0:
                self.doors_open = False
                self.rest_time = DELAY_AT_DESTINATION

        elif self.queue:
            # Begin next trip
            departure_call_back(self.current_dest_floor)
            self.__set_next_trip()

        else:
            # Idle: update future position and free time
            self.current_dest_floor, self.current_dest_y = self.position_when_free
            self.time_when_free = get_current_time()

    def __arrived(self) -> None:
        # Handle arrival: stop movement and open doors
        self.is_moving = False
        self.doors_open = True

    def __set_next_trip(self) -> None:
        # Start the next trip in the queue
        self.position_when_free = self.queue[-1]
        self.current_dest_floor, self.current_dest_y = self.queue.pop(0)
        self.is_moving = True
        pos_difference = self.current_dest_y - self.y
        self.current_direction = pos_difference // abs(pos_difference)
