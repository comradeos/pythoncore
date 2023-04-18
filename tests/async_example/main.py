import asyncio

async def main():
    task1 = asyncio.create_task(other_function())
    task2 = asyncio.create_task(other_return_function())
    print("A")
    await asyncio.sleep(5)
    print("B")
    await task1
    returned_value = await task2
    print(f"RET {returned_value}")

async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10

async def other_return_function():
    return 10

asyncio.run(main())