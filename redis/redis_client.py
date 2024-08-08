import pickle

from absl import app
from absl import flags
from absl import logging

from redis_queue import RedisQueue

FLAGS = flags.FLAGS


def define_flags():
    flags.DEFINE_string("host", "localhost", "Host of redis server")
    flags.DEFINE_string("port", "6379", "Port of redis server")
    flags.DEFINE_string("key", "redis-key", "Key of redis")


def run(argv):
    del argv

    rq = RedisQueue(host=FLAGS.host, port=FLAGS.port)
    key = FLAGS.key

    size = rq.size(key)
    logging.info(f"Initail size of redis queue = {size}")

    empty = rq.is_empty(key)
    logging.info(f"Redis queue is empty = {empty}")

    push_result = rq.push(key, "request1")
    logging.info(f"Push result = {push_result}")
    push_result = rq.push(key, b"request2")
    logging.info(f"Push result = {push_result}")
    push_result = rq.push(key, 3)
    logging.info(f"Push result = {push_result}")
    push_result = rq.push(key, 4.0)
    logging.info(f"Push result = {push_result}")

    lrange_result = rq.lrange_key(key, 0, -1)
    logging.info(f"Get result = {lrange_result}")

    popped_key = rq.popleft(key)
    logging.info(f"Popleft result = {popped_key}")

    value = {
        "id": "test",
        "string_data": "data1",
        "bytes_data": b"data1",
        "integer_data": 3,
        "float_data": 4.0,
    }
    set_result = rq.set(popped_key, pickle.dumps(value))
    logging.info(f"Set result = {set_result}")

    get_result = rq.get(popped_key)
    logging.info(f"Get result = {get_result}")

    value = "string_data"
    set_result = rq.set(popped_key, value)
    logging.info(f"Set result = {set_result}")

    get_result = rq.get(popped_key)
    logging.info(f"Get result = {get_result}")

    value = 10000
    set_result = rq.set(popped_key, value)
    logging.info(f"Set result = {set_result}")

    get_result = rq.get(popped_key)
    logging.info(f"Get result = {get_result}")

    delete_result = rq.delete_key(key)
    logging.info(f"Delete result = {delete_result}")



if __name__ == "__main__":
    define_flags()
    app.run(run)
