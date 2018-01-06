from PIL import Image, ImageEnhance, ImageFilter
from pytesseract import image_to_string

# use pytesseract to convert of string to image, after applying the filters.
def get_string_from_image(im):
    text = image_to_string(im)
    return text
