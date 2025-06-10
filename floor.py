import pygame

from config import *
from typing import *

from time_keeper import DeltaTime


class Floor:

    def __init__(self, level: int, pos: tuple[int, int]):
        self.image = pygame.image.load(FLOOR_IMAGE_PATH)
        self.level = level
        self.top_left = pos
        self.button_center = FLOOR_WIDTH // 2, (FLOOR_HEIGHT + FLOOR_SPACER) // 2
        self.awaiting_elevator = False
        self.is_occupied = True if level == 0 else False
        self.timer = 0

    def set_timer(self, time):
        self.timer = time

    def draw_timer(self):

        font = pygame.font.SysFont(None, FONT_SIZE + 4)  # Slightly larger text
        text = str(round(self.timer, 2))
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()

        # Add padding around the text
        padding = 3
        bg_rect = pygame.Rect(0, 0, text_rect.width + 2 * padding, text_rect.height + 2 * padding)

        # Position the background rectangle relative to the button center
        x, y = self.button_center
        bg_rect.topleft = (x + BUTTON_RADIUS + WHITE_MARGIN, y - BUTTON_RADIUS)

        # Draw white background
        pygame.draw.rect(self.image, WHITE, bg_rect)

        # Position text inside background rect
        text_rect.topleft = (bg_rect.left + padding, bg_rect.top + padding)

        # Blit the text
        self.image.blit(text_surface, text_rect)

    def draw(self, canvas: pygame.Surface) -> None:


        pygame.draw.rect(self.image, BLACK, (0, 0, FLOOR_WIDTH, FLOOR_SPACER))

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

        color = LIME_GREEN if self.awaiting_elevator else BLACK
        # Draw outline (black)
        pygame.draw.circle(self.image, color, self.button_center, BUTTON_RADIUS, width=2)

        # Draw level number in center
        text = str(self.level) if self.level > 0 else "E"
        font = pygame.font.SysFont(None, FONT_SIZE)
        font_surface = font.render(text, True, color)
        text_rect = font_surface.get_rect(center=self.button_center)
        self.image.blit(font_surface, text_rect)

        if self.awaiting_elevator and self.timer > 0:
            self.draw_timer()
        canvas.blit(self.image, self.top_left)

    def update(self):
        if self.awaiting_elevator and self.timer > 0:
            self.timer -= DeltaTime().dt
            if self.timer <= 0:
                self.timer = 0
                self.elevator_arrived()

    def ordered_elevator(self, click_pos: tuple[int, int]) -> Union[int, None]:
        x1, y1 = click_pos
        x2, y2 = self.button_center
        on_button = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 <= BUTTON_RADIUS  # euclidian distance
        if not self.is_occupied and on_button:
            return self.level

    def elevator_arrived(self) -> None:
        self.awaiting_elevator = False
        self.is_occupied = True
        self.image = pygame.image.load(FLOOR_IMAGE_PATH)
