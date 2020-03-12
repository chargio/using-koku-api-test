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
from openapi_client.models.cost_model_out import CostModelOut  # noqa: E501
from openapi_client.rest import ApiException

class TestCostModelOut(unittest.TestCase):
    """CostModelOut unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CostModelOut
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.cost_model_out.CostModelOut()  # noqa: E501
        if include_optional :
            return CostModelOut(
                name = '0', 
                description = '0', 
                source_type = '0', 
                providers = [
                    openapi_client.models.cost_model_resp_providers.CostModelResp_providers(
                        uuid = 'e5ff62e7-e6d6-5513-5532-45fe72792dae', 
                        name = 'provider', )
                    ], 
                rates = [
                    openapi_client.models.rate.Rate(
                        uuid = '83ee048e-3c1d-43ef-b945-108225ae52f4', 
                        metric = {"name":"cpu_core_per_hour","unit":"core-hours","display_name":"Compute usage Rate"}, 
                        tiered_rates = [{"value":0.22,"unit":"USD","usage":{"usage_start":0,"usage_end":10}}], )
                    ], 
                uuid = '0', 
                created_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                markup = openapi_client.models.markup.Markup(
                    value = 1.337, 
                    unit = 'percent', )
            )
        else :
            return CostModelOut(
                name = '0',
                description = '0',
                source_type = '0',
        )

    def testCostModelOut(self):
        """Test CostModelOut"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
