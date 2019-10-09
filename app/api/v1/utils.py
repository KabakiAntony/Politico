# this file will contain utils for the version_one of the api


def get_specific_objects(model,id):
    """This method will take the model where it has been called
    and the id of the object the user wishes to  to get
    model will be 'Office/Party' in that form strictly"""
    return_object = ""
    if (model == "Office"):
        return_object = model.get_office(id)
    elif (model == "Party"):
        return_object = model.get_party(id)
    else:
        return_object = "Model not found!"
    return return_object

        