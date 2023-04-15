from swagger_server.models.add_item_request import AddItemRequest
from swagger_server.models.inline_response2002 import InlineResponse2002
import pymongo

def add_item(item_request=AddItemRequest):

    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:ZDnkZaXIPslCBvRk@cluster0.txlg72g.mongodb.net/test")
    database = myclient["super_market"]
    collection = database["items"]

    item_request_dict = item_request.to_dict()
    try:
        response = collection.insert_one(item_request_dict)
        created_id = response.inserted_id
    except pymongo.errors.DuplicateKeyError:
        return {"error": "Name already exists"}, 400

    return InlineResponse2002(message="item added: " + str(created_id))
