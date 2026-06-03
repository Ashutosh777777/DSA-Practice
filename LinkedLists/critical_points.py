"""
Problem: Find the Minimum and Maximum Number of Nodes Between Critical Points
Platform: LeetCode
Link: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
Approach: Linked List / Critical Points
Time Complexity: O(n)
Space Complexity: O(k)
"""

from typing import Optional, List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        p1 = head

        p2 = head.next

        if not p1 or not p2 or not p2.next:
            return [-1, -1]

        c = 2

        a = []

        while p2.next:

            if p1.val < p2.val and p2.val > p2.next.val:
                a.append(c)

            elif p1.val > p2.val and p2.val < p2.next.val:
                a.append(c)

            p1 = p1.next
            p2 = p2.next
            c += 1

        if len(a) < 2:
            return [-1, -1]

        min_dist = float('inf')

        for i in range(1, len(a)):
            min_dist = min(min_dist, a[i] - a[i - 1])

        max_dist = a[-1] - a[0]

        return [min_dist, max_dist]


# A critical point is either a local maximum or a local minimum.
# A node is a local maximum if its value is greater than both neighbouring nodes.
# A node is a local minimum if its value is smaller than both neighbouring nodes.
# Use two pointers p1 and p2 to compare previous, current, and next nodes.
# Store the positions of all critical points in array a.
# If there are fewer than two critical points, return [-1, -1].
# Minimum distance is found between consecutive critical points.
# Maximum distance is found between the first and last critical points.
# Return [min_dist, max_dist].