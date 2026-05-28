# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        c1 = l1
        c2 = l2
        sum = 0
        dummy = ListNode(0)
        cur = dummy
        # head = ListNode(0, None)
        while c1 or c2 or carry:
            sum = carry
            if c1:
                sum+=c1.val
                c1 = c1.next
            if c2:
                sum+=c2.val
                c2 = c2.next
            carry = sum//10
            cur.next = ListNode(sum%10)
            cur = cur.next
        return dummy.next