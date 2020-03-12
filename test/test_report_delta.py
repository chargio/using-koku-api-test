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
from openapi_client.models.report_delta import ReportDelta  # noqa: E501
from openapi_client.rest import ApiException

class TestReportDelta(unittest.TestCase):
    """ReportDelta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReportDelta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.report_delta.ReportDelta()  # noqa: E501
        if include_optional :
            return ReportDelta(
                delta = '0'
            )
        else :
            return ReportDelta(
        )

    def testReportDelta(self):
        """Test ReportDelta"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
