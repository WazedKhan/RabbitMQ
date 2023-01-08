import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
message = " ".join(sys.argv[1:]) or "Hello World"

channel.basic_publish(exchange="", routing_key="hello", body=message)

print("[x] Sent %r" %message)