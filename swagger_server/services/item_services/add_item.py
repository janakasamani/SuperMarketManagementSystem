from swagger_server.models.add_item_request import AddItemRequest
from swagger_server.models.inline_response2002 import InlineResponse2002
import pymongo
import connexion


def add_item(item_request=AddItemRequest):
    # in order to know what user is currently using the application, we need to know context.
    # like english language: IN WHAT CONTEXT DO YOU MEAN!
    # to get what we stored in the authorization page, we check something called context
    token_payload = connexion.context['token_info']['test_key']

    # it will be like this, in the form of the dictionary
    # token_payload = {'iat': 1683122192, 'exp': 1683125792, 'id': '6417204935cf606b7c6b5104', 'username': 'jana.kasmani',
    #                  'role': 'admin'}

    #so lets say we want to see the username of the current user, we say token_payload.get("username")
    username = token_payload.get("username")
    print("username", username)
    # so now, u can do whatever u want with the data, u can get the user from mongo by filtering his username, lets say he has a balance u can get it too and update it if u want to buy, and etc... or if u want to store who added the item in mongo, u add the username to the dictionary of the item and store it
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
