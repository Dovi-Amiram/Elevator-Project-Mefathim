import json


def get_travel_distance(source, destination, level_height):
    return abs(source - destination) * level_height


def load_json(file_path):
    with open(file_path, 'r') as file:
        data_dict = json.load(file)
    return data_dict
