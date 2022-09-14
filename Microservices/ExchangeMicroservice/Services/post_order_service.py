import pika
import json
import os

def post_order(order=None):
    host = os.getenv("RABBIT_MQ_HOST", 'localhost')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    order_dictionary = order
    channel = connection.channel()
    channel.exchange_declare(exchange="monty.exchange",
                             exchange_type="direct")

    channel.queue_declare(queue="monty-queue",
                          durable=True)

    channel.queue_bind(exchange="monty.exchange",
                       queue="monty-queue",
                       routing_key="message")

    channel.basic_publish(exchange='monty.exchange',
                          routing_key='message',
                          body=json.dumps(order_dictionary))

    print(" [x] Sent order")
    connection.close()

    return {"Message": "Order Posted Successfully"}, 201
