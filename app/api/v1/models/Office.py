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
        """This will get a specific office from the Office List
        """ 
        the_office = [office for office in OFFICE if office['id']==id]
        return the_office
    
    def delete_office(id):
        """
        This method deletes an office whose id matches with the id that
         the user has supplied.
        On success it returns a success message that the office has been
         deleted 
        Or not found on successive calls to the endpoint 
        Or when the office has not been found from the word go
        """
        the_office = Office.get_office(id)
        if the_office:
            for office in OFFICE:
                if office["id"]==id:
                    OFFICE.remove(office)
                    # the dynamic nature of python allows me to return a string at this point
                    # normally the_office would be a list or an empty list
                    the_office = "Office deleted successfully."
        return the_office
    
    
    def modify_office(id,name):
        """This changes the name of the office and the type of office 
        given a new name and the type of office
        """
        the_office = Office.get_office(id)
        if the_office:
            for office in OFFICE:
                if office["id"]==id:
                    office["name"]=name
                    the_office = Office.get_office(id)
        return the_office
