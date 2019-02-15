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

from .proxy_resource_py3 import ProxyResource


class RedisPatchSchedule(ProxyResource):
    """Response to put/get patch schedules for Redis cache.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param schedule_entries: Required. List of patch schedules for a Redis
     cache.
    :type schedule_entries: list[~azure.mgmt.redis.models.ScheduleEntry]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'schedule_entries': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'schedule_entries': {'key': 'properties.scheduleEntries', 'type': '[ScheduleEntry]'},
    }

    def __init__(self, *, schedule_entries, **kwargs) -> None:
        super(RedisPatchSchedule, self).__init__(**kwargs)
        self.schedule_entries = schedule_entries
