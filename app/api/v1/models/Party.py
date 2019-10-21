PARTY = []

class Party:
    """
    This class holds all the methods for the creation of 
    parties.
    """

    """def __init__(self, name, logoUrl, hqAddress):
        
        Initializing the party and its attributes
        
        self.id = len(PARTY)
        self.name = name
        self.logoUrl = logoUrl
        self.hqAddress = hqAddress"""


    def new_party(self):
        """
        This creates new party and returns the updated party list
        """
        PARTY.append(self)
        return PARTY[-1]
    
    def get_parties():
        """Returns all parties in the our party list"""      
        return PARTY
    
    def get_party(party_id):
        """
        This will get a single party from the party list.
        """
        # this is a list comprehension to make code readable
        the_party = [party for party in PARTY if party["id"] == party_id]
        return the_party
    

    def delete_party(party_id):
        """
        Here we remove a party from our list.
        """
        for party in PARTY:
                if party["id"]==party_id:
                    PARTY.remove(party)
                    # the dynamic nature of python allows me to return a string at this point
                    # normally the_party would be a list or an empty list
                    return "Party deleted successfully."      
        return Party.get_party(party_id)
        
    

    def update_party(party_id,new_party_name):
        """
        This will update the name of the party.
        """
        for party in PARTY:
            if party["id"]==party_id:
                party["name"]=new_party_name
        return Party.get_party(party_id)            
       

        

    