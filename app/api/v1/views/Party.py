from flask import request
from app.api.v1 import version_one
from app.api.v1.models.Party import Party, PARTY
from app.api.utils import override_make_response,check_return


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
    Party.new_party(new_party)
    return override_make_response("Data",new_party,201)


@version_one.route('/parties', methods=['GET'])
def all_parties():
    """
    This will return the parties that exist at this point or 
    a no party was found message if none exists.
    """
    # existing_parties is a list of the parties found/not
    existing_parties = Party.get_parties()
    return check_return(existing_parties,"Party")

@version_one.route('parties/<int:id>', methods=['GET'])
def get_party(id):
    """
    This gets a specific party whose id matches with the one 
    supplied by the user or a not found message if no party matches 
    with the id supplied by the user
    """
    party = Party.get_party(id)
    return check_return(party,"Party")


@version_one.route('parties/<int:id>', methods=['DELETE'])
def remove_party(id):
    """
    This deletes a party if found  and returns a success message
    Or a faliure message if no party has been found and On successive hits 
    to this endpoint after the first successive hit.
    """
    is_deleted = Party.delete_party(id)
    return check_return(is_deleted,"Party")

@version_one.route('parties/<int:id>/name',methods=['PATCH'])
def update_party(id):
    """
    This updates the name of the party whose id has been supplied by the 
    user and returns the party with the new name in place it will always 
    return the same data on successful update and a party not found 
    message if the id supplied does not match with any of the existing parties.
    """
    try:
        party_data = request.get_json()  
        name = party_data["name"]
        party = Party.update_party(id,name)
    except:
        return override_make_response("Error","Key should be name !",400)
    return check_return(party,"Party")

