"""
The idea was to have an office and a party model
and it works just fine but then why have two files 
that perform the same operations this highly affects the 
maintainability of the code so I merged the operations 
and came up with a single file that acts on both sets of lists
# the  model argument stands for either office/party
"""
OFFICE = []
PARTY = []

def get_model(model):
    """
    This method helps to know if its a party or an office action 
    that is calling a certain method and then passes it the 
    corresponding list to act on.
    """
    list_model = ""
    if model == "Office":
        list_model = OFFICE
    elif model== "Party":
        list_model = PARTY
    return list_model


def new_object_item(model,self):
    """
    This adds or creates a new entry into the list be it a new
    party or an office
    """
    list_model = get_model(model)
    list_model.append(self)
    return list_model[-1] 


def get_specific_object_method(model,id):
    """This is for getting specific parties/offices"""
    list_model = get_model(model)
    for list_object in list_model:
        if list_object["id"] == id:
            return list_object


def delete_method(model,id):
    """This is for deleting parties/offices"""
    if get_specific_object_method(model,id):
        list_model = get_model(model)
        list_model.remove(get_specific_object_method(model,id))
        return f"{model} deleted successfully."


def update_method(model,id,update_name):
    """This is for updating"""
    list_object = get_specific_object_method(model,id)
    if list_object:
        list_object["name"]=update_name
    return get_specific_object_method(model,id)




            
        
        
        
            
        
    
    
