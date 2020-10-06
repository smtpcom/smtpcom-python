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
from smtpcom.models.messages_response_data_msg_data import MessagesResponseDataMsgData  # noqa: E501
from smtpcom.rest import ApiException

class TestMessagesResponseDataMsgData(unittest.TestCase):
    """MessagesResponseDataMsgData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessagesResponseDataMsgData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtpcom.models.messages_response_data_msg_data.MessagesResponseDataMsgData()  # noqa: E501
        if include_optional :
            return MessagesResponseDataMsgData(
                rcpt_to = '0', 
                _from = '0', 
                subject = '0'
            )
        else :
            return MessagesResponseDataMsgData(
        )

    def testMessagesResponseDataMsgData(self):
        """Test MessagesResponseDataMsgData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
