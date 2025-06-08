from config import *


class Elevator:

    def __init__(self, num, pos):
        self.num = num
        self.x, self.y = pos

    # def __set_initial_position(self, canvas_height):
    #     w, h = self.image.get_size()
    #     base_x, y = WHITE_MARGIN * 3 + FLOOR_WIDTH, canvas_height - WHITE_MARGIN - h // 2 - FLOOR_HEIGHT // 2
    #     x = base_x + (w + WHITE_MARGIN) * self.num
    #     return x, y

    def update(self):
        pass

    def draw(self, canvas):
        pos = self.x, self.y
        canvas.blit(self.image, pos)
