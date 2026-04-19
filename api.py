import uuid
from redis_client import RedisClient
from message_types import TaskMessage

class DemoAPI:
    def __init__(self):
        self.redis=RedisClient()
        self.command_channel="command"

    def create_session_task(self, user_text:str):
        request_id=str(uuid.uuid4())
        session_id=str(uuid.uuid4())

        reply_queue=f"reply:{request_id}"
        task=TaskMessage(
            request_id=request_id,
            session_id=session_id,
            task_type="create_session",
            payload={
                "user_text": user_text,
                "reply_queue":reply_queue
            }
        )
        print("\n[API] Seding task to worker...")
        self.redis.publish(self.command_channel, task.to_dict())

        print("[API] Waiting for worker result...")
        result=self.redis.wait_for_event(reply_queue, timeout=10)
        if result is None:
            print("[API] Timeout: worker did not reply")
            return None
        
        