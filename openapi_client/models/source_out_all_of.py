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


class SourceOutAllOf(object):
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
        'id': 'int',
        'uuid': 'str',
        'name': 'str',
        'source_type': 'str',
        'authentication': 'object',
        'billing_source': 'object',
        'provider_linked': 'bool',
        'infrastructure': 'str',
        'cost_models': 'list[ProviderOutAllOfCostModels]'
    }

    attribute_map = {
        'id': 'id',
        'uuid': 'uuid',
        'name': 'name',
        'source_type': 'source_type',
        'authentication': 'authentication',
        'billing_source': 'billing_source',
        'provider_linked': 'provider_linked',
        'infrastructure': 'infrastructure',
        'cost_models': 'cost_models'
    }

    def __init__(self, id=None, uuid=None, name=None, source_type=None, authentication=None, billing_source=None, provider_linked=False, infrastructure=None, cost_models=None, local_vars_configuration=None):  # noqa: E501
        """SourceOutAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._uuid = None
        self._name = None
        self._source_type = None
        self._authentication = None
        self._billing_source = None
        self._provider_linked = None
        self._infrastructure = None
        self._cost_models = None
        self.discriminator = None

        self.id = id
        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if source_type is not None:
            self.source_type = source_type
        if authentication is not None:
            self.authentication = authentication
        if billing_source is not None:
            self.billing_source = billing_source
        if provider_linked is not None:
            self.provider_linked = provider_linked
        if infrastructure is not None:
            self.infrastructure = infrastructure
        if cost_models is not None:
            self.cost_models = cost_models

    @property
    def id(self):
        """Gets the id of this SourceOutAllOf.  # noqa: E501


        :return: The id of this SourceOutAllOf.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceOutAllOf.


        :param id: The id of this SourceOutAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this SourceOutAllOf.  # noqa: E501


        :return: The uuid of this SourceOutAllOf.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this SourceOutAllOf.


        :param uuid: The uuid of this SourceOutAllOf.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this SourceOutAllOf.  # noqa: E501


        :return: The name of this SourceOutAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceOutAllOf.


        :param name: The name of this SourceOutAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_type(self):
        """Gets the source_type of this SourceOutAllOf.  # noqa: E501


        :return: The source_type of this SourceOutAllOf.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this SourceOutAllOf.


        :param source_type: The source_type of this SourceOutAllOf.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def authentication(self):
        """Gets the authentication of this SourceOutAllOf.  # noqa: E501

        Dictionary containing resource name.  # noqa: E501

        :return: The authentication of this SourceOutAllOf.  # noqa: E501
        :rtype: object
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this SourceOutAllOf.

        Dictionary containing resource name.  # noqa: E501

        :param authentication: The authentication of this SourceOutAllOf.  # noqa: E501
        :type: object
        """

        self._authentication = authentication

    @property
    def billing_source(self):
        """Gets the billing_source of this SourceOutAllOf.  # noqa: E501

        Dictionary containing billing source.  # noqa: E501

        :return: The billing_source of this SourceOutAllOf.  # noqa: E501
        :rtype: object
        """
        return self._billing_source

    @billing_source.setter
    def billing_source(self, billing_source):
        """Sets the billing_source of this SourceOutAllOf.

        Dictionary containing billing source.  # noqa: E501

        :param billing_source: The billing_source of this SourceOutAllOf.  # noqa: E501
        :type: object
        """

        self._billing_source = billing_source

    @property
    def provider_linked(self):
        """Gets the provider_linked of this SourceOutAllOf.  # noqa: E501

        Flag to indicate if provider is linked to source.  # noqa: E501

        :return: The provider_linked of this SourceOutAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._provider_linked

    @provider_linked.setter
    def provider_linked(self, provider_linked):
        """Sets the provider_linked of this SourceOutAllOf.

        Flag to indicate if provider is linked to source.  # noqa: E501

        :param provider_linked: The provider_linked of this SourceOutAllOf.  # noqa: E501
        :type: bool
        """

        self._provider_linked = provider_linked

    @property
    def infrastructure(self):
        """Gets the infrastructure of this SourceOutAllOf.  # noqa: E501

        OpenShift foundational infrastructure type.  # noqa: E501

        :return: The infrastructure of this SourceOutAllOf.  # noqa: E501
        :rtype: str
        """
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, infrastructure):
        """Sets the infrastructure of this SourceOutAllOf.

        OpenShift foundational infrastructure type.  # noqa: E501

        :param infrastructure: The infrastructure of this SourceOutAllOf.  # noqa: E501
        :type: str
        """

        self._infrastructure = infrastructure

    @property
    def cost_models(self):
        """Gets the cost_models of this SourceOutAllOf.  # noqa: E501

        List of cost model name and UUIDs associated with this provider.  # noqa: E501

        :return: The cost_models of this SourceOutAllOf.  # noqa: E501
        :rtype: list[ProviderOutAllOfCostModels]
        """
        return self._cost_models

    @cost_models.setter
    def cost_models(self, cost_models):
        """Sets the cost_models of this SourceOutAllOf.

        List of cost model name and UUIDs associated with this provider.  # noqa: E501

        :param cost_models: The cost_models of this SourceOutAllOf.  # noqa: E501
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
        if not isinstance(other, SourceOutAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceOutAllOf):
            return True

        return self.to_dict() != other.to_dict()
