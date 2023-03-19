from swagger_server.models.login_request import LoginRequest
from swagger_server.models.inline_response200 import InlineResponse200
import pymongo

def login_user(login_request: LoginRequest):

    myclient = pymongo.MongoClient("mongodb+srv://janakasamani:ZDnkZaXIPslCBvRk@cluster0.txlg72g.mongodb.net/test")
    database = myclient["super_market"]
    collection = database["users"]

    filter = {
        "username":login_request.username,
        "password":login_request.password,
        }
    login_response = collection.find_one(filter)
    if not login_response:
        return {"message":"BARRA YA KALB"},401
    else:
        return InlineResponse200(message="WELCOMEE MY FRIENDDD")


