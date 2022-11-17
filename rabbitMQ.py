import pika
from config import rabbitMQ_config

def send(body):
    connection = pika.BlockingConnection(pika.URLParameters(rabbitMQ_config["AMQP_URL"]))
    channel = connection.channel()

    channel.queue_declare(queue='ads')
    channel.basic_publish(exchange='', routing_key='ads', body=body)
    connection.close()


def main(callback):
    connection = pika.BlockingConnection(pika.URLParameters(rabbitMQ_config["AMQP_URL"]))
    channel = connection.channel()
    
    channel.queue_declare(queue='ads')
    channel.basic_consume(queue='ads', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    

