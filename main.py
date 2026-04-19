import redis
import threading
import time
from api import DemoAPI
from worker import DemoWorker
from sub_and_pub.run_publisher_subscriber import run_subscriber, run_publisher
def basic_redis_operations():
    r=redis.Redis(host='localhost', port=6379, db=0)
    r.set("name", "Alice")
    value=r.get("name")
    print(f"Value from Redis: {value}")

def subscriber_and_puboisher_demo():
    t1=threading.Thread(target=run_subscriber)
    t1.start()
    # start publisher(simulate frontend)
    t2=threading.Thread(target=run_publisher)
    t2.start()

def run_worker():
    worker=DemoWorker()
    worker.start()
    
def run_api():
    time.sleep(1)
    api=DemoAPI()
    api.create_session_task("hello redis project")
    
def complex_demo():
    worker_thread=threading.Thread(target=run_worker, daemon=True)
    api_thread=threading.Thread(target=run_api)

    worker_thread.start()
    api_thread.start()

    api_thread.join()
    print("Complex Demo Completed")

def main():
    # basic_redis_operations()
    complex_demo()

if __name__=="__main__":
    main()