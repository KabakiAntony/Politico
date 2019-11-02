from app.api.v1.v1_models_utils import get_method,delete_method,update_method
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
    

        

    