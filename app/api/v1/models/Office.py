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

    def get_office(id):
        """This will return a specific office object given the id
        supplied by the user Or an empty list if no office was found.
        This method will also be re-used by the methods that need 
        to know if an office exists before making any
        changes to it that is modify and delete
        """ 
        the_office = [office for office in OFFICE if office['id']==id]
        return the_office