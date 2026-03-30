"""
Problem: Swap nodes in pairs
Platform: LeetCode
Link: https://leetcode.com/problems/swap-nodes-in-pairs/
Approach: Recursion and linked list manipulation
Time Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        a = head
        b = head.next
        
        a.next = self.swapPairs(b.next)
        
        b.next = a
        
        return b