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
        This method deletes a party whose id matches with the id that
         the user has supplied.
        On success it returns a success message that the party has been
         deleted 
        Or not found on successive calls to the endpoint 
        Or when the party has not been found from the word go
        """
        the_party = Party.get_party(id)
        if the_party:
            for party in PARTY:
                if party["id"]==id:
                    PARTY.remove(party)
                    # the dynamic nature of python allows me to return a string at this point
                    # normally the_party would be a list or an empty list
                    the_party = "Party deleted successfully."
        return the_party
    

    def update_party(id,name):
        """
        This changes the name of the party and the type of party 
        given a new name and the type of party but we will just change 
        the name to prove concept.
        """
        the_party = Party.get_party(id)
        if the_party:
            for party in PARTY:
                if party["id"]==id:
                    party["name"]=name
                    the_party = Party.get_party(id)
        return the_party

        

    