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
from smtpcom.models.bad_request_schema_data import BadRequestSchemaData  # noqa: E501
from smtpcom.rest import ApiException

class TestBadRequestSchemaData(unittest.TestCase):
    """BadRequestSchemaData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BadRequestSchemaData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = smtpcom.models.bad_request_schema_data.BadRequestSchemaData()  # noqa: E501
        if include_optional :
            return BadRequestSchemaData(
                errors = KeyError()
            )
        else :
            return BadRequestSchemaData(
        )

    def testBadRequestSchemaData(self):
        """Test BadRequestSchemaData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
