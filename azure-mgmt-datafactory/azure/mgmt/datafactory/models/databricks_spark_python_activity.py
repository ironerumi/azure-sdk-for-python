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

from .execution_activity import ExecutionActivity


class DatabricksSparkPythonActivity(ExecutionActivity):
    """DatabricksSparkPython activity.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param python_file: Required. The URI of the Python file to be executed.
     DBFS paths are supported. Type: string (or Expression with resultType
     string).
    :type python_file: object
    :param parameters: Command line parameters that will be passed to the
     Python file.
    :type parameters: list[object]
    :param libraries: A list of libraries to be installed on the cluster that
     will execute the job.
    :type libraries: list[dict[str, object]]
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'python_file': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'python_file': {'key': 'typeProperties.pythonFile', 'type': 'object'},
        'parameters': {'key': 'typeProperties.parameters', 'type': '[object]'},
        'libraries': {'key': 'typeProperties.libraries', 'type': '[{object}]'},
    }

    def __init__(self, **kwargs):
        super(DatabricksSparkPythonActivity, self).__init__(**kwargs)
        self.python_file = kwargs.get('python_file', None)
        self.parameters = kwargs.get('parameters', None)
        self.libraries = kwargs.get('libraries', None)
        self.type = 'DatabricksSparkPython'
