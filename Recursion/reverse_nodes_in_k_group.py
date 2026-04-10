"""
Problem: Reverse Nodes in k-Group
Platform: LeetCode
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
Approach: Recursion + in-place reversal
Time Complexity: O(n)
Space Complexity: O(n/k) recursion stack
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        
				
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
		
        head.next = self.reverseKGroup(curr, k)
        return prev
    
# Check if at least k nodes exist; if not, return head as-is.
# Reverse the first k nodes using standard linked list reversal.
# Recursively process the remaining list from the (k+1)th node.
# Connect the reversed group with the result of recursive call.