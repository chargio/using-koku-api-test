# coding: utf-8

"""
    Cost Management

    The API for Project Koku and OpenShift cost management. You can find out more about Cost Management at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ReportOpenShiftAzureFilter(object):
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
        'subscription_guid': 'list[str]',
        'service_name': 'list[str]',
        'resource_location': 'list[str]',
        'instance_type': 'list[str]',
        'tag': 'list[str]',
        'project': 'list[str]',
        'cluster': 'list[str]',
        'node': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'resolution': 'resolution',
        'time_scope_value': 'time_scope_value',
        'time_scope_units': 'time_scope_units',
        'resource_scope': 'resource_scope',
        'subscription_guid': 'subscription_guid',
        'service_name': 'service_name',
        'resource_location': 'resource_location',
        'instance_type': 'instance_type',
        'tag': 'tag',
        'project': 'project',
        'cluster': 'cluster',
        'node': 'node'
    }

    def __init__(self, limit=None, offset=None, resolution=None, time_scope_value=None, time_scope_units=None, resource_scope=None, subscription_guid=None, service_name=None, resource_location=None, instance_type=None, tag=None, project=None, cluster=None, node=None, local_vars_configuration=None):  # noqa: E501
        """ReportOpenShiftAzureFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._limit = None
        self._offset = None
        self._resolution = None
        self._time_scope_value = None
        self._time_scope_units = None
        self._resource_scope = None
        self._subscription_guid = None
        self._service_name = None
        self._resource_location = None
        self._instance_type = None
        self._tag = None
        self._project = None
        self._cluster = None
        self._node = None
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
        if project is not None:
            self.project = project
        if cluster is not None:
            self.cluster = cluster
        if node is not None:
            self.node = node

    @property
    def limit(self):
        """Gets the limit of this ReportOpenShiftAzureFilter.  # noqa: E501

        Limits the data points returns and aggregates remaining data.  # noqa: E501

        :return: The limit of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ReportOpenShiftAzureFilter.

        Limits the data points returns and aggregates remaining data.  # noqa: E501

        :param limit: The limit of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ReportOpenShiftAzureFilter.  # noqa: E501

        Offsets the data points returned when using limit.  # noqa: E501

        :return: The offset of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ReportOpenShiftAzureFilter.

        Offsets the data points returned when using limit.  # noqa: E501

        :param offset: The offset of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def resolution(self):
        """Gets the resolution of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The resolution of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: ReportResolution
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this ReportOpenShiftAzureFilter.


        :param resolution: The resolution of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: ReportResolution
        """

        self._resolution = resolution

    @property
    def time_scope_value(self):
        """Gets the time_scope_value of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The time_scope_value of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: ReportTimeScopeValue
        """
        return self._time_scope_value

    @time_scope_value.setter
    def time_scope_value(self, time_scope_value):
        """Sets the time_scope_value of this ReportOpenShiftAzureFilter.


        :param time_scope_value: The time_scope_value of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: ReportTimeScopeValue
        """

        self._time_scope_value = time_scope_value

    @property
    def time_scope_units(self):
        """Gets the time_scope_units of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The time_scope_units of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: ReportTimeScopeUnits
        """
        return self._time_scope_units

    @time_scope_units.setter
    def time_scope_units(self, time_scope_units):
        """Sets the time_scope_units of this ReportOpenShiftAzureFilter.


        :param time_scope_units: The time_scope_units of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: ReportTimeScopeUnits
        """

        self._time_scope_units = time_scope_units

    @property
    def resource_scope(self):
        """Gets the resource_scope of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The resource_scope of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: list[ReportResourceScope]
        """
        return self._resource_scope

    @resource_scope.setter
    def resource_scope(self, resource_scope):
        """Sets the resource_scope of this ReportOpenShiftAzureFilter.


        :param resource_scope: The resource_scope of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: list[ReportResourceScope]
        """

        self._resource_scope = resource_scope

    @property
    def subscription_guid(self):
        """Gets the subscription_guid of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The subscription_guid of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._subscription_guid

    @subscription_guid.setter
    def subscription_guid(self, subscription_guid):
        """Sets the subscription_guid of this ReportOpenShiftAzureFilter.


        :param subscription_guid: The subscription_guid of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: list[str]
        """

        self._subscription_guid = subscription_guid

    @property
    def service_name(self):
        """Gets the service_name of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The service_name of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this ReportOpenShiftAzureFilter.


        :param service_name: The service_name of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: list[str]
        """

        self._service_name = service_name

    @property
    def resource_location(self):
        """Gets the resource_location of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The resource_location of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_location

    @resource_location.setter
    def resource_location(self, resource_location):
        """Sets the resource_location of this ReportOpenShiftAzureFilter.


        :param resource_location: The resource_location of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: list[str]
        """

        self._resource_location = resource_location

    @property
    def instance_type(self):
        """Gets the instance_type of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The instance_type of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ReportOpenShiftAzureFilter.


        :param instance_type: The instance_type of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: list[str]
        """

        self._instance_type = instance_type

    @property
    def tag(self):
        """Gets the tag of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The tag of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ReportOpenShiftAzureFilter.


        :param tag: The tag of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: list[str]
        """

        self._tag = tag

    @property
    def project(self):
        """Gets the project of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The project of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ReportOpenShiftAzureFilter.


        :param project: The project of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: list[str]
        """

        self._project = project

    @property
    def cluster(self):
        """Gets the cluster of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The cluster of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ReportOpenShiftAzureFilter.


        :param cluster: The cluster of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: list[str]
        """

        self._cluster = cluster

    @property
    def node(self):
        """Gets the node of this ReportOpenShiftAzureFilter.  # noqa: E501


        :return: The node of this ReportOpenShiftAzureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this ReportOpenShiftAzureFilter.


        :param node: The node of this ReportOpenShiftAzureFilter.  # noqa: E501
        :type: list[str]
        """

        self._node = node

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
        if not isinstance(other, ReportOpenShiftAzureFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportOpenShiftAzureFilter):
            return True

        return self.to_dict() != other.to_dict()
