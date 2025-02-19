from aircraft import Aircraft
class Flight:
    def __init__(self, lead:Aircraft, members: list[Aircraft]):
        self.lead = lead
        self.members = members
