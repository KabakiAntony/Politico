# it will be getting the response from the model and preparing 
# them for view by the user of the system

from flask import request
from app.api.v1 import version_one
from app.api.v1.models.Office import OFFICE,Office
from app.api.utils import override_make_response,check_return


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
        return override_make_response(
            "Data","Keys should be 'name' and 'office_type' ! ",400)
    new_office = {
        "name":name,
        "office_type":office_type,
        "id":len(OFFICE)
    }
    Office.new_office(new_office)
    return override_make_response("Data",new_office,201)