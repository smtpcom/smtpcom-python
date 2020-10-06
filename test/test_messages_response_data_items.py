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
from smtpcom.models.messages_response_data_items import MessagesResponseDataItems  # noqa: E501
from smtpcom.rest import ApiException

class TestMessagesResponseDataItems(unittest.TestCase):
    """MessagesResponseDataItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessagesResponseDataItems
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtpcom.models.messages_response_data_items.MessagesResponseDataItems()  # noqa: E501
        if include_optional :
            return MessagesResponseDataItems(
                msg_id = '0', 
                msg_time = 56, 
                channel = '0', 
                msg_data = smtpcom.models.messages_response_data_msg_data.MessagesResponseDataMsgData(
                    rcpt_to = '0', 
                    _from = '0',
                    subject = '0', ), 
                details = smtpcom.models.messages_response_data_details.MessagesResponseDataDetails(
                    delivery = smtpcom.models.messages_response_data_details_delivery.MessagesResponseDataDetailsDelivery(
                        finished = '0', 
                        retries = 56, 
                        event = '0', 
                        code = '0', 
                        status = '0', ), ), 
                opens = smtpcom.models.messages_response_data_opens.MessagesResponseDataOpens(
                    items = [
                        smtpcom.models.messages_response_data_opens_items.MessagesResponseDataOpensItems(
                            open_time = '0', 
                            remote_ip = '0', 
                            ua = '0', )
                        ], ), 
                clicks = smtpcom.models.messages_response_data_clicks.MessagesResponseDataClicks(
                    items = [
                        smtpcom.models.messages_response_data_clicks_items.MessagesResponseDataClicksItems(
                            click_time = '0', 
                            remote_ip = '0', 
                            ua = '0', )
                        ], ), 
                abuse = smtpcom.models.messages_response_data_abuse.MessagesResponseDataAbuse(
                    complaints = [
                        smtpcom.models.messages_response_data_abuse_complaints.MessagesResponseDataAbuseComplaints(
                            report_time = '0', 
                            provider = '0', )
                        ], ), 
                unsubs = smtpcom.models.messages_response_data_unsubs.MessagesResponseDataUnsubs(
                    items = [
                        smtpcom.models.messages_response_data_unsubs_items.MessagesResponseDataUnsubsItems(
                            unsub_time = '0', )
                        ], )
            )
        else :
            return MessagesResponseDataItems(
        )

    def testMessagesResponseDataItems(self):
        """Test MessagesResponseDataItems"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
