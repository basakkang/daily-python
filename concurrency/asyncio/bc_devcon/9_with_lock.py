import asyncio

lock = asyncio.Lock()

async def coro_A():
    while True:
        await asyncio.sleep(1)
        print('A done')

async def coro_B():
    async with lock:    
        await asyncio.sleep(1)
        print('B done')

async def coro_C():
    while True:
        await asyncio.sleep(1)
        print('C done')


async def main():
    loop = asyncio.get_event_loop()
    task_A = loop.create_task(coro_A())
    task_B_list = []
    for _ in range(10):
        task_B_list.append(loop.create_task(coro_B()))
    task_C = loop.create_task(coro_C())
    
    await asyncio.gather(task_A, *task_B_list, task_C)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
