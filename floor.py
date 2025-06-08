import pygame

from config import *


class Floor:

    def __init__(self, level, pos):
        self.level = level
        self.top_left = pos
        # self.images = {"regular": image, "button_compressed": image.copy(), "awaiting_elevator": image.copy()}
        # self.image = None
        # self.reg_rect, self.compressed_rect = self.__set_up_images(ceiling_color)
        # self.button_compressed = False
        self.awaiting_elevator = False

    def draw(self, canvas):
        pass

    def ordered_elevator(self, click_pos):
        pass

    # def __set_up_images(self, ceiling_color):
    #     reg, comp = None, None
    #     for image_type in self.images:
    #         current_image = self.images[image_type]
    #         x, y = current_image.get_rect().center
    #         y += FLOOR_SPACER // 2
    #
    #         if image_type != "button_compressed":
    #             # draw shadow
    #             w, h = BUTTON_RADIUS * 2, BUTTON_RADIUS * 2
    #             shadow_surface = pygame.Surface((w, h), pygame.SRCALPHA)  # Transparent surface
    #             button_rect = pygame.draw.circle(shadow_surface, SHADOW_COLOR, (w // 2, h // 2), BUTTON_RADIUS)
    #             button_rect.center = x, y
    #             current_image.blit(shadow_surface, button_rect)
    #
    #             # draw button
    #             shadow_x_offset = -5
    #             shadow_y_offset = 2
    #             x, y = x + shadow_x_offset, y + shadow_y_offset
    #         if image_type == "button_compressed":
    #             comp = pygame.draw.circle(current_image, LIGHT_GREY, (x, y), BUTTON_RADIUS)
    #         elif image_type == "regular":
    #             reg = pygame.draw.circle(current_image, LIGHT_GREY, (x, y), BUTTON_RADIUS)
    #         # draw button outline
    #         outline_color = LIME_GREEN if image_type == "awaiting_elevator" else VERY_DARK_GREY
    #         pygame.draw.circle(current_image, outline_color, (x, y), BUTTON_RADIUS, width=2)
    #
    #         # draw floor num
    #         text = str(self.level) if self.level > 0 else "E"
    #         text_color = outline_color
    #         font = pygame.font.SysFont(None, FONT_SIZE)
    #         font_surface = font.render(text, True, text_color)
    #         text_rect = font_surface.get_rect()
    #         text_rect.center = x, y
    #         current_image.blit(font_surface, text_rect)
    #
    #         # draw ceiling
    #         pygame.draw.rect(current_image, ceiling_color, pygame.Rect(0, 0, FLOOR_WIDTH, FLOOR_SPACER))
    #     return reg, comp
    #
    # def draw(self, canvas):
    #     x, base_y = WHITE_MARGIN, canvas.get_height() - WHITE_MARGIN - FLOOR_HEIGHT
    #     y = base_y - FLOOR_HEIGHT * self.level
    #     canvas.blit(self.image, (x, y))
    #
    # def button_pressed(self, pos):
    #     x, y = pos
    #     if self.reg_rect.collidepoint(x, y):
    #         self.button_compressed = True
    #
    # def update(self):
    #     if self.button_compressed:
    #         self.image = self.images["button_compressed"]
    #     elif self.awaiting_elevator:
    #         self.image = self.images["awaiting_elevator"]
    #     else:
    #         self.image = self.images["regular"]
