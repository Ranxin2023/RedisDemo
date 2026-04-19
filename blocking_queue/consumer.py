from BlockingQueue import BlockingQueue 

def main():
    queue=BlockingQueue()
    print("API is waiting for worker result...")
    result=queue.wait_for_event("session_create_done", timeout=0)
    print("API received result", result)

if __name__=='__main__':
    main()