# Separate Chaining Collision Handling
class MyHashMap:

    def __init__(self):
        self.initial_size = 1024
        self.bucket = [[] for _ in range(self.initial_size)]

    def _hash(self, key):
        return key % self.initial_size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for item in self.bucket[index]:
            # update
            if item[0] == key:
                item[1] = value
                return
        # insert
        self.bucket[index].append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        for item in self.bucket[index]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        for i, item in enumerate(self.bucket[index]):
            if item[0] == key:
                del self.bucket[index][i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
