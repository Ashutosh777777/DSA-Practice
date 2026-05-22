"""
Problem: Cycle Detection in Undirected Graph
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
Approach: DFS with Parent Tracking
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

class Solution:

    def isCycle(self, V, edges):
        # Code here

        def dfs(node, adj, visited, parent):

            visited[node] = True

            for nbr in adj[node]:

                if not visited[nbr]:

                    if dfs(nbr, adj, visited, node):
                        return True

                elif nbr != parent:
                    return True

            return False

        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V

        for i in range(V):

            if not visited[i]:

                if dfs(i, adj, visited, -1):
                    return True

        return False


# Build an adjacency list for the undirected graph.
# Use DFS to visit every connected component.
# Track parent to avoid counting the same edge as a cycle.
# If a visited neighbor is not the parent → cycle exists.
# Return False if no cycle is found in any component.