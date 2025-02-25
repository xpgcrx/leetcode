from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


# Time: O(n)
# Space: O(1)
def palindromic_linked_list(head: ListNode) -> bool:
    mid = find_middle(head)
    reversed_list_head = reverse_linked_list(mid)

    cur1 = head
    cur2 = reversed_list_head
    is_palindromic = True
    while cur2:
        if cur1.val != cur2.val:
            is_palindromic = False
        cur1 = cur1.next
        cur2 = cur2.next
    return is_palindromic


def find_middle(head: ListNode) -> ListNode:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse_linked_list(head: ListNode) -> ListNode:
    cur_node = head
    prev_node = None
    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node
    return prev_node
