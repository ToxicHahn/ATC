class Taxiway():
    """
    A class to represent a taxiway.

    Attributes:
        name (str): The name of the taxiway.
        start (tuple): The starting coordinates of the taxiway.
        end (tuple): The ending coordinates of the taxiway.
        occupied (bool): The occupancy status of the taxiway. Defaults to False.

    Methods:
        __init__(name, start, end): Initializes the Taxiway with a name, start, and end coordinates.
    """
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.occupied = False