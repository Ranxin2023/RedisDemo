from sub_and_pub.subscriber import RedisSubscriber
from sub_and_pub.publisher import RedisPublisher
import time
def run_subscriber():
    sub = RedisSubscriber()
    sub.start()

def run_publisher():
    pub=RedisPublisher()
    while True:
        msg={
            "type": "audio",
            "data":"hello revia"
        }
        pub.publish("input_audio_stream", msg)
        time.sleep(3)