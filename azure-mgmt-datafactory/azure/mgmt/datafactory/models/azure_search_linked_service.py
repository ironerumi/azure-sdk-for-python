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

from .linked_service import LinkedService


class AzureSearchLinkedService(LinkedService):
    """Linked service for Windows Azure Search Service.

    :param connect_via: The integration runtime reference.
    :type connect_via: :class:`IntegrationRuntimeReference
     <azure.mgmt.datafactory.models.IntegrationRuntimeReference>`
    :param description: Linked service description.
    :type description: str
    :param type: Polymorphic Discriminator
    :type type: str
    :param url: URL for Azure Search service. Type: string (or Expression with
     resultType string).
    :type url: object
    :param key: Admin Key for Azure Search service
    :type key: :class:`SecureString
     <azure.mgmt.datafactory.models.SecureString>`
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'url': {'required': True},
    }

    _attribute_map = {
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'typeProperties.url', 'type': 'object'},
        'key': {'key': 'typeProperties.key', 'type': 'SecureString'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, url, connect_via=None, description=None, key=None, encrypted_credential=None):
        super(AzureSearchLinkedService, self).__init__(connect_via=connect_via, description=description)
        self.url = url
        self.key = key
        self.encrypted_credential = encrypted_credential
        self.type = 'AzureSearch'