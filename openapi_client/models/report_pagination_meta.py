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


class ReportPaginationMeta(object):
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
        'count': 'int',
        'delta': 'ReportDelta',
        'group_by': 'OneOfReportGroupingReportAzureGroupingReportOpenShiftGroupingReportOpenShiftAWSGroupingReportOpenShiftAzureGrouping',
        'order_by': 'OneOfReportOrderingReportAzureOrderingReportCostsOpenShiftOrderingReportInventoryOpenShiftOrderingReportOpenShiftAWSOrderingReportOpenShiftAzureOrdering',
        'filter': 'OneOfReportFilterReportAzureFilterReportOpenShiftFilterReportOpenShiftAWSFilterReportOpenShiftAzureFilter',
        'units': 'str'
    }

    attribute_map = {
        'count': 'count',
        'delta': 'delta',
        'group_by': 'group_by',
        'order_by': 'order_by',
        'filter': 'filter',
        'units': 'units'
    }

    def __init__(self, count=None, delta=None, group_by=None, order_by=None, filter=None, units=None, local_vars_configuration=None):  # noqa: E501
        """ReportPaginationMeta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._delta = None
        self._group_by = None
        self._order_by = None
        self._filter = None
        self._units = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if delta is not None:
            self.delta = delta
        if group_by is not None:
            self.group_by = group_by
        if order_by is not None:
            self.order_by = order_by
        if filter is not None:
            self.filter = filter
        if units is not None:
            self.units = units

    @property
    def count(self):
        """Gets the count of this ReportPaginationMeta.  # noqa: E501


        :return: The count of this ReportPaginationMeta.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ReportPaginationMeta.


        :param count: The count of this ReportPaginationMeta.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def delta(self):
        """Gets the delta of this ReportPaginationMeta.  # noqa: E501


        :return: The delta of this ReportPaginationMeta.  # noqa: E501
        :rtype: ReportDelta
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """Sets the delta of this ReportPaginationMeta.


        :param delta: The delta of this ReportPaginationMeta.  # noqa: E501
        :type: ReportDelta
        """

        self._delta = delta

    @property
    def group_by(self):
        """Gets the group_by of this ReportPaginationMeta.  # noqa: E501


        :return: The group_by of this ReportPaginationMeta.  # noqa: E501
        :rtype: OneOfReportGroupingReportAzureGroupingReportOpenShiftGroupingReportOpenShiftAWSGroupingReportOpenShiftAzureGrouping
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ReportPaginationMeta.


        :param group_by: The group_by of this ReportPaginationMeta.  # noqa: E501
        :type: OneOfReportGroupingReportAzureGroupingReportOpenShiftGroupingReportOpenShiftAWSGroupingReportOpenShiftAzureGrouping
        """

        self._group_by = group_by

    @property
    def order_by(self):
        """Gets the order_by of this ReportPaginationMeta.  # noqa: E501


        :return: The order_by of this ReportPaginationMeta.  # noqa: E501
        :rtype: OneOfReportOrderingReportAzureOrderingReportCostsOpenShiftOrderingReportInventoryOpenShiftOrderingReportOpenShiftAWSOrderingReportOpenShiftAzureOrdering
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ReportPaginationMeta.


        :param order_by: The order_by of this ReportPaginationMeta.  # noqa: E501
        :type: OneOfReportOrderingReportAzureOrderingReportCostsOpenShiftOrderingReportInventoryOpenShiftOrderingReportOpenShiftAWSOrderingReportOpenShiftAzureOrdering
        """

        self._order_by = order_by

    @property
    def filter(self):
        """Gets the filter of this ReportPaginationMeta.  # noqa: E501


        :return: The filter of this ReportPaginationMeta.  # noqa: E501
        :rtype: OneOfReportFilterReportAzureFilterReportOpenShiftFilterReportOpenShiftAWSFilterReportOpenShiftAzureFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ReportPaginationMeta.


        :param filter: The filter of this ReportPaginationMeta.  # noqa: E501
        :type: OneOfReportFilterReportAzureFilterReportOpenShiftFilterReportOpenShiftAWSFilterReportOpenShiftAzureFilter
        """

        self._filter = filter

    @property
    def units(self):
        """Gets the units of this ReportPaginationMeta.  # noqa: E501

        The units for the output data.  # noqa: E501

        :return: The units of this ReportPaginationMeta.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this ReportPaginationMeta.

        The units for the output data.  # noqa: E501

        :param units: The units of this ReportPaginationMeta.  # noqa: E501
        :type: str
        """

        self._units = units

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
        if not isinstance(other, ReportPaginationMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportPaginationMeta):
            return True

        return self.to_dict() != other.to_dict()
