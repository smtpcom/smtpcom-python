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
from smtp.models.v4_messages_recipients import V4MessagesRecipients  # noqa: E501
from smtp.rest import ApiException

class TestV4MessagesRecipients(unittest.TestCase):
    """V4MessagesRecipients unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V4MessagesRecipients
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtp.models.v4_messages_recipients.V4MessagesRecipients()  # noqa: E501
        if include_optional :
            return V4MessagesRecipients(
                to = [
                    smtp.models.V4MessagesRecipientsTo(
                        name = '0', 
                        address = '0', )
                    ], 
                cc = [
                    smtp.models.V4MessagesRecipientsTo(
                        name = '0', 
                        address = '0', )
                    ], 
                bcc = [
                    smtp.models.V4MessagesRecipientsTo(
                        name = '0', 
                        address = '0', )
                    ], 
                bulk_list = [
                    smtp.models.V4MessagesRecipientsTo(
                        name = '0', 
                        address = '0', )
                    ]
            )
        else :
            return V4MessagesRecipients(
        )

    def testV4MessagesRecipients(self):
        """Test V4MessagesRecipients"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
