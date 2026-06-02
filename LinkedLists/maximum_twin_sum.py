"""
Problem: Maximum Twin Sum of a Linked List
Platform: LeetCode
Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
Approach: Stack / Linked List
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def pairSum(self, head: Optional[ListNode]) -> int:

        n = 0

        cur = head

        while cur:
            n += 1
            cur = cur.next

        i = 0

        cur = head

        stack = []

        while i < n // 2:
            stack.append(cur.val)
            cur = cur.next
            i += 1

        m = 0

        while cur:
            m = max(m, cur.val + stack.pop())
            cur = cur.next

        return m


# Count the total number of nodes in the linked list.
# Store the values of the first half of the linked list in a stack.
# Start traversing from the second half of the linked list.
# For every node in the second half, pop one value from the stack.
# Add both values to calculate the twin sum.
# Keep track of the maximum twin sum found.
# Return the maximum twin sum.