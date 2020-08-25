# coding: utf-8

"""
    SMTP Public API overview

    SMTP.com Public API v4  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Contact: support@smtp.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from smtp.configuration import Configuration


class MessagesResponseDataClicksItems(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'click_time': 'str',
        'remote_ip': 'str',
        'ua': 'str'
    }

    attribute_map = {
        'click_time': 'click_time',
        'remote_ip': 'remote_ip',
        'ua': 'ua'
    }

    def __init__(self, click_time=None, remote_ip=None, ua=None, local_vars_configuration=None):  # noqa: E501
        """MessagesResponseDataClicksItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._click_time = None
        self._remote_ip = None
        self._ua = None
        self.discriminator = None

        if click_time is not None:
            self.click_time = click_time
        if remote_ip is not None:
            self.remote_ip = remote_ip
        if ua is not None:
            self.ua = ua

    @property
    def click_time(self):
        """Gets the click_time of this MessagesResponseDataClicksItems.  # noqa: E501

        Timestamp of when message links were clicked  # noqa: E501

        :return: The click_time of this MessagesResponseDataClicksItems.  # noqa: E501
        :rtype: str
        """
        return self._click_time

    @click_time.setter
    def click_time(self, click_time):
        """Sets the click_time of this MessagesResponseDataClicksItems.

        Timestamp of when message links were clicked  # noqa: E501

        :param click_time: The click_time of this MessagesResponseDataClicksItems.  # noqa: E501
        :type click_time: str
        """

        self._click_time = click_time

    @property
    def remote_ip(self):
        """Gets the remote_ip of this MessagesResponseDataClicksItems.  # noqa: E501

        IP address of where links were clicked  # noqa: E501

        :return: The remote_ip of this MessagesResponseDataClicksItems.  # noqa: E501
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """Sets the remote_ip of this MessagesResponseDataClicksItems.

        IP address of where links were clicked  # noqa: E501

        :param remote_ip: The remote_ip of this MessagesResponseDataClicksItems.  # noqa: E501
        :type remote_ip: str
        """

        self._remote_ip = remote_ip

    @property
    def ua(self):
        """Gets the ua of this MessagesResponseDataClicksItems.  # noqa: E501

        User agent of device on which links were clicked  # noqa: E501

        :return: The ua of this MessagesResponseDataClicksItems.  # noqa: E501
        :rtype: str
        """
        return self._ua

    @ua.setter
    def ua(self, ua):
        """Sets the ua of this MessagesResponseDataClicksItems.

        User agent of device on which links were clicked  # noqa: E501

        :param ua: The ua of this MessagesResponseDataClicksItems.  # noqa: E501
        :type ua: str
        """

        self._ua = ua

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MessagesResponseDataClicksItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessagesResponseDataClicksItems):
            return True

        return self.to_dict() != other.to_dict()
