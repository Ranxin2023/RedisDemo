import redis
import json

class RedisSubscriber:
    def __init__(self):
        self.redis=redis.Redis(host='localhost', port=6379, db=0)
        self.pubsub=self.redis.pubsub()
    
    def start(self):
        self.pubsub.subscribe("input_audio_stream")
        print("Listening on channel: input_audio_stream")
        for message in self.pubsub.listen():
            pass

    def handle_message(self, raw_data):
        data=json.loads(raw_data)
        print(f"Received, {data}")
        # simulate worker
        result=data["data"].upper()
        print(f"Processed result:{result}")

