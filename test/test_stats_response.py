# coding: utf-8

"""
    SMTP Public API overview

    SMTP.com Public API v4  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@smtp.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import smtp
from smtp.models.stats_response import StatsResponse  # noqa: E501
from smtp.rest import ApiException

class TestStatsResponse(unittest.TestCase):
    """StatsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StatsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtp.models.stats_response.StatsResponse()  # noqa: E501
        if include_optional :
            return StatsResponse(
                status = '0', 
                data = smtp.models.stats_response_data.StatsResponseData(
                    items = [
                        smtp.models.stats_response_data_items.StatsResponseDataItems(
                            accepted = 56, 
                            complained = 56, 
                            delivered = 56, 
                            clicked = 56, 
                            opened = 56, 
                            failed = 56, 
                            unsubscribed = 56, 
                            queued = 56, )
                        ], )
            )
        else :
            return StatsResponse(
        )

    def testStatsResponse(self):
        """Test StatsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
