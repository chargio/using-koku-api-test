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


class SourceIn(object):
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
        'authentication': 'object',
        'billing_source': 'object'
    }

    attribute_map = {
        'authentication': 'authentication',
        'billing_source': 'billing_source'
    }

    def __init__(self, authentication=None, billing_source=None, local_vars_configuration=None):  # noqa: E501
        """SourceIn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authentication = None
        self._billing_source = None
        self.discriminator = None

        self.authentication = authentication
        self.billing_source = billing_source

    @property
    def authentication(self):
        """Gets the authentication of this SourceIn.  # noqa: E501

        Dictionary containing resource name.  # noqa: E501

        :return: The authentication of this SourceIn.  # noqa: E501
        :rtype: object
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this SourceIn.

        Dictionary containing resource name.  # noqa: E501

        :param authentication: The authentication of this SourceIn.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and authentication is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication`, must not be `None`")  # noqa: E501

        self._authentication = authentication

    @property
    def billing_source(self):
        """Gets the billing_source of this SourceIn.  # noqa: E501

        Dictionary containing billing source.  # noqa: E501

        :return: The billing_source of this SourceIn.  # noqa: E501
        :rtype: object
        """
        return self._billing_source

    @billing_source.setter
    def billing_source(self, billing_source):
        """Sets the billing_source of this SourceIn.

        Dictionary containing billing source.  # noqa: E501

        :param billing_source: The billing_source of this SourceIn.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and billing_source is None:  # noqa: E501
            raise ValueError("Invalid value for `billing_source`, must not be `None`")  # noqa: E501

        self._billing_source = billing_source

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
        if not isinstance(other, SourceIn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceIn):
            return True

        return self.to_dict() != other.to_dict()
