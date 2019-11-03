"""
I have decided to combine the party and office views
because they have similar operations it doesn't make 
any sense to have to views that have the same
operations it only goes to affect the maintainability 
of the code.
"""
from flask import request
from app.api.v1 import version_one
from app.api.utils import override_make_response,check_return
from app.api.v1.models.v1_models_utils import get_specific_object_method,\
    delete_method,update_method,get_model,new_object_item,OFFICE,PARTY

def get_request_path(request_path):
    """This just gets the request path and breaks it down"""
    r_path = request_path.split('/')[-1]
    if r_path == "offices":
        return_path = "Office"
    elif r_path == "parties":
        return_path = "Party"
    else:
        return_path = "Path not found!"
    return return_path


@version_one.route('/parties',methods=['GET'])
@version_one.route('/offices',methods=['GET'])
def all_offices_or_parties():
    """
    Returns all parties/offices in the list or an empty list
    if the list is empty.
    """
    view_model = get_request_path(request.path)
    return check_return(get_model(f"{view_model}"),f"{view_model}")
