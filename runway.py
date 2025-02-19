class Runway:
    """
    A class to represent a runway.

    Attributes:
        direction (str): The direction of the runway.
        occupied (bool): The occupancy status of the runway. Defaults to False.

    Methods:
        __init__(direction: str, occupied: bool = False) -> None:
            Initializes the Runway with a direction and occupancy status.
    """
    def __init__(self, direction: str, occupied: bool = False) -> None:
        self.direction = direction
        self.occupied = occupied
        