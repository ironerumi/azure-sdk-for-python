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


class SharedAccessAuthorizationRuleCreateOrUpdateParameters(Model):
    """Parameters supplied to the Create Or Update Authorization Rules operation.

    All required parameters must be populated in order to send to Azure.

    :param location: Data center location.
    :type location: str
    :param name: Name of the AuthorizationRule.
    :type name: str
    :param rights: Required. The rights associated with the rule.
    :type rights: list[str or
     ~azure.mgmt.eventhub.v2015_08_01.models.AccessRights]
    """

    _validation = {
        'rights': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'rights': {'key': 'properties.rights', 'type': '[AccessRights]'},
    }

    def __init__(self, **kwargs):
        super(SharedAccessAuthorizationRuleCreateOrUpdateParameters, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.name = kwargs.get('name', None)
        self.rights = kwargs.get('rights', None)
