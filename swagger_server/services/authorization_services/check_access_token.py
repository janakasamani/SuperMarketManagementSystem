from helpers.token_helpers import decode_token
import connexion
from connexion.exceptions import ProblemException
def check_access_token(token, required_scopes):
    payload = decode_token(token)

    user_role = payload.get("role")

    if user_role == "admin":
        pass
    elif user_role == "cashier":
        allowed_apis = ["add_item","edit_item","get_item","get_user"]

    elif user_role == "customer":
        allowed_apis = ["get_item"]

    api_endpoint = connexion.request.endpoint.split("controller_")[1]
    if api_endpoint in allowed_apis:
        #THIS IS FOR LATER ON FOR CODE TO KNOW WHO IS USING IT FROM TOKEN.
        return {'sub': payload.get("id"),'test_key':payload}
    else:
        raise ProblemException(status=401, title="Unauthorized", detail="You are not allowed to use this API.")