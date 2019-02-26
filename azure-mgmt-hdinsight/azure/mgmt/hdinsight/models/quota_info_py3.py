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


class QuotaInfo(Model):
    """The quota properties for the cluster.

    :param cores_used: The cores used by the cluster.
    :type cores_used: int
    """

    _attribute_map = {
        'cores_used': {'key': 'coresUsed', 'type': 'int'},
    }

    def __init__(self, *, cores_used: int=None, **kwargs) -> None:
        super(QuotaInfo, self).__init__(**kwargs)
        self.cores_used = cores_used
