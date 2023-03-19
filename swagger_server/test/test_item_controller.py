# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.add_item_request import AddItemRequest  # noqa: E501
from swagger_server.models.edit_item_request import EditItemRequest  # noqa: E501
from swagger_server.models.get_item_response import GetItemResponse  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.test import BaseTestCase


class TestItemController(BaseTestCase):
    """ItemController integration test stubs"""

    def test_item_add_get(self):
        """Test case for item_add_get

        get item
        """
        query_string = [('type', 'type_example'),
                        ('expired', true)]
        response = self.client.open(
            '/api/v3/item/add',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_item_add_post(self):
        """Test case for item_add_post

        add the item
        """
        body = AddItemRequest()
        response = self.client.open(
            '/api/v3/item/add',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_item_add_put(self):
        """Test case for item_add_put

        edit item
        """
        body = EditItemRequest()
        response = self.client.open(
            '/api/v3/item/add',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
