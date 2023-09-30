import os
import base64
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

os.chdir(os.path.dirname(__file__))

numbers = {
    0: '[нуль]',
    1: '[один]',
    2: '[два]',
    3: '[три]',
    4: '[чотири]',
    5: '[п\'ять]',
    6: '[шість]',
    7: '[сім]',
    8: '[вісім]',
    9: '[дев\'ять]',
}


captcha_text = ''
captcha_numbers = ''

for i in range(3):
    item = random.choice(list(numbers.items()))
    captcha_numbers += str(item[0])
    captcha_text += item[1]

def create_image(size, bg_color, message, font, font_color):
    W, H = size
    image = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)/2, (H-h)/2), message, font=font, fill=font_color)
    return image

font = ImageFont.truetype(r"resources\Roboto-Light.ttf", size=24)

my_image = create_image((300, 50), '#a1a1a1', captcha_text, font, 'black')

buffered = BytesIO()
my_image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue())

print(img_str)

my_image.save("aaa.png")


print("#"*40)