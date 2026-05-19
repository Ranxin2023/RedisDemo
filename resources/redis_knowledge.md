# Redis Basic Knowledge
## Table of Contents
- [Redis Persistence Mechanisms](#redis-persistence-mechanisms)
## Redis Persistence Mechanisms
### 1. RDB (Redis Database Snapshot)
#### Concept
- RDB works by creating **point-in-time snapshots** of the Redis memory data.
- Redis periodically saves the entire dataset into a binary file:
```
dump.rdb
```
- This file contains a snapshot of all Redis data at a specific moment.

#### How RDB Works
#### Advantages of RDB
- Very fast recovery
- Compact binary file
    - RDB files are compressed and efficient.
- Good for backups
    - Easy to copy and archive.
#### Disadvantages of RDB
- Possible data loss
### RDB Demo
```python
import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

# clear database
r.flushdb()

# add data
r.set("name", "John")
r.set("city", "Davis")

print(r.keys("*"))

# force RDB save
r.save()

print("RDB snapshot created.")
```

### 2. AOF (Append Only File)
#### Concept
- AOF logs: **every write command** that modifies Redis data.

-  Example:
```redis
SET name John
SET age 25
HSET user city Davis
```

- These commands are appended into:`appendonly.aof`
- When Redis restarts:
    - it replays all commands
    - reconstructs the dataset

#### How AOF Works
- Enable AOF:
```config
appendonly yes
```
#### AOF Sync Policies
```conf
appendfsync always
```
#### Advantages of AOF
- Better durability
    - Usually loses at most:**1 second of data**
- Human-readable log
    - You can inspect commands.

