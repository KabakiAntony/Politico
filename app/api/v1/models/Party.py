from app.api.v1.v1_utils import get_method,delete_method,update_method
from app.api.v1.models.Lists import PARTY

#PARTY = []

class Party:
    """
    This class holds all the methods for the creation of 
    parties.
    """

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
        
        for party in PARTY:
            if party["id"] == party_id:
                return party"""
        return get_method("Party",party_id)
    

    def delete_party(party_id):
        """
        Here we remove a party from our list.
        
        if Party.get_party(party_id):
            PARTY.remove(Party.get_party(party_id))
            return "Party deleted successfully."    
        """
        return delete_method("Party",party_id)

    def update_party(party_id,new_party_name):
        """
        This will update the name of the party.
        
        party = Party.get_party(id)
        if party:
            party["name"]= new_party_name
        return Party.get_party(party_id)""" 
        return update_method("Party",party_id,new_party_name)           
       

        

    