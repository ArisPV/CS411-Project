from urllib.request import urlopen
import json

def call_instagram_api(access_key):
    """ Gets the JSON file with the information that we seek using the access
        key.
    """

    url = 'https://api.instagram.com/v1/users/self/?access_token=' + access_key

    response = urlopen(url)
    string = response.read().decode('utf-8')
    json_data = json.loads(string)
    
    return json_data 
