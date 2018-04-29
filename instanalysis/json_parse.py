import json
from google.protobuf.json_format import MessageToJson

def json_parse(json_file):
    """ This calls all of the JSON parsing helper functions in this file.
    """

    json_data = json.load(json_file)
    
    labels = json_parse_labels(json_data)
    is_spoof = json_is_spoof(json_data)
    is_racy = json_is_racy(json_data)
    if(json_has_landmark(json_data)):
        landmark = json_landmark(json_data)
    else:
        landmark = None
    has_text = json_has_text(json_data)
    has_face = json_has_face(json_data)
    if has_face:
        emotion = json_face_emotion(json_data)
    else:
        emotion = None

    # Do a if landmark == None if you want to ascertain whether or not there
    # is a landmark in the image.
    return labels, is_spoof, is_racy, landmark, has_text, has_face, emotion

def json_parse_labels(json_data):
    """ Parses the Label Annotations from the Google Cloud Image JSON file
    """

    label_annotations = json_data['labelAnnotations']
    label_dict = {}
    
    for i in label_annotations:
        if i['score'] >= 0.9:
            label_dict[i['description']] = i['score']
            
    if label_dict == {}:
        label_dict[label_annotations[0]['description']] = top_label_1_score = label_annotations[0]['score']
    
    return label_dict


def json_is_spoof(json_data):
    """ Detects if the image is a spoof image (meme) from the Google Cloud Image
        JSON file
    """

    safeSearch_annotations = json_data['safeSearchAnnotation']

    if safeSearch_annotations['spoof'] == 'VERY_LIKELY':
        return True

    return False

def json_is_racy(json_data):
    """ Detects if the image is a racy image from the Google Cloud Image JSON file
    """

    safeSearch_annotations = json_data['safeSearchAnnotation']

    if safeSearch_annotations['racy'] == 'VERY_LIKELY':
        return True

    return False

def json_has_landmark(json_data):
    """ Detects if the image contains a landmark using the Google Cloud Image JSON
    file.
    """

    return 'landmarkAnnotations' in json_data

def json_landmark(json_data):
    """ Detects what the landmark is using the Google Cloud Image JSON file
    """
    
    if not(json_has_landmark(json_data)):
        return ('There is no landmark.')

    landmark_annotations = json_data['landmarkAnnotations']

    return landmark_annotations[0]['description']

def json_has_text(json_data):
    """ Detects if the image has text using Google Cloud Image JSON file
    """

    return 'textAnnotations' in json_data

def json_has_face(json_data):
    """ Detects if the image contains a face using Google Cloud image JSON file
    """

    return 'faceAnnotations' in json_data

def json_face_emotion(json_data):
    """ Detects the emotion of the face using Google Cloud image JSON file
    """

    if not(json_has_face(json_data)):
        return ('There is no face.')
    
    face_annotations = json_data['faceAnnotations']
    likelihood_name = {'UNKNOWN': 0, 'VERY_UNLIKELY': 1, 'UNLIKELY': 2,
                       'POSSIBLE': 3, 'LIKELY': 4, 'VERY_LIKELY': 5}

    joy = [likelihood_name[face_annotations['joyLikelihood']], 'joy']
    sorrow = [likelihood_name[face_annotations['sorrowLikelihood']], 'sorrow']
    anger = [likelihood_name[face_annotations['angerLikelihood']], 'anger']
    surprise = [likelihood_name[face_annotations['surpriseLikelihood']], 'surprise']

    emotion = max([joy, sorrow, anger, surprise])

    return emotion[1]


