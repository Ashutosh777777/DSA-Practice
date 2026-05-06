"""
Problem: DFS of Graph
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
Approach: Recursive Depth First Search (DFS)
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

class Solution:
    def dfs(self, adj):
        V = len(adj)
        visited = [False] * V
        ans = []

        def solve(node):
            visited[node] = True
            ans.append(node)

            for neighbour in adj[node]:
                if not visited[neighbour]:
                    solve(neighbour)

        solve(0)
        return ans

# DFS explores a path completely before backtracking.
# Start traversal from node 0.
# Mark node as visited to avoid revisiting.
# Recursively visit all unvisited neighbours.
# Traversal order is stored in ans list.