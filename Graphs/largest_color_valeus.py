"""
Problem: Largest Color Value in a Directed Graph
Platform: LeetCode
Link: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
Approach: Topological Sort + Dynamic Programming
Time Complexity: O(V + E * 26)
Space Complexity: O(V * 26 + E)
"""

from collections import deque

class Solution:

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        n = len(colors)
        ans = 0

        graph = [[] for _ in range(n)]
        id = [0] * n

        cnt = [[0] * 26 for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            id[v] += 1

        q = deque()

        for i in range(n):
            if id[i] == 0:
                q.append(i)

        pro = 0

        while q:

            node = q.popleft()
            pro += 1

            c_idx = ord(colors[node]) - ord('a')

            cnt[node][c_idx] += 1

            ans = max(ans, cnt[node][c_idx])

            for nbr in graph[node]:

                id[nbr] -= 1

                for j in range(26):
                    cnt[nbr][j] = max(cnt[nbr][j], cnt[node][j])

                if id[nbr] == 0:
                    q.append(nbr)

        return ans if pro == n else -1


# Use Kahn's algorithm to process nodes in topological order.
# cnt[node][c] stores max frequency of color c on any path ending at node.
# Add current node's color count when processing it.
# Push best color counts from current node to all neighbors.
# If all nodes are not processed, graph has a cycle → return -1.