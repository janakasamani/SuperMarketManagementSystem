# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GetUserResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, username: str=None, role: str=None, is_active: bool=None):  # noqa: E501
        """GetUserResponse - a model defined in Swagger

        :param name: The name of this GetUserResponse.  # noqa: E501
        :type name: str
        :param username: The username of this GetUserResponse.  # noqa: E501
        :type username: str
        :param role: The role of this GetUserResponse.  # noqa: E501
        :type role: str
        :param is_active: The is_active of this GetUserResponse.  # noqa: E501
        :type is_active: bool
        """
        self.swagger_types = {
            'name': str,
            'username': str,
            'role': str,
            'is_active': bool
        }

        self.attribute_map = {
            'name': 'name',
            'username': 'username',
            'role': 'role',
            'is_active': 'is_active'
        }
        self._name = name
        self._username = username
        self._role = role
        self._is_active = is_active

    @classmethod
    def from_dict(cls, dikt) -> 'GetUserResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetUserResponse of this GetUserResponse.  # noqa: E501
        :rtype: GetUserResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this GetUserResponse.


        :return: The name of this GetUserResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this GetUserResponse.


        :param name: The name of this GetUserResponse.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def username(self) -> str:
        """Gets the username of this GetUserResponse.


        :return: The username of this GetUserResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this GetUserResponse.


        :param username: The username of this GetUserResponse.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def role(self) -> str:
        """Gets the role of this GetUserResponse.


        :return: The role of this GetUserResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this GetUserResponse.


        :param role: The role of this GetUserResponse.
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
        """Gets the is_active of this GetUserResponse.


        :return: The is_active of this GetUserResponse.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        """Sets the is_active of this GetUserResponse.


        :param is_active: The is_active of this GetUserResponse.
        :type is_active: bool
        """

        self._is_active = is_active
