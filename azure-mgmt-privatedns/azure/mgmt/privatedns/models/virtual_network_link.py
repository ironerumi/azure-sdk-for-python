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

from .tracked_resource import TrackedResource


class VirtualNetworkLink(TrackedResource):
    """Describes a link to virtual network for a Private DNS zone.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Example -
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateDnsZoneName}'.
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Example -
     'Microsoft.Network/privateDnsZones'.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives
    :type location: str
    :param etag: The ETag of the virtual network link.
    :type etag: str
    :param virtual_network: The reference of the virtual network.
    :type virtual_network: ~azure.mgmt.privatedns.models.SubResource
    :param registration_enabled: Is auto-registration of virtual machine
     records in the virtual network in the Private DNS zone enabled?
    :type registration_enabled: bool
    :ivar virtual_network_link_state: The status of the virtual network link
     to the Private DNS zone. Possible values are 'InProgress' and 'Done'. This
     is a read-only property and any attempt to set this value will be ignored.
     Possible values include: 'InProgress', 'Completed'
    :vartype virtual_network_link_state: str or
     ~azure.mgmt.privatedns.models.VirtualNetworkLinkState
    :ivar provisioning_state: The provisioning state of the resource. This is
     a read-only property and any attempt to set this value will be ignored.
     Possible values include: 'Creating', 'Updating', 'Deleting', 'Succeeded',
     'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.privatedns.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'virtual_network_link_state': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'virtual_network': {'key': 'properties.virtualNetwork', 'type': 'SubResource'},
        'registration_enabled': {'key': 'properties.registrationEnabled', 'type': 'bool'},
        'virtual_network_link_state': {'key': 'properties.virtualNetworkLinkState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VirtualNetworkLink, self).__init__(**kwargs)
        self.etag = kwargs.get('etag', None)
        self.virtual_network = kwargs.get('virtual_network', None)
        self.registration_enabled = kwargs.get('registration_enabled', None)
        self.virtual_network_link_state = None
        self.provisioning_state = None
