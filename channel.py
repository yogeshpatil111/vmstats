import pika

channel_host = 'localhost'
exchange_name = "vmstats"


"""
Create initial exchange for Communication with Hypervisors.
"""
def createChannel():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_host))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange_name,durable=True,
                     type='fanout')
    connection.close()

"""
Publish Messages on the exchange
"""
def publishMessage(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_host))
    channel = connection.channel() 

    channel.basic_publish(exchange=exchange_name,
                  routing_key='',
                  body=message)
    connection.close()

"""
Start listening on the Queues for incoming messages
"""
def listenChannel(queue_name, callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_host))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange_name,durable=True,
                         type='fanout')

    result = channel.queue_declare(queue=queue_name,durable=True)

    channel.queue_bind(exchange=exchange_name,
                       queue=queue_name) 

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)

    channel.start_consuming()

"""
Create initial Queues on the fanout Exchange for listening Message
"""
def subscribeChannel(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_host))
    channel = connection.channel()

    result = channel.queue_declare(queue=queue_name,durable=True)

    channel.queue_bind(exchange=exchange_name,
                       queue=queue_name)
    
    
    connection.close()
