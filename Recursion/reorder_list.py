"""
Problem: Reorder List
Platform: LeetCode
Link: https://leetcode.com/problems/reorder-list/
Approach: Recursion with two pointers (front pointer + backtracking)
Time Complexity: O(n) since each node is processed once
Space Complexity: O(n) due to recursion stack
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """        
        self.front = head
        
        def rec(curr):
            if not curr:
                return
            
            rec(curr.next)
            
            if not self.front:
                return
            if self.front == curr:
                curr.next = None
                self.front = None
                return
            if self.front.next == curr:
                curr.next = None
                self.front.next = curr
                self.front = None
                return 
            temp = self.front.next
            self.front.next = curr
            curr.next = temp
            
            self.front = temp
        
        rec(head)
        
        
        
# Use recursion to reach the end of the list while maintaining a global front pointer from the start.
# On backtracking, insert the current (end) node after the front node and move front forward.
# Handle stopping conditions when pointers meet or cross to avoid cycles and terminate the list.
# Achieves reordering in O(n) time with O(n) recursion space, avoiding repeated traversal.