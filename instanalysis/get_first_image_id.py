import json

def check_first_image_id(json_file):
    """ Gets the first image ID in the JSON file so we can check if it is in the
        database or not.
    """

    json_data = json.load(json_file)

    return json_data['data'][0]['id']

