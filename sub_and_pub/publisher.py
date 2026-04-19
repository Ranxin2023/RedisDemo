import redis
import json

class RedisPublisher:
    def __init__(self):
        self.redis=redis.Redis(host='localhost', port=6379, db=0)
    
    def publish(self, channel, message):
        self.redis.publish(channel, json.jumps(message))
        print(f"[Publisher]Send to {channel}:{message}")