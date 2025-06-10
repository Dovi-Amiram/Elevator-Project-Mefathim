from building import *

def building_factory(num_of_floors: int, num_of_elevators: int,
                     building_type: Optional[str] = None) -> AbstractBuilding:
    """
    Create a building instance with the specified number of floors and elevators.

    Params:
        num_of_floors (int): Total number of floors (must be ≥ 2).
        num_of_elevators (int): Number of elevators (1 ≤ elevators < floors).
        building_type (Optional[str]): Optional tag for future building types.

    Returns:
        AbstractBuilding: A concrete instance of a Building.
    """
    # Edge case validation
    assert num_of_floors >= 2, "No buildings with less than 2 floors!"
    assert 1 <= num_of_elevators, "There must be at least one elevator!"
    assert num_of_elevators < num_of_floors, "There cannot be more elevators than floors."

    match building_type:
        case _:
            return Building(num_of_floors, num_of_elevators)
