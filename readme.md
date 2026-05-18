# Redis Demo Project
A hands-on Redis learning and demo project built with Python.
This repository demonstrates core Redis data structures, persistence mechanisms, pub/sub messaging, blocking queues, and worker-based task processing.

## Features

This project includes examples for:

- Redis Connection Setup
- Redis Strings
- Redis Sets
- Redis Persistence (RDB)
- Publisher / Subscriber Messaging
- Blocking Queue Processing
- Worker-based Task Consumption
- Simple Redis Client Wrapper
- API Integration Structure

## Project Structure
```bash
REDIS_DEMO/
│
├── basic_redis_demo/
│   ├── main.py
│   ├── rdb_demo.py
│   ├── redis_connection.py
│   └── set_demo.py
│
├── blocking_queue/
│   ├── BlockingQueue.py
│   ├── consumer.py
│   └── producer.py
│
├── resources/
│   ├── no_sql.md
│   └── redis_knowledge.md
│
├── sub_and_pub/
│   ├── publisher.py
│   ├── subscriber.py
│   └── run_publisher_subscriber.py
│
├── api.py
├── main.py
├── message_types.py
├── redis_client.py
├── run_demo.py
├── worker.py
└── .gitignore
```

## Getting Started
### 1. Install Redis
- **Windows**
    - Download Redis:
        - Official Microsoft Archive:
        - https://github.com/microsoftarchive/redis/releases

### 2. Install Python Dependencies
- Install required packages:
```bash
pip install redis
```
### 3. Start Redis Server
```bash
redis-server
```

- Test connection:
```bash
redis-cli ping
```