from swagger_server.models.login_request import LoginRequest
from swagger_server.models.login_response import LoginResponse
import pymongo
from helpers.token_helpers import get_token
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


        token = get_token(login_response)
        return LoginResponse(message="WELCOMEE MY FRIENDDD",token=token)


