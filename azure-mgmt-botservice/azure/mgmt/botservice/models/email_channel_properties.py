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


class EmailChannelProperties(Model):
    """The parameters to provide for the Email channel.

    All required parameters must be populated in order to send to Azure.

    :param email_address: Required. The email address
    :type email_address: str
    :param password: Required. The password for the email address. Value only
     returned through POST to the action Channel List API, otherwise empty.
    :type password: str
    :param is_enabled: Required. Whether this channel is enabled for the bot
    :type is_enabled: bool
    """

    _validation = {
        'email_address': {'required': True},
        'password': {'required': True},
        'is_enabled': {'required': True},
    }

    _attribute_map = {
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(EmailChannelProperties, self).__init__(**kwargs)
        self.email_address = kwargs.get('email_address', None)
        self.password = kwargs.get('password', None)
        self.is_enabled = kwargs.get('is_enabled', None)
