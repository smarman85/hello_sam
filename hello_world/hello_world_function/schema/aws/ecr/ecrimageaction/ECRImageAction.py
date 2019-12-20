# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class ECRImageAction(object):


    _types = {
        'action_type': 'str',
        'image_digest': 'str',
        'image_tag': 'str',
        'repository_name': 'str',
        'result': 'str'
    }

    _attribute_map = {
        'action_type': 'action-type',
        'image_digest': 'image-digest',
        'image_tag': 'image-tag',
        'repository_name': 'repository-name',
        'result': 'result'
    }

    def __init__(self, action_type=None, image_digest=None, image_tag=None, repository_name=None, result=None):  # noqa: E501
        self._action_type = None
        self._image_digest = None
        self._image_tag = None
        self._repository_name = None
        self._result = None
        self.discriminator = None
        self.action_type = action_type
        self.image_digest = image_digest
        self.image_tag = image_tag
        self.repository_name = repository_name
        self.result = result


    @property
    def action_type(self):

        return self._action_type

    @action_type.setter
    def action_type(self, action_type):


        self._action_type = action_type


    @property
    def image_digest(self):

        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):


        self._image_digest = image_digest


    @property
    def image_tag(self):

        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):


        self._image_tag = image_tag


    @property
    def repository_name(self):

        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):


        self._repository_name = repository_name


    @property
    def result(self):

        return self._result

    @result.setter
    def result(self, result):


        self._result = result

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
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
        if issubclass(ECRImageAction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ECRImageAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

