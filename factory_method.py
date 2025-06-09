from building import *

def building_factory(num_of_floors: int, num_of_elevators: int,
                     building_type: Optional[str] = None) -> AbstractBuilding:
    match building_type:
        case _:
            return Building(num_of_floors, num_of_elevators)