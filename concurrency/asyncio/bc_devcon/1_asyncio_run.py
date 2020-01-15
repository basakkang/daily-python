import asyncio

async def main():
    """
    async 코루틴
    """
    print('Welcome to the BC DevCon')

if __name__ == "__main__":
    # main 이란 코루틴을 complete될 때까지 run한다.
    asyncio.run(main())
