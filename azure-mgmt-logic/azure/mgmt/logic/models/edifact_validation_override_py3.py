# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EdifactValidationOverride(Model):
    """The Edifact validation override settings.

    All required parameters must be populated in order to send to Azure.

    :param message_id: Required. The message id on which the validation
     settings has to be applied.
    :type message_id: str
    :param enforce_character_set: Required. The value indicating whether to
     validate character Set.
    :type enforce_character_set: bool
    :param validate_edi_types: Required. The value indicating whether to
     validate EDI types.
    :type validate_edi_types: bool
    :param validate_xsd_types: Required. The value indicating whether to
     validate XSD types.
    :type validate_xsd_types: bool
    :param allow_leading_and_trailing_spaces_and_zeroes: Required. The value
     indicating whether to allow leading and trailing spaces and zeroes.
    :type allow_leading_and_trailing_spaces_and_zeroes: bool
    :param trailing_separator_policy: Required. The trailing separator policy.
     Possible values include: 'NotSpecified', 'NotAllowed', 'Optional',
     'Mandatory'
    :type trailing_separator_policy: str or
     ~azure.mgmt.logic.models.TrailingSeparatorPolicy
    :param trim_leading_and_trailing_spaces_and_zeroes: Required. The value
     indicating whether to trim leading and trailing spaces and zeroes.
    :type trim_leading_and_trailing_spaces_and_zeroes: bool
    """

    _validation = {
        'message_id': {'required': True},
        'enforce_character_set': {'required': True},
        'validate_edi_types': {'required': True},
        'validate_xsd_types': {'required': True},
        'allow_leading_and_trailing_spaces_and_zeroes': {'required': True},
        'trailing_separator_policy': {'required': True},
        'trim_leading_and_trailing_spaces_and_zeroes': {'required': True},
    }

    _attribute_map = {
        'message_id': {'key': 'messageId', 'type': 'str'},
        'enforce_character_set': {'key': 'enforceCharacterSet', 'type': 'bool'},
        'validate_edi_types': {'key': 'validateEDITypes', 'type': 'bool'},
        'validate_xsd_types': {'key': 'validateXSDTypes', 'type': 'bool'},
        'allow_leading_and_trailing_spaces_and_zeroes': {'key': 'allowLeadingAndTrailingSpacesAndZeroes', 'type': 'bool'},
        'trailing_separator_policy': {'key': 'trailingSeparatorPolicy', 'type': 'str'},
        'trim_leading_and_trailing_spaces_and_zeroes': {'key': 'trimLeadingAndTrailingSpacesAndZeroes', 'type': 'bool'},
    }

    def __init__(self, *, message_id: str, enforce_character_set: bool, validate_edi_types: bool, validate_xsd_types: bool, allow_leading_and_trailing_spaces_and_zeroes: bool, trailing_separator_policy, trim_leading_and_trailing_spaces_and_zeroes: bool, **kwargs) -> None:
        super(EdifactValidationOverride, self).__init__(**kwargs)
        self.message_id = message_id
        self.enforce_character_set = enforce_character_set
        self.validate_edi_types = validate_edi_types
        self.validate_xsd_types = validate_xsd_types
        self.allow_leading_and_trailing_spaces_and_zeroes = allow_leading_and_trailing_spaces_and_zeroes
        self.trailing_separator_policy = trailing_separator_policy
        self.trim_leading_and_trailing_spaces_and_zeroes = trim_leading_and_trailing_spaces_and_zeroes
