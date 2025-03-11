from collections import OrderedDict


# Space: O(n)
class LRUCache:
    def __init__(self, capacity: int):
        self.datas = OrderedDict()
        self.capacity = capacity

    # Time: O(1)
    def get(self, key: int) -> int:
        if key in self.datas:
            self.datas.move_to_end(key)
            return self.datas[key]
        return -1

    # Time: O(1)
    def put(self, key: int, value: int) -> None:
        if len(self.datas) == self.capacity:
            self.datas.popitem(last=False)
        elif key in self.datas:
            self.datas.move_to_end(key)
        self.datas[key] = value
