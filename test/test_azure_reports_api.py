# coding: utf-8

"""
    Cost Management

    The API for Cost Management.  You can find out more about     Cost Management at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.azure_reports_api import AzureReportsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestAzureReportsApi(unittest.TestCase):
    """AzureReportsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.azure_reports_api.AzureReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_azure_cost_reports(self):
        """Test case for get_azure_cost_reports

        Query to obtain cost reports  # noqa: E501
        """
        pass

    def test_get_azure_instance_reports(self):
        """Test case for get_azure_instance_reports

        Query to obtain Azure instance type data  # noqa: E501
        """
        pass

    def test_get_azure_storage_reports(self):
        """Test case for get_azure_storage_reports

        Query to obtain AWS storage data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
