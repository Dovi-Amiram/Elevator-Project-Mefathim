from static_functions import *
import pygame

MENIVIM_MODE = False
JSON_FILE_PATH = "data.json"
MENIVIM_FILE_PATH = "menivim.json"

FILE_PATH = MENIVIM_FILE_PATH if MENIVIM_MODE else JSON_FILE_PATH
# get data from json file

data = load_json(FILE_PATH)

DING_FILE_PATH = "ding.mp3"
NUM_OF_ELEVATORS = data["num_of_elevators"]
NUM_OF_LEVELS = data["num_of_levels"] + 1
ELEVATOR_SCALE = (60, 60)
ELEVATOR_IMAGE = pygame.transform.scale(pygame.image.load(data["elevator_image"]), ELEVATOR_SCALE)
LEVEL_IMAGE = pygame.image.load(data["level_image"])

# constants
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 750
WHITE_MARGIN = 7
BLACK_SPACER_HEIGHT = 7

BUTTON_WIDTH, BUTTON_HEIGHT = 45, 30
BUTTON_COLOR = (220, 220, 220)  # Grey color
TEXT_COLOR = pygame.Color("black")  # Black color
SHADOW_COLOR = (50, 50, 50)
BORDER_COLOR = (30, 30, 30)
FONT_SIZE = 30

CAPTION = "Dovi's Elevator Project - Mefathim"
TRAVEL_TIME_PER_LEVEL = 0.5  # in seconds

LEVEL_WIDTH, LEVEL_HEIGHT = LEVEL_IMAGE.get_size()
LEVEL_HEIGHT += BLACK_SPACER_HEIGHT

LEVEL_RECT = LEVEL_IMAGE.get_rect()
LEVEL_RECT.height = LEVEL_HEIGHT
LEVEL_RECT.topleft = (WHITE_MARGIN, 0)

ELEVATOR_WIDTH, ELEVATOR_HEIGHT = ELEVATOR_IMAGE.get_size()

TRAVEL_SPEED = int((LEVEL_HEIGHT + BLACK_SPACER_HEIGHT) / TRAVEL_TIME_PER_LEVEL)
DELAY_AT_DESTINATION = 2  # in seconds

WORLD_HEIGHT = NUM_OF_LEVELS * LEVEL_HEIGHT + 2 * WHITE_MARGIN
WORLD_WIDTH = WINDOW_WIDTH

# update window height to fit building height
WINDOW_HEIGHT = min(WINDOW_HEIGHT, WORLD_HEIGHT)

# colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
