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

from smtpcom.configuration import Configuration


class InlineObject1(object):
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
        'mime': 'str',
        'channel': 'str',
        'recipients': 'V4MessagesMimeRecipients',
        'originator': 'V4MessagesOriginator'
    }

    attribute_map = {
        'mime': 'mime',
        'channel': 'channel',
        'recipients': 'recipients',
        'originator': 'originator'
    }

    def __init__(self, mime=None, channel=None, recipients=None, originator=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mime = None
        self._channel = None
        self._recipients = None
        self._originator = None
        self.discriminator = None

        if mime is not None:
            self.mime = mime
        if channel is not None:
            self.channel = channel
        if recipients is not None:
            self.recipients = recipients
        if originator is not None:
            self.originator = originator

    @property
    def mime(self):
        """Gets the mime of this InlineObject1.  # noqa: E501

        A completely prepared full MIME container of the email, compliant with RFC 2045, RFC 2046, RFC 2047, RFC 4288, RFC 4289 and RFC 2049. No validation will be performed during API submission and it will be attempted to be delivered as is. Any errors while processing and delivering this email will be available only via callbacks.    # noqa: E501

        :return: The mime of this InlineObject1.  # noqa: E501
        :rtype: str
        """
        return self._mime

    @mime.setter
    def mime(self, mime):
        """Sets the mime of this InlineObject1.

        A completely prepared full MIME container of the email, compliant with RFC 2045, RFC 2046, RFC 2047, RFC 4288, RFC 4289 and RFC 2049. No validation will be performed during API submission and it will be attempted to be delivered as is. Any errors while processing and delivering this email will be available only via callbacks.    # noqa: E501

        :param mime: The mime of this InlineObject1.  # noqa: E501
        :type mime: str
        """

        self._mime = mime

    @property
    def channel(self):
        """Gets the channel of this InlineObject1.  # noqa: E501

        Name of the channel through which the email will be sent.  # noqa: E501

        :return: The channel of this InlineObject1.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this InlineObject1.

        Name of the channel through which the email will be sent.  # noqa: E501

        :param channel: The channel of this InlineObject1.  # noqa: E501
        :type channel: str
        """

        self._channel = channel

    @property
    def recipients(self):
        """Gets the recipients of this InlineObject1.  # noqa: E501


        :return: The recipients of this InlineObject1.  # noqa: E501
        :rtype: V4MessagesMimeRecipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this InlineObject1.


        :param recipients: The recipients of this InlineObject1.  # noqa: E501
        :type recipients: V4MessagesMimeRecipients
        """

        self._recipients = recipients

    @property
    def originator(self):
        """Gets the originator of this InlineObject1.  # noqa: E501


        :return: The originator of this InlineObject1.  # noqa: E501
        :rtype: V4MessagesOriginator
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """Sets the originator of this InlineObject1.


        :param originator: The originator of this InlineObject1.  # noqa: E501
        :type originator: V4MessagesOriginator
        """

        self._originator = originator

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
        if not isinstance(other, InlineObject1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject1):
            return True

        return self.to_dict() != other.to_dict()
