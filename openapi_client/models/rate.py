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


class Rate(object):
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
        'uuid': 'str',
        'metric': 'object',
        'cost_type': 'str',
        'tiered_rates': 'list[object]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'metric': 'metric',
        'cost_type': 'cost_type',
        'tiered_rates': 'tiered_rates'
    }

    def __init__(self, uuid=None, metric=None, cost_type=None, tiered_rates=None, local_vars_configuration=None):  # noqa: E501
        """Rate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._metric = None
        self._cost_type = None
        self._tiered_rates = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        self.metric = metric
        if cost_type is not None:
            self.cost_type = cost_type
        if tiered_rates is not None:
            self.tiered_rates = tiered_rates

    @property
    def uuid(self):
        """Gets the uuid of this Rate.  # noqa: E501


        :return: The uuid of this Rate.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Rate.


        :param uuid: The uuid of this Rate.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def metric(self):
        """Gets the metric of this Rate.  # noqa: E501


        :return: The metric of this Rate.  # noqa: E501
        :rtype: object
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this Rate.


        :param metric: The metric of this Rate.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and metric is None:  # noqa: E501
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def cost_type(self):
        """Gets the cost_type of this Rate.  # noqa: E501


        :return: The cost_type of this Rate.  # noqa: E501
        :rtype: str
        """
        return self._cost_type

    @cost_type.setter
    def cost_type(self, cost_type):
        """Sets the cost_type of this Rate.


        :param cost_type: The cost_type of this Rate.  # noqa: E501
        :type: str
        """
        allowed_values = ["Infrastructure", "Supplementary"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cost_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cost_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cost_type, allowed_values)
            )

        self._cost_type = cost_type

    @property
    def tiered_rates(self):
        """Gets the tiered_rates of this Rate.  # noqa: E501


        :return: The tiered_rates of this Rate.  # noqa: E501
        :rtype: list[object]
        """
        return self._tiered_rates

    @tiered_rates.setter
    def tiered_rates(self, tiered_rates):
        """Sets the tiered_rates of this Rate.


        :param tiered_rates: The tiered_rates of this Rate.  # noqa: E501
        :type: list[object]
        """

        self._tiered_rates = tiered_rates

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
        if not isinstance(other, Rate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rate):
            return True

        return self.to_dict() != other.to_dict()
