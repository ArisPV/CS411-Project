from google.cloud import vision
from google.cloud.vision import types

import io
import os
#import sys

from json_parse import json_parse_labels, json_is_spoof, json_is_racy, json_has_landmark, json_landmark, json_has_text, json_has_face, json_face_emotion
import json
from google.protobuf.json_format import MessageToJson

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="service_account.json"

#path_name = str(sys.argv[1])

DEBUG = False

# # Instantiates a client
# client = vision.ImageAnnotatorClient()

# # The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     path_name)

# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()

# image = types.Image(content=content)

# # Performs label detection on the image file
# response = client.label_detection(image=image)


# print(response)

def analyze_file(filename):
        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        # The name of the image file to annotate
        file_name = os.path.join(os.path.dirname(__file__), filename)
	
        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
                content = image_file.read()
        image = types.Image(content=content)
	
        # Performs label detection on the image file
        response_label = client.label_detection(image=image)
        serialized_label = MessageToJson(response_label)
        labels = json_parse_labels(serialized_label)

        response_safe_search = client.safe_search_detection(image=image)
        serialized_safe_search = MessageToJson(response_safe_search)
        is_spoof = json_is_spoof(serialized_safe_search)
        
        is_racy = json_is_racy(serialized_safe_search)

        response_landmark = client.landmark_detection(image=image)
        serialized_landmark = MessageToJson(response_landmark)
        if(json_has_landmark(serialized_landmark)):
                landmark = json_landmark(serialized_landmark)
        else:
                landmark = None

        response_text = client.text_detection(image=image)
        serialized_text = MessageToJson(response_text)
        has_text = json_has_text(serialized_text)

        response_face = client.face_detection(image=image)
        serialized_face = MessageToJson(response_face)
        has_face = json_has_face(serialized_face)
        if has_face:
                emotion = json_face_emotion(serialized_face)
        else:
                emotion = None
	
        
        return labels, is_spoof, is_racy, landmark, has_text, has_face, emotion







