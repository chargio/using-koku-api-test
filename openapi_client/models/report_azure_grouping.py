# coding: utf-8

"""
    Cost Management

    The API for Project Koku and OpenShift cost management. You can find out more about Project Koku at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ReportAzureGrouping(object):
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
        'subscription_guid': 'list[str]',
        'service_name': 'list[str]',
        'resource_location': 'list[str]',
        'instance_type': 'list[str]',
        'tag': 'list[str]'
    }

    attribute_map = {
        'subscription_guid': 'subscription_guid',
        'service_name': 'service_name',
        'resource_location': 'resource_location',
        'instance_type': 'instance_type',
        'tag': 'tag'
    }

    def __init__(self, subscription_guid=None, service_name=None, resource_location=None, instance_type=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """ReportAzureGrouping - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._subscription_guid = None
        self._service_name = None
        self._resource_location = None
        self._instance_type = None
        self._tag = None
        self.discriminator = None

        if subscription_guid is not None:
            self.subscription_guid = subscription_guid
        if service_name is not None:
            self.service_name = service_name
        if resource_location is not None:
            self.resource_location = resource_location
        if instance_type is not None:
            self.instance_type = instance_type
        if tag is not None:
            self.tag = tag

    @property
    def subscription_guid(self):
        """Gets the subscription_guid of this ReportAzureGrouping.  # noqa: E501


        :return: The subscription_guid of this ReportAzureGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._subscription_guid

    @subscription_guid.setter
    def subscription_guid(self, subscription_guid):
        """Sets the subscription_guid of this ReportAzureGrouping.


        :param subscription_guid: The subscription_guid of this ReportAzureGrouping.  # noqa: E501
        :type: list[str]
        """

        self._subscription_guid = subscription_guid

    @property
    def service_name(self):
        """Gets the service_name of this ReportAzureGrouping.  # noqa: E501


        :return: The service_name of this ReportAzureGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ReportAzureGrouping.


        :param service_name: The service_name of this ReportAzureGrouping.  # noqa: E501
        :type: list[str]
        """

        self._service_name = service_name

    @property
    def resource_location(self):
        """Gets the resource_location of this ReportAzureGrouping.  # noqa: E501


        :return: The resource_location of this ReportAzureGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_location

    @resource_location.setter
    def resource_location(self, resource_location):
        """Sets the resource_location of this ReportAzureGrouping.


        :param resource_location: The resource_location of this ReportAzureGrouping.  # noqa: E501
        :type: list[str]
        """

        self._resource_location = resource_location

    @property
    def instance_type(self):
        """Gets the instance_type of this ReportAzureGrouping.  # noqa: E501


        :return: The instance_type of this ReportAzureGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ReportAzureGrouping.


        :param instance_type: The instance_type of this ReportAzureGrouping.  # noqa: E501
        :type: list[str]
        """

        self._instance_type = instance_type

    @property
    def tag(self):
        """Gets the tag of this ReportAzureGrouping.  # noqa: E501


        :return: The tag of this ReportAzureGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ReportAzureGrouping.


        :param tag: The tag of this ReportAzureGrouping.  # noqa: E501
        :type: list[str]
        """

        self._tag = tag

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
        if not isinstance(other, ReportAzureGrouping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportAzureGrouping):
            return True

        return self.to_dict() != other.to_dict()
