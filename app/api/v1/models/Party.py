PARTY = []

class Party:
    """
    This class holds all the methods for the creation of 
    parties.
    """

    def __init__(self, name, logoUrl, hqAddress):
        """
        Initializing the party and its attributes
        """
        self.id = len(parties)
        self.name = name
        self.logoUrl = logoUrl
        self.hqAddress = hqAddress


    def new_party(self):
        """
        This creates new party and returns the updated party list
        """
        PARTY.append(self)
        return PARTY

    