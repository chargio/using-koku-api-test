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


class ReportFilter(object):
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
        'limit': 'int',
        'offset': 'int',
        'resolution': 'ReportResolution',
        'time_scope_value': 'ReportTimeScopeValue',
        'time_scope_units': 'ReportTimeScopeUnits',
        'resource_scope': 'list[ReportResourceScope]',
        'account': 'list[str]',
        'service': 'list[str]',
        'region': 'list[str]',
        'az': 'list[str]',
        'tag': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'resolution': 'resolution',
        'time_scope_value': 'time_scope_value',
        'time_scope_units': 'time_scope_units',
        'resource_scope': 'resource_scope',
        'account': 'account',
        'service': 'service',
        'region': 'region',
        'az': 'az',
        'tag': 'tag'
    }

    def __init__(self, limit=None, offset=None, resolution=None, time_scope_value=None, time_scope_units=None, resource_scope=None, account=None, service=None, region=None, az=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """ReportFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._limit = None
        self._offset = None
        self._resolution = None
        self._time_scope_value = None
        self._time_scope_units = None
        self._resource_scope = None
        self._account = None
        self._service = None
        self._region = None
        self._az = None
        self._tag = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if resolution is not None:
            self.resolution = resolution
        if time_scope_value is not None:
            self.time_scope_value = time_scope_value
        if time_scope_units is not None:
            self.time_scope_units = time_scope_units
        if resource_scope is not None:
            self.resource_scope = resource_scope
        if account is not None:
            self.account = account
        if service is not None:
            self.service = service
        if region is not None:
            self.region = region
        if az is not None:
            self.az = az
        if tag is not None:
            self.tag = tag

    @property
    def limit(self):
        """Gets the limit of this ReportFilter.  # noqa: E501

        Limits the data points returns and aggregates remaining data.  # noqa: E501

        :return: The limit of this ReportFilter.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ReportFilter.

        Limits the data points returns and aggregates remaining data.  # noqa: E501

        :param limit: The limit of this ReportFilter.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ReportFilter.  # noqa: E501

        Offsets the data points returned when using limit.  # noqa: E501

        :return: The offset of this ReportFilter.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ReportFilter.

        Offsets the data points returned when using limit.  # noqa: E501

        :param offset: The offset of this ReportFilter.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def resolution(self):
        """Gets the resolution of this ReportFilter.  # noqa: E501


        :return: The resolution of this ReportFilter.  # noqa: E501
        :rtype: ReportResolution
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ReportFilter.


        :param resolution: The resolution of this ReportFilter.  # noqa: E501
        :type: ReportResolution
        """

        self._resolution = resolution

    @property
    def time_scope_value(self):
        """Gets the time_scope_value of this ReportFilter.  # noqa: E501


        :return: The time_scope_value of this ReportFilter.  # noqa: E501
        :rtype: ReportTimeScopeValue
        """
        return self._time_scope_value

    @time_scope_value.setter
    def time_scope_value(self, time_scope_value):
        """Sets the time_scope_value of this ReportFilter.


        :param time_scope_value: The time_scope_value of this ReportFilter.  # noqa: E501
        :type: ReportTimeScopeValue
        """

        self._time_scope_value = time_scope_value

    @property
    def time_scope_units(self):
        """Gets the time_scope_units of this ReportFilter.  # noqa: E501


        :return: The time_scope_units of this ReportFilter.  # noqa: E501
        :rtype: ReportTimeScopeUnits
        """
        return self._time_scope_units

    @time_scope_units.setter
    def time_scope_units(self, time_scope_units):
        """Sets the time_scope_units of this ReportFilter.


        :param time_scope_units: The time_scope_units of this ReportFilter.  # noqa: E501
        :type: ReportTimeScopeUnits
        """

        self._time_scope_units = time_scope_units

    @property
    def resource_scope(self):
        """Gets the resource_scope of this ReportFilter.  # noqa: E501


        :return: The resource_scope of this ReportFilter.  # noqa: E501
        :rtype: list[ReportResourceScope]
        """
        return self._resource_scope

    @resource_scope.setter
    def resource_scope(self, resource_scope):
        """Sets the resource_scope of this ReportFilter.


        :param resource_scope: The resource_scope of this ReportFilter.  # noqa: E501
        :type: list[ReportResourceScope]
        """

        self._resource_scope = resource_scope

    @property
    def account(self):
        """Gets the account of this ReportFilter.  # noqa: E501


        :return: The account of this ReportFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ReportFilter.


        :param account: The account of this ReportFilter.  # noqa: E501
        :type: list[str]
        """

        self._account = account

    @property
    def service(self):
        """Gets the service of this ReportFilter.  # noqa: E501


        :return: The service of this ReportFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ReportFilter.


        :param service: The service of this ReportFilter.  # noqa: E501
        :type: list[str]
        """

        self._service = service

    @property
    def region(self):
        """Gets the region of this ReportFilter.  # noqa: E501


        :return: The region of this ReportFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ReportFilter.


        :param region: The region of this ReportFilter.  # noqa: E501
        :type: list[str]
        """

        self._region = region

    @property
    def az(self):
        """Gets the az of this ReportFilter.  # noqa: E501


        :return: The az of this ReportFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this ReportFilter.


        :param az: The az of this ReportFilter.  # noqa: E501
        :type: list[str]
        """

        self._az = az

    @property
    def tag(self):
        """Gets the tag of this ReportFilter.  # noqa: E501


        :return: The tag of this ReportFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ReportFilter.


        :param tag: The tag of this ReportFilter.  # noqa: E501
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
        if not isinstance(other, ReportFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportFilter):
            return True

        return self.to_dict() != other.to_dict()
