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
from smtp.models.v4_messages_originator import V4MessagesOriginator  # noqa: E501
from smtp.rest import ApiException

class TestV4MessagesOriginator(unittest.TestCase):
    """V4MessagesOriginator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V4MessagesOriginator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtp.models.v4_messages_originator.V4MessagesOriginator()  # noqa: E501
        if include_optional :
            return V4MessagesOriginator(
                _from = smtp.models.V4MessagesRecipientsTo(
                    name = '0', 
                    address = '0', ), 
                reply_to = smtp.models.V4MessagesRecipientsTo(
                    name = '0', 
                    address = '0', )
            )
        else :
            return V4MessagesOriginator(
        )

    def testV4MessagesOriginator(self):
        """Test V4MessagesOriginator"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
