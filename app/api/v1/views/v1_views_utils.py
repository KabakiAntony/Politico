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
        return_model = "Office"
    elif r_path == "parties":
        return_model = "Party"
    return return_model


@version_one.route('/parties',methods=['GET'])
@version_one.route('/offices',methods=['GET'])
def all_offices_or_parties():
    """
    Returns all parties/offices in the list or an empty list
    if the list is empty.
    """
    view_model = get_request_path(request.path)
    return check_return(get_model(f"{view_model}"),f"{view_model}")

@version_one.route('/offices/<int:id>/name',methods=['PATCH'])
@version_one.route('/parties/<int:id>/name',methods=['PATCH'])
def update_office_or_party(id):
    """This updates the name of the party or the office whose id 
    has been supplied """
    r_path = request.path.split('/')[-3]
    r_model =""
    if r_path == "offices":
        r_model = "Office"
    elif r_path == "parties":
        r_model = "Party"
    try:
        r_data = request.get_json()  
        name = r_data["name"]
    except:
        return override_make_response("Error","Key should be 'name'!",400)
    return check_return(update_method(f"{r_model}",id,name),f"{r_model}")



@version_one.route('/parties/<int:id>', methods=['GET','DELETE'])
@version_one.route('/offices/<int:id>', methods=['GET','DELETE'])
def get_or_delete_parties_offices(id):
    """
    This gets or deletes parties or offices"""
    r_path = request.path.split('/')[-2]
    r_model =""
    if r_path == "offices":
        r_model = "Office"
    elif r_path == "parties":
        r_model = "Party"
    if request.method == 'GET':
        return check_return(get_specific_object_method(f"{r_model}",id),f"{r_model}")
    else:
        return check_return(delete_method(f"{r_model}",id),f"{r_model}")



    

