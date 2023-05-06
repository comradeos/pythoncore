from time import sleep
from threading import Thread
import asyncio

my_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
]

async def translate(target_list:list, item_index:int):
    await asyncio.sleep(1)
    target_list[item_index] = "b"

tasks = []

async def main():
    for i in my_list:
        item_index = my_list.index(i)
        tasks.append(asyncio.create_task(translate(my_list, item_index)))

    for i in tasks:
        await i
        
    print(my_list[0:5])
    
asyncio.run(main())