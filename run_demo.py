import threading
import time
from api import DemoAPI
from worker import DemoWorker

def run_worker():
    worker=DemoWorker()
    worker.start()

def run_api():
    time.sleep(1)
    api=DemoAPI()
    api.create_session_task("Hello redis project")

if __name__=='__main__':
    worker_thread=threading.Thread(target=run_worker, demon=True)
    api_thread=threading.Thread(target=run_api)

    worker_thread.start()
    api_thread.start()
    api_thread.join()