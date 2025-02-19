from airport import Airport
class Map:
    """
    A class to represent a map containing airports.

    Attributes
    ----------
    airports : list
        A list to store airport objects.

    Methods
    -------
    add_airport(airport: Airport):
        Adds an airport to the map.
    
    get_airports():
        Returns the list of airports in the map.
    """
    def __init__(self):
        self.airports = []
    def add_airport(self, airport: Airport):
        self.airports.append(airport)
    def get_airports(self):
        return self.airports


class Caucasus(Map):
    def __init__(self):
        super().__init__()
        self.add_airport(Airport("Anapa",))
