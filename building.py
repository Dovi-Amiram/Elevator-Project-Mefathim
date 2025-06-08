from config import *
from elevator import *
from floor import *


class Building:
    def __init__(self, num_of_floors, num_of_elevators):
        canvas_height = WHITE_MARGIN * 2 + FLOOR_HEIGHT * num_of_floors
        canvas_width = WHITE_MARGIN * 2 + FLOOR_WIDTH + (ELEVATOR_WIDTH + WHITE_MARGIN) * num_of_elevators
        self.canvas = pygame.Surface(canvas_width, canvas_height)
        # scaled_elevator_image = pygame.transform.scale(pygame.image.load(ELEVATOR_IMAGE_PATH), ELEVATOR_SIZE)
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

    def draw(self):
        for floor in self.floors:
            floor.draw(self.canvas)
        for elevator in self.elevators:
            elevator.draw(self.canvas)

    def update(self, click_pos):
        for floor in self.floors:
            ordering_floor = floor.ordered_elevator(click_pos)
            if ordering_floor:
                self.allocate_elevator(ordering_floor)
        for elevator in self.elevators:
            elevator.update()

    def allocate_elevator(self, floor_num):
        pass
