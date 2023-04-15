# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.add_user_request import AddUserRequest  # noqa: E501
from swagger_server.models.edit_user_request import EditUserRequest  # noqa: E501
from swagger_server.models.get_user_response import GetUserResponse  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.login_request import LoginRequest  # noqa: E501
from swagger_server.models.login_response import LoginResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_add_user(self):
        """Test case for add_user

        add the user
        """
        body = AddUserRequest()
        response = self.client.open(
            '/api/v3/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_user(self):
        """Test case for edit_user

        edit the user
        """
        body = EditUserRequest()
        response = self.client.open(
            '/api/v3/user',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        get user
        """
        query_string = [('username', 'username_example')]
        response = self.client.open(
            '/api/v3/user',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_user(self):
        """Test case for login_user

        login the user
        """
        body = LoginRequest()
        response = self.client.open(
            '/api/v3/user/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
