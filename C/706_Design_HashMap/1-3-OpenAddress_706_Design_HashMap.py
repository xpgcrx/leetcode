# Open Address(Linear Probing) Collision Handling
class MyHashMap:

    def __init__(self):
        self.initial_size = 1000
        self.buckets = [None] * self.initial_size

    def _hash(self, key):
        return key % self.initial_size

    def _find_slot(self, key, for_insert=False):
        index = self._hash(key)
        while True:
            if self.buckets[index] is None:
                if for_insert:
                    return index
                else:
                    return -1
            elif self.buckets[index][0] == key:
                return index
            index = (index + 1) % self.initial_size

    def put(self, key: int, value: int) -> None:
        index = self._find_slot(key, for_insert=True)
        self.buckets[index] = [key, value]

    def get(self, key: int) -> int:
        index = self._find_slot(key)
        if index != -1:
            return self.buckets[index][1]
        return -1

    def remove(self, key: int) -> None:
        index = self._find_slot(key)
        if index != -1:
            self.buckets[index] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
