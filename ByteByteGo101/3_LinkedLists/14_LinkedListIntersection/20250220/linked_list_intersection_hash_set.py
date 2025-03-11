from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


# Time: O(n + m)
# Space: O(n)
def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode:
    node_hash = set()
    cur = head_A
    while cur:
        node_hash.add(id(cur))
        cur = cur.next

    cur = head_B
    while cur:
        if id(cur) in node_hash:
            return cur
        cur = cur.next
    return None
