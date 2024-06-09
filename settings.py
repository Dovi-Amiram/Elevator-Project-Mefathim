from static_functions import *
import pygame

MENIVIM_MODE = False
JSON_FILE_PATH = "data.json"
MENIVIM_FILE_PATH = "menivim.json"

FILE_PATH = MENIVIM_FILE_PATH if MENIVIM_MODE else JSON_FILE_PATH
# get data from json file

data = load_json(FILE_PATH)

NUM_OF_ELEVATORS = data["num_of_elevators"]
NUM_OF_LEVELS = data["num_of_levels"] + 1
ELEVATOR_SCALE = (60, 60)
ELEVATOR_IMAGE = pygame.transform.scale(pygame.image.load(data["elevator_img_path"]), ELEVATOR_SCALE)
LEVEL_IMAGE = pygame.image.load(data["level_img_path"])

# constants
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 750
WHITE_MARGIN = 7
BLACK_SPACER_HEIGHT = 7
SCROLL_BAR_WIDTH = 20
SCROLL_BAR_COLOR = (150, 150, 150)
SCROLL_BAR_BG_COLOR = (200, 200, 200)
CAPTION = "Dovi's Elevator Project - Mefathim"
TRAVEL_TIME_PER_LEVEL = 0.5  # in seconds

LEVEL_WIDTH, LEVEL_HEIGHT = LEVEL_IMAGE.get_size()
LEVEL_HEIGHT += BLACK_SPACER_HEIGHT
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
