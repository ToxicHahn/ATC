class Aircraft:
    def __init__(self, callsign, tYpe, location, airspeed):
        self.callsign = callsign
        self.type = tYpe
        self.location = location
        self.flight_plan = []
        self.fuel = 100
        self.airspeed = airspeed
        self.altitudeMSL = 0
        self.heading = 0
    
