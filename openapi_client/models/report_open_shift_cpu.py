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


class ReportOpenShiftCpu(object):
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
        'meta': 'ReportPaginationMeta',
        'links': 'PaginationLinks',
        'data': 'list[object]'
    }

    attribute_map = {
        'meta': 'meta',
        'links': 'links',
        'data': 'data'
    }

    def __init__(self, meta=None, links=None, data=None, local_vars_configuration=None):  # noqa: E501
        """ReportOpenShiftCpu - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._meta = None
        self._links = None
        self._data = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if links is not None:
            self.links = links
        self.data = data

    @property
    def meta(self):
        """Gets the meta of this ReportOpenShiftCpu.  # noqa: E501


        :return: The meta of this ReportOpenShiftCpu.  # noqa: E501
        :rtype: ReportPaginationMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ReportOpenShiftCpu.


        :param meta: The meta of this ReportOpenShiftCpu.  # noqa: E501
        :type: ReportPaginationMeta
        """

        self._meta = meta

    @property
    def links(self):
        """Gets the links of this ReportOpenShiftCpu.  # noqa: E501


        :return: The links of this ReportOpenShiftCpu.  # noqa: E501
        :rtype: PaginationLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ReportOpenShiftCpu.


        :param links: The links of this ReportOpenShiftCpu.  # noqa: E501
        :type: PaginationLinks
        """

        self._links = links

    @property
    def data(self):
        """Gets the data of this ReportOpenShiftCpu.  # noqa: E501


        :return: The data of this ReportOpenShiftCpu.  # noqa: E501
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ReportOpenShiftCpu.


        :param data: The data of this ReportOpenShiftCpu.  # noqa: E501
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
        if not isinstance(other, ReportOpenShiftCpu):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportOpenShiftCpu):
            return True

        return self.to_dict() != other.to_dict()
