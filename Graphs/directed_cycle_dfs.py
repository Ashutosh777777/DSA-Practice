"""
Problem: Cycle Detection in Directed Graph
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
Approach: DFS with Recursion Stack
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

class Solution:

    def isCyclic(self, V, edges):
        # code here

        def dfs(node, adj, vis, cur):

            vis[node] = 1
            cur[node] = 1

            for nbr in adj[node]:

                if not vis[nbr]:

                    if dfs(nbr, adj, vis, cur):
                        return True

                elif cur[nbr] == 1:
                    return True

            cur[node] = 0

            return False

        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)

        vis = [0] * V
        cur = [0] * V

        for i in range(V):

            if not vis[i]:

                if dfs(i, adj, vis, cur):
                    return True

        return False


# Build adjacency list for the directed graph.
# Use vis[] to mark permanently visited nodes.
# Use cur[] to track nodes in the current DFS path.
# If a neighbor is already in current path → cycle exists.
# Remove node from current path while backtracking.