from swagger_server.models.get_user_response import GetUserResponse
import pymongo

def get_user(username = None):

    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:ZDnkZaXIPslCBvRk@cluster0.txlg72g.mongodb.net/test")
    database = myclient["super_market"]
    collection = database["users"]

    filter = {}
    if username:
        filter["username"] = username

    user = collection.find_one(filter)


    return GetUserResponse.from_dict(user)