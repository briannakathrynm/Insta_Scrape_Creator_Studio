import urllib
from urllib import request


def url_to_img(url, filename, make_directory):
    """
    Getting the actual photo file or video file from an Instagram url
    Args:
    url: photo/thumbnail URL from insights_details
    filename: filename to be saved to folder
    Returns:
    Image file, saved locally to folder listed below
    """
    image_url = url
    urllib.request.urlretrieve(image_url, make_directory + "\\" + filename)
