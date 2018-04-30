import json


def read_insta_json(json_data, list_of_image_ids):
    """ Runs all the helper functions below
    """

    user_info = []
   
    for i in range(len(json_data['data'])):
        image_data = json_data['data'][i]
        
        image_id = json_image_id(image_data)
        
        if image_id not in list_of_image_ids:

            if json_is_image(image_data):
                image_url = return_insta_image(image_data)
                image_time = json_image_time(image_data)
                has_caption = json_has_caption(image_data)
                user_has_liked = json_user_has_liked(image_data)
                image_likes = json_how_many_likes(image_data)
                hashtags = json_hashtags(image_data)
                image_filter = json_filter(image_data)
                comment_count = json_comment_count(image_data)
                are_users_tagged = json_users_tagged_in_photo(image_data)
        
                user_info.append([image_url, image_id, image_time, has_caption, user_has_liked,
                image_likes, hashtags, image_filter, comment_count, are_users_tagged])
        
    return user_info

def return_insta_image(image_data):
    """ Takes the JSON file provided by Instagram API and returns the link to
        the image.
    """

    return image_data['images']['standard_resolution']['url']

def json_image_id(image_data):
    """ Takes the image ID from the JSON file provided by the Instagram API
    """

    return image_data['id']

def json_image_time(image_data):
    """ Time created
    """

    return image_data['created_time']

def json_has_caption(image_data):
    """ Checks if the user had a caption.
    """

    return image_data['caption'] is None

def json_user_has_liked(image_data):
    """ Sees if the user has liked his/her own post.
    """

    return image_data['user_has_liked']

def json_how_many_likes(image_data):
    """ How many likes the user has in their image.
    """

    return image_data['likes']['count']

def json_hashtags(image_data):
    """ Gives the hashtags that are associated with the picture provided. If there
        are none, then it will return an empty list.
    """

    return image_data['tags']

def json_filter(image_data):
    """ Gives what filter is being used. If there is no filter being used it will
        be recognized as "Normal"
    """

    return image_data['filter']

def json_comment_count(image_data):
    """ Gives the amount of comments on that picture
    """

    return image_data['comments']['count']

def json_is_image(image_data):
    """ Sees if it is an image or not, we are not analyzing videos -- we are ignoring
        those.
    """

    return image_data['type'] == "image"

def json_users_tagged_in_photo(image_data):
    """ Returns if you tagged other users in your photo or not
    """

    return image_data['users_in_photo'] != []
