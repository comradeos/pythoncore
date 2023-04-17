import asyncio

async def my_func():
    for i in range(1, 10):
        print(f"my_func -> {i}")
        await asyncio.sleep(1)

async def my_func_2():
    for i in range(1, 10):
        print(f"my_func_2 -> {i}")
        await asyncio.sleep(0.5)
        
async def main():
    t1 = asyncio.create_task(my_func())
    t2 = asyncio.create_task(my_func_2())
    await asyncio.gather(t1, t2)
    
asyncio.run(main())

