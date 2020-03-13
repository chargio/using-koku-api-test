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
from openapi_client.models.report import Report  # noqa: E501
from openapi_client.rest import ApiException

class TestReport(unittest.TestCase):
    """Report unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Report
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.report.Report()  # noqa: E501
        if include_optional :
            return Report(
                meta = openapi_client.models.report_pagination_meta.ReportPaginationMeta(
                    count = 30, 
                    delta = {"delta":"cost"}, 
                    group_by = null, 
                    order_by = null, 
                    filter = null, 
                    units = '0', ), 
                links = openapi_client.models.pagination_links.PaginationLinks(
                    first = '/cost-management/v1/(resources)/?offset=0', 
                    previous = '/cost-management/v1/(resources)/?offset=20', 
                    next = '/cost-management/v1/(resources)/?offset=40', 
                    last = '/cost-management/v1/(resources)/?offset=100', )
            )
        else :
            return Report(
        )

    def testReport(self):
        """Test Report"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
