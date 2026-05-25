"""
Problem: Longest Cycle in a Graph
Platform: LeetCode
Link: https://leetcode.com/problems/longest-cycle-in-a-graph/
Approach: DFS with Path Depth Tracking
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):

    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """

        ans = -1
        n = len(edges)

        vis = [0] * n
        path = [0] * n

        def dfs(node, depth):
            nonlocal ans

            vis[node] = 1
            path[node] = depth

            nbr = edges[node]

            if nbr != -1:

                if not vis[nbr]:
                    dfs(nbr, depth + 1)

                elif path[nbr] != 0:
                    ans = max(ans, depth - path[nbr] + 1)

            path[node] = 0

        for i in range(n):

            if not vis[i]:
                dfs(i, 1)

        return ans


# Each node has at most one outgoing edge.
# vis[] marks nodes that are already visited globally.
# path[] stores depth of nodes in the current DFS path.
# If a neighbor is already in current path, a cycle is found.
# Cycle length = current depth - neighbor depth + 1.
# Backtrack by removing node from current DFS path.