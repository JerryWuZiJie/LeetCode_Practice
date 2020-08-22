# two pointers (in fact not necessary)
"""
two approach:
1: run through the list and store the length
2: keep track of the last nth node and remove it (save some while checks but almost the same)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # use a pointer to always point at the last nth node
        dummy = p = p2 = ListNode(0, head)

        # keep track of last nth node
        for _ in range(n):
            # p.next will exist otherwise there's input error
            p = p.next

        while p.next is not None:
            p = p.next
            p2 = p2.next

        p2.next = p2.next.next

        return dummy.next
