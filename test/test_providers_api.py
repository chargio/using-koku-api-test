# coding: utf-8

"""
    Cost Management

    The API for Project Koku and OpenShift cost management. You can find out more about Cost Management at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.providers_api import ProvidersApi  # noqa: E501
from openapi_client.rest import ApiException


class TestProvidersApi(unittest.TestCase):
    """ProvidersApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.providers_api.ProvidersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_provider(self):
        """Test case for create_provider

        Create a provider  # noqa: E501
        """
        pass

    def test_delete_provider(self):
        """Test case for delete_provider

        Delete a provider  # noqa: E501
        """
        pass

    def test_get_provider(self):
        """Test case for get_provider

        Get a provider  # noqa: E501
        """
        pass

    def test_list_providers(self):
        """Test case for list_providers

        List the providers  # noqa: E501
        """
        pass

    def test_update_provider(self):
        """Test case for update_provider

        Update a provider  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
