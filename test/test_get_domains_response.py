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

import smtpcom
from smtpcom.models.get_domains_response import GetDomainsResponse  # noqa: E501
from smtpcom.rest import ApiException

class TestGetDomainsResponse(unittest.TestCase):
    """GetDomainsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetDomainsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtpcom.models.get_domains_response.GetDomainsResponse()  # noqa: E501
        if include_optional :
            return GetDomainsResponse(
                status = '0', 
                data = smtpcom.models.get_domains_response_data.GetDomainsResponseData(
                    items = [
                        smtpcom.models.get_domains_response_data_items.GetDomainsResponseDataItems(
                            domain_name = '0', 
                            enabled = True, )
                        ], )
            )
        else :
            return GetDomainsResponse(
        )

    def testGetDomainsResponse(self):
        """Test GetDomainsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
