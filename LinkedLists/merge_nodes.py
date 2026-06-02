"""
Problem: Merge Nodes in Between Zeros
Platform: LeetCode
Link: https://leetcode.com/problems/merge-nodes-in-between-zeros/
Approach: Linked List / Prefix Sum
Time Complexity: O(n)
Space Complexity: O(k)
"""

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)

        tail = dummy

        cur = head.next

        s = 0

        while cur:

            if cur.val == 0:
                tail.next = ListNode(s)
                tail = tail.next
                s = 0

            else:
                s += cur.val

            cur = cur.next

        return dummy.next


# Skip the first zero because it only marks the start of the list.
# Use cur to traverse the linked list.
# Keep adding node values into s until another zero is found.
# Whenever a zero is found, create a new node with the current sum.
# Attach this new node to the answer list using tail.
# Reset the sum to 0 for the next segment.
# Finally, return dummy.next as the head of the merged linked list.