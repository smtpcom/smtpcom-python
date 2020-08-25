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
from smtp.models.update_account_response import UpdateAccountResponse  # noqa: E501
from smtp.rest import ApiException

class TestUpdateAccountResponse(unittest.TestCase):
    """UpdateAccountResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateAccountResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtp.models.update_account_response.UpdateAccountResponse()  # noqa: E501
        if include_optional :
            return UpdateAccountResponse(
                status = '0', 
                data = smtp.models.update_account_response_data.UpdateAccountResponse_data(
                    account = '0', )
            )
        else :
            return UpdateAccountResponse(
        )

    def testUpdateAccountResponse(self):
        """Test UpdateAccountResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()