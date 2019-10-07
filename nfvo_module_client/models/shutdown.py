# coding: utf-8

"""
    NFVO Module Service

    NFVO module service for the NI project.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Shutdown(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'vnf_instance_id': 'str'
    }

    attribute_map = {
        'vnf_instance_id': 'vnf_instance_id'
    }

    def __init__(self, vnf_instance_id=None):  # noqa: E501
        """Shutdown - a model defined in Swagger"""  # noqa: E501

        self._vnf_instance_id = None
        self.discriminator = None

        if vnf_instance_id is not None:
            self.vnf_instance_id = vnf_instance_id

    @property
    def vnf_instance_id(self):
        """Gets the vnf_instance_id of this Shutdown.  # noqa: E501


        :return: The vnf_instance_id of this Shutdown.  # noqa: E501
        :rtype: str
        """
        return self._vnf_instance_id

    @vnf_instance_id.setter
    def vnf_instance_id(self, vnf_instance_id):
        """Sets the vnf_instance_id of this Shutdown.


        :param vnf_instance_id: The vnf_instance_id of this Shutdown.  # noqa: E501
        :type: str
        """

        self._vnf_instance_id = vnf_instance_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Shutdown, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Shutdown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
