from redis_connection import r
def rdb_demo():
    # clear database
    r.flushdb()

    # add data
    r.set("name", "John")
    r.set("city", "Davis")

    print(r.keys("*"))

    # force RDB save
    r.save()

    print("RDB snapshot created.")

