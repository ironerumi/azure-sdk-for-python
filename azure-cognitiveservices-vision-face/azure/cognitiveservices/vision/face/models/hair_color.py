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


class HairColor(Model):
    """Hair color and associated confidence.

    :param color: Name of the hair color. Possible values include: 'unknown',
     'white', 'gray', 'blond', 'brown', 'red', 'black', 'other'
    :type color: str or
     ~azure.cognitiveservices.vision.face.models.HairColorType
    :param confidence: Confidence level of the color
    :type confidence: float
    """

    _attribute_map = {
        'color': {'key': 'color', 'type': 'HairColorType'},
        'confidence': {'key': 'confidence', 'type': 'float'},
    }

    def __init__(self, color=None, confidence=None):
        super(HairColor, self).__init__()
        self.color = color
        self.confidence = confidence