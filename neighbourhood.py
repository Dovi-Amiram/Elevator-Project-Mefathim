from delta_time import DeltaTime
from factory_method import *


class Neighbourhood:
    def __init__(self):
        self.buildings = [building_factory(*specs) for specs in BUILDINGS.values()]
        max_canvas_height = max([building.canvas.get_height() for building in self.buildings])
        canvas_height = max(max_canvas_height, WINDOW_HEIGHT)
        canvas_width = sum([building.canvas.get_width() for building in self.buildings])
        self.canvas = pygame.Surface((canvas_width, canvas_height))
        self.building_borders = {}
        current_left = 0
        for i, building in enumerate(self.buildings):
            current_width = self.buildings[i].canvas.get_width()
            self.building_borders[i] = (current_left, current_left + current_width)
            current_left += current_width

    def handle_click(self, pos: tuple[int, int]) -> None:
        x, _ = pos
        for i, building in enumerate(self.buildings):
            left, right = self.building_borders[i]
            if left < x < right:
                building.handle_click(pos)
                return

    def draw(self):
        self.canvas.fill(SWAN_WING)
        for i, building in enumerate(self.buildings):
            x_top_left, _ = self.building_borders[i]
            y_top_left = self.canvas.get_height() - self.buildings[i].canvas.get_height()
            top_left = x_top_left, y_top_left
            self.canvas.blit(building.canvas, top_left)

    def update(self):
        for building in self.buildings:
            building.update()
        self.draw()
