import asyncio

async def print1():
    print(1)

async def print2():
    await asyncio.sleep(2)
    print(2)

async def print3():
    print(3)

async def main():
    tasks = []
    task1 = asyncio.create_task(print1())
    task2 = asyncio.create_task(print2())
    task3 = asyncio.create_task(print3())

    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)

    await asyncio.gather(*tasks)

asyncio.run(main())