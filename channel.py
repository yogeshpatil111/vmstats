import pika
import ConfigParser
import base64
import os

config_path = "vm.config"

channel_host = 'localhost'
exchange_name = "vmstats"
username = "guest"
password = "guest"

def get_config():
    global channel_host
    global username
    global password
    
    if os.path.exists(config_path):
        config = ConfigParser.ConfigParser()
        config.read(config_path)
        
        if config.has_section("channel"):
            for option in config.options("channel"):
                if "host" == option:
                    channel_host = config.get("channel", "host")
                if "username" == option:
                    username = config.get("channel", "username")
                if "password" == option:
                    username = config.get("channel", "password")

get_config()

"""
Create initial exchange for Communication with Hypervisors.
"""
def createChannel():
    credentials = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_host,credentials=credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange_name,durable=True,
                     type='fanout')
    connection.close()

"""
Publish Messages on the exchange
"""
def publishMessage(message):
    credentials = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_host,credentials=credentials))
    channel = connection.channel() 

    channel.basic_publish(exchange=exchange_name,
                  routing_key='',
                  body=message)
    connection.close()

"""
Start listening on the Queues for incoming messages
"""
def listenChannel(queue_name, callback):
    credentials = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_host,credentials=credentials))
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
    credentials = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=channel_host,credentials=credentials))
    channel = connection.channel()

    result = channel.queue_declare(queue=queue_name,durable=True)

    channel.queue_bind(exchange=exchange_name,
                       queue=queue_name)
    
    
    connection.close()
