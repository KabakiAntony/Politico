from app.api.v1.v1_utils import get_method,delete_method,update_method
from app.api.v1.models.Lists import OFFICE


class Office:
    """
    This class will hold all the data, data operations, attributes and 
    the methods of this class that will be dealing with the data of the class
    """

    def new_office(self):
        """
        This creates a new office object with all the attributes 
        supplied in the dunder init
        """
        OFFICE.append(self)
        return OFFICE[-1]
    

    def get_offices():
        """This will return all the offices in the given list 
        Or an empty list if no offices exist"""
        return OFFICE

    def get_office(id):
        """This will get a specific office from the Office List"""
        return get_method("Office",id)
        
    
    def delete_office(id):
        """This method deletes an office"""
        return delete_method("Office",id)
    
    def modify_office(id,new_office_name):
        """Changes the name of the office"""
        return update_method("Office",id,new_office_name)
        

         
        

