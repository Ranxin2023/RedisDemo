# NoSQL
## Table Of Contents
- [Common NoSQL](#common-nosql)
- [Key-Value Store](#1-key-value-store)
- [Column Family Database](#2-column-family-database)
- [Comparison Summary](#comparison-summary)
## Common NoSQL
| Category                | Examples                                            | Typical Use Cases                                              | Data Model                                                            | Advantages                                                                        | Disadvantages                                                                            |
| ----------------------- | --------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Key-Value Store**     | Tokyo Cabinet, Tyrant, Redis, Voldemort, Oracle BDB | Content caching, high-concurrency data access, logging systems | Data stored as key-value pairs, usually implemented using hash tables | Very fast lookup speed                                                            | Poorly structured data, usually treated as strings or binary blobs                       |
| **Column-Family Store** | Cassandra, HBase, Riak                              | Distributed file systems, large-scale distributed storage      | Data stored by columns; related column data grouped together          | Fast queries, highly scalable, easier distributed expansion                       | Limited functionality compared with relational databases                                 |
| **Document Database**   | CouchDB, MongoDB                                    | Web applications; values are structured documents              | Key-value pairs where the value is structured document data           | Flexible schema, no need for predefined table structures                          | Query performance may be lower; lacks unified query language                             |
| **Graph Database**      | Neo4J, InfoGrid, Infinite Graph                     | Social networks, recommendation systems, knowledge graphs      | Graph structure (nodes + edges)                                       | Excellent for relationship-based queries (shortest path, multi-hop relationships) | Some operations require scanning large parts of the graph; difficult distributed scaling |


## 1. Key-Value Store
### Core Idea
- Key-Value databases are the simplest type of NoSQL database.
- They work exactly like a giant dictionary or hashmap:
- Example:
```json
"user123" : "John"
```
or
```json
"session_abc" : "{token: xyz}"
```
### Common Use Cases
**1. Cache Systems**
- Example:

    - user session cache
    - API response cache
    - webpage cache

- Example with Redis:
```python
SET user:1001 "Ranxin"
GET user:1001
```
**2. Real-Time Counters**
- Example:
    - likes
    - views
    - online users
- Redis is commonly used because increment operations are extremely fast.

**3. Session Storage**
- Websites store login sessions:
```
session_id -> user_info
```

### Advantages
- **Extremely Fast**
    - Often faster than relational databases.
- **Easy Horizontal Scaling**
    - Can distribute keys across servers.
- **Simple Design**
    - Easy to implement and maintain.
### Disadvantages
- 
## 2. Column-Family Database
### Core Idea
### Why “Column Family”
- Related columns are grouped into “families”.
- Example:
- Another family:
```
UserActivity:
    last_login
    clicks
```

## 4. Graph Database
### Examples:
- Neo4J
- InfiniteGraph

### Core Idea
- Graph databases focus on relationships.
- They store:
    - Nodes (entities)
    - Edges (relationships)
- Example:
```
Alice --friend--> Bob
Bob --friend--> Charlie
```

### Why Graph Databases Exist
### Typical Applications
#### 1. Social Networks
- Facebook-like systems:
    - friends
    - followers
    - recommendations
#### 2. Recommendation Systems
```
Users who liked X also liked Y
```
#### 3. Knowledge Graphs
- Google Knowledge Graph.

#### 4. Fraud Detection
- Banking relationship analysis.

### Advantages
- Extremely Good Relationship Queries
    - Example:
        - shortest path
        - mutual friends
        - multi-hop connections
- Natural Representation
    - Many real-world systems are relationship-based.
### Disadvantages
- Hard Distributed Scaling
    - Graphs are highly connected.
    - Splitting across servers is difficult.
- Some Queries Can Be Expensive
    - Large graph traversals may consume huge resources.

## Comparison Summary
| **Database Type** | **Best At**          | **Worst At**                         |
| ------------- | ------------------------ | ------------------------------------ |
| Key-Value     | Ultra-fast lookup/cache  | Complex queries                      |
| Column-Family | Massive distributed data | Transactions/joins                   |
| Document      | Flexible web app data    | Heavy relational analysis            |
| Graph         | Relationship analysis    | Large-scale distributed partitioning |


## How To Choose
### Use Key-Value When You Need
- cache
- sessions
- ultra-fast reads/writes

### Use Column-Family When
- big data
- distributed systems
- time-series storage

### Use Document DB When
- flexible schemas
- 