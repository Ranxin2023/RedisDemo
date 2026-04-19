import json
import redis
from typing import Optional, Any

class RedisClient:
    def __init__(self, host="localhost", port=6379, db=0):
        self.redis=redis.Redis(
            host=host, 
            port=port,
            db=db,
            decode_responses=True,
        )

    # --------------------------Pub/Sub-----------------------
    def publish(self, channel:str, message: dict)->None:
        self.redis.publish(channel, json.dumps(message))
        print()

    def subscribe(self, channel:str):
        pubsub=self.redis.pubsub()
        pubsub.subscribe(channel)
        print("f[subscribe] listening on channel={channel}")
        return pubsub

    # ------------------------ Blocking Queue ------------------------------
    def signal_event(self, queue_name:str, value:dict)->None:
        self.redis.lpush(queue_name, json.dumps(value))
        print("")

    def wait_for_event(self, queue_name: str, timeout: Optional[int]=0)->Optional[dict]:
        result=self.redis.blpop(queue_name, timeout=timeout)
        if result is None:
            print(f"[wait_for_event] timeout, queue={queue_name}")
            return None
        _, raw_value=result
        value=json.loads(raw_value)
        print(f"[wiat_for_event] queue={queue_name}, value={value}")
        return value
    
    def set_data(self, key:str, value:Any)->None:
        self.redis.set(key, json.dumps(value))
        print(f"[wait_for_event] key={key}, value={value}")

    def get_data(self, key:str)->Optional[Any]:
        raw=self.redis.get(key)
        if raw is None:
            return None
        value=json.loads(raw)
        print(f"[get_data] key={key}, value={value}")
        return value