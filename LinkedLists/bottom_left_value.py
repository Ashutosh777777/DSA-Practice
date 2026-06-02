"""
Problem: Find Bottom Left Tree Value
Platform: LeetCode
Link: https://leetcode.com/problems/find-bottom-left-tree-value/
Approach: BFS / Level Order Traversal
Time Complexity: O(n)
Space Complexity: O(w)
"""

from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = deque([root])

        ans = root.val

        while q:

            level = []

            for _ in range(len(q)):

                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans = level[0]

        return ans


# Use BFS to traverse the tree level by level.
# For each level, store the node values in an array.
# The first value of every level is the leftmost value of that level.
# Keep updating ans with the first value of the current level.
# After BFS ends, ans will store the leftmost value of the bottom level.
# Return ans.