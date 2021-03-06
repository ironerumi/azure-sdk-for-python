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


class AddressResponse(Model):
    """Describes main public IP address and any extra virtual IPs.

    :param service_ip_address: Main public virtual IP.
    :type service_ip_address: str
    :param internal_ip_address: Virtual Network internal IP address of the App
     Service Environment if it is in internal load-balancing mode.
    :type internal_ip_address: str
    :param outbound_ip_addresses: IP addresses appearing on outbound
     connections.
    :type outbound_ip_addresses: list[str]
    :param vip_mappings: Additional virtual IPs.
    :type vip_mappings: list[~azure.mgmt.web.models.VirtualIPMapping]
    """

    _attribute_map = {
        'service_ip_address': {'key': 'serviceIpAddress', 'type': 'str'},
        'internal_ip_address': {'key': 'internalIpAddress', 'type': 'str'},
        'outbound_ip_addresses': {'key': 'outboundIpAddresses', 'type': '[str]'},
        'vip_mappings': {'key': 'vipMappings', 'type': '[VirtualIPMapping]'},
    }

    def __init__(self, **kwargs):
        super(AddressResponse, self).__init__(**kwargs)
        self.service_ip_address = kwargs.get('service_ip_address', None)
        self.internal_ip_address = kwargs.get('internal_ip_address', None)
        self.outbound_ip_addresses = kwargs.get('outbound_ip_addresses', None)
        self.vip_mappings = kwargs.get('vip_mappings', None)
