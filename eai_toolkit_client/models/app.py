# coding: utf-8

"""
    EAI Toolkit

    EAI Toolkit API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class App(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'app_id': 'str',
        'entrypoint_url': 'str',
        'export_name': 'str',
        'name': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'entrypoint_url': 'entrypoint_url',
        'export_name': 'export_name',
        'name': 'name',
        'user_id': 'user_id'
    }

    def __init__(self, app_id=None, entrypoint_url=None, export_name=None, name=None, user_id=None):  # noqa: E501
        """App - a model defined in OpenAPI"""  # noqa: E501

        self._app_id = None
        self._entrypoint_url = None
        self._export_name = None
        self._name = None
        self._user_id = None
        self.discriminator = None

        self.app_id = app_id
        self.entrypoint_url = entrypoint_url
        self.export_name = export_name
        self.name = name
        self.user_id = user_id

    @property
    def app_id(self):
        """Gets the app_id of this App.  # noqa: E501


        :return: The app_id of this App.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this App.


        :param app_id: The app_id of this App.  # noqa: E501
        :type: str
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def entrypoint_url(self):
        """Gets the entrypoint_url of this App.  # noqa: E501


        :return: The entrypoint_url of this App.  # noqa: E501
        :rtype: str
        """
        return self._entrypoint_url

    @entrypoint_url.setter
    def entrypoint_url(self, entrypoint_url):
        """Sets the entrypoint_url of this App.


        :param entrypoint_url: The entrypoint_url of this App.  # noqa: E501
        :type: str
        """
        if entrypoint_url is None:
            raise ValueError("Invalid value for `entrypoint_url`, must not be `None`")  # noqa: E501

        self._entrypoint_url = entrypoint_url

    @property
    def export_name(self):
        """Gets the export_name of this App.  # noqa: E501


        :return: The export_name of this App.  # noqa: E501
        :rtype: str
        """
        return self._export_name

    @export_name.setter
    def export_name(self, export_name):
        """Sets the export_name of this App.


        :param export_name: The export_name of this App.  # noqa: E501
        :type: str
        """
        if export_name is None:
            raise ValueError("Invalid value for `export_name`, must not be `None`")  # noqa: E501

        self._export_name = export_name

    @property
    def name(self):
        """Gets the name of this App.  # noqa: E501


        :return: The name of this App.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this App.


        :param name: The name of this App.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def user_id(self):
        """Gets the user_id of this App.  # noqa: E501


        :return: The user_id of this App.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this App.


        :param user_id: The user_id of this App.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, App):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
