import sys
import time
import redis

r = redis.Redis()

p = r.pubsub()
p.subscribe('general-chat')

history = r.lrange('general-history', 0, 5)

for message in reversed(history):
    print(message, '\n')

while True:
    time.sleep(1.10)
    message = p.get_message()
    if message:
        if message['type'] == 'message':

            print(message['data'].decode())
