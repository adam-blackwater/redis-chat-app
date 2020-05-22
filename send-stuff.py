import redis

r = redis.Redis()

go = True

while go:

    message = input()

    r.lpush('general-history', message)

    r.publish('general-chat', message)
    if message == 'stop':
        go = False 

