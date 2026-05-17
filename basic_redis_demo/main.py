import redis
r = redis.Redis(
        host='localhost',
        port=6379,
        decode_responses=True
    )
def string_demo():
    print("-------redis string demo-------")
    r.set("message", "hello")
    r.append("message", "world")
    print(r.get("message"))

def mset_demo():
    print("-------mset demo------")
    r.mset({
        "name":"John",
        "age":25,
        "city":"Davis"
    })
    values=r.mget("name", "age", "city")
    print(f"Values get from mset is {values}")

def hash_demo():
    print("-------hash demo--------")
    # user_data={"name":"John", "age":"25", "city":"Davis"}
    # , "age":"25", "city":"Davis"
    r.hset(name="user:1002", mapping={"name":"John"})
    r.hset(name="user:1002", mapping={"age":25})
    r.hset(name="user:1002", mapping={"city":"Davis"})
    user=r.hgetall("user:1002")
    print(f"user in hash demo is {user}")
    r.hset("user:1002", "age", 26)
    r.hset("user:1002", "score", 100)
    r.hincrby("user:1002", "score", 10)
    score=r.hget("user:1002", "score")
    name=r.hget("user:1002", "name")
    print(f"name from hash demo user:1002 is {name} with score of {score}")

def main():

    r.set("name", "John")

    print(r.get("name"))
    r.delete("name")
    print(r.exists("name"))
    r.lpush("tasks", "task1")
    r.lpush("tasks", "task2")
    r.set("views", 0)

    r.incr("views")

    print(r.get("views"))
    print(r.rpop("tasks"))
    r.hset("user:1", "name", "Tom")
    print(r.hget("user:1", "name"))
    print(r.hgetall("user:1"))

if __name__=='__main__':
    # string_demo()
    # mset_demo()
    hash_demo()
    # main()