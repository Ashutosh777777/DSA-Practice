"""
Problem: Minimum Steps by Knight
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/steps-by-knight5927/1
Approach: BFS / Shortest Path on Grid
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

from collections import deque

class Solution:

    def minStepToReachTarget(self, knightPos, targetPos, n):

        coordinates = [
            (-1, -2), (-1, 2),
            (1, 2), (1, -2),
            (-2, -1), (-2, 1),
            (2, -1), (2, 1)
        ]

        def helper(srcx, srcy, tarx, tary):

            visited = [[0 for _ in range(n)] for _ in range(n)]

            q = deque()
            q.append((srcx, srcy))

            visited[srcx][srcy] = 1

            steps = 0

            while q:

                size = len(q)

                for _ in range(size):

                    x, y = q.popleft()

                    if x == tarx and y == tary:
                        return steps

                    for dx, dy in coordinates:

                        newx = x + dx
                        newy = y + dy

                        if (
                            0 <= newx < n and
                            0 <= newy < n and
                            visited[newx][newy] == 0
                        ):
                            visited[newx][newy] = 1
                            q.append((newx, newy))

                steps += 1

            return -1

        srcx = knightPos[0] - 1
        srcy = knightPos[1] - 1

        tarx = targetPos[0] - 1
        tary = targetPos[1] - 1

        return helper(srcx, srcy, tarx, tary)


# Use BFS because each knight move has equal cost.
# Convert 1-based board positions into 0-based indices.
# Try all 8 possible knight moves from each cell.
# visited prevents revisiting the same board position.
# Level-wise BFS count gives minimum number of moves.