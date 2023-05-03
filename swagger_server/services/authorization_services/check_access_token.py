from helpers.token_helpers import decode_token
import connexion
from connexion.exceptions import ProblemException
def check_access_token(token, required_scopes):
    # the function below attemps to decode the token. if the token is valid and has not expired, it will raise an exception telling the user the token is invalid
    #else it is going to return a dictionary with all the details that we stored in the token, such as username and role.
    payload = decode_token(token)


    #we are defining allowed apis that a user can call first as empty, then based on his role, we fill up his allowed APIS
    allowed_apis =[]
    # Fetching the users role from his token
    user_role = payload.get("role")

    if user_role == "admin":
        allowed_apis =["add_item","edit_item","get_item","get_user","add_user"]
    elif user_role == "cashier":
        allowed_apis = ["add_item","edit_item","get_item","get_user"]

    elif user_role == "customer":
        allowed_apis = ["get_item"]

    api_endpoint = connexion.request.endpoint.split("controller_")[1]
    if api_endpoint in allowed_apis:
        #THIS IS FOR LATER ON FOR CODE TO KNOW WHO IS USING IT FROM TOKEN. We are storing the token payload that includes the username and role for later use, check add item
        return {'sub': payload.get("id"),'test_key':payload}
    else:
        raise ProblemException(status=401, title="Unauthorized", detail="You are not allowed to use this API.")