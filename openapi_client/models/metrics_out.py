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


class MetricsOut(object):
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
        'source_type': 'str',
        'metric': 'str',
        'label_metric': 'str',
        'label_measurement': 'str',
        'label_measurement_unit': 'str',
        'default_cost_type': 'str'
    }

    attribute_map = {
        'source_type': 'source_type',
        'metric': 'metric',
        'label_metric': 'label_metric',
        'label_measurement': 'label_measurement',
        'label_measurement_unit': 'label_measurement_unit',
        'default_cost_type': 'default_cost_type'
    }

    def __init__(self, source_type=None, metric=None, label_metric=None, label_measurement=None, label_measurement_unit=None, default_cost_type=None, local_vars_configuration=None):  # noqa: E501
        """MetricsOut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_type = None
        self._metric = None
        self._label_metric = None
        self._label_measurement = None
        self._label_measurement_unit = None
        self._default_cost_type = None
        self.discriminator = None

        self.source_type = source_type
        self.metric = metric
        self.label_metric = label_metric
        self.label_measurement = label_measurement
        self.label_measurement_unit = label_measurement_unit
        self.default_cost_type = default_cost_type

    @property
    def source_type(self):
        """Gets the source_type of this MetricsOut.  # noqa: E501


        :return: The source_type of this MetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this MetricsOut.


        :param source_type: The source_type of this MetricsOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source_type is None:  # noqa: E501
            raise ValueError("Invalid value for `source_type`, must not be `None`")  # noqa: E501

        self._source_type = source_type

    @property
    def metric(self):
        """Gets the metric of this MetricsOut.  # noqa: E501


        :return: The metric of this MetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this MetricsOut.


        :param metric: The metric of this MetricsOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and metric is None:  # noqa: E501
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def label_metric(self):
        """Gets the label_metric of this MetricsOut.  # noqa: E501


        :return: The label_metric of this MetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._label_metric

    @label_metric.setter
    def label_metric(self, label_metric):
        """Sets the label_metric of this MetricsOut.


        :param label_metric: The label_metric of this MetricsOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label_metric is None:  # noqa: E501
            raise ValueError("Invalid value for `label_metric`, must not be `None`")  # noqa: E501

        self._label_metric = label_metric

    @property
    def label_measurement(self):
        """Gets the label_measurement of this MetricsOut.  # noqa: E501


        :return: The label_measurement of this MetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._label_measurement

    @label_measurement.setter
    def label_measurement(self, label_measurement):
        """Sets the label_measurement of this MetricsOut.


        :param label_measurement: The label_measurement of this MetricsOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label_measurement is None:  # noqa: E501
            raise ValueError("Invalid value for `label_measurement`, must not be `None`")  # noqa: E501

        self._label_measurement = label_measurement

    @property
    def label_measurement_unit(self):
        """Gets the label_measurement_unit of this MetricsOut.  # noqa: E501


        :return: The label_measurement_unit of this MetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._label_measurement_unit

    @label_measurement_unit.setter
    def label_measurement_unit(self, label_measurement_unit):
        """Sets the label_measurement_unit of this MetricsOut.


        :param label_measurement_unit: The label_measurement_unit of this MetricsOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label_measurement_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `label_measurement_unit`, must not be `None`")  # noqa: E501

        self._label_measurement_unit = label_measurement_unit

    @property
    def default_cost_type(self):
        """Gets the default_cost_type of this MetricsOut.  # noqa: E501


        :return: The default_cost_type of this MetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._default_cost_type

    @default_cost_type.setter
    def default_cost_type(self, default_cost_type):
        """Sets the default_cost_type of this MetricsOut.


        :param default_cost_type: The default_cost_type of this MetricsOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_cost_type is None:  # noqa: E501
            raise ValueError("Invalid value for `default_cost_type`, must not be `None`")  # noqa: E501

        self._default_cost_type = default_cost_type

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
        if not isinstance(other, MetricsOut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricsOut):
            return True

        return self.to_dict() != other.to_dict()
