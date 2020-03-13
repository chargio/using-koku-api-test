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


class ReportOrdering(object):
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
        'cost': 'str',
        'usage': 'str',
        'delta': 'str',
        'account_alias': 'str',
        'region': 'str',
        'service': 'str'
    }

    attribute_map = {
        'cost': 'cost',
        'usage': 'usage',
        'delta': 'delta',
        'account_alias': 'account_alias',
        'region': 'region',
        'service': 'service'
    }

    def __init__(self, cost=None, usage=None, delta=None, account_alias=None, region=None, service=None, local_vars_configuration=None):  # noqa: E501
        """ReportOrdering - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cost = None
        self._usage = None
        self._delta = None
        self._account_alias = None
        self._region = None
        self._service = None
        self.discriminator = None

        if cost is not None:
            self.cost = cost
        if usage is not None:
            self.usage = usage
        if delta is not None:
            self.delta = delta
        if account_alias is not None:
            self.account_alias = account_alias
        if region is not None:
            self.region = region
        if service is not None:
            self.service = service

    @property
    def cost(self):
        """Gets the cost of this ReportOrdering.  # noqa: E501


        :return: The cost of this ReportOrdering.  # noqa: E501
        :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this ReportOrdering.


        :param cost: The cost of this ReportOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cost not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cost` ({0}), must be one of {1}"  # noqa: E501
                .format(cost, allowed_values)
            )

        self._cost = cost

    @property
    def usage(self):
        """Gets the usage of this ReportOrdering.  # noqa: E501


        :return: The usage of this ReportOrdering.  # noqa: E501
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ReportOrdering.


        :param usage: The usage of this ReportOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and usage not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `usage` ({0}), must be one of {1}"  # noqa: E501
                .format(usage, allowed_values)
            )

        self._usage = usage

    @property
    def delta(self):
        """Gets the delta of this ReportOrdering.  # noqa: E501


        :return: The delta of this ReportOrdering.  # noqa: E501
        :rtype: str
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """Sets the delta of this ReportOrdering.


        :param delta: The delta of this ReportOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and delta not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `delta` ({0}), must be one of {1}"  # noqa: E501
                .format(delta, allowed_values)
            )

        self._delta = delta

    @property
    def account_alias(self):
        """Gets the account_alias of this ReportOrdering.  # noqa: E501


        :return: The account_alias of this ReportOrdering.  # noqa: E501
        :rtype: str
        """
        return self._account_alias

    @account_alias.setter
    def account_alias(self, account_alias):
        """Sets the account_alias of this ReportOrdering.


        :param account_alias: The account_alias of this ReportOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and account_alias not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `account_alias` ({0}), must be one of {1}"  # noqa: E501
                .format(account_alias, allowed_values)
            )

        self._account_alias = account_alias

    @property
    def region(self):
        """Gets the region of this ReportOrdering.  # noqa: E501


        :return: The region of this ReportOrdering.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ReportOrdering.


        :param region: The region of this ReportOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and region not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `region` ({0}), must be one of {1}"  # noqa: E501
                .format(region, allowed_values)
            )

        self._region = region

    @property
    def service(self):
        """Gets the service of this ReportOrdering.  # noqa: E501


        :return: The service of this ReportOrdering.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ReportOrdering.


        :param service: The service of this ReportOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and service not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

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
        if not isinstance(other, ReportOrdering):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportOrdering):
            return True

        return self.to_dict() != other.to_dict()
