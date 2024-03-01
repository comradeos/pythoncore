import time
import requests
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    print('Hello Docker')
    # Отправляем GET-запрос на страницу
    response = requests.get(r'https://www.ebay.com/itm/185997734023')

    # Используем регулярное выражение для поиска цены
    price = re.search(r'US \$([0-9,\.]+)', response.text)

    print(price)

    with open('output.txt', 'w') as file:
        file.write(response.text)

    # Выводим цену
    if price:
        print(price.group(0))
    else:
        print("Цена не найдена")
        
    time.sleep(5)







