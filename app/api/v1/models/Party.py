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
    
    def get_parties():
        """This will return all the parties in the given list 
        Or an empty list if no parties exist"""      
        return PARTY
    
    def get_party(id):
        """
        This will return a specific party object given the id
        supplied by the user Or an empty list if no party was found.
        This method will also be re-used by the methods that need 
        to know if an party exists before making any
        changes to it that is modify and delete
        """
        # this is a list comprehension to make code readable
        the_party = [party for party in PARTY if party["id"] == id]
        return the_party

    