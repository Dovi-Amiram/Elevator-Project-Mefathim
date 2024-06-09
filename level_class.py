import pygame
from settings import *

class Level:

    def __init__(self, level_num, image):
        self.__num = level_num
        self.__image = image
        self.__rect = None
        self.__deck = 0
        self.__x = 0
        self.__y = 0

    def draw(self, world):
        # Calculate the position of the level in the world
        # Draw the level image
        world.blit(self.__image, self.__rect)
        self.__draw_black_space()
        self.__draw_button()

        # # Draw the button with the floor number
        # button_x = x_pos + (self.__image_width - BUTTON_WIDTH) // 2
        # button_y = y_pos + (self.__image_height - BUTTON_HEIGHT) // 2
        # button_rect = pygame.Rect(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        # self.draw_button(world, self.__num, button_rect)

    def __draw_button(self, surface, floor_number, button_rect):
        # Draw the shadow effect
        shadow_rect = button_rect.move(3, 3)
        pygame.draw.rect(surface, SHADOW_COLOR, shadow_rect, border_radius=10)

        # Draw the button rectangle with border
        pygame.draw.rect(surface, BUTTON_COLOR, button_rect, border_radius=10)
        pygame.draw.rect(surface, BORDER_COLOR, button_rect, 2, border_radius=10)

        # Create the text surface with the floor number
        font = pygame.font.Font(None, FONT_SIZE)  # You can choose any font and size
        text_surface = font.render(str(floor_number), True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=button_rect.center)

        # Draw the text on the button
        surface.blit(text_surface, text_rect)

    def set_rect(self, rect):
        self.__rect = rect

    def get_num(self):
        return self.__num
