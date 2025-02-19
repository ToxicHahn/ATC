class Gate:
    """
    A class to represent an airport gate.

    Attributes
    ----------
    name : str
        The name of the gate.
    occupied : bool
        The occupancy status of the gate.

    Methods
    -------
    set_occupied():
        Sets the gate's status to occupied.
    set_unoccupied():
        Sets the gate's status to unoccupied.
    is_occupied() -> bool:
        Returns the occupancy status of the gate.
    get_name() -> str:
        Returns the name of the gate.
    """
    def __init__(self, name):
        self.name = name
        self.occupied = False
    def set_occupied(self):
        self.occupied = True
    def set_unoccupied(self):
        self.occupied = False
    def is_occupied(self):
        return self.occupied
    def get_name(self):
        return self.name
