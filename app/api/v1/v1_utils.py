from app.api.v1.models.Lists import OFFICE,PARTY

def get_method(model,id):
    """This is a utility method for getting"""
    if model == "Office":
        for office in OFFICE:
                if office["id"]==id:
                    return office
    else:
        for party in PARTY:
                if party["id"]==id:
                    return party


def delete_method(model,id):
    """This is a utility method for deleting"""
    if model == "Office":
        if get_method(model,id):
            OFFICE.remove(get_method(model,id))
            return "Office deleted successfully."
    else:
        if get_method(model,id):
            PARTY.remove(get_method(model,id))
            return "Party deleted successfully."


def update_method(model,id,update_name):
    """This is a utility method for updating"""
    if model == "Office":
        office = get_method(model,id)
        if office:
            office["name"]=update_name
        return get_method(model,id)
    else:
        party = get_method(model,id)
        if party:
            party["name"]=update_name
        return get_method(model,id)


            
        
        
        
            
        
    
    
