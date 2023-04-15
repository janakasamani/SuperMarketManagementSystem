from swagger_server.models.get_item_response import GetItemResponse
import pymongo

def get_item(item_type=None, expired=None):
    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:ZDnkZaXIPslCBvRk@cluster0.txlg72g.mongodb.net/test")
    database = myclient["super_market"]
    collection = database["items"]

    filter = {}
    if item_type:
        filter["item_type"] = item_type
    if expired:
        filter["expired"] = expired

    item = collection.find_one(filter)
    return GetItemResponse.from_dict(item)


