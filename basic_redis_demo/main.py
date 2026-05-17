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
    r.hset("user:1001", "name", "John")
    r.hset("user:1001", "age", 25)
    name=r.hget("user:1001", "name")
    print(f"name from hash demo user:1001 is {name}")
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