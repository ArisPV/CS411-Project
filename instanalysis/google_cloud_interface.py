from google.cloud import vision
from google.cloud.vision import types

import io
import os
#import sys

from json_parse import json_parse_labels
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
	response = client.label_detection(image=image)
	serialized = MessageToJson(response)

	# clear json file
	open('response.json', 'w').close()
	# now write to it
	print(serialized, file=open('response.json','a'))
	labels, is_spoof, is_racy, landmark, has_text, has_face, emotion = json_parse_labels('response.json')
	return labels, is_spoof, is_racy, landmark, has_text, has_face, emotion







