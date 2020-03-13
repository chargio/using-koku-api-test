# coding: utf-8

"""
    Cost Management

    The API for Project Koku and OpenShift cost management. You can find out more about Cost Management at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class CostModelResp(object):
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
        'name': 'str',
        'description': 'str',
        'source_type': 'str',
        'providers': 'list[CostModelRespProviders]',
        'rates': 'list[Rate]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'source_type': 'source_type',
        'providers': 'providers',
        'rates': 'rates'
    }

    def __init__(self, name=None, description=None, source_type=None, providers=None, rates=None, local_vars_configuration=None):  # noqa: E501
        """CostModelResp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._source_type = None
        self._providers = None
        self._rates = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.source_type = source_type
        if providers is not None:
            self.providers = providers
        if rates is not None:
            self.rates = rates

    @property
    def name(self):
        """Gets the name of this CostModelResp.  # noqa: E501


        :return: The name of this CostModelResp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CostModelResp.


        :param name: The name of this CostModelResp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CostModelResp.  # noqa: E501


        :return: The description of this CostModelResp.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CostModelResp.


        :param description: The description of this CostModelResp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def source_type(self):
        """Gets the source_type of this CostModelResp.  # noqa: E501


        :return: The source_type of this CostModelResp.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this CostModelResp.


        :param source_type: The source_type of this CostModelResp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source_type is None:  # noqa: E501
            raise ValueError("Invalid value for `source_type`, must not be `None`")  # noqa: E501

        self._source_type = source_type

    @property
    def providers(self):
        """Gets the providers of this CostModelResp.  # noqa: E501


        :return: The providers of this CostModelResp.  # noqa: E501
        :rtype: list[CostModelRespProviders]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """Sets the providers of this CostModelResp.


        :param providers: The providers of this CostModelResp.  # noqa: E501
        :type: list[CostModelRespProviders]
        """

        self._providers = providers

    @property
    def rates(self):
        """Gets the rates of this CostModelResp.  # noqa: E501


        :return: The rates of this CostModelResp.  # noqa: E501
        :rtype: list[Rate]
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this CostModelResp.


        :param rates: The rates of this CostModelResp.  # noqa: E501
        :type: list[Rate]
        """

        self._rates = rates

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
        if not isinstance(other, CostModelResp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CostModelResp):
            return True

        return self.to_dict() != other.to_dict()
