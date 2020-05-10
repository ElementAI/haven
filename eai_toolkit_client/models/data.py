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


class Data(object):
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
        'account': 'FieldAccount',
        'created': 'str',
        'creator': 'FieldCreator',
        'full_name': 'str',
        'id': 'str',
        'name': 'str',
        'organization': 'FieldOrganization',
        'tags': 'list[object]',
        'urn': 'str'
    }

    attribute_map = {
        'account': 'account',
        'created': 'created',
        'creator': 'creator',
        'full_name': 'fullName',
        'id': 'id',
        'name': 'name',
        'organization': 'organization',
        'tags': 'tags',
        'urn': 'urn'
    }

    def __init__(self, account=None, created=None, creator=None, full_name=None, id=None, name=None, organization=None, tags=None, urn=None):  # noqa: E501
        """Data - a model defined in OpenAPI"""  # noqa: E501

        self._account = None
        self._created = None
        self._creator = None
        self._full_name = None
        self._id = None
        self._name = None
        self._organization = None
        self._tags = None
        self._urn = None
        self.discriminator = None

        self.account = account
        self.created = created
        self.creator = creator
        if full_name is not None:
            self.full_name = full_name
        self.id = id
        if name is not None:
            self.name = name
        self.organization = organization
        if tags is not None:
            self.tags = tags
        self.urn = urn

    @property
    def account(self):
        """Gets the account of this Data.  # noqa: E501


        :return: The account of this Data.  # noqa: E501
        :rtype: FieldAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Data.


        :param account: The account of this Data.  # noqa: E501
        :type: FieldAccount
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def created(self):
        """Gets the created of this Data.  # noqa: E501


        :return: The created of this Data.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Data.


        :param created: The created of this Data.  # noqa: E501
        :type: str
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def creator(self):
        """Gets the creator of this Data.  # noqa: E501


        :return: The creator of this Data.  # noqa: E501
        :rtype: FieldCreator
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Data.


        :param creator: The creator of this Data.  # noqa: E501
        :type: FieldCreator
        """
        if creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")  # noqa: E501

        self._creator = creator

    @property
    def full_name(self):
        """Gets the full_name of this Data.  # noqa: E501


        :return: The full_name of this Data.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Data.


        :param full_name: The full_name of this Data.  # noqa: E501
        :type: str
        """
        if full_name is not None and not re.search(r'^|[a-z0-9_]+(\.[a-z0-9_]+)*$', full_name):  # noqa: E501
            raise ValueError(r"Invalid value for `full_name`, must be a follow pattern or equal to `/^|[a-z0-9_]+(\.[a-z0-9_]+)*$/`")  # noqa: E501

        self._full_name = full_name

    @property
    def id(self):
        """Gets the id of this Data.  # noqa: E501

        Unique id of the resource  # noqa: E501

        :return: The id of this Data.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Data.

        Unique id of the resource  # noqa: E501

        :param id: The id of this Data.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Data.  # noqa: E501


        :return: The name of this Data.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Data.


        :param name: The name of this Data.  # noqa: E501
        :type: str
        """
        if name is not None and not re.search(r'^[a-z0-9_]*$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-z0-9_]*$/`")  # noqa: E501

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this Data.  # noqa: E501


        :return: The organization of this Data.  # noqa: E501
        :rtype: FieldOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Data.


        :param organization: The organization of this Data.  # noqa: E501
        :type: FieldOrganization
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def tags(self):
        """Gets the tags of this Data.  # noqa: E501

        Tags of the resource  # noqa: E501

        :return: The tags of this Data.  # noqa: E501
        :rtype: list[object]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Data.

        Tags of the resource  # noqa: E501

        :param tags: The tags of this Data.  # noqa: E501
        :type: list[object]
        """

        self._tags = tags

    @property
    def urn(self):
        """Gets the urn of this Data.  # noqa: E501

        URN of the resource  # noqa: E501

        :return: The urn of this Data.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this Data.

        URN of the resource  # noqa: E501

        :param urn: The urn of this Data.  # noqa: E501
        :type: str
        """
        if urn is None:
            raise ValueError("Invalid value for `urn`, must not be `None`")  # noqa: E501
        if urn is not None and not re.search(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:(account|policy|role|user|team):[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:(data|job|service|role|policy):[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?)?$', urn):  # noqa: E501
            raise ValueError(r"Invalid value for `urn`, must be a follow pattern or equal to `/^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:(account|policy|role|user|team):[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:(data|job|service|role|policy):[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?)?$/`")  # noqa: E501

        self._urn = urn

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
        if not isinstance(other, Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
