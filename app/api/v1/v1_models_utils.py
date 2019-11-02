from app.api.v1.models.Lists import OFFICE,PARTY

def get_model(model):
    """Just get the model and return the list corresponding to it"""
    if model == "Office":
        list_model = OFFICE
    else:
        list_model = PARTY
    return list_model


def get_method(model,id):
    """This is for getting parties/offices"""
    list_model = get_model(model)
    for list_object in list_model:
        if list_object["id"] == id:
            return list_object


def delete_method(model,id):
    """This is for deleting parties/offices"""
    if get_method(model,id):
        list_model = get_model(model)
        list_model.remove(get_method(model,id))
        return f"{model} deleted successfully."


def update_method(model,id,update_name):
    """This is for updating"""
    list_object = get_method(model,id)
    if list_object:
        list_object["name"]=update_name
    return get_method(model,id)




            
        
        
        
            
        
    
    
