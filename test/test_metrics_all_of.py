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
from openapi_client.models.metrics_all_of import MetricsAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestMetricsAllOf(unittest.TestCase):
    """MetricsAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetricsAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.metrics_all_of.MetricsAllOf()  # noqa: E501
        if include_optional :
            return MetricsAllOf(
                data = [
                    openapi_client.models.metrics_out.MetricsOut(
                        source_type = '0', 
                        metric = '0', 
                        label_metric = '0', 
                        label_measurement = '0', 
                        label_measurement_unit = '0', )
                    ]
            )
        else :
            return MetricsAllOf(
                data = [
                    openapi_client.models.metrics_out.MetricsOut(
                        source_type = '0', 
                        metric = '0', 
                        label_metric = '0', 
                        label_measurement = '0', 
                        label_measurement_unit = '0', )
                    ],
        )

    def testMetricsAllOf(self):
        """Test MetricsAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
