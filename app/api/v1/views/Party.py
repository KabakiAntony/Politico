from flask import request
from app.api.v1 import version_one
from app.api.utils import override_make_response,check_return
from app.api.v1.models.v1_models_utils import get_specific_object_method,delete_method,update_method,get_model,new_object_item,PARTY


@version_one.route('/parties', methods=['POST'])
def create_party():
    """
    This  creates a new party with the parameters of
    name, logourl, hqaddress and an auto generated id
    and returns it as a part of the response to the user
    """
    try:
        party_data = request.get_json()  
        name = party_data["name"]
        address = party_data["hqAddress"]
        logo = party_data["logoUrl"]
    except:
        return override_make_response(
            "Error","Keys should be 'name','hqAddress','logoUrl' !",400)
    new_party = {
        "name": name,
        "hqAddress": address,
        "logoUrl": logo,
        "id": len(PARTY)
    }
    new_object_item("Party",new_party)
    return override_make_response("Data",new_party,201)

@version_one.route('parties/<int:party_id>', methods=['GET','DELETE'])
def get_or_delete(party_id):
    """This view combines delete and get since they have similar routes"""
    if request.method == 'GET':
        return check_return(get_specific_object_method("Party",party_id),"Party")
    else:
        return check_return(delete_method("Party",party_id),"Party")