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
- 