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


class V4MessagesBodyAttachments(object):
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
        'version': 'str',
        'type': 'str',
        'disposition': 'str',
        'filename': 'str',
        'cid': 'str',
        'content': 'str'
    }

    attribute_map = {
        'version': 'version',
        'type': 'type',
        'disposition': 'disposition',
        'filename': 'filename',
        'cid': 'cid',
        'content': 'content'
    }

    def __init__(self, version=None, type=None, disposition=None, filename=None, cid=None, content=None, local_vars_configuration=None):  # noqa: E501
        """V4MessagesBodyAttachments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._type = None
        self._disposition = None
        self._filename = None
        self._cid = None
        self._content = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if type is not None:
            self.type = type
        if disposition is not None:
            self.disposition = disposition
        if filename is not None:
            self.filename = filename
        if cid is not None:
            self.cid = cid
        if content is not None:
            self.content = content

    @property
    def version(self):
        """Gets the version of this V4MessagesBodyAttachments.  # noqa: E501

        MIME version. By default set to `1.0`  # noqa: E501

        :return: The version of this V4MessagesBodyAttachments.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V4MessagesBodyAttachments.

        MIME version. By default set to `1.0`  # noqa: E501

        :param version: The version of this V4MessagesBodyAttachments.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def type(self):
        """Gets the type of this V4MessagesBodyAttachments.  # noqa: E501

        MIME type. By default set to `application/octet-stream`  # noqa: E501

        :return: The type of this V4MessagesBodyAttachments.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V4MessagesBodyAttachments.

        MIME type. By default set to `application/octet-stream`  # noqa: E501

        :param type: The type of this V4MessagesBodyAttachments.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def disposition(self):
        """Gets the disposition of this V4MessagesBodyAttachments.  # noqa: E501

        Content-disposition, either `inline` or `attachment`. By default set to `attachment`  # noqa: E501

        :return: The disposition of this V4MessagesBodyAttachments.  # noqa: E501
        :rtype: str
        """
        return self._disposition

    @disposition.setter
    def disposition(self, disposition):
        """Sets the disposition of this V4MessagesBodyAttachments.

        Content-disposition, either `inline` or `attachment`. By default set to `attachment`  # noqa: E501

        :param disposition: The disposition of this V4MessagesBodyAttachments.  # noqa: E501
        :type disposition: str
        """

        self._disposition = disposition

    @property
    def filename(self):
        """Gets the filename of this V4MessagesBodyAttachments.  # noqa: E501

        Name of attached file  # noqa: E501

        :return: The filename of this V4MessagesBodyAttachments.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this V4MessagesBodyAttachments.

        Name of attached file  # noqa: E501

        :param filename: The filename of this V4MessagesBodyAttachments.  # noqa: E501
        :type filename: str
        """

        self._filename = filename

    @property
    def cid(self):
        """Gets the cid of this V4MessagesBodyAttachments.  # noqa: E501

        Content ID for inline dispositions. By default this is equal to the filename. Can be used in HTML content to address an attached image using “cid:” URL scheme.  # noqa: E501

        :return: The cid of this V4MessagesBodyAttachments.  # noqa: E501
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this V4MessagesBodyAttachments.

        Content ID for inline dispositions. By default this is equal to the filename. Can be used in HTML content to address an attached image using “cid:” URL scheme.  # noqa: E501

        :param cid: The cid of this V4MessagesBodyAttachments.  # noqa: E501
        :type cid: str
        """

        self._cid = cid

    @property
    def content(self):
        """Gets the content of this V4MessagesBodyAttachments.  # noqa: E501

        Actual attachment content in its raw form  # noqa: E501

        :return: The content of this V4MessagesBodyAttachments.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this V4MessagesBodyAttachments.

        Actual attachment content in its raw form  # noqa: E501

        :param content: The content of this V4MessagesBodyAttachments.  # noqa: E501
        :type content: str
        """

        self._content = content

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
        if not isinstance(other, V4MessagesBodyAttachments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V4MessagesBodyAttachments):
            return True

        return self.to_dict() != other.to_dict()
