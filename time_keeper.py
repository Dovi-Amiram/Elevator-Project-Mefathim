import pygame.time


def get_current_time() -> float:
    """
    Returns:
        float: Current time in seconds since Pygame was initialized.
    """
    return pygame.time.get_ticks() / 1000


def singleton(class_):
    """
    Singleton decorator. Ensures only one instance of the class is created.

    Params:
        class_ (type): Class to be made a singleton.

    Returns:
        Callable: A function that returns the singleton instance.
    """
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class DeltaTime:
    """
    Tracks time elapsed between frames. Should be updated once per frame.
    """

    def __init__(self):
        self.__last_update = get_current_time()
        self.__delta_time = 0.0

    def update(self) -> None:
        """
        Update the internal delta time. Call once per frame.
        """
        current_time = get_current_time()
        self.__delta_time = current_time - self.__last_update
        self.__last_update = current_time

    @property
    def dt(self) -> float:
        """
        Returns:
            float: Time (in seconds) elapsed since last update.
        """
        return self.__delta_time
