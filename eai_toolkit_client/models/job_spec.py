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


class JobSpec(object):
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
        'bid': 'int',
        'command': 'list[str]',
        'data': 'list[str]',
        'environment_vars': 'list[str]',
        'image': 'str',
        'interactive': 'bool',
        'is_process_agent': 'bool',
        'max_run_time': 'int',
        'name': 'str',
        'options': 'dict(str, object)',
        'preemptable': 'bool',
        'resources': 'JobSpecResources',
        'restartable': 'bool',
        'role': 'str',
        'tags': 'list[object]',
        'workdir': 'str'
    }

    attribute_map = {
        'bid': 'bid',
        'command': 'command',
        'data': 'data',
        'environment_vars': 'environmentVars',
        'image': 'image',
        'interactive': 'interactive',
        'is_process_agent': 'isProcessAgent',
        'max_run_time': 'maxRunTime',
        'name': 'name',
        'options': 'options',
        'preemptable': 'preemptable',
        'resources': 'resources',
        'restartable': 'restartable',
        'role': 'role',
        'tags': 'tags',
        'workdir': 'workdir'
    }

    def __init__(self, bid=None, command=None, data=None, environment_vars=None, image=None, interactive=None, is_process_agent=None, max_run_time=None, name=None, options=None, preemptable=None, resources=None, restartable=None, role=None, tags=None, workdir=None):  # noqa: E501
        """JobSpec - a model defined in OpenAPI"""  # noqa: E501

        self._bid = None
        self._command = None
        self._data = None
        self._environment_vars = None
        self._image = None
        self._interactive = None
        self._is_process_agent = None
        self._max_run_time = None
        self._name = None
        self._options = None
        self._preemptable = None
        self._resources = None
        self._restartable = None
        self._role = None
        self._tags = None
        self._workdir = None
        self.discriminator = None

        if bid is not None:
            self.bid = bid
        if command is not None:
            self.command = command
        if data is not None:
            self.data = data
        if environment_vars is not None:
            self.environment_vars = environment_vars
        if image is not None:
            self.image = image
        if interactive is not None:
            self.interactive = interactive
        if is_process_agent is not None:
            self.is_process_agent = is_process_agent
        if max_run_time is not None:
            self.max_run_time = max_run_time
        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if preemptable is not None:
            self.preemptable = preemptable
        if resources is not None:
            self.resources = resources
        if restartable is not None:
            self.restartable = restartable
        if role is not None:
            self.role = role
        if tags is not None:
            self.tags = tags
        if workdir is not None:
            self.workdir = workdir

    @property
    def bid(self):
        """Gets the bid of this JobSpec.  # noqa: E501


        :return: The bid of this JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this JobSpec.


        :param bid: The bid of this JobSpec.  # noqa: E501
        :type: int
        """
        if bid is not None and bid < 0:  # noqa: E501
            raise ValueError("Invalid value for `bid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bid = bid

    @property
    def command(self):
        """Gets the command of this JobSpec.  # noqa: E501


        :return: The command of this JobSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this JobSpec.


        :param command: The command of this JobSpec.  # noqa: E501
        :type: list[str]
        """

        self._command = command

    @property
    def data(self):
        """Gets the data of this JobSpec.  # noqa: E501


        :return: The data of this JobSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this JobSpec.


        :param data: The data of this JobSpec.  # noqa: E501
        :type: list[str]
        """

        self._data = data

    @property
    def environment_vars(self):
        """Gets the environment_vars of this JobSpec.  # noqa: E501


        :return: The environment_vars of this JobSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._environment_vars

    @environment_vars.setter
    def environment_vars(self, environment_vars):
        """Sets the environment_vars of this JobSpec.


        :param environment_vars: The environment_vars of this JobSpec.  # noqa: E501
        :type: list[str]
        """

        self._environment_vars = environment_vars

    @property
    def image(self):
        """Gets the image of this JobSpec.  # noqa: E501


        :return: The image of this JobSpec.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this JobSpec.


        :param image: The image of this JobSpec.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def interactive(self):
        """Gets the interactive of this JobSpec.  # noqa: E501


        :return: The interactive of this JobSpec.  # noqa: E501
        :rtype: bool
        """
        return self._interactive

    @interactive.setter
    def interactive(self, interactive):
        """Sets the interactive of this JobSpec.


        :param interactive: The interactive of this JobSpec.  # noqa: E501
        :type: bool
        """

        self._interactive = interactive

    @property
    def is_process_agent(self):
        """Gets the is_process_agent of this JobSpec.  # noqa: E501


        :return: The is_process_agent of this JobSpec.  # noqa: E501
        :rtype: bool
        """
        return self._is_process_agent

    @is_process_agent.setter
    def is_process_agent(self, is_process_agent):
        """Sets the is_process_agent of this JobSpec.


        :param is_process_agent: The is_process_agent of this JobSpec.  # noqa: E501
        :type: bool
        """

        self._is_process_agent = is_process_agent

    @property
    def max_run_time(self):
        """Gets the max_run_time of this JobSpec.  # noqa: E501


        :return: The max_run_time of this JobSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_run_time

    @max_run_time.setter
    def max_run_time(self, max_run_time):
        """Sets the max_run_time of this JobSpec.


        :param max_run_time: The max_run_time of this JobSpec.  # noqa: E501
        :type: int
        """
        if max_run_time is not None and max_run_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `max_run_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_run_time = max_run_time

    @property
    def name(self):
        """Gets the name of this JobSpec.  # noqa: E501


        :return: The name of this JobSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobSpec.


        :param name: The name of this JobSpec.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this JobSpec.  # noqa: E501


        :return: The options of this JobSpec.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this JobSpec.


        :param options: The options of this JobSpec.  # noqa: E501
        :type: dict(str, object)
        """

        self._options = options

    @property
    def preemptable(self):
        """Gets the preemptable of this JobSpec.  # noqa: E501


        :return: The preemptable of this JobSpec.  # noqa: E501
        :rtype: bool
        """
        return self._preemptable

    @preemptable.setter
    def preemptable(self, preemptable):
        """Sets the preemptable of this JobSpec.


        :param preemptable: The preemptable of this JobSpec.  # noqa: E501
        :type: bool
        """

        self._preemptable = preemptable

    @property
    def resources(self):
        """Gets the resources of this JobSpec.  # noqa: E501


        :return: The resources of this JobSpec.  # noqa: E501
        :rtype: JobSpecResources
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this JobSpec.


        :param resources: The resources of this JobSpec.  # noqa: E501
        :type: JobSpecResources
        """

        self._resources = resources

    @property
    def restartable(self):
        """Gets the restartable of this JobSpec.  # noqa: E501


        :return: The restartable of this JobSpec.  # noqa: E501
        :rtype: bool
        """
        return self._restartable

    @restartable.setter
    def restartable(self, restartable):
        """Sets the restartable of this JobSpec.


        :param restartable: The restartable of this JobSpec.  # noqa: E501
        :type: bool
        """

        self._restartable = restartable

    @property
    def role(self):
        """Gets the role of this JobSpec.  # noqa: E501


        :return: The role of this JobSpec.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this JobSpec.


        :param role: The role of this JobSpec.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def tags(self):
        """Gets the tags of this JobSpec.  # noqa: E501

        Tags of the resource  # noqa: E501

        :return: The tags of this JobSpec.  # noqa: E501
        :rtype: list[object]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this JobSpec.

        Tags of the resource  # noqa: E501

        :param tags: The tags of this JobSpec.  # noqa: E501
        :type: list[object]
        """

        self._tags = tags

    @property
    def workdir(self):
        """Gets the workdir of this JobSpec.  # noqa: E501


        :return: The workdir of this JobSpec.  # noqa: E501
        :rtype: str
        """
        return self._workdir

    @workdir.setter
    def workdir(self, workdir):
        """Sets the workdir of this JobSpec.


        :param workdir: The workdir of this JobSpec.  # noqa: E501
        :type: str
        """

        self._workdir = workdir

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
        if not isinstance(other, JobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
