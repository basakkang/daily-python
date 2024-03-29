import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print(" [x] received %r" % body)

    channel.basic_consume(
        queue="hello",
        auto_ack=True,
        on_message_callback=callback
    )

    channel.start_consuming()

if __name__ == "__main__":
    main()
