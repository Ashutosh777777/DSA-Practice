from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        q = deque()
        fresh = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        time = 0

        while q:
            i, j, t = q.popleft()
            time = max(time, t)

            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if ni < 0 or nj < 0 or ni >= r or nj >= c:
                    continue

                if grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    q.append((ni, nj, t + 1))

        if fresh != 0:
            return -1

        return time