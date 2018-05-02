import requests
import os.path

def download_image(url, image_id):
    """ Downloads an image taking the url and the image ID supplied by the
        JSON file and finds the image and downloads it.
    """
    save_path = 'app/static/img/' 
    image_name = image_id + '.jpg'
    complete_name = os.path.join(save_path, image_name)
    
    image = open(complete_name, 'wb')
    image.write(requests.get(url).content)
    image.close()


    
