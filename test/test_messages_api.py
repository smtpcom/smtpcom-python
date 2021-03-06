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

import smtpcom
from smtpcom.api.messages_api import MessagesApi  # noqa: E501
from smtpcom.rest import ApiException


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self):
        self.api = smtpcom.api.messages_api.MessagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v4_messages_get(self):
        """Test case for v4_messages_get

        Get Detailed Messages Info  # noqa: E501
        """
        pass

    def test_v4_messages_mime_post(self):
        """Test case for v4_messages_mime_post

        Send MIME Message  # noqa: E501
        """
        pass

    def test_v4_messages_post(self):
        """Test case for v4_messages_post

        Send a Message  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
