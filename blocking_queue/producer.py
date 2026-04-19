import time
from BlockingQueue import BlockingQueue

def main():
    queue=BlockingQueue()
    print("Worker is processing something...")
    queue.signal_event("session_create_done", "OK")

if __name__=='__main__':
    main()

