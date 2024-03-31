# This is not HashMap, but this passes tests
class MyHashMap:

    def __init__(self):
        self.elements = []

    def put(self, key: int, value: int) -> None:
        for element in self.elements:
            k = element[0]
            if k == key:
                element[1] = value
                return
        self.elements.append([key, value])

    def get(self, key: int) -> int:
        for element in self.elements:
            k = element[0]
            if k == key:
                return element[1]
        return -1

    def remove(self, key: int) -> None:
        for i, element in enumerate(self.elements):
            k = element[0]
            if k == key:
                self.elements.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
