from ds import MultiLevelListNode

"""
Definition of MultiLevelListNode:
class MultiLevelListNode:
    def __init__(self, val=None, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child
"""


def flatten_multi_level_list(head: MultiLevelListNode) -> MultiLevelListNode:
    if head is None:
        return head

    cur = head
    tail = get_tail(head)

    while cur is not None:
        if cur.child is not None:
            tail.next = cur.child
            cur.child = None
            tail = get_tail(tail)
        cur = cur.next
    return head


def get_tail(node: MultiLevelListNode) -> MultiLevelListNode:
    while node.next is not None:
        node = node.next
    return node
