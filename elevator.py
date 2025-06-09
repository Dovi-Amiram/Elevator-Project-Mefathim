from config import *
from typing import *


class Elevator:

    def __init__(self, num: int, pos: tuple[int, int]):
        self.num = num
        self.x, self.y = self.pos = pos
        self.image = pygame.transform.scale(pygame.image.load(ELEVATOR_IMAGE_PATH), ELEVATOR_SIZE)

    def draw(self, canvas) -> None:
        canvas.blit(self.image, self.pos)

    def update(self, arrived_at_dest: Callable) -> None:
        pass
