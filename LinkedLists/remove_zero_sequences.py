"""
Problem: Remove Zero Sum Consecutive Nodes from Linked List
Platform: LeetCode
Link: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
Approach: Prefix Sum + Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prefix = 0
        cur = dummy
        m = {}

        while cur:
            prefix += cur.val
            m[prefix] = cur
            cur = cur.next

        prefix = 0
        cur = dummy

        while cur:
            prefix += cur.val
            cur.next = m[prefix].next
            cur = cur.next

        return dummy.next


# Use prefix sum to detect zero-sum sublists.
# If same prefix sum appears again, nodes between them sum to zero.
# First pass stores the latest node for every prefix sum.
# Second pass skips all zero-sum ranges using stored latest nodes.
# Dummy node handles deletion from the head cleanly.