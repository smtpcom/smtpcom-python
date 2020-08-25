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
from smtp.models.channels_data import ChannelsData  # noqa: E501
from smtp.rest import ApiException

class TestChannelsData(unittest.TestCase):
    """ChannelsData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ChannelsData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtp.models.channels_data.ChannelsData()  # noqa: E501
        if include_optional :
            return ChannelsData(
                items = [
                    smtp.models.channels_data_items.Channels_data_items(
                        status = '0', 
                        quota = 56, 
                        name = '0', 
                        usage = 56, 
                        date_created = 56, 
                        smtp_username = '0', )
                    ]
            )
        else :
            return ChannelsData(
        )

    def testChannelsData(self):
        """Test ChannelsData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()