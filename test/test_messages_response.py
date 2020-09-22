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
from smtp.models.messages_response import MessagesResponse  # noqa: E501
from smtp.rest import ApiException

class TestMessagesResponse(unittest.TestCase):
    """MessagesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessagesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtp.models.messages_response.MessagesResponse()  # noqa: E501
        if include_optional :
            return MessagesResponse(
                status = '0', 
                data = smtp.models.messages_response_data.MessagesResponse_data(
                    items = [
                        smtp.models.messages_response_data_items.MessagesResponse_data_items(
                            msg_id = '0', 
                            msg_time = 56, 
                            channel = '0', 
                            smtp_vars = smtp.models.smtp_vars.smtp_vars(), 
                            msg_data = smtp.models.messages_response_data_msg_data.MessagesResponse_data_msg_data(
                                rcpt_to = '0', 
                                _from = '0',
                                subject = '0', ), 
                            details = smtp.models.messages_response_data_details.MessagesResponse_data_details(
                                delivery = smtp.models.messages_response_data_details_delivery.MessagesResponse_data_details_delivery(
                                    finished = '0', 
                                    retries = 56, 
                                    event = '0', 
                                    code = '0', 
                                    status = '0', ), ), 
                            opens = smtp.models.messages_response_data_opens.MessagesResponse_data_opens(), 
                            clicks = smtp.models.messages_response_data_clicks.MessagesResponse_data_clicks(), 
                            abuse = smtp.models.messages_response_data_abuse.MessagesResponse_data_abuse(
                                complaints = [
                                    smtp.models.messages_response_data_abuse_complaints.MessagesResponse_data_abuse_complaints(
                                        report_time = '0', 
                                        provider = '0', )
                                    ], ), 
                            unsubs = smtp.models.messages_response_data_unsubs.MessagesResponse_data_unsubs(), )
                        ], )
            )
        else :
            return MessagesResponse(
        )

    def testMessagesResponse(self):
        """Test MessagesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
