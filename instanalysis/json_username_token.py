import json

json_file = open('poof.json', 'r')
json_file.close

def get_token_and_username(json_file):

    json_data = json.load(json_file)

    username = json_data['user']['username']
    access_token = json_data['access_token']
    return username, access_token

