"""
Problem: Count Complete Tree Nodes
Platform: LeetCode
Link: https://leetcode.com/problems/count-complete-tree-nodes/
Approach: Optimized recursion using properties of Complete Binary Tree
Time Complexity: O(log^2 n)
Space Complexity: O(log n) recursion stack
"""
class Solution(object):
    def countNodes(self, root):
        l, r, h = root, root, 0
        while l and r:
            l, r, h = l.left, r.right, h + 1
        return 2**h - 1 if l == r else sum(map(self.countNodes, (root.left, root.right))) + 1

# Compare leftmost and rightmost heights to detect perfect subtree.
# If equal → nodes = 2^h - 1, else recurse on left and right.
# Uses Complete Binary Tree property to avoid full traversal.
# Overall complexity reduced to O(log^2 n).