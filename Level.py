import pygame

BLACK = (0, 0, 0)
BUTTON_WIDTH, BUTTON_HEIGHT = 45, 30
BUTTON_COLOR = (220, 220, 220)  # Grey color
TEXT_COLOR = (0, 0, 0)  # Black color
SHADOW_COLOR = (50, 50, 50)
BORDER_COLOR = (30, 30, 30)
FONT_SIZE = 30


class Level:

    def __init__(self, level_num, image, space_height=7, space_color=BLACK):
        self.__space_color = space_color
        self.__space_height = space_height
        self.__image = image
        self.__image_height = image.get_height()
        self.__image_width = image.get_width()
        self.__num = level_num
        self.__top_level = False
        self.__deck = 0

    def draw_self(self, world, x_margin):
        # Calculate the position of the level in the world
        x_pos = x_margin
        y_pos = self.__deck - self.__image_height

        space_x = x_pos
        space_y = y_pos - self.__space_height
        space_rect = pygame.Rect(space_x, space_y, self.__image_width, self.__space_height)

        if not self.__top_level:
            pygame.draw.rect(world, self.__space_color, space_rect)

        # Draw the level image
        world.blit(self.__image, (x_pos, y_pos))

        # Draw the button with the floor number
        button_x = x_pos + (self.__image_width - BUTTON_WIDTH) // 2
        button_y = y_pos + (self.__image_height - BUTTON_HEIGHT) // 2
        button_rect = pygame.Rect(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.draw_button(world, self.__num, button_rect)

    def draw_button(self, surface, floor_number, button_rect):
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

    def display_timer(self, world):
        pass

    def handle_event(self, event):
        pass

    def call_elevator(self):
        pass

    def mark_as_top_level(self):
        self.__top_level = True

    def set_deck(self, world, white_margin):
        world_height = world.get_height()
        self.__deck = world_height - ((white_margin + self.__image_height) * self.__num + white_margin)

    def get_deck(self):
        return self.__deck

    def get_num(self):
        return self.__num
