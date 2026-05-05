"""
Problem: Breadth First Search (BFS) of Graph
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
Approach: BFS using Queue
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque

class Solution:
    def bfs(self, adj):
        q = deque()
        visited = set()
        ans = []

        q.append(0)
        visited.add(0)

        while q:
            node = q.popleft()
            ans.append(node)

            for i in adj[node]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)

        return ans

# Use queue to explore nodes level by level.
# Start from node 0 and mark it as visited.
# Visit all adjacent nodes and push unvisited ones into queue.
# Continue until queue becomes empty.
# Ensures each node is visited exactly once.