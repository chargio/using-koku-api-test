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


class ReportOpenShiftAzureStorageInventory(object):
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
        'group_by': 'ReportOpenShiftAzureGrouping',
        'order_by': 'ReportOpenShiftAzureOrdering',
        'filter': 'ReportOpenShiftAzureFilter',
        'data': 'list[object]'
    }

    attribute_map = {
        'group_by': 'group_by',
        'order_by': 'order_by',
        'filter': 'filter',
        'data': 'data'
    }

    def __init__(self, group_by=None, order_by=None, filter=None, data=None, local_vars_configuration=None):  # noqa: E501
        """ReportOpenShiftAzureStorageInventory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_by = None
        self._order_by = None
        self._filter = None
        self._data = None
        self.discriminator = None

        if group_by is not None:
            self.group_by = group_by
        if order_by is not None:
            self.order_by = order_by
        if filter is not None:
            self.filter = filter
        self.data = data

    @property
    def group_by(self):
        """Gets the group_by of this ReportOpenShiftAzureStorageInventory.  # noqa: E501


        :return: The group_by of this ReportOpenShiftAzureStorageInventory.  # noqa: E501
        :rtype: ReportOpenShiftAzureGrouping
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ReportOpenShiftAzureStorageInventory.


        :param group_by: The group_by of this ReportOpenShiftAzureStorageInventory.  # noqa: E501
        :type: ReportOpenShiftAzureGrouping
        """

        self._group_by = group_by

    @property
    def order_by(self):
        """Gets the order_by of this ReportOpenShiftAzureStorageInventory.  # noqa: E501


        :return: The order_by of this ReportOpenShiftAzureStorageInventory.  # noqa: E501
        :rtype: ReportOpenShiftAzureOrdering
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ReportOpenShiftAzureStorageInventory.


        :param order_by: The order_by of this ReportOpenShiftAzureStorageInventory.  # noqa: E501
        :type: ReportOpenShiftAzureOrdering
        """

        self._order_by = order_by

    @property
    def filter(self):
        """Gets the filter of this ReportOpenShiftAzureStorageInventory.  # noqa: E501


        :return: The filter of this ReportOpenShiftAzureStorageInventory.  # noqa: E501
        :rtype: ReportOpenShiftAzureFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ReportOpenShiftAzureStorageInventory.


        :param filter: The filter of this ReportOpenShiftAzureStorageInventory.  # noqa: E501
        :type: ReportOpenShiftAzureFilter
        """

        self._filter = filter

    @property
    def data(self):
        """Gets the data of this ReportOpenShiftAzureStorageInventory.  # noqa: E501


        :return: The data of this ReportOpenShiftAzureStorageInventory.  # noqa: E501
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ReportOpenShiftAzureStorageInventory.


        :param data: The data of this ReportOpenShiftAzureStorageInventory.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, ReportOpenShiftAzureStorageInventory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportOpenShiftAzureStorageInventory):
            return True

        return self.to_dict() != other.to_dict()
