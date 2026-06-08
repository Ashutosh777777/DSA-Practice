"""
Problem: Path With Minimum Effort
Platform: LeetCode
Link: https://leetcode.com/problems/path-with-minimum-effort/
Approach: Dijkstra's Algorithm
Time Complexity: O((m * n) log(m * n))
Space Complexity: O(m * n)
"""

import heapq

class Solution(object):

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        n = len(heights)
        m = len(heights[0])

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        dist = [[float('inf')] * m for _ in range(n)]

        pq = []
        heapq.heappush(pq, (0, 0, 0))

        dist[0][0] = 0

        while pq:

            effort, x, y = heapq.heappop(pq)

            if x == n - 1 and y == m - 1:
                return effort

            if effort > dist[x][y]:
                continue

            for k in range(4):

                i = x + dx[k]
                j = y + dy[k]

                if i < 0 or j < 0 or i >= n or j >= m:
                    continue

                ne = max(
                    effort,
                    abs(heights[x][y] - heights[i][j])
                )

                if ne < dist[i][j]:

                    dist[i][j] = ne

                    heapq.heappush(pq, (ne, i, j))

        return dist[n - 1][m - 1]


# Treat each cell as a graph node.
# Edge weight = absolute height difference between adjacent cells.
# Path effort = maximum edge weight encountered on the path.
# Use Dijkstra where distance means minimum effort required to reach a cell.
# For every neighbor, effort becomes max(current effort, edge weight).
# First time destination is popped from heap gives the minimum possible effort.