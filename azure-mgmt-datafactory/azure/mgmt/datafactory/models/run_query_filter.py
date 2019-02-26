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


class RunQueryFilter(Model):
    """Query filter option for listing runs.

    All required parameters must be populated in order to send to Azure.

    :param operand: Required. Parameter name to be used for filter. The
     allowed operands to query pipeline runs are PipelineName, RunStart, RunEnd
     and Status; to query activity runs are ActivityName, ActivityRunStart,
     ActivityRunEnd, ActivityType and Status, and to query trigger runs are
     TriggerName, TriggerRunTimestamp and Status. Possible values include:
     'PipelineName', 'Status', 'RunStart', 'RunEnd', 'ActivityName',
     'ActivityRunStart', 'ActivityRunEnd', 'ActivityType', 'TriggerName',
     'TriggerRunTimestamp'
    :type operand: str or ~azure.mgmt.datafactory.models.RunQueryFilterOperand
    :param operator: Required. Operator to be used for filter. Possible values
     include: 'Equals', 'NotEquals', 'In', 'NotIn'
    :type operator: str or
     ~azure.mgmt.datafactory.models.RunQueryFilterOperator
    :param values: Required. List of filter values.
    :type values: list[str]
    """

    _validation = {
        'operand': {'required': True},
        'operator': {'required': True},
        'values': {'required': True},
    }

    _attribute_map = {
        'operand': {'key': 'operand', 'type': 'str'},
        'operator': {'key': 'operator', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(RunQueryFilter, self).__init__(**kwargs)
        self.operand = kwargs.get('operand', None)
        self.operator = kwargs.get('operator', None)
        self.values = kwargs.get('values', None)
