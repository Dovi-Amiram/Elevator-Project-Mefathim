import pygame
from settings import *

FONT_SIZE = 30
BUTTON_SHADOW_OFFSET = 4


class Level:

    def __init__(self, level_num, image, rect):
        self.__num = level_num
        self.__image = image
        self.__rect = rect
        self.__elevator_on_the_way = self.__num == 0
        self.__display_timer = False
        self.__timer = 0
        self.__button_rect = None
        self.__set_up_button_rect()
        self.__button_color = pygame.Color("gray65")
        self.__shadow_color = pygame.Color("gray20")
        self.__font_color = pygame.Color("gray15")
        self.__font = pygame.font.SysFont(None, FONT_SIZE)

    def __set_up_button_rect(self):
        button_width = self.__rect.width // 3
        button_height = self.__rect.height // 3
        self.__button_rect = pygame.Rect(0, 0, button_width, button_height)
        self.__button_rect.center = self.__rect.center

    def __draw_button(self, world):
        # Draw the shadow first
        shadow_rect = self.__button_rect.move(BUTTON_SHADOW_OFFSET, BUTTON_SHADOW_OFFSET)
        pygame.draw.rect(world, self.__shadow_color, shadow_rect)

        # Draw the button
        pygame.draw.rect(world, self.__button_color, self.__button_rect)

        # Draw the level number on the button
        text_surface = self.__font.render(str(self.__num), True, self.__font_color)
        text_rect = text_surface.get_rect(center=self.__button_rect.center)
        world.blit(text_surface, text_rect)

    def draw(self, world):
        world.blit(self.__image, self.__rect)
        self.__draw_button(world)

    def update(self):
        pass

    def elevator_arrived(self):
        self.__button_color = BUTTON_COLOR
        self.__display_timer = False
        ding = pygame.mixer.Sound(DING_FILE_PATH)
        ding.play()

    def get_num(self):
        return self.__num

    def elevator_on_the_way(self):
        return self.__elevator_on_the_way

    def check_call(self, x, y):
        if self.__button_rect.collidepoint(x, y):
            print(x, y)
            print(self.__button_rect)
            self.__button_color = pygame.Color("green")
            self.__elevator_on_the_way = True
            print(self.__num)
            return True
        return False

    def get_ceiling_y(self):
        return self.__rect.y

    def get_height(self):
        return self.__rect.height
