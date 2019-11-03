from flask import request
from app.api.v1 import version_one
from app.api.utils import override_make_response,check_return
from app.api.v1.models.v1_models_utils import get_specific_object_method,delete_method,update_method,get_model,new_object_item,PARTY


@version_one.route('/parties', methods=['POST'])
def create_party():
    """
    Creates a new party
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
