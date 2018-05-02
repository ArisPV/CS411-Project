import json
from google.protobuf.json_format import MessageToJson

# Contains a bunch of helper functions that parse through different JSONs to find
# relevant information.

def json_parse_labels(json_file):
    """ Parses the Label Annotations from the Google Cloud Image JSON file
    """
    
    json_data = json.loads(json_file)
    label_annotations = json_data['labelAnnotations']
    label_dict = {}
    
    for i in label_annotations:
        if i['score'] >= 0.9:
            label_dict[i['description']] = i['score']
            
    if label_dict == {}:
        label_dict[label_annotations[0]['description']] = top_label_1_score = label_annotations[0]['score']
    
    return label_dict


def json_is_spoof(json_file):
    """ Detects if the image is a spoof image (meme) from the Google Cloud Image
        JSON file
    """

    json_data = json.loads(json_file)
    safeSearch_annotations = json_data['safeSearchAnnotation']

    if safeSearch_annotations['spoof'] == 'VERY_LIKELY':
        return True

    return False

def json_is_racy(json_file):
    """ Detects if the image is a racy image from the Google Cloud Image JSON file
    """

    json_data = json.loads(json_file)
    safeSearch_annotations = json_data['safeSearchAnnotation']

    if safeSearch_annotations['adult'] == 'VERY_LIKELY':
        return True

    return False

def json_has_landmark(json_file):
    """ Detects if the image contains a landmark using the Google Cloud Image JSON
    file.
    """

    json_data = json.loads(json_file)
    return 'landmarkAnnotations' in json_data

def json_landmark(json_file):
    """ Detects what the landmark is using the Google Cloud Image JSON file
    """

    json_data = json.loads(json_file)

    landmark_annotations = json_data['landmarkAnnotations']

    return landmark_annotations[0]['description']

def json_has_text(json_file):
    """ Detects if the image has text using Google Cloud Image JSON file
    """

    json_data = json.loads(json_file)
    return 'textAnnotations' in json_data

def json_has_face(json_file):
    """ Detects if the image contains a face using Google Cloud image JSON file
    """

    json_data = json.loads(json_file)
    return 'faceAnnotations' in json_data

def json_face_emotion(json_file):
    """ Detects the emotion of the face using Google Cloud image JSON file
    """

    json_data = json.loads(json_file)
    
    face_annotations = json_data['faceAnnotations']
    likelihood_name = {'UNKNOWN': 0, 'VERY_UNLIKELY': 1, 'UNLIKELY': 2,
                       'POSSIBLE': 3, 'LIKELY': 4, 'VERY_LIKELY': 5}

    # This JSON can be formatted a number of ways depending on how many
    # people can be in the image at once. Since grabbing everyone's emotions
    # and finding a good balance of their emotions was slightly tedious, I just
    # opted to do the first detected person's emotion.
    if type(face_annotations) == list:
        joy = [likelihood_name[face_annotations[0]['joyLikelihood']], 'joy']
        sorrow = [likelihood_name[face_annotations[0]['sorrowLikelihood']], 'sorrow']
        anger = [likelihood_name[face_annotations[0]['angerLikelihood']], 'anger']
        surprise = [likelihood_name[face_annotations[0]['surpriseLikelihood']], 'surprise']
    # If there is only one person in the image.
    else:
        joy = [likelihood_name[face_annotations['joyLikelihood']], 'joy']
        sorrow = [likelihood_name[face_annotations['sorrowLikelihood']], 'sorrow']
        anger = [likelihood_name[face_annotations['angerLikelihood']], 'anger']
        surprise = [likelihood_name[face_annotations['surpriseLikelihood']], 'surprise']

    emotion = max([joy, sorrow, anger, surprise])

    return emotion[1]


