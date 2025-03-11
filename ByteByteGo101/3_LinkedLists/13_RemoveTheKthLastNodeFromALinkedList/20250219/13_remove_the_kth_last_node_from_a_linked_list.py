from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


# Time:O(n)
# Space:O(1)
def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    leader = trailer = dummy
    for _ in range(k):
        leader = leader.next
        if not leader:
            return head

    while leader.next:
        leader = leader.next
        trailer = trailer.next
    trailer.next = trailer.next.next
    return dummy.next
