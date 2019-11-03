# it will be getting the response from the model and preparing 
# them for view by the user of the system
from flask import request
from app.api.v1 import version_one
from app.api.utils import override_make_response,check_return
from app.api.v1.models.v1_models_utils import get_specific_object_method,delete_method,update_method,get_model,new_object_item,OFFICE



@version_one.route('/offices',methods=['POST'])
def create_office():
    """This creates a new office given that the
    name and the type are supplied by the user the id will be 
    auto generated""" 
    try:
        office_data = request.get_json()  
        name = office_data["name"]        
        office_type = office_data["office_type"]
    except:
        return override_make_response("Error","Keys should be 'name' and 'office_type' ! ",400)
    new_office = {
        "name":name,
        "office_type":office_type,
        "id":len(OFFICE)
    }
    new_object_item("Office",new_office)
    return override_make_response("Data",new_office,201)

"""
@version_one.route('/offices',methods=['GET'])
def all_offices():
    
    This returns the offices or an empty list.
    
    return check_return(get_model("Office"),"Office")"""

@version_one.route('/offices/<int:office_id>',methods=['GET','DELETE'])
def delete_or_get(office_id):
    """This gets or deletes an office since they have similar
    endpoints"""
    if request.method == 'GET':
        return check_return(get_specific_object_method("Office",office_id),"Office")
    else:
        return check_return(delete_method("Office",office_id),"Office")


@version_one.route('/offices/<int:id>/name',methods=['PATCH'])
def update_office(id):
    """
    updates the name of the office.
    """
    try:
        office_data = request.get_json()  
        name = office_data["name"]
    except:
        return override_make_response("Error","Key should be 'name'!",400)
    return check_return(update_method("Office",id,name),"Office")
