# it will be getting the response from the model and preparing 
# them for view by the user of the system
from flask import request
from app.api.v1 import version_one
from app.api.utils import override_make_response,check_return
from app.api.v1.models.v1_models_utils import get_specific_object_method,\
    delete_method,update_method,get_model,new_object_item,OFFICE


@version_one.route('/offices',methods=['POST'])
def create_office():
    """
    This creates an  new office
    """
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
