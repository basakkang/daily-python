
import asyncio
import time

async def devcon():
    print('DevCon 시작')
    await asyncio.sleep(3)
    print('DevCon 종료')

async def eat_sushi():
    print('스시집 도착')
    await asyncio.sleep(2)
    print('아 잘먹었다')

async def main():
    loop = asyncio.get_event_loop()
    await loop.create_task(devcon())
    await loop.create_task(eat_sushi())

if __name__ == "__main__":
    t1 = time.perf_counter()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    t2 = time.perf_counter()
    print(f'DevCon 하고 밥먹는데 걸린 시간은? {t2 - t1}')
