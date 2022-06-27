import asyncio
import aio_pika


async def callback(message: aio_pika.abc.AbstractIncomingMessage) -> None:
    async with message.process():
        print(message.body)

async def main():
    # Connection
    connection = await aio_pika.connect()
    channel = await connection.channel()
    queue = await channel.declare_queue("async-hello", auto_delete=True)

    await queue.consume(callback=callback)

    try:
        await asyncio.Future()
    finally:
        await connection.close()

if __name__ == "__main__":
    asyncio.run(main())
