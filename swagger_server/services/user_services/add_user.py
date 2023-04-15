from swagger_server.models.add_user_request import AddUserRequest
import pymongo
from swagger_server.models.inline_response200 import InlineResponse200

def add_user(user_request: AddUserRequest):

    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:ZDnkZaXIPslCBvRk@cluster0.txlg72g.mongodb.net/test")
    database = myclient["super_market"]
    collection = database["users"]


    jana_user_dictionary = {
        "username":user_request.username,
        "password":user_request.password,
        "role":user_request.role,
        "name":user_request.name,
        "is_active":user_request.is_active

    } # In Case u wanna do it manually
    # password = jana_user_dictionary.pop("password","") # in case u want to remove something from dictionary

    user_request_dict = user_request.to_dict() #Automatically

    try:
        response = collection.insert_one(user_request_dict)

        created_id = response.inserted_id
    except pymongo.errors.DuplicateKeyError:
        return {"error": "Name already exists"}

    message = "User Created Successfully"
    return InlineResponse200(message=message)


