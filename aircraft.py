class Aircraft:
    """
    A class to represent an aircraft.

    Attributes:
        callsign (str): The unique identifier for the aircraft.
        type (str): The type/model of the aircraft.
        location (tuple): The current location of the aircraft as a tuple of coordinates (latitude, longitude).
        airspeed (float): The current airspeed of the aircraft in knots.
        fuel (float): The current amount of fuel in the aircraft in gallons.
        flight_plan (list): The flight plan of the aircraft as a list of waypoints.
        fuelPercentage (float): The percentage of fuel remaining in the aircraft.
        altitudeMSL (float): The current altitude of the aircraft above mean sea level in feet.
        heading (float): The current heading of the aircraft in degrees.
    """
    def __init__(self, callsign, tYpe, location, airspeed, fuel):
        self.callsign = callsign
        self.type = tYpe
        self.location = location
        self.flight_plan = []
        self.fuel = fuel
        self.fuelPercentage = self.fuel/ self.fuelCapacity
        self.airspeed = airspeed
        self.altitudeMSL = 0
        self.heading = 0
    
