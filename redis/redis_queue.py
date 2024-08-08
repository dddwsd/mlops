from typing import List, Union

import redis


class RedisQueue(object):
    """
        Redis Lists are an ordered list, First In First Out Queue
        Redis List pushing new values on the head (on the left) of the list.
        The max length of a list is 4,294,967,295

        https://redis-py.readthedocs.io/en/stable/commands.html#redis.commands
    """

    def __init__(self, **redis_kwargs):
        self.rq = redis.Redis(**redis_kwargs)

    def size(self, key: str) -> int:
        """Get size of key.

        Args:
            key (str): Redis key

        Returns:
            int: The number of value in key
        """
        return self.rq.llen(key)

    def is_empty(self, key: str) -> bool:
        """Get the key is empty.

        Args:
            key (str): Redis key

        Returns:
            bool: The status about key is empty or not
        """
        return self.size(key) == 0

    def push(self, key: str, value: Union[bytes, str, int, float]) -> int:
        """Push value to key.

        Args:
            key (str): Redis key
            value (Union[bytes, str, int, float]): The value accumulated on the
                key

        Returns:
            int: The number of value in key
        """
        return self.rq.rpush(key, value)

    def popleft(self, key: str, isBlocking=False, timeout=None) -> bytes:
        """Pop a value from the left of the key.

        Args:
            key (str): Redis key
            isBlocking (bool, optional): Whether the pop operation should be
                blocking or not.
                Defaults to False.
            timeout (_type_, optional): Timeout duration when the key is empty
                and isBlocking is true.
                Defaults to None.

        Returns:
            bytes: In python3, even if push value as str, float, or int, return
                value is bytes.
        """
        if isBlocking:
            value = self.rq.blpop(key, timeout=timeout)
        else:
            value = self.rq.lpop(key)
        return value

    def lrange_key(self, key: str, start:int , end: int) -> List[bytes]:
        """Accumulated list of key.

        Args:
            key (str): Redis key
            start (int): Start position of list
            end (int): End position of list

        Returns:
            List[bytes]: In python3, even if push value as str, float, or int,
                return value is bytes.
        """
        return self.rq.lrange(key, start, end)

    def get(self, key: str) -> bytes:
        """Get value of key.

        Args:
            key (str): Redis key

        Returns:
            bytes: In python3, even if set data as str, float, or int,
                return value is bytes.
        """
        return self.rq.get(key)

    def set(self, key: str, data: Union[bytes, str, int, float]) -> bool:
        """Set data to value of key.

        Args:
            key (str): Redis key
            data (Union[bytes, str, int, float]): Value

        Returns:
            bool: Success or failure of the set operation
        """
        return self.rq.set(key, data)

    def delete_key(self, key: str) -> int:
        """Delete key in redis

        Args:
            key (str): Redis key

        Returns:
            int: The number of deleted key
        """
        return self.rq.delete(key)
