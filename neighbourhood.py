from time_keeper import DeltaTime
from factory_method import *


class Neighbourhood:
    def __init__(self):
        """
        Initialize all buildings in the neighbourhood and construct a unified canvas.
        """
        self.buildings = [building_factory(*specs) for specs in BUILDINGS.values()]

        # Determine canvas dimensions
        max_canvas_height = max(building.canvas.get_height() for building in self.buildings)
        canvas_height = max(max_canvas_height, WINDOW_HEIGHT)
        canvas_width = sum(building.canvas.get_width() for building in self.buildings)
        self.canvas = pygame.Surface((canvas_width, canvas_height))

        # Track building boundaries for click detection
        self.building_borders = {}
        current_left = 0
        for i, building in enumerate(self.buildings):
            current_width = building.canvas.get_width()
            self.building_borders[i] = (current_left, current_left + current_width)
            current_left += current_width

    def handle_click(self, pos: tuple[int, int]) -> None:
        """
        Params:
            pos (tuple[int, int]): Global click position on the canvas.

        Routes the click to the appropriate building.
        """
        x, y = pos
        for i, building in enumerate(self.buildings):
            left, right = self.building_borders[i]
            if left < x < right:
                relative_pos = (x - left, y - (self.canvas.get_height() - building.canvas.get_height()))
                building.handle_click(relative_pos)
                return

    def update(self) -> None:
        """
        Update all buildings and redraw the canvas.
        """
        for building in self.buildings:
            building.update()
        self.draw()

    def draw(self) -> None:
        """
        Blit all building canvases onto the neighbourhood canvas.
        """
        self.canvas.fill(SWAN_WING)
        for i, building in enumerate(self.buildings):
            x_top_left = self.building_borders[i][0]
            y_top_left = self.canvas.get_height() - building.canvas.get_height()
            self.canvas.blit(building.canvas, (x_top_left, y_top_left))
