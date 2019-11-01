from app.api.v1.v1_utils import get_method,delete_method,update_method
from app.api.v1.models.Lists import PARTY

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
        """This will get a single party from the party list."""
        return get_method("Party",party_id)
    

    def delete_party(party_id):
        """Remove a party from our list."""
        return delete_method("Party",party_id)

    def update_party(party_id,new_party_name):
        """This will update the name of the party.""" 
        return update_method("Party",party_id,new_party_name)           
       

        

    