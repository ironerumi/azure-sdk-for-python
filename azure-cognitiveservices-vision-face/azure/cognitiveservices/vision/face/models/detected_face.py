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


class DetectedFace(Model):
    """Detected Face object.

    All required parameters must be populated in order to send to Azure.

    :param face_id:
    :type face_id: str
    :param recognition_model: Possible values include: 'recognition_01',
     'recognition_02'. Default value: "recognition_01" .
    :type recognition_model: str or
     ~azure.cognitiveservices.vision.face.models.RecognitionModel
    :param face_rectangle: Required.
    :type face_rectangle:
     ~azure.cognitiveservices.vision.face.models.FaceRectangle
    :param face_landmarks:
    :type face_landmarks:
     ~azure.cognitiveservices.vision.face.models.FaceLandmarks
    :param face_attributes:
    :type face_attributes:
     ~azure.cognitiveservices.vision.face.models.FaceAttributes
    """

    _validation = {
        'face_rectangle': {'required': True},
    }

    _attribute_map = {
        'face_id': {'key': 'faceId', 'type': 'str'},
        'recognition_model': {'key': 'recognitionModel', 'type': 'str'},
        'face_rectangle': {'key': 'faceRectangle', 'type': 'FaceRectangle'},
        'face_landmarks': {'key': 'faceLandmarks', 'type': 'FaceLandmarks'},
        'face_attributes': {'key': 'faceAttributes', 'type': 'FaceAttributes'},
    }

    def __init__(self, **kwargs):
        super(DetectedFace, self).__init__(**kwargs)
        self.face_id = kwargs.get('face_id', None)
        self.recognition_model = kwargs.get('recognition_model', "recognition_01")
        self.face_rectangle = kwargs.get('face_rectangle', None)
        self.face_landmarks = kwargs.get('face_landmarks', None)
        self.face_attributes = kwargs.get('face_attributes', None)
