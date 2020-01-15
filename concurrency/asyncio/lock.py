import asyncio

async def coro1(lock):
    await lock.acquire()
    try:
        print('욕심쟁이라 release 안해여')
    finally:
        print('release 안하고 끝났쥬')

async def coro2(lock):
    while True:
        await asyncio.sleep(1)
        print('나 좀 줘!! 몇번 불릴까?')
        await lock.acquire()
        try:
            print('욕심쟁이라 release 안해여')
        finally:
            print('안하쥬')


def main():
    lock = asyncio.Lock()
    loop = asyncio.get_event_loop()
    loop.create_task(coro1(lock))
    loop.create_task(coro2(lock))
    loop.run_forever()

if __name__ == '__main__':
    main()
