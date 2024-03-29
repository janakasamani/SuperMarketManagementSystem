# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class EditUserRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, username: str=None, role: str=None, is_active: bool=None, password: str=None):  # noqa: E501
        """EditUserRequest - a model defined in Swagger

        :param name: The name of this EditUserRequest.  # noqa: E501
        :type name: str
        :param username: The username of this EditUserRequest.  # noqa: E501
        :type username: str
        :param role: The role of this EditUserRequest.  # noqa: E501
        :type role: str
        :param is_active: The is_active of this EditUserRequest.  # noqa: E501
        :type is_active: bool
        :param password: The password of this EditUserRequest.  # noqa: E501
        :type password: str
        """
        self.swagger_types = {
            'name': str,
            'username': str,
            'role': str,
            'is_active': bool,
            'password': str
        }

        self.attribute_map = {
            'name': 'name',
            'username': 'username',
            'role': 'role',
            'is_active': 'is_active',
            'password': 'password'
        }
        self._name = name
        self._username = username
        self._role = role
        self._is_active = is_active
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'EditUserRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EditUserRequest of this EditUserRequest.  # noqa: E501
        :rtype: EditUserRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this EditUserRequest.


        :return: The name of this EditUserRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this EditUserRequest.


        :param name: The name of this EditUserRequest.
        :type name: str
        """

        self._name = name

    @property
    def username(self) -> str:
        """Gets the username of this EditUserRequest.


        :return: The username of this EditUserRequest.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this EditUserRequest.


        :param username: The username of this EditUserRequest.
        :type username: str
        """

        self._username = username

    @property
    def role(self) -> str:
        """Gets the role of this EditUserRequest.


        :return: The role of this EditUserRequest.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this EditUserRequest.


        :param role: The role of this EditUserRequest.
        :type role: str
        """
        allowed_values = ["cashier", "customer", "admin"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def is_active(self) -> bool:
        """Gets the is_active of this EditUserRequest.


        :return: The is_active of this EditUserRequest.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        """Sets the is_active of this EditUserRequest.


        :param is_active: The is_active of this EditUserRequest.
        :type is_active: bool
        """

        self._is_active = is_active

    @property
    def password(self) -> str:
        """Gets the password of this EditUserRequest.


        :return: The password of this EditUserRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this EditUserRequest.


        :param password: The password of this EditUserRequest.
        :type password: str
        """

        self._password = password
