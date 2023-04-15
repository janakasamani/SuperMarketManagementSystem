from swagger_server.models.edit_user_request import EditUserRequest
from swagger_server.models.inline_response200 import InlineResponse200
import pymongo

def edit_user(edit_request:EditUserRequest):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:ZDnkZaXIPslCBvRk@cluster0.txlg72g.mongodb.net/test")
    database = myclient["super_market"]
    collection = database["users"]

    filter = {
        "name": edit_request.name
    }

    results = collection.update_one(filter,{"$set":{"name":""}})

    return InlineResponse200(message="done")


