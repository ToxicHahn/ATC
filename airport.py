from taxiway import Taxiway
from runway import Runway
class Airport():
    def __init__(self, name):
        self.name = name
        self.gates = []
        self.taxiways: list[Taxiway] = []
        self.runways: list[Runway] = []
        self.tower: str = None


