"""
Problem: Chef and Wells
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/chef-and-wells/1
Approach: Multi-Source BFS
Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""

from typing import List
from collections import deque

class Solution:

    def chefAndWells(self, n: int, m: int, c: List[List[str]]) -> List[List[int]]:

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        result = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if c[i][j] == 'W':
                    q.append((i, j))

        counter = 1

        while q:

            size = len(q)

            while size > 0:

                row, col = q.popleft()

                for k in range(4):

                    new_row = row + dx[k]
                    new_col = col + dy[k]

                    if (
                        0 <= new_row < n and
                        0 <= new_col < m and
                        (c[new_row][new_col] == 'H' or c[new_row][new_col] == '.')
                    ):

                        if c[new_row][new_col] == 'H':
                            result[new_row][new_col] = 2 * counter

                        c[new_row][new_col] = 'X'
                        q.append((new_row, new_col))

                size -= 1

            counter += 1

        for i in range(n):
            for j in range(m):

                if c[i][j] == 'H':
                    result[i][j] = -1

        return result


# Start BFS from all wells at the same time.
# This is multi-source BFS, so the first time a house is reached is shortest.
# counter represents distance level from nearest well.
# For every reachable house, store 2 * distance in result.
# Mark visited cells as 'X' to avoid revisiting.
# Houses left unvisited after BFS are unreachable, so mark them as -1.