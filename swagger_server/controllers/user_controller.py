import connexion
import six

from swagger_server.models.add_user_request import AddUserRequest  # noqa: E501
from swagger_server.models.edit_user_request import EditUserRequest  # noqa: E501
from swagger_server.models.get_user_response import GetUserResponse  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.login_request import LoginRequest  # noqa: E501
from swagger_server import util
from swagger_server.services.user_services.add_user import add_user
from swagger_server.services.user_services.get_user import get_user
from swagger_server.services.user_services.login_user import login_user


def user_get(username=None):  # noqa: E501
    """get user

     # noqa: E501

    :param username: 
    :type username: str

    :rtype: GetUserResponse
    """
    return get_user(username=username)


def user_login_post(body=None):  # noqa: E501
    """login the user

    login user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = LoginRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return login_user(login_request=body)


def user_post(body=None):  # noqa: E501
    """add the user

    add the user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = AddUserRequest.from_dict(connexion.request.get_json())  # noqa: E501

    return add_user(user_request=body)


def user_put(body=None):  # noqa: E501
    """edit the user

    edit the user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = EditUserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
