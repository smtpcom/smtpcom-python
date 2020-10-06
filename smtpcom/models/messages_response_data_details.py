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


class MessagesResponseDataDetails(object):
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
        'delivery': 'MessagesResponseDataDetailsDelivery'
    }

    attribute_map = {
        'delivery': 'delivery'
    }

    def __init__(self, delivery=None, local_vars_configuration=None):  # noqa: E501
        """MessagesResponseDataDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._delivery = None
        self.discriminator = None

        if delivery is not None:
            self.delivery = delivery

    @property
    def delivery(self):
        """Gets the delivery of this MessagesResponseDataDetails.  # noqa: E501


        :return: The delivery of this MessagesResponseDataDetails.  # noqa: E501
        :rtype: MessagesResponseDataDetailsDelivery
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this MessagesResponseDataDetails.


        :param delivery: The delivery of this MessagesResponseDataDetails.  # noqa: E501
        :type delivery: MessagesResponseDataDetailsDelivery
        """

        self._delivery = delivery

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
        if not isinstance(other, MessagesResponseDataDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessagesResponseDataDetails):
            return True

        return self.to_dict() != other.to_dict()