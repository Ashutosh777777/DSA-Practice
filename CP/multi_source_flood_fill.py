"""
Problem: Color Grid
Platform: LeetCode
Approach: Multi-source BFS with level-wise propagation
Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""
class Solution(object):
    def colorGrid(self, n, m, sources):
        """
        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """
        x = n
        y = m
        arr = sources[:]
        mat = [[0] * y for _ in range(x)]
        dq = deque()

        for a, b, c in arr:
            mat[a][b] = c
            dq.append((a, b, c))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while dq:
            sz = len(dq)
            nxt = {}

            for _ in range(sz):
                i, j, val = dq.popleft()

                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy

                    if 0 <= ni < x and 0 <= nj < y and mat[ni][nj] == 0:
                        if (ni, nj) not in nxt:
                            nxt[(ni, nj)] = val
                        else:
                            nxt[(ni, nj)] = max(nxt[(ni, nj)], val)

            for (i, j), val in nxt.items():
                mat[i][j] = val
                dq.append((i, j, val))

        return mat
# Initialize the grid with given source colors and push all sources into the queue.
# Perform BFS level by level so all colors spread one step at the same time.
# For each level, store candidate colors for uncolored neighbors in a temporary map.
# If multiple colors reach the same cell in the same step, assign the maximum color value.