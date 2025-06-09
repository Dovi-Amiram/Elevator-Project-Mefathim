import pygame

from config import *
from typing import *


class Floor:

    def __init__(self, level: int, pos: tuple[int, int]):
        self.level = level
        self.top_left = pos
        self.image = pygame.image.load(FLOOR_IMAGE_PATH)
        self.button_center = FLOOR_WIDTH // 2, (FLOOR_HEIGHT + FLOOR_SPACER) // 2
        self.awaiting_elevator = False
        self.spacer_rect = pygame.Rect(0, 0, FLOOR_WIDTH, FLOOR_SPACER)
        self.__initial_image_setup()
        self.color_button()

    def color_button(self) -> None:
        color = LIME_GREEN if self.awaiting_elevator else BLACK
        # Draw outline (black)
        pygame.draw.circle(self.image, color, self.button_center, BUTTON_RADIUS, width=2)

        # Draw level number in center
        text = str(self.level) if self.level > 0 else "E"
        font = pygame.font.SysFont(None, FONT_SIZE)
        font_surface = font.render(text, True, color)
        text_rect = font_surface.get_rect(center=self.button_center)
        self.image.blit(font_surface, text_rect)

    def __initial_image_setup(self) -> None:
        # draw spacer
        # spacer_start_pos = x_top_left, y_top_left = self.top_left
        # spacer_end_pos = x_top_left + FLOOR_WIDTH, y_top_left
        pygame.draw.rect(self.image, BLACK, self.spacer_rect)

        # Set dimensions
        shadow_w, shadow_h = BUTTON_RADIUS * 2, BUTTON_RADIUS * 2

        # Create shadow surface (transparent background)
        shadow_surface = pygame.Surface((shadow_w, shadow_h), pygame.SRCALPHA)

        # Draw shadow (black or semi-transparent black)
        pygame.draw.circle(shadow_surface, (0, 0, 0, 100), (shadow_w // 2, shadow_h // 2), BUTTON_RADIUS)
        # Blit shadow to the main surface at offset position
        shadow_x_offset = -3
        shadow_y_offset = 2
        x, y = self.button_center

        # blit shadow
        self.image.blit(shadow_surface, (x + shadow_x_offset - BUTTON_RADIUS, y + shadow_y_offset - BUTTON_RADIUS))

        # Draw main button (grey)
        pygame.draw.circle(self.image, (169, 169, 169), self.button_center, BUTTON_RADIUS)

    def draw(self, canvas: pygame.Surface) -> None:
        self.color_button()
        canvas.blit(self.image, self.top_left)

    def update(self):
        # timer update
        pass

    def ordered_elevator(self, click_pos: tuple[int, int]) -> Union[int, None]:
        x1, y1 = click_pos
        x2, y2 = self.button_center
        on_button = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 <= BUTTON_RADIUS # euclidian distance
        if on_button:
            self.awaiting_elevator = True
            return self.level

    def elevator_arrived(self) -> None:
        self.awaiting_elevator = False
