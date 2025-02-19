from taxiway import Taxiway
from runway import Runway

class Airport():
    """
    A class to represent an airport.

    Attributes:
        name (str): The name of the airport.
        gates (list): A list of gates at the airport.
        taxiways (list[Taxiway]): A list of taxiways at the airport.
        runways (list[Runway]): A list of runways at the airport.
        tower (float): The height of the control tower at the airport.
        location (tuple): The geographical location of the airport (latitude, longitude).
        wind (dict): A dictionary containing wind speed and direction.

    Methods:
        add_taxiway(taxiway: Taxiway): Adds a taxiway to the airport.
        add_runway(runway: Runway): Adds a runway to the airport.
        add_gate(gate): Adds a gate to the airport.
        set_tower(tower): Sets the height of the control tower.
        set_wind(speed, direction): Sets the wind speed and direction.
        get_wind(): Returns the current wind speed and direction.
        get_runways(): Returns the list of runways.
        get_taxiways(): Returns the list of taxiways.
        get_gates(): Returns the list of gates.
        get_tower(): Returns the height of the control tower.
        get_name(): Returns the name of the airport.
    """
    def __init__(self, name, gates, taxiways, runways, tower, location:tuple, wind={"speed": 0, "direction": 0}):
        self.name = name
        self.gates = gates
        self.taxiways: list[Taxiway] = taxiways
        self.runways: list[Runway] = runways
        self.tower: float = tower
        self.wind = wind
        self.location = location
    def add_taxiway(self, taxiway: Taxiway):
        self.taxiways.append(taxiway)
    def add_runway(self, runway: Runway):
        self.runways.append(runway)
    def add_gate(self, gate):
        self.gates.append(gate)
    def set_tower(self, tower):
        self.tower = tower
    def set_wind(self, speed, direction):
        self.wind = {"speed": speed, "direction": direction}
    def get_wind(self):
        return self.wind
    def get_runways(self):
        return self.runways
    def get_taxiways(self):
        return self.taxiways
    def get_gates(self):
        return self.gates
    def get_tower(self):
        return self.tower
    def get_name(self):
        return self.name
    
