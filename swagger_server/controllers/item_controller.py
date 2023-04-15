import connexion
import six

from swagger_server.models.add_item_request import AddItemRequest  # noqa: E501
from swagger_server.models.edit_item_request import EditItemRequest  # noqa: E501
from swagger_server.models.get_item_response import GetItemResponse  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server import util
from swagger_server.services.item_services.add_item import add_item as add_item_service
from swagger_server.services.item_services.get_item import get_item as get_item_service

def add_item(body=None):  # noqa: E501
    """add the item

    add the item # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    if connexion.request.is_json:
        body = AddItemRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return add_item_service(item_request=body)


def edit_item(body=None):  # noqa: E501
    """edit item

    edit item # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = EditItemRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic'


def get_item(item_type=None, expired=None):  # noqa: E501
    """get item

     # noqa: E501

    :param type: 
    :type type: str
    :param expired: 
    :type expired: bool

    :rtype: GetItemResponse
    """
    return get_item_service(item_type=item_type, expired=expired)
