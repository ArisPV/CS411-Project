# Import literally everything.
from json_username_token import get_token_and_username
from instagram_json_call import call_instagram_api
import instagram_json_parse
from db import check_user, get_list_of_img_id, update_db
import download_image
from google_cloud_interface import analyze_file
import json


def api_main(access_token_json):
    """ Calls all of like everything.
    """

    username, access_token = get_token_and_username(access_token_json)
    
    insta_json_data = call_instagram_api(access_token)
    
    list_img = []
    if not check_user(username):
        list_img = get_list_of_img_id(username)
    
    user_info = read_insta_json(insta_json_data, list_img)
    #Iterate through all of the lists in user info

    for i in user_info:
        image_url = user_info[i][0]
        image_id = user_info[i][1]
        download_image(image_url, image_id)

        labels, is_spoof, is_racy, landmark, has_text, has_face, emotion = analyze_file('app/static/img/' + image_id + '.jpg')
        google_image_output = [labels, is_spoof, is_racy, landmark, has_text, has_face, emotion]

        user_info[i].append(google_image_output)

    # Get the information from the database using the output_db function.
    # The return values from this would only be the newly updated images that
    # didn't already exist on the database beforehand.
    
    update_db(username, user_info)

    return username
