# Redis Demo Project

A hands-on Redis learning and demo project built with Python.
This repository demonstrates core Redis data structures, persistence mechanisms, pub/sub messaging, blocking queues, and worker-based task processing.

## Table Of Contents
- [Introduction](#introduction)
    - [What is Redis](#what-is-redis)
    - [Why Redis is Fast](#why-redis-is-fast)
    - [Redis Data Structure](#redis-data-structures)
        - [String](#1-string)
        - [List](#2-list)
        - [Set](#3-set)
    - [Redis Common Use Cases](#redis-common-use-cases)
        - [Cache System](#1-cache-system)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
    - [Install Redis](#1-install-redis)
    - [Install Python Dependencies](#2-install-python-dependencies)
## Introduction
### What is Redis?
#### Redis Introduction

Redis is an **open-source in-memory NoSQL database** primarily used for:

- Caching
- Real-time applications
- Message queues
- Session storage
- Pub/Sub systems
- High-speed data access

Redis stands for:

- **REmote DIctionary Server**

Unlike traditional SQL databases such as MySQL or PostgreSQL, Redis stores most data directly in memory (RAM) instead of disk, making it extremely fast.
#### Why Redis is Fast
- Traditional databases:
```
Application → Disk → Database
```
- Redis:
```
Application → Memory (RAM)
```

- Memory access is much faster than disk access.
- Typical performance:

| **Database** | **Speed**        |
| -------- | ------------ |
| MySQL    | milliseconds |
| Redis    | microseconds |

### Redis Data Structures
#### **1. String**

```python
r.set("user:name", "John")
name = r.get("user:name")
```
#### **2. List**
- Ordered collection.
```redis
["task1", "task2", "task3"]
```
python:
```python
r.lpush("tasks", "task1")
r.lpush("tasks", "task2")
```
#### 3. Set
- Unordered unique collection.
```redis
{"python", "redis", "backend"}
```

### Redis Common Use Cases
#### 1. Cache System
- Most popular use case.
- Instead of querying a slow database repeatedly:
```
User → Redis Cache → Database
```
- Redis stores frequently used data in memory.
- Examples:
    - User profile cache
    - API response cache
    - Product cache
#### 2. Session Storage
- Websites store login sessions in Redis.
- Example:
```
session:abc123 → user_id:1001
```
#### 3. Message Queue
- Redis Lists can act as queues.
- Producer:
```python
r.lpush("queue", "task1")
```

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

## Redis Project Structure Demonstrated
### 1. Basic Redis Demo
- Location:
```bash
basic_redis_demo/
```
