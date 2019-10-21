# this is the office model
OFFICE = []


class Office:
    """
    This class will hold all the data, data operations, attributes and 
    the methods of this class that will be dealing with the data of the class
    
    def __init__(self,name,office_type):
    
        This initializes the attribs of the office that is the
        name, type and id
        self.name = name 
        self.office_type = office_type 
        self.id = len(OFFICE)
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
        """This will get a specific office from the Office List
        """ 
        for office in OFFICE:
            if office["id"]==id:
                return office
    
    def delete_office(id):
        """This method deletes an office."""    
        if Office.get_office(id):
            OFFICE.remove(Office.get_office(id))
            return "Office deleted successfully."
    
    def modify_office(id,new_office_name):
        """Changes the name of the office"""
        office = Office.get_office(id)
        if office:
            office["name"]=new_office_name
        return Office.get_office(id)
         
        

