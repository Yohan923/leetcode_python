"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations
: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?
"""


class Node:

    def __init__(self, key=None, val=None, pre=None, post=None):
        self.key = key
        self.val = val
        self.post = pre
        self.pre = post


class DLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.post = self.tail
        self.tail.pre = self.head

    def add_node(self, node):
        node.pre = self.head
        node.post = self.head.post

        self.head.post.pre = node
        self.head.post = node

    def remove(self, node):
        pre = node.pre
        post = node.post

        pre.post = post
        post.pre = pre

    def move_to_head(self,node):
        self.remove(node)
        self.add_node(node)

    def pop(self):
        res = self.tail.pre
        self.remove(res)
        return res


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = DLinkedList()
        self.count = 0
        self.capacity = capacity
        self.cache_dict = dict()

    def get(self, key: int) -> int:
        node = self.cache_dict.get(key)
        if not node:
            return -1

        self.cache.move_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache_dict.get(key)

        if not node:
            new_node = Node()
            new_node.key = key
            new_node.val = value

            self.cache_dict[key] = new_node
            self.cache.add_node(new_node)

            self.count += 1

            if self.count > self.capacity:
                tail = self.cache.pop()
                self.cache_dict.pop(tail.key)
                self.count -= 1
        else:
            node.val = value
            self.cache.move_to_head(node)


if __name__ == '__main__':
    test = LRUCache(2)
    test.put(1, 1)
    test.put(2, 2)
    test.get(1)
    test.put(3, 3)
    test.get(2)
    test.put(4, 4)
    test.get(1)
    test.get(3)
    test.get(4)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
