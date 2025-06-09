import pygame.time


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
        self.__last_update = pygame.time.get_ticks() / 1000  # convert to seconds
        self.__delta = 0  # delta time

    def update(self) -> None:
        current_time = pygame.time.get_ticks() / 1000  # convert to seconds
        self.__delta = current_time - self.__last_update
        self.__last_update = current_time

    @property
    def dt(self) -> float:
        return self.__delta
