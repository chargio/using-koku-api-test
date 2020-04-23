# coding: utf-8

"""
    Cost Management

    The API for Project Koku and OpenShift cost management. You can find out more about Project Koku at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Status(object):
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
        'api_version': 'int',
        'commit': 'str',
        'server_address': 'str',
        'rbac_cache_ttl': 'int',
        'platform_info': 'object',
        'python_version': 'str',
        'modules': 'object'
    }

    attribute_map = {
        'api_version': 'api_version',
        'commit': 'commit',
        'server_address': 'server_address',
        'rbac_cache_ttl': 'rbac_cache_ttl',
        'platform_info': 'platform_info',
        'python_version': 'python_version',
        'modules': 'modules'
    }

    def __init__(self, api_version=None, commit=None, server_address=None, rbac_cache_ttl=None, platform_info=None, python_version=None, modules=None, local_vars_configuration=None):  # noqa: E501
        """Status - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._commit = None
        self._server_address = None
        self._rbac_cache_ttl = None
        self._platform_info = None
        self._python_version = None
        self._modules = None
        self.discriminator = None

        self.api_version = api_version
        if commit is not None:
            self.commit = commit
        if server_address is not None:
            self.server_address = server_address
        if rbac_cache_ttl is not None:
            self.rbac_cache_ttl = rbac_cache_ttl
        if platform_info is not None:
            self.platform_info = platform_info
        if python_version is not None:
            self.python_version = python_version
        if modules is not None:
            self.modules = modules

    @property
    def api_version(self):
        """Gets the api_version of this Status.  # noqa: E501


        :return: The api_version of this Status.  # noqa: E501
        :rtype: int
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this Status.


        :param api_version: The api_version of this Status.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and api_version is None:  # noqa: E501
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def commit(self):
        """Gets the commit of this Status.  # noqa: E501


        :return: The commit of this Status.  # noqa: E501
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this Status.


        :param commit: The commit of this Status.  # noqa: E501
        :type: str
        """

        self._commit = commit

    @property
    def server_address(self):
        """Gets the server_address of this Status.  # noqa: E501


        :return: The server_address of this Status.  # noqa: E501
        :rtype: str
        """
        return self._server_address

    @server_address.setter
    def server_address(self, server_address):
        """Sets the server_address of this Status.


        :param server_address: The server_address of this Status.  # noqa: E501
        :type: str
        """

        self._server_address = server_address

    @property
    def rbac_cache_ttl(self):
        """Gets the rbac_cache_ttl of this Status.  # noqa: E501


        :return: The rbac_cache_ttl of this Status.  # noqa: E501
        :rtype: int
        """
        return self._rbac_cache_ttl

    @rbac_cache_ttl.setter
    def rbac_cache_ttl(self, rbac_cache_ttl):
        """Sets the rbac_cache_ttl of this Status.


        :param rbac_cache_ttl: The rbac_cache_ttl of this Status.  # noqa: E501
        :type: int
        """

        self._rbac_cache_ttl = rbac_cache_ttl

    @property
    def platform_info(self):
        """Gets the platform_info of this Status.  # noqa: E501


        :return: The platform_info of this Status.  # noqa: E501
        :rtype: object
        """
        return self._platform_info

    @platform_info.setter
    def platform_info(self, platform_info):
        """Sets the platform_info of this Status.


        :param platform_info: The platform_info of this Status.  # noqa: E501
        :type: object
        """

        self._platform_info = platform_info

    @property
    def python_version(self):
        """Gets the python_version of this Status.  # noqa: E501


        :return: The python_version of this Status.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this Status.


        :param python_version: The python_version of this Status.  # noqa: E501
        :type: str
        """

        self._python_version = python_version

    @property
    def modules(self):
        """Gets the modules of this Status.  # noqa: E501


        :return: The modules of this Status.  # noqa: E501
        :rtype: object
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this Status.


        :param modules: The modules of this Status.  # noqa: E501
        :type: object
        """

        self._modules = modules

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
        if not isinstance(other, Status):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Status):
            return True

        return self.to_dict() != other.to_dict()
