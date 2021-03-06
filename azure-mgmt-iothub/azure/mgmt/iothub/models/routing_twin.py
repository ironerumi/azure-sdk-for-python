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


class RoutingTwin(Model):
    """Twin reference input parameter. This is an optional parameter.

    :param tags: Twin Tags
    :type tags: object
    :param properties:
    :type properties: ~azure.mgmt.iothub.models.RoutingTwinProperties
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': 'object'},
        'properties': {'key': 'properties', 'type': 'RoutingTwinProperties'},
    }

    def __init__(self, **kwargs):
        super(RoutingTwin, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.properties = kwargs.get('properties', None)
