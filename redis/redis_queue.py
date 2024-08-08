from typing import List

import redis


class RedisQueue(object):
    """
        Redis Lists are an ordered list, First In First Out Queue
        Redis List pushing new elements on the head (on the left) of the list.
        The max length of a list is 4,294,967,295
    """

    def __init__(self, **redis_kwargs):
        self.rq = redis.Redis(**redis_kwargs)

    def get_size(self, key):
        return self.rq.llen(key)

    def is_empty(self, key):
        return self.get_size(key) == 0

    def push(self, key, element):
        self.rq.rpush(key, element)

    def popleft(self, key, isBlocking=False, timeout=None) -> str:
        if isBlocking:
            element = self.rq.blpop(key, timeout=timeout)
        else:
            element = self.rq.lpop(key)
        return element

    def get(self, key) -> str:
        return self.rq.get(key)

    def set(self, key, data):
        return self.rq.set(key, data)

    def get_with_index(self, key, index):
        element = self.rq.lindex(key, index)
        return element

    def lrange_key(self, key, start, end) -> List[str]:
        keys = self.rq.lrange(key, start, end)
        return keys

    def get_keys_with_pattern(self, pattern) -> List[str]:
        keys = self.rq.keys(pattern)
        return keys

    def delete_element_in_keys(self, key, element, count=0):
        return self.rq.lrem(key, count, element)
