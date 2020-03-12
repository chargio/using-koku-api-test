# coding: utf-8

"""
    Cost Management

    The API for Cost Management.  You can find out more about     Cost Management at [https://github.com/project-koku/](https://github.com/project-koku/).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.report_open_shift_azure_ordering import ReportOpenShiftAzureOrdering  # noqa: E501
from openapi_client.rest import ApiException

class TestReportOpenShiftAzureOrdering(unittest.TestCase):
    """ReportOpenShiftAzureOrdering unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReportOpenShiftAzureOrdering
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.report_open_shift_azure_ordering.ReportOpenShiftAzureOrdering()  # noqa: E501
        if include_optional :
            return ReportOpenShiftAzureOrdering(
                cost = 'asc', 
                usage = 'asc', 
                delta = 'asc', 
                subscription_guid = 'asc', 
                resource_location = 'asc', 
                service_name = 'asc', 
                instance_type = 'asc', 
                cluster = 'asc', 
                project = 'asc', 
                node = 'asc'
            )
        else :
            return ReportOpenShiftAzureOrdering(
        )

    def testReportOpenShiftAzureOrdering(self):
        """Test ReportOpenShiftAzureOrdering"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
