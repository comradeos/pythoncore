import os, random
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
from pillow_heif import register_heif_opener

os.chdir(os.path.dirname(__file__))

register_heif_opener()

image = Image.open('IMG_1216.PNG').convert('RGB')
image.thumbnail((1000, 1000), Image.Resampling.LANCZOS)
image.save('__output.jpg', "JPEG")
