# this is the office model
OFFICE = []

class Office:
    """
    This class will hold all the data, data operations, attributes and 
    the methods of this class that will be dealing with the data of the class
    """
    def __init__(self,name,office_type):
        """
        This initializes the attribs of the office that is the
        name, type and id """
        self.name = name 
        self.office_type = office_type 
        self.id = len(OFFICE)
    

    def new_office(self):
        """
        This creates a new office object with all the attributes 
        supplied in the dunder init
        """
        OFFICE.append(self)
        return OFFICE
    

    def get_offices():
        """This will return all the offices in the given list 
        Or an empty list if no offices exist"""
        return OFFICE