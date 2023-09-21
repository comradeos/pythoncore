import random

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
    captcha_text += str(item[0])
    captcha_numbers += item[1]

print(captcha_text)
print(captcha_numbers)