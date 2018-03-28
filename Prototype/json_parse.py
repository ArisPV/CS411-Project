import json


# This is just to grab some json txt files for testing purposes. Feel free
# to comment this out when assembling code.
#json_file = open('jsontest.txt', 'r')
#json_file.close


# This function takes the labels from the JSON file and returns the highest
# result. This can be adjusted later to take in all of the results if need be.

def json_parse_labels(json_file):
    """ This function returns a string which the Google Image API uses as a
        label and a float number which is the percent likeliness the API has
        assigned to the label.
    """
    #json_file = open(json_file,'r')
    json_data = json.load(json_file)
    label_annotations = json_data['labelAnnotations']
    
    top_label_1_desc = label_annotations[0]['description']
    top_label_1_score = label_annotations[0]['score']

    return [top_label_1_desc, top_label_1_score]

