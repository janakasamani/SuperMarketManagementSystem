from typing import List
from swagger_server.services.authorization_services.check_access_token import check_access_token as check_access_token_service
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_access_token(api_key, required_scopes):
    return check_access_token_service(api_key, required_scopes)


