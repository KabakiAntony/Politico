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
        """Returns all parties in the our party list"""      
        return PARTY
    
    def get_party(id):
        """
        This will get a single party from the party list.
        """
        # this is a list comprehension to make code readable
        the_party = [party for party in PARTY if party["id"] == id]
        return the_party
    

    def delete_party(id):
        """
        Here we remove a party from our list.
        """
        the_party = Party.get_party(id)
        for party in PARTY:
                if party["id"]==id:
                    PARTY.remove(party)
                    # the dynamic nature of python allows me to return a string at this point
                    # normally the_party would be a list or an empty list
                    the_party = "Party deleted successfully."
        return the_party
    

    def update_party(id,name):
        """
        This will update the name of the party.
        """
        the_party = Party.get_party(id)
        for party in PARTY:
                if party["id"]==id:
                    party["name"]=name
                    the_party = Party.get_party(id)            
        return the_party

        

    