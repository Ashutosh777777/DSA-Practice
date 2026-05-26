"""
Problem: Topological Sort
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/topological-sort/1
Approach: BFS / Kahn's Algorithm
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import deque

class Solution:

    def topoSort(self, V, edges):
        # Code here

        id = [0] * V
        ans = []
        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)

        for i in range(V):

            for x in adj[i]:
                id[x] += 1

        q = deque()

        for i in range(V):

            if id[i] == 0:
                q.append(i)

        while q:

            f = q.popleft()
            ans.append(f)

            for x in adj[f]:

                id[x] -= 1

                if id[x] == 0:
                    q.append(x)

        return ans


# Build adjacency list from directed edges.
# id[] stores indegree of each vertex.
# Start BFS with all vertices having indegree 0.
# Remove one node at a time and reduce indegree of its neighbors.
# If a neighbor's indegree becomes 0, add it to queue.
# ans stores one valid topological ordering of the DAG.