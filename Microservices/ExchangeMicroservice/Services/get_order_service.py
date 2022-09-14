import json
import pika
import os
def get_order():
    host = os.getenv("RABBIT_MQ_HOST",'localhost')

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel = connection.channel()

    status = channel.queue_declare(queue="monty-queue",
                          durable=True)
    if status.method.message_count == 0:
        return {"Message": "There are no Available Messages to Consume."}, 200
    def callback(ch, method, properties, body):
        global response
        response = json.loads(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        channel.stop_consuming()


    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='monty-queue', on_message_callback=callback)

    print(' [*] Waiting for messages.')
    x = channel.start_consuming()
    channel.close()
    return response

