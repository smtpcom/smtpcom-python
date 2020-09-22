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
from smtp.models.account_data import AccountData  # noqa: E501
from smtp.rest import ApiException

class TestAccountData(unittest.TestCase):
    """AccountData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtp.models.account_data.AccountData()  # noqa: E501
        if include_optional :
            return AccountData(
                status = '0', 
                first_name = '0', 
                last_name = '0', 
                phone = '0', 
                website = '0', 
                email = '0', 
                company_name = '0', 
                address = smtp.models.account_data_address.AccountDataAddress(
                    street = '0', 
                    city = '0', 
                    state = '0', 
                    country = '0', ), 
                usage = 56, 
                date_created = 56
            )
        else :
            return AccountData(
        )

    def testAccountData(self):
        """Test AccountData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
