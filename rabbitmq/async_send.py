import asyncio
import aio_pika

async def main():
    connection = await aio_pika.connect()
    channel = await connection.channel()
    queue = await channel.declare_queue("async-hello", auto_delete=True)

    await channel.default_exchange.publish(
        aio_pika.Message(body="hello".encode()),
        routing_key="async-hello"
    )

if __name__ == "__main__":
    asyncio.run(main())
