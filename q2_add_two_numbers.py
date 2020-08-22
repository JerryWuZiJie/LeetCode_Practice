# one way linkedlist, so have to do everything before going to next node
"""
When you need to do operation after while loop, use
	Pre-operation with first node
	While ListNode.next is not None:
		ListNode = ListNode.next
		operation
	other operation
If not, use
	While ListNode is not None:
		Operation
        ListNode = ListNode.next
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # adding l2 val to l1 val, carry to store carry
        head = l1
        temp = l1.val + l2.val
        l1.val = temp % 10
        carry = temp // 10
        while l1.next is not None and l2.next is not None:
            l1 = l1.next
            l2 = l2.next
            temp = l1.val + l2.val + carry
            l1.val = temp % 10
            carry = temp // 10

        # if l1 left, add carry and return
        while l1.next is not None:  # then l2.next must be None
            if carry == 0:
                return head
            l1 = l1.next
            temp = l1.val + carry
            l1.val = temp % 10
            carry = temp // 10

        # if l2 left, append and add carry
        while l2.next is not None:
            l2 = l2.next
            temp = l2.val + carry
            l1.next = ListNode(temp % 10)
            carry = temp // 10
            l1 = l1.next

        # add carry
        if carry != 0:
            l1.next = ListNode(carry)

        return head


# java implementation, less checking, shorter code
'''
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;
    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;
        int y = (q != null) ? q.val : 0;
        int sum = carry + x + y;
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (p != null) p = p.next;
        if (q != null) q = q.next;
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;
}
'''

# Interesting: recursive
# implementation
'''
def addTwoNumbers(self, l1, l2, c=0):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    val = l1.val + l2.val + c
    c = val // 10
    ret = ListNode(val % 10)

    if (l1.next != None or l2.next != None or c != 0):
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        ret.next = self.addTwoNumbers(l1.next, l2.next, c)
    return ret
'''
