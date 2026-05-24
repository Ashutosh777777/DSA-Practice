"""
Problem: Eventual Safe States
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/eventual-safe-states/1
Approach: DFS with Recursion Stack
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

class Solution:

    def safeNodes(self, V, edges):
        # Code here

        def dfs(node, adj, vis, cur, safe):

            vis[node] = 1
            cur[node] = 1

            for nbr in adj[node]:

                if not vis[nbr]:

                    res = dfs(nbr, adj, vis, cur, safe)

                    if res:
                        return True

                else:

                    if cur[nbr] == 1:
                        return True

            cur[node] = 0
            safe[node] = 1

            return False

        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)

        vis = [0] * V
        cur = [0] * V
        safe = [0] * V

        ans = []

        for i in range(V):

            if not vis[i]:
                dfs(i, adj, vis, cur, safe)

        for i in range(V):

            if safe[i] == 1:
                ans.append(i)

        return ans


# Safe nodes are nodes that do not lead to any cycle.
# Use DFS and recursion stack to detect cycles in directed graph.
# cur[] tracks nodes in the current DFS path.
# If a cycle is found, that path is unsafe.
# A node is marked safe only after all its paths finish without cycle.
# Finally, return all nodes marked safe in increasing order.