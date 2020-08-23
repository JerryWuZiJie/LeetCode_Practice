"""
# Java
# interesting recursion example, but will modify the original lists
public ListNode mergeTwoLists(ListNode l1, ListNode l2){
    if(l1 == null) return l2;
    if(l2 == null) return l1;
    if(l1.val < l2.val){
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    } else{
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
}
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        p = dummy

        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                p.next = ListNode(l2.val)
                p = p.next
                l2 = l2.next
            else:
                p.next = ListNode(l1.val)
                p = p.next
                l1 = l1.next

        while l1 is not None:
            p.next = ListNode(l1.val)
            p = p.next
            l1 = l1.next
        while l2 is not None:
            p.next = ListNode(l2.val)
            p = p.next
            l2 = l2.next

        return dummy.next
