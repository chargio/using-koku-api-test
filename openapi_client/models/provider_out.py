# coding: utf-8

"""
    Cost Management

    The API for Cost Management.  You can find out more about     Cost Management at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ProviderOut(object):
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
        'type': 'str',
        'uuid': 'str',
        'authentication': 'ProviderAuthenticationOut',
        'billing_source': 'ProviderBillingSourceOut',
        'customer': 'CustomerOut',
        'created_by': 'UserOut',
        'stats': 'object',
        'infrastructure': 'str',
        'active': 'bool',
        'cost_models': 'list[ProviderOutAllOfCostModels]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'uuid': 'uuid',
        'authentication': 'authentication',
        'billing_source': 'billing_source',
        'customer': 'customer',
        'created_by': 'created_by',
        'stats': 'stats',
        'infrastructure': 'infrastructure',
        'active': 'active',
        'cost_models': 'cost_models'
    }

    def __init__(self, name=None, type=None, uuid=None, authentication=None, billing_source=None, customer=None, created_by=None, stats=None, infrastructure=None, active=None, cost_models=None, local_vars_configuration=None):  # noqa: E501
        """ProviderOut - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._uuid = None
        self._authentication = None
        self._billing_source = None
        self._customer = None
        self._created_by = None
        self._stats = None
        self._infrastructure = None
        self._active = None
        self._cost_models = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.uuid = uuid
        self.authentication = authentication
        self.billing_source = billing_source
        self.customer = customer
        self.created_by = created_by
        if stats is not None:
            self.stats = stats
        if infrastructure is not None:
            self.infrastructure = infrastructure
        if active is not None:
            self.active = active
        if cost_models is not None:
            self.cost_models = cost_models

    @property
    def name(self):
        """Gets the name of this ProviderOut.  # noqa: E501


        :return: The name of this ProviderOut.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProviderOut.


        :param name: The name of this ProviderOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this ProviderOut.  # noqa: E501


        :return: The type of this ProviderOut.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProviderOut.


        :param type: The type of this ProviderOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def uuid(self):
        """Gets the uuid of this ProviderOut.  # noqa: E501


        :return: The uuid of this ProviderOut.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ProviderOut.


        :param uuid: The uuid of this ProviderOut.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def authentication(self):
        """Gets the authentication of this ProviderOut.  # noqa: E501


        :return: The authentication of this ProviderOut.  # noqa: E501
        :rtype: ProviderAuthenticationOut
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this ProviderOut.


        :param authentication: The authentication of this ProviderOut.  # noqa: E501
        :type: ProviderAuthenticationOut
        """
        if self.local_vars_configuration.client_side_validation and authentication is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication`, must not be `None`")  # noqa: E501

        self._authentication = authentication

    @property
    def billing_source(self):
        """Gets the billing_source of this ProviderOut.  # noqa: E501


        :return: The billing_source of this ProviderOut.  # noqa: E501
        :rtype: ProviderBillingSourceOut
        """
        return self._billing_source

    @billing_source.setter
    def billing_source(self, billing_source):
        """Sets the billing_source of this ProviderOut.


        :param billing_source: The billing_source of this ProviderOut.  # noqa: E501
        :type: ProviderBillingSourceOut
        """
        if self.local_vars_configuration.client_side_validation and billing_source is None:  # noqa: E501
            raise ValueError("Invalid value for `billing_source`, must not be `None`")  # noqa: E501

        self._billing_source = billing_source

    @property
    def customer(self):
        """Gets the customer of this ProviderOut.  # noqa: E501


        :return: The customer of this ProviderOut.  # noqa: E501
        :rtype: CustomerOut
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ProviderOut.


        :param customer: The customer of this ProviderOut.  # noqa: E501
        :type: CustomerOut
        """
        if self.local_vars_configuration.client_side_validation and customer is None:  # noqa: E501
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def created_by(self):
        """Gets the created_by of this ProviderOut.  # noqa: E501


        :return: The created_by of this ProviderOut.  # noqa: E501
        :rtype: UserOut
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ProviderOut.


        :param created_by: The created_by of this ProviderOut.  # noqa: E501
        :type: UserOut
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def stats(self):
        """Gets the stats of this ProviderOut.  # noqa: E501

        Dictionary key is the start of a billing month.  Value is report processing statistics.  # noqa: E501

        :return: The stats of this ProviderOut.  # noqa: E501
        :rtype: object
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this ProviderOut.

        Dictionary key is the start of a billing month.  Value is report processing statistics.  # noqa: E501

        :param stats: The stats of this ProviderOut.  # noqa: E501
        :type: object
        """

        self._stats = stats

    @property
    def infrastructure(self):
        """Gets the infrastructure of this ProviderOut.  # noqa: E501

        OpenShift foundational infrastructure type.  # noqa: E501

        :return: The infrastructure of this ProviderOut.  # noqa: E501
        :rtype: str
        """
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, infrastructure):
        """Sets the infrastructure of this ProviderOut.

        OpenShift foundational infrastructure type.  # noqa: E501

        :param infrastructure: The infrastructure of this ProviderOut.  # noqa: E501
        :type: str
        """

        self._infrastructure = infrastructure

    @property
    def active(self):
        """Gets the active of this ProviderOut.  # noqa: E501

        Flag to indicate when the provider is configured correctly  # noqa: E501

        :return: The active of this ProviderOut.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ProviderOut.

        Flag to indicate when the provider is configured correctly  # noqa: E501

        :param active: The active of this ProviderOut.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def cost_models(self):
        """Gets the cost_models of this ProviderOut.  # noqa: E501

        List of cost model name and UUIDs associated with this provider.  # noqa: E501

        :return: The cost_models of this ProviderOut.  # noqa: E501
        :rtype: list[ProviderOutAllOfCostModels]
        """
        return self._cost_models

    @cost_models.setter
    def cost_models(self, cost_models):
        """Sets the cost_models of this ProviderOut.

        List of cost model name and UUIDs associated with this provider.  # noqa: E501

        :param cost_models: The cost_models of this ProviderOut.  # noqa: E501
        :type: list[ProviderOutAllOfCostModels]
        """

        self._cost_models = cost_models

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
        if not isinstance(other, ProviderOut):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProviderOut):
            return True

        return self.to_dict() != other.to_dict()
