import pygame.time

def get_current_time() -> float:
    return pygame.time.get_ticks() / 1000  # convert to seconds

def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class DeltaTime:

    def __init__(self):
        self.__last_update = get_current_time()  # convert to seconds
        self.__delta_time = 0  # delta time

    def update(self) -> None:
        current_time = get_current_time()  # convert to seconds
        self.__delta_time = current_time - self.__last_update
        self.__last_update = current_time

    @property
    def dt(self) -> float:
        return self.__delta_time
