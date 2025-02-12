from config import *
from elevator import *
from floor import *


class Building:
    def __init__(self, num_of_floors, num_of_elevators, canvas_height):
        scaled_elevator_image = pygame.transform.scale(pygame.image.load(ELEVATOR_IMAGE_PATH), ELEVATOR_SIZE)
        # create floors
        self.floors = [Floor(i, pygame.image.load(FLOOR_IMAGE_PATH)) for i in range(num_of_floors - 1)]
        self.floors.append(Floor(num_of_floors - 1, pygame.image.load(FLOOR_IMAGE_PATH), ceiling_color=GREY))
        # create elevators
        self.elevators = [Elevator(i, scaled_elevator_image.copy(), canvas_height) for i in range(num_of_elevators)]

    def draw(self, canvas):
        for floor in self.floors:
            floor.draw(canvas)
        for elevator in self.elevators:
            elevator.draw(canvas)

    def update(self):
        for floor in self.floors:
            floor.update()

    def allocate_elevator(self, level):
        pass
