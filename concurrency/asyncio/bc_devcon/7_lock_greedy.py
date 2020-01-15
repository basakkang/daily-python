import asyncio

lock = asyncio.Lock()

async def coro1():
    await lock.acquire()
    try:
        print('욕심쟁이라 release 안해여')
    finally:
        print('release 안하고 끝났쥬')

async def coro2():
    while True:
        await asyncio.sleep(1)
        print('나 좀 줘!! 몇번 불릴까?')
        await lock.acquire()
        try:
            print('욕심쟁이라 release 안해여')
        finally:
            print('안하쥬')


async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(coro1())
    task2 = loop.create_task(coro2())
    await task1
    await task2

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
