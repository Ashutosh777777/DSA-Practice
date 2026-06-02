"""
Problem: Reverse Odd Levels of Binary Tree
Platform: LeetCode
Link: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
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

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = deque([root])

        flag = False

        while q:

            level = []

            for _ in range(len(q)):

                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                level.append(node)

            i = 0
            j = len(level) - 1

            if flag:

                while i < j:
                    level[i].val, level[j].val = level[j].val, level[i].val
                    i += 1
                    j -= 1

            flag = not flag

        return root


# Use BFS to traverse the tree level by level.
# Store all nodes of the current level in an array.
# Use a flag to identify odd levels.
# For odd levels, reverse the node values using two pointers.
# Swap only the values, not the actual tree nodes.
# Finally, return the original root because the tree is modified in-place.