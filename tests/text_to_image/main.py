import os, random
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO

os.chdir(os.path.dirname(__file__))

width, height = 200, 50
start_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
end_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
img = Image.new('RGB', (width, height), color=start_color)
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(r"resources\Roboto-Light.ttf", size=24)

draw.text((40, 10), "Hello world!", fill=(0, 0, 0), font=font)

buffered = BytesIO()
img.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue())

print(img_str)

img.save("aaa.png")