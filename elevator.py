from config import *


class Elevator:

    def __init__(self, num, image, canvas_height):
        self.num = num
        self.image = image
        self.x, self.y = self.__set_initial_position(canvas_height)

    def __set_initial_position(self, canvas_height):
        w, h = self.image.get_size()
        base_x, y = WHITE_MARGIN * 3 + FLOOR_WIDTH, canvas_height - WHITE_MARGIN - h // 2 - FLOOR_HEIGHT // 2
        x = base_x + (w + WHITE_MARGIN) * self.num
        return x, y

    def draw(self, canvas):
        pos = self.x, self.y
        canvas.blit(self.image, pos)
