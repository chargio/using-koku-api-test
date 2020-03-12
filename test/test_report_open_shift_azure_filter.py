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
from openapi_client.models.report_open_shift_azure_filter import ReportOpenShiftAzureFilter  # noqa: E501
from openapi_client.rest import ApiException

class TestReportOpenShiftAzureFilter(unittest.TestCase):
    """ReportOpenShiftAzureFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReportOpenShiftAzureFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.report_open_shift_azure_filter.ReportOpenShiftAzureFilter()  # noqa: E501
        if include_optional :
            return ReportOpenShiftAzureFilter(
                limit = 5, 
                offset = 5, 
                resolution = 'daily', 
                time_scope_value = -10, 
                time_scope_units = 'day', 
                resource_scope = [], 
                subscription_guid = [
                    '0'
                    ], 
                service_name = [
                    '0'
                    ], 
                resource_location = [
                    '0'
                    ], 
                instance_type = [
                    '0'
                    ], 
                tag = [
                    '0'
                    ], 
                project = [
                    '0'
                    ], 
                cluster = [
                    '0'
                    ], 
                node = [
                    '0'
                    ]
            )
        else :
            return ReportOpenShiftAzureFilter(
        )

    def testReportOpenShiftAzureFilter(self):
        """Test ReportOpenShiftAzureFilter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
