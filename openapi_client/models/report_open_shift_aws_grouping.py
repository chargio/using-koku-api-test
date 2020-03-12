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


class ReportOpenShiftAWSGrouping(object):
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
        'account': 'list[str]',
        'service': 'list[str]',
        'region': 'list[str]',
        'az': 'list[str]',
        'instance_type': 'list[str]',
        'storage_type': 'list[str]',
        'tag': 'list[str]',
        'cluster': 'list[str]',
        'project': 'list[str]',
        'node': 'list[str]'
    }

    attribute_map = {
        'account': 'account',
        'service': 'service',
        'region': 'region',
        'az': 'az',
        'instance_type': 'instance_type',
        'storage_type': 'storage_type',
        'tag': 'tag',
        'cluster': 'cluster',
        'project': 'project',
        'node': 'node'
    }

    def __init__(self, account=None, service=None, region=None, az=None, instance_type=None, storage_type=None, tag=None, cluster=None, project=None, node=None, local_vars_configuration=None):  # noqa: E501
        """ReportOpenShiftAWSGrouping - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account = None
        self._service = None
        self._region = None
        self._az = None
        self._instance_type = None
        self._storage_type = None
        self._tag = None
        self._cluster = None
        self._project = None
        self._node = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if service is not None:
            self.service = service
        if region is not None:
            self.region = region
        if az is not None:
            self.az = az
        if instance_type is not None:
            self.instance_type = instance_type
        if storage_type is not None:
            self.storage_type = storage_type
        if tag is not None:
            self.tag = tag
        if cluster is not None:
            self.cluster = cluster
        if project is not None:
            self.project = project
        if node is not None:
            self.node = node

    @property
    def account(self):
        """Gets the account of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The account of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ReportOpenShiftAWSGrouping.


        :param account: The account of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :type: list[str]
        """

        self._account = account

    @property
    def service(self):
        """Gets the service of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The service of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ReportOpenShiftAWSGrouping.


        :param service: The service of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :type: list[str]
        """

        self._service = service

    @property
    def region(self):
        """Gets the region of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The region of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ReportOpenShiftAWSGrouping.


        :param region: The region of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :type: list[str]
        """

        self._region = region

    @property
    def az(self):
        """Gets the az of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The az of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this ReportOpenShiftAWSGrouping.


        :param az: The az of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :type: list[str]
        """

        self._az = az

    @property
    def instance_type(self):
        """Gets the instance_type of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The instance_type of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ReportOpenShiftAWSGrouping.


        :param instance_type: The instance_type of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :type: list[str]
        """

        self._instance_type = instance_type

    @property
    def storage_type(self):
        """Gets the storage_type of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The storage_type of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this ReportOpenShiftAWSGrouping.


        :param storage_type: The storage_type of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :type: list[str]
        """

        self._storage_type = storage_type

    @property
    def tag(self):
        """Gets the tag of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The tag of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ReportOpenShiftAWSGrouping.


        :param tag: The tag of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :type: list[str]
        """

        self._tag = tag

    @property
    def cluster(self):
        """Gets the cluster of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The cluster of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ReportOpenShiftAWSGrouping.


        :param cluster: The cluster of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :type: list[str]
        """

        self._cluster = cluster

    @property
    def project(self):
        """Gets the project of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The project of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ReportOpenShiftAWSGrouping.


        :param project: The project of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :type: list[str]
        """

        self._project = project

    @property
    def node(self):
        """Gets the node of this ReportOpenShiftAWSGrouping.  # noqa: E501


        :return: The node of this ReportOpenShiftAWSGrouping.  # noqa: E501
        :rtype: list[str]
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this ReportOpenShiftAWSGrouping.


        :param node: The node of this ReportOpenShiftAWSGrouping.  # noqa: E501
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
        if not isinstance(other, ReportOpenShiftAWSGrouping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportOpenShiftAWSGrouping):
            return True

        return self.to_dict() != other.to_dict()
