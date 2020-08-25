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


class StatsResponseDataItems(object):
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
        'accepted': 'int',
        'complained': 'int',
        'delivered': 'int',
        'clicked': 'int',
        'opened': 'int',
        'failed': 'int',
        'unsubscribed': 'int',
        'queued': 'int'
    }

    attribute_map = {
        'accepted': 'accepted',
        'complained': 'complained',
        'delivered': 'delivered',
        'clicked': 'clicked',
        'opened': 'opened',
        'failed': 'failed',
        'unsubscribed': 'unsubscribed',
        'queued': 'queued'
    }

    def __init__(self, accepted=None, complained=None, delivered=None, clicked=None, opened=None, failed=None, unsubscribed=None, queued=None, local_vars_configuration=None):  # noqa: E501
        """StatsResponseDataItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accepted = None
        self._complained = None
        self._delivered = None
        self._clicked = None
        self._opened = None
        self._failed = None
        self._unsubscribed = None
        self._queued = None
        self.discriminator = None

        if accepted is not None:
            self.accepted = accepted
        if complained is not None:
            self.complained = complained
        if delivered is not None:
            self.delivered = delivered
        if clicked is not None:
            self.clicked = clicked
        if opened is not None:
            self.opened = opened
        if failed is not None:
            self.failed = failed
        if unsubscribed is not None:
            self.unsubscribed = unsubscribed
        if queued is not None:
            self.queued = queued

    @property
    def accepted(self):
        """Gets the accepted of this StatsResponseDataItems.  # noqa: E501


        :return: The accepted of this StatsResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """Sets the accepted of this StatsResponseDataItems.


        :param accepted: The accepted of this StatsResponseDataItems.  # noqa: E501
        :type accepted: int
        """

        self._accepted = accepted

    @property
    def complained(self):
        """Gets the complained of this StatsResponseDataItems.  # noqa: E501


        :return: The complained of this StatsResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._complained

    @complained.setter
    def complained(self, complained):
        """Sets the complained of this StatsResponseDataItems.


        :param complained: The complained of this StatsResponseDataItems.  # noqa: E501
        :type complained: int
        """

        self._complained = complained

    @property
    def delivered(self):
        """Gets the delivered of this StatsResponseDataItems.  # noqa: E501


        :return: The delivered of this StatsResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """Sets the delivered of this StatsResponseDataItems.


        :param delivered: The delivered of this StatsResponseDataItems.  # noqa: E501
        :type delivered: int
        """

        self._delivered = delivered

    @property
    def clicked(self):
        """Gets the clicked of this StatsResponseDataItems.  # noqa: E501


        :return: The clicked of this StatsResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._clicked

    @clicked.setter
    def clicked(self, clicked):
        """Sets the clicked of this StatsResponseDataItems.


        :param clicked: The clicked of this StatsResponseDataItems.  # noqa: E501
        :type clicked: int
        """

        self._clicked = clicked

    @property
    def opened(self):
        """Gets the opened of this StatsResponseDataItems.  # noqa: E501


        :return: The opened of this StatsResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._opened

    @opened.setter
    def opened(self, opened):
        """Sets the opened of this StatsResponseDataItems.


        :param opened: The opened of this StatsResponseDataItems.  # noqa: E501
        :type opened: int
        """

        self._opened = opened

    @property
    def failed(self):
        """Gets the failed of this StatsResponseDataItems.  # noqa: E501


        :return: The failed of this StatsResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this StatsResponseDataItems.


        :param failed: The failed of this StatsResponseDataItems.  # noqa: E501
        :type failed: int
        """

        self._failed = failed

    @property
    def unsubscribed(self):
        """Gets the unsubscribed of this StatsResponseDataItems.  # noqa: E501


        :return: The unsubscribed of this StatsResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._unsubscribed

    @unsubscribed.setter
    def unsubscribed(self, unsubscribed):
        """Sets the unsubscribed of this StatsResponseDataItems.


        :param unsubscribed: The unsubscribed of this StatsResponseDataItems.  # noqa: E501
        :type unsubscribed: int
        """

        self._unsubscribed = unsubscribed

    @property
    def queued(self):
        """Gets the queued of this StatsResponseDataItems.  # noqa: E501


        :return: The queued of this StatsResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._queued

    @queued.setter
    def queued(self, queued):
        """Sets the queued of this StatsResponseDataItems.


        :param queued: The queued of this StatsResponseDataItems.  # noqa: E501
        :type queued: int
        """

        self._queued = queued

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
        if not isinstance(other, StatsResponseDataItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatsResponseDataItems):
            return True

        return self.to_dict() != other.to_dict()
