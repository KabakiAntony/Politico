# it will be getting the response from the model and preparing 
# them for view by the user of the system

from flask import request
from app.api.v1 import version_one
from app.api.v1.models.Office import OFFICE,Office
from app.api.utils import override_make_response,check_return

specific_office = '/offices/<int:id>'


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
            "Error","Keys should be 'name' and 'office_type' ! ",
            400)
    new_office = {
        "name":name,
        "office_type":office_type,
        "id":len(OFFICE)
    }
    Office.new_office(new_office)
    return override_make_response(
        "Data",new_office,
        201)


@version_one.route('/offices',methods=['GET'])
def all_offices():
    """
    This returns the offices that exist at this point or 
    a no office was found message.
    """
    existing_offices = Office.get_offices()
    return check_return(existing_offices,"Office")

@version_one.route(specific_office,methods=['GET'])
def get_office(id):
    """
    This gets a specific office whose id matches with the one 
    supplied by the user
    """
    office = Office.get_office(id)
    return check_return(office,"Office")


@version_one.route(specific_office,methods=['DELETE'])
def remove_office(id):
    """This deletes an office if found  and returns a success message
    Or a faliure message if no office has been found """
    is_deleted = Office.delete_office(id)
    return check_return(is_deleted,"Office")


@version_one.route('/offices/<int:id>/name',methods=['PATCH'])
def update_office(id):
    """
    This updates the name of the office whose id has been supplied by the 
    user and returns the office with the new name in place it will always 
    return the same data on successful update.
    """
    try:
        office_data = request.get_json()  
        name = office_data["name"]
    except:
        return override_make_response(
            "Error","Key should be 'name'!",
            400)
    office = Office.modify_office(id,name)
    return check_return(office,"Office")
