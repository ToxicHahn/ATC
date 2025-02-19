class Taxiway():
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.occupied = []