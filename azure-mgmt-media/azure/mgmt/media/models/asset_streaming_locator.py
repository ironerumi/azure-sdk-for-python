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


class AssetStreamingLocator(Model):
    """Properties of the Streaming Locator.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Streaming Locator name.
    :vartype name: str
    :ivar asset_name: Asset Name.
    :vartype asset_name: str
    :ivar created: The creation time of the Streaming Locator.
    :vartype created: datetime
    :ivar start_time: The start time of the Streaming Locator.
    :vartype start_time: datetime
    :ivar end_time: The end time of the Streaming Locator.
    :vartype end_time: datetime
    :ivar streaming_locator_id: StreamingLocatorId of the Streaming Locator.
    :vartype streaming_locator_id: str
    :ivar streaming_policy_name: Name of the Streaming Policy used by this
     Streaming Locator.
    :vartype streaming_policy_name: str
    :ivar default_content_key_policy_name: Name of the default
     ContentKeyPolicy used by this Streaming Locator.
    :vartype default_content_key_policy_name: str
    """

    _validation = {
        'name': {'readonly': True},
        'asset_name': {'readonly': True},
        'created': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'streaming_locator_id': {'readonly': True},
        'streaming_policy_name': {'readonly': True},
        'default_content_key_policy_name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'asset_name': {'key': 'assetName', 'type': 'str'},
        'created': {'key': 'created', 'type': 'iso-8601'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'streaming_locator_id': {'key': 'streamingLocatorId', 'type': 'str'},
        'streaming_policy_name': {'key': 'streamingPolicyName', 'type': 'str'},
        'default_content_key_policy_name': {'key': 'defaultContentKeyPolicyName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AssetStreamingLocator, self).__init__(**kwargs)
        self.name = None
        self.asset_name = None
        self.created = None
        self.start_time = None
        self.end_time = None
        self.streaming_locator_id = None
        self.streaming_policy_name = None
        self.default_content_key_policy_name = None
