"""
Problem: Number of Operations to Make Network Connected
Platform: LeetCode
Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
Approach: DFS / Connected Components
Time Complexity: O(n + e)
Space Complexity: O(n + e)
"""

from typing import List

class Solution:

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        adj = [[] for _ in range(n)]

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(src):

            visited[src] = True

            for nbr in adj[src]:

                if not visited[nbr]:
                    dfs(nbr)

        components = 0

        for i in range(n):

            if not visited[i]:
                dfs(i)
                components += 1

        return components - 1


# At least n - 1 cables are needed to connect n computers.
# If connections are fewer than n - 1, connection is impossible.
# Build an undirected graph using given connections.
# Count connected components using DFS.
# To connect k components, we need k - 1 operations.