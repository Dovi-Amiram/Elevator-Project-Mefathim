import pygame

from config import *
from typing import *

from time_keeper import DeltaTime

pygame.mixer.init()


class Floor:
    # Class-level sound: loaded once for all instances
    ding = pygame.mixer.Sound(DING_SOUND_PATH)

    def __init__(self, level: int, pos: tuple[int, int]):
        """
        Params:
            level (int): The floor number (0 for entrance).
            pos (tuple[int, int]): The (x, y) top-left coordinate on the canvas.
        """
        self.image = pygame.image.load(FLOOR_IMAGE_PATH)
        self.level = level
        self.top_left = pos
        self.button_center = FLOOR_WIDTH // 2, (FLOOR_HEIGHT + FLOOR_SPACER) // 2
        self.awaiting_elevator = False
        self.is_occupied = True if level == 0 else False
        self.timer = 0


    def draw_timer(self) -> None:
        # Draw the timer and its background beside the button
        font = pygame.font.SysFont("Consolas", TIMER_FONT_SIZE, bold=True)
        text = str(round(self.timer, 2))
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect()

        padding = 3
        bg_rect = pygame.Rect(0, 0, text_rect.width + 2 * padding, text_rect.height + 2 * padding)

        x, y = self.button_center
        bg_rect.topleft = (x + BUTTON_RADIUS + WHITE_MARGIN, y - BUTTON_RADIUS)

        pygame.draw.rect(self.image, WHITE, bg_rect)
        text_rect.topleft = (bg_rect.left + padding, bg_rect.top + padding)
        self.image.blit(text_surface, text_rect)

    def draw_button(self) -> None:
        # Draw the button with shadow, circle, outline, and floor label
        shadow_w, shadow_h = BUTTON_RADIUS * 2, BUTTON_RADIUS * 2
        shadow_surface = pygame.Surface((shadow_w, shadow_h), pygame.SRCALPHA)
        pygame.draw.circle(shadow_surface, (0, 0, 0, 100), (shadow_w // 2, shadow_h // 2), BUTTON_RADIUS)

        shadow_x_offset = -3
        shadow_y_offset = 2
        x, y = self.button_center
        self.image.blit(shadow_surface, (x + shadow_x_offset - BUTTON_RADIUS, y + shadow_y_offset - BUTTON_RADIUS))

        pygame.draw.circle(self.image, (169, 169, 169), self.button_center, BUTTON_RADIUS)

        color = LIME_GREEN if self.awaiting_elevator else BLACK
        pygame.draw.circle(self.image, color, self.button_center, BUTTON_RADIUS, width=2)

        text = str(self.level) if self.level > 0 else "E"
        font = pygame.font.SysFont("Arial Bold", BUTTON_FONT_SIZE)
        font_surface = font.render(text, True, color)
        text_rect = font_surface.get_rect(center=self.button_center)
        self.image.blit(font_surface, text_rect)

    def draw(self, canvas: pygame.Surface) -> None:
        """
        Params:
            canvas (pygame.Surface): The screen to draw this floor on.
        """
        pygame.draw.rect(self.image, BLACK, (0, 0, FLOOR_WIDTH, FLOOR_SPACER))
        self.draw_button()
        if self.awaiting_elevator and self.timer > 0:
            self.draw_timer()
        canvas.blit(self.image, self.top_left)

    def set_timer(self, time: float) -> None:
        self.timer = time

    def update(self) -> None:
        # Update the countdown and handle elevator arrival if time runs out
        if self.awaiting_elevator and self.timer > 0:
            self.timer -= DeltaTime().dt
            if self.timer <= 0:
                self.timer = 0
                self.elevator_arrived()

    def ordered_elevator(self, click_pos: tuple[int, int]) -> Union[int, None]:
        """
        Params:
            click_pos (tuple[int, int]): The position of the mouse click.

        Returns:
            int | None: The floor level if the call button was clicked; otherwise None.
        """
        x1, y1 = click_pos
        x2, y2 = self.button_center
        on_button = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 <= BUTTON_RADIUS
        if not self.is_occupied and on_button:
            return self.level

    def elevator_arrived(self) -> None:
        # Handle elevator arrival: mark occupied, play sound, reset image
        self.awaiting_elevator = False
        self.is_occupied = True
        Floor.ding.play()
        self.image = pygame.image.load(FLOOR_IMAGE_PATH)
