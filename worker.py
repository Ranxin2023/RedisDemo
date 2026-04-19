import json
import time
from redis_client import RedisClient
from message_types import ResultMessage

class DemoWorker:
    def __init__(self):
        self.redis=RedisClient()
        self.command_channel="command"

    def process_task(self, task:dict):
        request_id=task["request_id"]
        session_id=task["session_id"]
        task_type=task["task_type"]
        payload=task["payload"]

        print(f"\n[Worker] Received task: request_id={request_id}, task_type={task_type}")

        if task_type == "create_session":
            user_text=payload["user_text"]
            reply_queue=payload["reply_queue"]

            print(f"[Worker] Processing user_text={user_text}")
            time.sleep(3)

            session_key=f"session:{session_id}"
            session_data = {
                "session_id": session_id,
                "user_text": user_text,
                "state": "ready"
            }

            self.redis.set_data(session_key, session_data)
            result = ResultMessage(
                request_id=request_id, 
                session_id=session_id,
                status="success",
                result={
                    "message": f"Session create for: {user_text}",
                    "session_key": session_key
                }
            )
            self.redis.signal_event(reply_queue, result.to_dict())
        else:
            print(f"[Worker] Unknown task_type={task_type}")

    def start(self):
        pubsub=self.redis.subscribe(self.command_channel)
        for message in pubsub.listen():
            if message["type"]!="message":
                continue
            task=json.loads(message["data"])
            self.process_task(task)