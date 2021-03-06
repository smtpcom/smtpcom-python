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


class AccountDataAddress(object):
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
        'street': 'str',
        'city': 'str',
        'state': 'str',
        'country': 'str'
    }

    attribute_map = {
        'street': 'street',
        'city': 'city',
        'state': 'state',
        'country': 'country'
    }

    def __init__(self, street=None, city=None, state=None, country=None, local_vars_configuration=None):  # noqa: E501
        """AccountDataAddress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._street = None
        self._city = None
        self._state = None
        self._country = None
        self.discriminator = None

        if street is not None:
            self.street = street
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country

    @property
    def street(self):
        """Gets the street of this AccountDataAddress.  # noqa: E501

        Account owner’s street address  # noqa: E501

        :return: The street of this AccountDataAddress.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this AccountDataAddress.

        Account owner’s street address  # noqa: E501

        :param street: The street of this AccountDataAddress.  # noqa: E501
        :type street: str
        """

        self._street = street

    @property
    def city(self):
        """Gets the city of this AccountDataAddress.  # noqa: E501

        Account owner’s city  # noqa: E501

        :return: The city of this AccountDataAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AccountDataAddress.

        Account owner’s city  # noqa: E501

        :param city: The city of this AccountDataAddress.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this AccountDataAddress.  # noqa: E501

        Account owner’s state  # noqa: E501

        :return: The state of this AccountDataAddress.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AccountDataAddress.

        Account owner’s state  # noqa: E501

        :param state: The state of this AccountDataAddress.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this AccountDataAddress.  # noqa: E501

        Account owner’s country  # noqa: E501

        :return: The country of this AccountDataAddress.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AccountDataAddress.

        Account owner’s country  # noqa: E501

        :param country: The country of this AccountDataAddress.  # noqa: E501
        :type country: str
        """

        self._country = country

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
        if not isinstance(other, AccountDataAddress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountDataAddress):
            return True

        return self.to_dict() != other.to_dict()
