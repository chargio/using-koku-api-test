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


class ReportInventoryOpenShiftOrdering(object):
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
        'cluster': 'str',
        'project': 'str',
        'node': 'str',
        'usage': 'str',
        'request': 'str',
        'infrastructure': 'str',
        'supplementary': 'str',
        'cost': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'cluster': 'cluster',
        'project': 'project',
        'node': 'node',
        'usage': 'usage',
        'request': 'request',
        'infrastructure': 'infrastructure',
        'supplementary': 'supplementary',
        'cost': 'cost',
        'limit': 'limit'
    }

    def __init__(self, cluster=None, project=None, node=None, usage=None, request=None, infrastructure=None, supplementary=None, cost=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """ReportInventoryOpenShiftOrdering - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster = None
        self._project = None
        self._node = None
        self._usage = None
        self._request = None
        self._infrastructure = None
        self._supplementary = None
        self._cost = None
        self._limit = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if project is not None:
            self.project = project
        if node is not None:
            self.node = node
        if usage is not None:
            self.usage = usage
        if request is not None:
            self.request = request
        if infrastructure is not None:
            self.infrastructure = infrastructure
        if supplementary is not None:
            self.supplementary = supplementary
        if cost is not None:
            self.cost = cost
        if limit is not None:
            self.limit = limit

    @property
    def cluster(self):
        """Gets the cluster of this ReportInventoryOpenShiftOrdering.  # noqa: E501


        :return: The cluster of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ReportInventoryOpenShiftOrdering.


        :param cluster: The cluster of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cluster not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cluster` ({0}), must be one of {1}"  # noqa: E501
                .format(cluster, allowed_values)
            )

        self._cluster = cluster

    @property
    def project(self):
        """Gets the project of this ReportInventoryOpenShiftOrdering.  # noqa: E501


        :return: The project of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ReportInventoryOpenShiftOrdering.


        :param project: The project of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and project not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `project` ({0}), must be one of {1}"  # noqa: E501
                .format(project, allowed_values)
            )

        self._project = project

    @property
    def node(self):
        """Gets the node of this ReportInventoryOpenShiftOrdering.  # noqa: E501


        :return: The node of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this ReportInventoryOpenShiftOrdering.


        :param node: The node of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and node not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `node` ({0}), must be one of {1}"  # noqa: E501
                .format(node, allowed_values)
            )

        self._node = node

    @property
    def usage(self):
        """Gets the usage of this ReportInventoryOpenShiftOrdering.  # noqa: E501


        :return: The usage of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ReportInventoryOpenShiftOrdering.


        :param usage: The usage of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and usage not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `usage` ({0}), must be one of {1}"  # noqa: E501
                .format(usage, allowed_values)
            )

        self._usage = usage

    @property
    def request(self):
        """Gets the request of this ReportInventoryOpenShiftOrdering.  # noqa: E501


        :return: The request of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this ReportInventoryOpenShiftOrdering.


        :param request: The request of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and request not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `request` ({0}), must be one of {1}"  # noqa: E501
                .format(request, allowed_values)
            )

        self._request = request

    @property
    def infrastructure(self):
        """Gets the infrastructure of this ReportInventoryOpenShiftOrdering.  # noqa: E501


        :return: The infrastructure of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :rtype: str
        """
        return self._infrastructure

    @infrastructure.setter
    def infrastructure(self, infrastructure):
        """Sets the infrastructure of this ReportInventoryOpenShiftOrdering.


        :param infrastructure: The infrastructure of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and infrastructure not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `infrastructure` ({0}), must be one of {1}"  # noqa: E501
                .format(infrastructure, allowed_values)
            )

        self._infrastructure = infrastructure

    @property
    def supplementary(self):
        """Gets the supplementary of this ReportInventoryOpenShiftOrdering.  # noqa: E501


        :return: The supplementary of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :rtype: str
        """
        return self._supplementary

    @supplementary.setter
    def supplementary(self, supplementary):
        """Sets the supplementary of this ReportInventoryOpenShiftOrdering.


        :param supplementary: The supplementary of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and supplementary not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `supplementary` ({0}), must be one of {1}"  # noqa: E501
                .format(supplementary, allowed_values)
            )

        self._supplementary = supplementary

    @property
    def cost(self):
        """Gets the cost of this ReportInventoryOpenShiftOrdering.  # noqa: E501


        :return: The cost of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this ReportInventoryOpenShiftOrdering.


        :param cost: The cost of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cost not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cost` ({0}), must be one of {1}"  # noqa: E501
                .format(cost, allowed_values)
            )

        self._cost = cost

    @property
    def limit(self):
        """Gets the limit of this ReportInventoryOpenShiftOrdering.  # noqa: E501


        :return: The limit of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ReportInventoryOpenShiftOrdering.


        :param limit: The limit of this ReportInventoryOpenShiftOrdering.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and limit not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `limit` ({0}), must be one of {1}"  # noqa: E501
                .format(limit, allowed_values)
            )

        self._limit = limit

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
        if not isinstance(other, ReportInventoryOpenShiftOrdering):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportInventoryOpenShiftOrdering):
            return True

        return self.to_dict() != other.to_dict()
