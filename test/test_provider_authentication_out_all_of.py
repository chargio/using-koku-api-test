# coding: utf-8

"""
    Cost Management

    The API for Project Koku and OpenShift cost management. You can find out more about Cost Management at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.provider_authentication_out_all_of import ProviderAuthenticationOutAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestProviderAuthenticationOutAllOf(unittest.TestCase):
    """ProviderAuthenticationOutAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProviderAuthenticationOutAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.provider_authentication_out_all_of.ProviderAuthenticationOutAllOf()  # noqa: E501
        if include_optional :
            return ProviderAuthenticationOutAllOf(
                uuid = '57e60f90-8c0c-4bd1-87a0-2143759aae1c'
            )
        else :
            return ProviderAuthenticationOutAllOf(
                uuid = '57e60f90-8c0c-4bd1-87a0-2143759aae1c',
        )

    def testProviderAuthenticationOutAllOf(self):
        """Test ProviderAuthenticationOutAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
