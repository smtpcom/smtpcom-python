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

import smtp
from smtp.api.reports_api import ReportsApi  # noqa: E501
from smtp.rest import ApiException


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self):
        self.api = smtp.api.reports_api.ReportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v4_reports_get(self):
        """Test case for v4_reports_get

        Get All Reports  # noqa: E501
        """
        pass

    def test_v4_reports_ondemand_post(self):
        """Test case for v4_reports_ondemand_post

        Create On-Demand Report  # noqa: E501
        """
        pass

    def test_v4_reports_periodic_post(self):
        """Test case for v4_reports_periodic_post

        Create Periodic Report  # noqa: E501
        """
        pass

    def test_v4_reports_periodic_report_id_delete(self):
        """Test case for v4_reports_periodic_report_id_delete

        Delete a Periodic Report  # noqa: E501
        """
        pass

    def test_v4_reports_periodic_report_id_patch(self):
        """Test case for v4_reports_periodic_report_id_patch

        Update Periodic Report  # noqa: E501
        """
        pass

    def test_v4_reports_report_id_get(self):
        """Test case for v4_reports_report_id_get

        Get Report Details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
