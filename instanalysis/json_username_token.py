import json


def get_token_and_username(json_file):
    """ File takes the JSON input returned from the OAuth call and returns
        the acces key and the username of the user.
    """

    # File takes a string input.
    # Change it to be loads when committing, as .load is for testing purposes.
    json_data = json.loads(json_file)
    
    username = json_data['user']['username']
    access_token = json_data['access_token']
    return username, access_token


