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
from openapi_client.models.provider_authentication_out import ProviderAuthenticationOut  # noqa: E501
from openapi_client.rest import ApiException

class TestProviderAuthenticationOut(unittest.TestCase):
    """ProviderAuthenticationOut unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProviderAuthenticationOut
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.provider_authentication_out.ProviderAuthenticationOut()  # noqa: E501
        if include_optional :
            return ProviderAuthenticationOut(
                provider_resource_name = 'arn:aws:iam::PRODUCTION-ACCOUNT-ID:role/CostData', 
                credentials = {"subscription_id":"f695f74f-36a4-4112-9fe6-74415fac75a2","tenant_id":"319d4d72-7ddc-45d0-9d63-a2db0a36e048","client_id":"ce26bd50-2e5a-4eb7-9504-a05a79568e25","client_secret":"abc123"}, 
                uuid = '57e60f90-8c0c-4bd1-87a0-2143759aae1c'
            )
        else :
            return ProviderAuthenticationOut(
                uuid = '57e60f90-8c0c-4bd1-87a0-2143759aae1c',
        )

    def testProviderAuthenticationOut(self):
        """Test ProviderAuthenticationOut"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
