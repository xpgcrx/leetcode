class DoublyLinkedListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next: DoublyLinkedListNode = None
        self.prev: DoublyLinkedListNode = None


# Space: O(n)
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap: dict[int, DoublyLinkedListNode] = dict()
        self.head = DoublyLinkedListNode(
            -1, -1
        )  # the node just before the least recently used node
        self.tail = DoublyLinkedListNode(
            -1, -1
        )  # the node just after the most recently used node
        self.head.next = self.tail
        self.tail.prev = self.head

    # Time: O(1)
    def get(self, key: int) -> int:
        if key in self.hashmap:
            self._move_node_to_end(self.hashmap[key])
            return self.hashmap[key].value
        return -1

    # Time: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._move_node_to_end(self.hashmap[key])
            self.hashmap[key].value = value
        else:
            if len(self.hashmap) == self.capacity:
                del self.hashmap[self.head.next.key]
                self._remove_node(self.head.next)

            new_node = DoublyLinkedListNode(key, value)
            self.hashmap[key] = new_node
            self._add_to_end(new_node)

    def _remove_node(self, node: DoublyLinkedListNode):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_end(self, node: DoublyLinkedListNode):
        prev_node = self.tail.prev

        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
        prev_node.next = node

    def _move_node_to_end(self, node: DoublyLinkedListNode):
        self._remove_node(node)
        self._add_to_end(node)
