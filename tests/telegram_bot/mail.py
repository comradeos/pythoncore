# 6622960143:AAHk3FlrmgNpq9mYQp4Y8diLUtKPmrlvZc4
# @raspmsg

import os
import time
import random
import asyncio
import subprocess
from aiogram import Bot

messages = [
    'Агов',
    'А бодай тобі',
    'Дзуськи',
    'Так отож!',
    'Хай йому грець',
]

async def send_message(msg:str):
    bot = Bot(token='secret token')
    try:
        await bot.send_message(chat_id='@raspmsg', text=msg)
    finally:
        await bot.close()

def check_mac_address(target:str):
    with open('output.txt', 'r') as file:
        lines = file.readlines()
        if any(target in line for line in lines):
            print(f'Found {target}')
            msg = random.choice(messages)
            msg += f' {target} is in the area!'
            print(msg)
            # asyncio.run(send_message(''))
        else:
            print('Not found...')

def main():
    # os.chdir(os.path.dirname(__file__))
    target = 'F4:C2:48:7C:01:85'

    while True:
        subprocess.run(['bash', 'scan.sh'])
        print('Scanning...')
        time.sleep(3)
        check_mac_address(target)

if __name__ == '__main__':
    main()

