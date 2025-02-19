from aircraft import Aircraft
class Flight:
    """
    A class to represent a flight formation.

    Attributes:
    -----------
    lead : Aircraft
        The lead aircraft in the formation.
    members : list[Aircraft]
        A list of aircraft that are members of the formation.

    Methods:
    --------
    __init__(self, lead: Aircraft, members: list[Aircraft]):
        Initializes the Flight instance with a lead aircraft and a list of member aircraft.
    """
    def __init__(self, lead:Aircraft, members: list[Aircraft]):
        self.lead = lead
        self.members = members
