import redis
from typing import Optional

class BlockingQueue:
    def __init__(self, host="localhost", port=6379, db=0):
        self.redis=redis.Redis(host=host, port=port, db=db, decode_responses=True)
    
    def signal_event(self, queue_name: str, value:str)->None:
        '''
        append an event to queue
        equal to signal_event()
        '''
        self.redis.lpush(queue_name, value)
        print(f"[signal_event] pushed to {queue_name}:{value}")
    
    def wait_for_event(self, queue_name: str, timeout: Optional[int]=0)->Optional[str]:
        '''
        block to wait for one event
        timeout=0 means keep waiting
        timeout=5 means at most wait for 5 seconds
        similar to wait_for_event()
        '''
        result=self.redis.blpop(queue_name, timeout=timeout)
        if result is None:
            print(f"[wait_for_event] timeout on queue:{queue_name}")
            return None
        _, value=result
        print(f"[wait_for_event] got from {queue_name}:{value}")
        return value