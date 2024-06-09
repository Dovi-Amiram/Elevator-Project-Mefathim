import json


JSON_FILE_PATH = "data.json"
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 750
WHITE_MARGIN = 7
BLACK_SPACER_HEIGHT = 7
SCROLL_BAR_WIDTH = 20
SCROLL_BAR_COLOR = (150, 150, 150)
SCROLL_BAR_BG_COLOR = (200, 200, 200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CAPTION = "Dovi's Elevator Project - Mefathim"


def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


data = load_json(JSON_FILE_PATH)


def calculate_world_height(num_of_levels, level_height):
    # Calculate the total height of the world dynamically
    total_level_height = (
            num_of_levels * (level_height + BLACK_SPACER_HEIGHT) - BLACK_SPACER_HEIGHT)
    return total_level_height + 2 * WHITE_MARGIN



